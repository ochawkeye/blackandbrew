import time
import os
import sys
import nflgame
import subprocess

import fireleague_config

def dict_to_list(key, value):
    result = []
    result.append(key)
    for each in value:
        result.append(each)
    return result


def convert_to_good_format(name, team, position):
    #Edge cases first
    big_team = team.upper()
    if position == 'DEF':
        return big_team
    if name == 'Robert Griffin III' and big_team == 'WAS':
        return 'R.Griffin, WAS'
    #Jacquizz Rodgers conversion was for year 2012
    #if name == 'Jacquizz Rodgers' and big_team == 'ATL':
    #    return 'Jz.Rodgers, ATL'
    if name == 'James Jones' and big_team == 'GB':
        return 'Ja.Jones, GB'
    if name == 'Drew Davis' and big_team == 'ATL':
        return 'DJ.Davis, ATL'
    if name == 'Cecil Shorts III' and big_team == 'JAC':
        return 'C.Shorts, JAC'
    if name == 'DeAngelo Williams' and big_team == 'CAR':
        return 'De.Williams, CAR'
    if name == 'Ted Ginn Jr.' and big_team == 'CAR':
        return 'T.Ginn, CAR'
    else:
        space_marker = name.find(' ')
        new_name = name[0]+'.'+name[space_marker+1:]+', '+big_team
        return new_name

if __name__ == "__main__":
    # By default, go with current year and week...
    year, period = nflgame.live.current_year_and_week()
    # ...unless commandline arguments change
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
        except IndexError:
            year = nflgame.live.current_year_and_week()[0]
        try:
            period = int(sys.argv[2])
        except IndexError:
            period = nflgame.live.current_year_and_week()[1]
    print 'Parsing Fireleague rosters for %s week %s' % (year, period)

    filepath = os.path.dirname(os.path.abspath(__file__))

    #teams = [
    #    10106223, 10109051, 10110788, 10111577, 10112483,
    #    10127676, 10141117, 10166054, 10187930, 10199955,
    #    10235905, 10282038, 10284052, 10340894, 10347390,
    #    10403070, 10481639, 10533123, 10684899, 10870530]
    teams = fireleague_config.teams

    rosters = {}
    for each in teams:
        roster_list = []
        marker = 0
        player_marker = 0
        team_fn = '%s-week%02d.html' % (each, period)
        with open(os.path.join(filepath, team_fn), 'rb') as team_file:
            all_html_data = team_file.read()
        team_key = '<h3 class="leaguename">'
        marker = all_html_data.find(team_key)+len(team_key)
        end_of_marker = all_html_data.find('<', marker)
        team_name = all_html_data[marker:end_of_marker]
        blank_key = '<div class="lu_empty">'
        player_key = 'class="alink">'
        nfl_team_key = '<div class="athletelinkmeta">'
        blank_count = all_html_data.count(blank_key)
        locked_count = all_html_data.count(player_key)
        print '%s: Not locked=%s, Locked=%s' % (
            team_fn, blank_count, locked_count)
        for i in range(blank_count+locked_count):
            # Not add len(search string) so '-1' returned if not found
            blank_start = all_html_data.find(blank_key, player_marker)
            player_start = all_html_data.find(player_key, player_marker)
            if player_start != -1 and blank_start != -1:
                if player_start < blank_start:
                    player_start += len(player_key)  # Offset by size of key
                    player_end = all_html_data.find('</a>', player_start)
                    player_marker = player_end+1
                    player_name = all_html_data[player_start:player_end] #First Last #Num
                    player_name = player_name.rsplit(' #', 1)[0]
                    NFL_start = all_html_data.find(nfl_team_key, player_marker)+29
                    NFL_end = all_html_data.find('<span', NFL_start)
                    NFL_name = all_html_data[NFL_start:NFL_end] #Team abbreviated, not CAP
                    player_marker = NFL_end+1
                    position_start = all_html_data.find('>&nbsp;(',player_marker)+8
                    position_end = all_html_data.find(')</span>',position_start)
                    position = all_html_data[position_start:position_end]
                    roster_list.append(convert_to_good_format(player_name, NFL_name, position))
                if blank_start < player_start:
                    blank_end = all_html_data.find('</div', blank_start)
                    player_marker = blank_end+1
                    roster_list.append('')
            if player_start == -1:
                roster_list.append('')
            if blank_start == -1:
                    player_start += len(player_key)
                    player_end = all_html_data.find('</a>', player_start)
                    player_marker = player_end+1
                    player_name = all_html_data[player_start:player_end] #First Last #Num
                    player_name = player_name.rsplit(' #', 1)[0]
                    NFL_start = all_html_data.find(nfl_team_key, player_marker)+29
                    NFL_end = all_html_data.find('<span', NFL_start)
                    NFL_name = all_html_data[NFL_start:NFL_end] #Team abbreviated, not CAP
                    player_marker = NFL_end+1
                    position_start = all_html_data.find('>&nbsp;(',player_marker)+8
                    position_end = all_html_data.find(')</span>',position_start)
                    position = all_html_data[position_start:position_end]
                    roster_list.append(convert_to_good_format(player_name, NFL_name, position))
        rosters[team_name] = roster_list

    #Create CSV file for team rosters
    import csv
    roster_fn = 'week %02d %s rosters.csv' % (period, year)
    with open(os.path.join(filepath, roster_fn), 'wb') as f:
        w = csv.writer(f)
        w.writerow(['Team'])
        for key, value in rosters.items():
            w.writerow(dict_to_list(key, value))

    filename = 'advancednflstats.py'
    subprocess.call('python "%s"' % os.path.join(filepath, filename))

    print 'Task complete.  If livescoring4.py is configured correctly the please proceed.'
