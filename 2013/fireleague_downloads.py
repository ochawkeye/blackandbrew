from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
import nflgame

import fireleague_config


def fireleague_login(browser):
    browser.get('http://fireleague.com/index.php/login')
    print 'received login page'
    time.sleep(2.0)
    username = browser.find_element_by_name('username')
    #username.send_keys('XXXXXXXXXXXX')
    username.send_keys(fireleague_config.username)
    password = browser.find_element_by_name('password')
    #password.send_keys('XXXXXX'+Keys.RETURN)
    password.send_keys(fireleague_config.password+Keys.RETURN)
    for i in range(10):
        time.sleep(1.0)
        print '.',
    print '.'
    return browser


def download_teams(browser, period, teams, filepath):
    url_beg = 'http://football.fireleague.com/user/teams/'
    url_mid = '/lineup?period=71'
    i = 1
    for each in teams:
        time.sleep(2.0)
        url = '%s%s%s%02d' % (url_beg, each, url_mid, period)
        print '%s of %s: %s' % (i, len(teams), url)

        team_filename = '%s-week%02d.html' % (each, period)
        browser.get(url)
        all_html = browser.page_source.encode('ascii', 'ignore')
        with open(os.path.join(filepath, team_filename), 'wb') as x:
            x.write(all_html)
        i += 1
    return browser


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
    if name == 'Jacquizz Rodgers' and big_team == 'ATL':
        return 'Jz.Rodgers, ATL'
    if name == 'James Jones' and big_team == 'GB':
        return 'Ja.Jones, GB'
    if name == 'Drew Davis' and big_team == 'ATL':
        return 'DJ.Davis, ATL'
    if name == 'Cecil Shorts III' and big_team == 'JAC':
        return 'C.Shorts, JAC'
    if name == 'DeAngelo Williams' and big_team == 'CAR':
        return 'De.Williams, CAR'
    else:
        space_marker = name.find(' ')
        new_name = name[0]+'.'+name[space_marker+1:]+', '+big_team
        return new_name

if __name__ == "__main__":
    # By default go with current season and week...
    year, period = nflgame.live.current_year_and_week()

    # ...But if any command line arguments are present, those will overwrite
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
        except IndexError:
            year = nflgame.live.current_year_and_week()[0]
        try:
            period = int(sys.argv[2])
        except IndexError:
            period = nflgame.live.current_year_and_week()[1]
    print 'Downloading Fireleague rosters for %s week %s' % (year, period)

    teams = fireleague_config.teams

    filepath = os.path.dirname(os.path.abspath(__file__))
    # Get local session of firefox
    browser = webdriver.Chrome(
        executable_path=os.path.join(filepath, 'chromedriver.exe'))
    print 'Browser opened...'
    browser = fireleague_login(browser)
    print 'Logged into Fireleague.com...'
    browser = download_teams(browser, period, teams, filepath)

    browser.close()