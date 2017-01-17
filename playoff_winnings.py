#! /usr/bin/python
"""A Python script that will update player winnings in the blackandbrew db."""

import pymssql

import database_config as db_config


def current_winnings_from_db(table):
    """Return current balance for each owner in blackandbrew database."""
    conn = pymssql.connect(db_config.SERVER, db_config.USER, db_config.PASSWORD)
    cursor = conn.cursor()

    query = "SELECT * FROM {}".format(table)
    cursor.execute(query)

    balances = {row[1]: [row[4], row[7]] for row in cursor}

    conn.close()
    return balances


def update_players_winnings(table, player, add_amount):
    """Increase a single player's balance by the desired amount."""
    conn = pymssql.connect(db_config.SERVER, db_config.USER, db_config.PASSWORD)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM {} WHERE Players='{}'".format(table, player))
    current_balance = cursor.fetchone()[4]
    new_balance = current_balance + add_amount

    query = "UPDATE {} SET balance={} WHERE Players='{}'".format(table, new_balance, player)
    print query
    cursor.execute(query)
    conn.commit()

    conn.close()


def print_winnings(balance_table):
    for k, v in sorted(balance_table.items(), key=lambda e: e[0]):
        if not v[1] and 'Select Your Name' not in k:
            print '{:<40}\t{:>7}'.format(k, v[0])


if __name__ == '__main__':
    # print_winnings(current_winnings_from_db('Players'))

    update_players_winnings('Players', 'Logan, Nicole', 0)

    print_winnings(current_winnings_from_db('Players'))

