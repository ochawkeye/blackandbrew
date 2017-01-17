#! /usr/bin/python
"""A Python script that will do weekly updates for playoff database.

This will spider through blackandbrew.com playoff rosters, determine which
players have been used that are still alive in the playoffs, and add those
teams to a 'Selected' table on blackandbrew.net that gets used by the roster
builder so NFL players cannot be reused more than once.

This will also remove players that have been eliminated from the playoffs
from the pool of players that can be selected in the `Rosters` table.
"""

import sys
import os
import fnmatch
import csv
from collections import defaultdict

import pymssql

import nflgame
import database_config as db_config


def current_year():
    """Return current NFL season unless specified otherwise in command line."""
    try:
        return int(sys.argv[1])
    except:
        return nflgame.live.current_year_and_week()[0]


def find_roster_files(year, directory=os.getcwd()):
    """Return a list of playoff roster files for a given season"""
    return list(fnmatch.filter(
        os.listdir(directory), '*{} rosters.csv'.format(year)))


def find_week_used(filename):
    """Map a playoff numeric week to its name."""
    week_map = {'01': 'Wildcard',
                '02': 'Divisional',
                '03': 'Conference',
                '04': 'Super Bowl',
                '05': 'Super Bowl'}
    for week in week_map:
        if 'week {}'.format(week) in filename:
            return week_map[week]


def long_nfl_teamname(abbreviated_name):
    for team in nflgame.teams:
        if team[0] == abbreviated_name:
            return team[1]
    return None


def find_players_used(year, teams_remaining):
    """Return a dict of players still alive and have been used for a given year.

    Args:
        year: used to identify *-roster.csv files for the desired season
        teams_remaining: only teams still in the playoffs need be collected

    Returns:
        a dictionary of owner: [nfl_player, week_used, nfl_player_team] values

        {
            'Schroeder, Ben': [['A.Rodgers', 'Wildcard', 'GB'],
                               ['L.Bell', 'Divisional', 'PIT']],
            'Schroeder, Dave': [['T.Brady', 'Divisional', 'NE'],
                                ['L.Bell', 'Divisional', 'PIT']]
        }
    """
    players_used = defaultdict(list)

    for filename in find_roster_files(year):
        week_used = find_week_used(filename)
        print filename, week_used

        with open(filename, 'rb') as roster_file:
            weekly_rosters = csv.reader(roster_file)
            for row in weekly_rosters:
                if row[0] != 'Team':
                    owner = row[0]
                    for i in range(1, 6):
                        try:
                            player_name, player_team = row[i].split(', ')
                        except ValueError:  # empty field
                            player_name, player_team = None, None
                        if player_team in teams_remaining:
                            players_used[owner] += [(player_name, week_used, player_team)]
                    if row[6] in teams_remaining:  # defense selected
                        players_used[owner] += [(long_nfl_teamname(row[6]), week_used, row[6])]
    return players_used


def write_sql_row_to_db(conn, cursor, table, *sql_data):
    query = "INSERT INTO {} VALUES {}".format(table, sql_data)
    print query
    cursor.execute(query)
    conn.commit()
    return int(cursor.lastrowid)


def delete_sql_row_from_db(conn, cursor, table, column, sql_data):
    query = "DELETE FROM {} WHERE {}='{}'".format(table, column, sql_data)
    print query
    cursor.execute(query)
    conn.commit()


def blank_out_database_table(cursor, table_name):
    cursor.execute("""
        IF OBJECT_ID('{table}', 'U') IS NOT NULL
            DROP TABLE {table};

       CREATE TABLE {table} (
           id INT IDENTITY(1,1) PRIMARY KEY,
           Players VARCHAR(100),
           Pro VARCHAR(50),
           Week VARCHAR(20),
           team VARCHAR(50),
       )
       """.format(table=table_name))


def insert_used_into_db(players_used, table):

    conn = pymssql.connect(db_config.SERVER, db_config.USER, db_config.PASSWORD)
    cursor = conn.cursor()

    blank_out_database_table(cursor, '{}'.format(table))
    for owner in players_used:
        for record in players_used[owner]:
            write_sql_row_to_db(conn, cursor, 'dbo.{}'.format(table), owner, record[0], record[1], record[2])

    conn.close()


def get_nfl_teams_remaining():
    return ['ATL', 'PIT', 'NE', 'GB']


def get_nfl_teams_eliminated():
    return [team[0] for team in nflgame.teams if team[0] not in get_nfl_teams_remaining()]


def delete_eliminated_players_from_db(teams_eliminated, table):

    conn = pymssql.connect(db_config.SERVER, db_config.USER, db_config.PASSWORD)
    cursor_delete = conn.cursor()

    for team in teams_eliminated:
        delete_sql_row_from_db(conn, cursor_delete, 'dbo.{}'.format(table), 'Team', team)

    conn.close()

if __name__ == '__main__':

    players_used = find_players_used(current_year(), get_nfl_teams_remaining())
    insert_used_into_db(players_used, 'Selected')

    delete_eliminated_players_from_db(get_nfl_teams_eliminated(), 'Rosters')
