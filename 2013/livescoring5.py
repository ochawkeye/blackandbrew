import nflgame
import nflgame.game
import nflgame.alert
import datetime
import os
import csv
import ftplib
import sys
import traceback
import time
from pylab import savefig
import matplotlib.pyplot as plt
import numpy as np

import fireleague_config

def get_league_owners(year, season_type):
    league_owners = {}
    if year == 2012 and season_type == 'REG':
        league_owners = {
            "NU6 Times": ["DJ", 'Darrin Johnson'],
            "Marvelous Favreless": ["TR", 'Tom Rickert'],
            "Show me your TD's": ["MA", 'Mike Arndorfer'],
            "Herky's Heroes": ["TC", 'Travis Colling'],
            "SBBTitans": ["MD", 'Mike Dunne'],
            "DA BEARS": ["JH", 'John Hoberg'],
            "Herky's Huskers": ["MM", 'Marty McDevitt'],
            "DezmaNez": ["DB", 'Dennis Beaver'],
            "Ponder over yonder": ["DS", 'Dave Schroeder'],
            "ORION the HUNTER": ["DM", 'Dave McDevitt'],
            "Ramrod": ["BL", 'Bryan LaFleur'],
            "R Motter551": ["RM", 'Robin Motter'],
            "Raider Nation": ["VL", 'Vince Loggia'],
            "Flint Tropics": ["TG", 'Tony Grasso'],
            "Luftybc": ["KL", 'Kevin Luft'],
            "Wetzie72": ["GW", 'Grant Wetz'],
            "Meet the Ferentz": ["BS", 'Ben Schroeder'],
            "IceCreamClones": ["DK", 'Dick Kennedy'],
            "Cwalter536": ["ZW", 'Chuck Walter'],
            "B1G Husker Power": ["JL", 'Jeff Lewon'], }
    elif year == 2012 and season_type == 'POST':
        league_owners = {
            "Arndorfer, Mike": ["Worm", "Mike"],
            "Beaver, Dennis": ["DB", "Dennis"],
            "Bertul, Ryan": ["RB", "Ryan"],
            "Billiet, Mike": ["MB", "Mike"],
            "Brown, Will": ["WB", "Will"],
            "Colling, Travis": ["TC", "Travis"],
            "DeHaven, Matt": ["MaD", "Matt"],
            "DiMeo, Joe": ["JD", "Joe"],
            "Drey, Troy": ["TD", "Troy"],
            "Dunne, Mike": ["MiD", "Mike"],
            "Engler, Mike": ["ME", "Mike"],
            "Fisher, Joey": ["JF", "Joey"],
            "Fitzpatrick, Tom": ["TF", "Tom"],
            "Grasso, Tony": ["TG", "Tony"],
            "Hoberg, John": ["JH", "John"],
            "Johnson, Darrin": ["DJ", "Darrin"],
            "Jones, Mike": ["MJ", "Mike"],
            "Kennedy, Dick": ["DK", "Dick"],
            "Koedam, Justin": ["JuK", "Jusin"],
            "Krajack, Jon": ["JoK", "Jon"],
            "Kuhlman, Jason": ["JaK", "Jason"],
            "LaFleur, Bryan": ["BL", "Bryan"],
            "Laures, Chris": ["CL", "Chris"],
            "Laures, Katie": ["KL", "Katie"],
            "Leitschuck, Tom": ["TL", "Tom"],
            "Lewon, Jeff": ["JL", "Jeff"],
            "Loggia, Vince": ["VL", "Vince"],
            "Luft, Kevin": ["KL", "Kevin"],
            "Materna, Justin": ["JM", "Justin"],
            "Matthes, Todd": ["TM", "Todd"],
            "McDevitt, Dave": ["Mac", "Dave"],
            "McDevitt, Maggie": ["MM", "Maggie"],
            "Motter, Robin": ["RM", "Robin"],
            "Munro, Stuart": ["SM", "Stuart"],
            "Pauls, Brian": ["BP", "Brian"],
            "Ritt, Jim": ["JiR", "Jim"],
            "Rowlette, Jamey": ["JaR", "Jamey"],
            "Schroeder, Ben": ["BeS", "Ben"],
            "Schroeder, Dave": ["DS", "Dave"],
            "Schroeder, Kelly": ["KS", "Kelly"],
            "Schroeder, Sam": ["SS", "Sam"],
            "Spears, Bob": ["BoS", "Bob"],
            "Strong, Cameron": ["CS", "Cameron"],
            "Theis, Jerry": ["JeT", "Jerry"],
            "Walter, Chuck": ["CW", "Chuck"],
            "Wetz, Grant": ["GW", "Grant"],
            "Wetz, Scott": ["SW", "Scott"],

            "Fitzpatrick, Mike": ["MF", "Mike"],

            "Koedam, Brett": ["BK", "Brett"],
            "Schroeder, Jay": ["JS", "Jay"],
            "Schroeder, Mike": ["MS", "Mike"],
            "Tott, Mike": ["MT", "Mike"],

            "McDevitt, Martin": ["MarM", "Martin"],
            "Thaxton, Jasper": ["JaT", "Jasper"], }
    elif year == 2013 and season_type == 'REG':
        league_owners = {
            "99 problems all QB pitches": "DS",
            "Meet the Ferentz": "BS",
            "husker maxwell": "CW",
            "SBBTitans": "MD",
            "Ramrod": "BL",
            "Rockin Robin's Rowdies": "RM",
            "Year of the Huskers": "JL",
            "IceCreamClones": "DK",
            "Lambeau Legends": "TR",
            "Nu5 Times": "DJ",
            "Wetzie72": "GW",
            "Herky's Heroes": "TC",
            "Raider Nation": "VL",
            "Get a Kluwe!!!": "MA",
            "DA BEARS": "JH",
            "motorboatin": "DM",
            "WWSKMorgenDo": "DB",
            "Niners58": "SW",
            "Flint Tropics": "TG",
            "Luftybc": "KL"}
        league_owners = {
            "99 problems all QB pitches": ["DS", 'Dave Schroeder'],
            "Meet the Ferentz": ["BS", 'Ben Schroeder'],
            "husker maxwell": ["CW", "Chuck Walter"],
            "SBBTitans": ["MD", 'Mike Dunne'],
            "Ramrod": ["BL", "Bryan LaFleur"],
            "Rockin Robin's Rowdies": ["RM", 'Robin Motter'],
            "Year of the Huskers": ["JL", 'Jeff Lewon'],
            "IceCreamClones": ["DK", 'Dick Kennedy'],
            "Lambeau Legends": ["TR", "Tom Rickert"],
            "Nu5 Times": ["DJ", 'Darrin Johnson'],
            "Wetzie72": ["GW", 'Grant Wetz'],
            "Herky's Heroes": ["TC", 'Travis Colling'],
            "Raider Nation": ["VL", 'Vince Loggia'],
            "Get a Kluwe!!!": ["Worm", 'Mike Arndorfer'],
            "DA BEARS": ["JH", 'John Hoberg'],
            "motorboatin": ["Mac", "Dave McDevitt"],
            "WWSKMorgenDo": ["DB", 'Dennis Beaver'],
            "Niners58": ["SW", "Scott Wetz"],
            "Flint Tropics": ["TG", 'Tony Grasso'],
            "Luftybc": ["Lufty", 'Kevin Luft'], }
    elif year == 2013 and season_type == 'POST':
        league_owners = {
            "Arndorfer, Mike": ["Worm", "Mike"],        # Entered
            "Beaver, Dennis": ["DB", "Dennis"],
            "Bertul, Ryan": ["RB", "Ryan"],             # Entered   PAID
            "Billiet, Mike": ["MB", "Mike"],            # Entered
            "Bowers, Jared": ["JB", "Jared"],
            "Brown, Will": ["WB", "Will"],              # Entered
            "Calamia, Steve": ["SC", "Steve"],          # Entered   PAID
            "Colling, Travis": ["TC", "Travis"],        # Entered
            "Comune, Pat": ["PC", "Pat"],               # Entered   PAID
            "DeHaven, Matt": ["MaD", "Matt"],
            "DiMeo, Joe": ["JD", "Joe"],                # Entered   PAID
            "Drey, Troy": ["TD", "Troy"],               # Entered
            "Dunne, Mike": ["MiD", "Mike"],             # Entered
            "Engler, Mike": ["ME", "Mike"],             # Out
            "Fisher, Joey": ["JF", "Joey"],             # Entered   PAID
            "Fitzpatrick, Tom": ["TF", "Tom"],          # Entered
            "Gallant, Andrew": ["AG", "burntsushi"],    # Entered   PAID
            "Grasso, Tony": ["TG", "Tony"],             # Entered
            "Hartnett, Shane": ["SH", "Shane"],
            "Hemmingstad,John": ["JHe", "John"],        # Invalid
            "Hoberg, John": ["JHo", "John"],            # Entered
            "Hoskins, Adam": ["AH", "Adam"],            # Entered   PAID
            "Johnson, Darrin": ["DJ", "Darrin"],        # Entered
            "Jones, Mike": ["MJ", "Mike"],
            "Jones, Phil": ["PJ", "Phil"],              # Entered
            "Kennedy, Dick": ["DK", "Dick"],            # Entered
            "Koedam, Justin": ["JuK", "Jusin"],         # Entered   PAID
            "Krajack, Jon": ["JoK", "Jon"],             # Entered
            "Kuhlman, Jason": ["JaK", "Jason"],         # Entered
            "LaFleur, Bryan": ["BL", "Bryan"],          # Entered
            "Laures, Chris": ["CL", "Chris"],           # Entered
            "Laures, Katie": ["KL", "Katie"],           # Entered
            "Leitschuck, Tom": ["TL", "Tom"],           # Entered
            "Lewon, Jeff": ["JL", "Jeff"],              # Entered
            "Loggia, Vince": ["VL", "Vince"],           # Entered
            "Luft, Kevin": ["KL", "Kevin"],             # Entered
            "Materna, Justin": ["JM", "Justin"],        # Entered   PAID
            "Matthes, Todd": ["TM", "Todd"],            # Entered
            "McDevitt, Dave": ["Mac", "Dave"],          # Entered
            "McDevitt, Maggie": ["MM", "Maggie"],
            "Motter, Robin": ["RM", "Robin"],           # Entered
            "Munro, Stuart": ["SM", "Stuart"],          # Entered
            "Oestmann, Aaron": ["AO", "Aaron"],
            "Pauls, Brian": ["BP", "Brian"],
            "Ritt, Jim": ["JiR", "Jim"],                # Entered   PAID
            "Rowlette, Jamey": ["JaR", "Jamey"],        # Entered
            "Schroeder, Ben": ["BeS", "Ben"],           # Entered
            "Schroeder, Dave": ["DS", "Dave"],          # Entered
            "Schroeder, Kelly": ["KS", "Kelly"],        # Entered
            "Schroeder, Sam": ["SS", "Sam"],            # Entered
            "Spears, Bob": ["BoS", "Bob"],
            "Strong, Cameron": ["CS", "Cameron"],       # Entered   PAID
            "Theis, Jerry": ["JeT", "Jerry"],           # Entered
            "Walter, Chuck": ["CW", "Chuck"],           # Entered
            "Wetz, Grant": ["GW", "Grant"],             # Entered
            "Wetz, Scott": ["SW", "Scott"],

            "Fitzpatrick, Mike": ["MF", "Mike"],
            "Koedam, Brett": ["BK", "Brett"],
            "Schroeder, Jay": ["JS", "Jay"],
            "Schroeder, Mike": ["MS", "Mike"],
            "Tott, Mike": ["MT", "Mike"],
            "McDevitt, Martin": ["MarM", "Martin"],
            "Thaxton, Jasper": ["JaT", "Jasper"], }
    else:
        league_owners = []
        print 'No owners setup for %s and/or season %s' % (year, season_type)
    return league_owners


def d(name, stat_to_check):
    """
    # Function that checks to see if scoring category exists for a player and
    # if it does exist return the value associated with that category.  If it
    # does not exist, a 0 is returned instead of an error.
    # ie. if passing yards was requsted for a RB, an error would normally occur
    # since no passing yard statistic for that player exists by default.
    # This allows all players to have a stats space in the same format.
    """
    if stat_to_check in name.__dict__:
        return name.stats[stat_to_check]
    else:
        return 0


def return_game_time(teamname):
    """
    Returns either 'Final', 'Final OT, 'Pregame' or 'Qx xx:xx'
    """
    if teamname in looked_up_game_times:
        return looked_up_game_times[teamname]
    games = nflgame.games_gen(year, week, teamname, teamname, kind=season_type)
    if not games:  # Bye week
        looked_up_game_times[teamname] = 'Bye'
        return 'Bye'
    for game in games:
        result = str(game.time)
        if result:
            if result == 'final overtime':
                result = 'Final OT'
            looked_up_game_times[teamname] = result
            return result
    else:
        looked_up_game_times[teamname] = 'Pregame'
        return 'Pregame'


def nice_score(teamname):
    if teamname in looked_up_scores:
        return looked_up_scores[teamname]
    games = nflgame.games_gen(year, week, teamname, teamname, kind=season_type)
    if not games:
        looked_up_scores[teamname] = 'Bye'
        return 'Bye'
    for game in games:
        if game.away == teamname:
            result = '@%s %s-%s' % (
                game.home, game.score_away, game.score_home)
        else:
            result = 'vs.%s %s-%s' % (
                game.away, game.score_home, game.score_away)
        looked_up_scores[teamname] = result
        return result


def calculate_game_remaining(teamname):
    status = str(return_game_time(teamname))
    if status == 'Pregame':
        return 60
    elif status in ['Bye', 'Final', 'Final OT']:
        return 0
    elif status == 'Halftime':
        return 30
    else:
        quarter, time = status.split()
        minutes = int(time.split(':')[0])
        if quarter == 'Q1':
            return 45+minutes
        elif quarter == 'Q2':
            return 30+minutes
        elif quarter == 'Q3':
            return 15+minutes
        elif quarter == 'Q4':
            return 0+minutes
        else:
            return 0


def game_current_or_past(teamname):
    """Used for calculating how many players remain to be played"""
    if return_game_time(teamname) in ['Final', 'Final OT']:
        return 2
    else:
        return 1


def game_played(teamname):
    """
    Used for calculating defensive points. 200 awarded as soon as game starts
    """
    if return_game_time(teamname) not in ["Pregame", "Bye"]:
        return 1
    else:
        return 0


def strip_teamname(player_record):
    """
    Only team name is required to determine if game is currently being played
    """
    if player_record.count(','):
        marker = player_record.find(', ')
        return player_record[marker+2:]
    else:
        return player_record


def check_if_score(name):
    """
    Function to check if player or defense score exists
    """
    if str(name) in result:
        return result[name][25]
    else:
        if name in defense_results:
            return defense_results[name][10]
        else:
            if name != '':
                '''
                #########################################################
                ###         ALWAYS SEEM TO BE LOOKING FOR THIS       ####
                #########################################################
                '''
                print 'Did not find', name
                did_not_find.append(name)

                with open(os.path.join(
                        filepath, 'week%s errorlog.txt' % week), 'wb') as f:
                    now = datetime.datetime.now()
                    timestamp = '%s-%s-%s %s-%s' % (
                        now.year, now.month, now.day, now.hour, now.minute)
                    f.write('\n%s - Did not find %s' % (timestamp, name))
            return 0


def ftp_store(filepath, filename, ftp):
    with open(os.path.join(filepath, filename), 'rb') as f:
        ftp.storbinary('STOR ' + filename, f)


def upload_files_to_ftp(week, year, season_type, filepath):
    print 'Logging in...'
    ftp = ftplib.FTP()
    ftp.connect(fireleague_config.ftp_site)
    print ftp.getwelcome()
    try:
        try:
            ftp.login(fireleague_config.ftp_user, fireleague_config.ftp_pass)
            ftp.cwd('/blackand/%s' % year)
            print 'Currently in:', ftp.pwd()
            print 'Uploading...'
            print '...player points',
            filename = 'week%02d-%s-%s-game.html' % (
                week, year, season_type)
            ftp_store(filepath, filename, ftp)
            print 'OK'
            print '...results file',
            filename = 'week%02d-%s-%s-results.html' % (
                week, year, season_type)
            ftp_store(filepath, filename, ftp)
            print 'OK'
            print '...matrix file',
            filename = 'week%02d-%s-%s-matrix.html' % (
                week, year, season_type)
            ftp_store(filepath, filename, ftp)
            print 'OK'
            print '...graph image',
            filename = 'week%02d-%s-%s-graph.png' % (
                week, year, season_type)
            ftp_store(filepath, filename, ftp)
            print 'OK'
            if season_type == 'POST':
                print '...total points',
                filename = 'totalscores%s.html' % (
                    year)
                ftp_store(filepath, filename, ftp)
                print 'OK'
        finally:
            print 'Quitting...'
            ftp.quit()
    except:
        traceback.print_exc()

if __name__ == "__main__":

    year, week = nflgame.live.current_year_and_week()
    if week > 17:
        season_type = 'POST'
    else:
        season_type = 'REG'

    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
        except IndexError:
            year = nflgame.live.current_year_and_week()[0]
        try:
            week = int(sys.argv[2])
        except IndexError:
            week = nflgame.live.current_year_and_week()[1]
        try:
            if sys.argv[3] in ['PRE', 'REG', 'POST']:
                season_type = sys.argv[3]
            else:
                print 'Invalid season type', sys.argv[3]
                print 'Reverting to "REG"'
                season_type = 'REG'
        except IndexError:
            season_type = 'REG'
    print year, week, season_type
    while True:
        looked_up_game_times = {}
        looked_up_scores = {}
        did_not_find = []
        filepath = os.path.dirname(os.path.abspath(__file__))

        games = nflgame.games(year, week=week, kind=season_type)
        players = nflgame.combine_game_stats(games)
        meta = nflgame.players
        nfl_teams = nflgame.teams
        result = {}
        league_owners = get_league_owners(year, season_type)

        #Iterate through each player and add the number of points they have
        # scored
        for x in players:
            id_number = x.playerid
            '''
            points = +1*(d(x, 'passing_yds'))
            points += +60*(d(x, 'passing_tds'))
            points += -45*(d(x, 'passing_ints'))
            points += -2*(d(x, 'passing_att')-d(x, 'passing_cmp'))
            points += +2*(d(x, 'rushing_yds'))
            points += +60*(d(x, 'rushing_tds'))
            points += +2*(d(x, 'receiving_rec'))
            points += +2*(d(x, 'receiving_yds'))
            points += +60*(d(x, 'receiving_tds'))
            points += -45*(d(x, 'fumbles_lost'))
            points += +20*(d(x, 'passing_twoptm'))
            points += +20*(d(x, 'rushing_twoptm'))
            points += +20*(d(x, 'receiving_twoptm'))
            points += +10*(d(x, 'kicking_xpmade'))
            points += -20*(d(x, 'kicking_xpmissed'))
            '''
            points = +1*(getattr(x, 'passing_yds'))
            points += +60*(getattr(x, 'passing_tds'))
            points += -45*getattr(x, 'passing_ints')
            points += -2*(getattr(x, 'passing_att')-getattr(x, 'passing_cmp'))
            points += +2*(getattr(x, 'rushing_yds'))
            points += +60*(getattr(x, 'rushing_tds'))
            points += +2*(getattr(x, 'receiving_rec'))
            points += +2*(getattr(x, 'receiving_yds'))
            points += +60*(getattr(x, 'receiving_tds'))
            points += -45*(getattr(x, 'fumbles_lost'))
            points += +20*(getattr(x, 'passing_twoptm'))
            points += +20*(getattr(x, 'rushing_twoptm'))
            points += +20*(getattr(x, 'receiving_twoptm'))
            points += +10*(getattr(x, 'kicking_xpmade'))
            points += -20*(getattr(x, 'kicking_xpmissed'))
            #REMOVED THESE SINCE THEY WERE NOT ACCURATE
            #HANDLING THESE STATS BASED ON PLAY-BY-PLAY LATER.
            #points += -10*(d(x, 'kickret_ret'))
            #points += +1*(d(x, 'kickret_ret')*d(x, 'kickret_avg'))
            #points += +60*(d(x, 'kickret_tds'))
            #points += +2*(d(x, 'puntret_ret')*d(x, 'puntret_avg'))
            #points += +60*(d(x, 'puntret_tds'))

            #Store the results in a dictionary (key = 'players's name, team')
            #The nine '0' records are placeholders for the soon to be added
            # KR, PR, and FG points
            result[str(x)+', '+x.team] = [
                str(x), x.team, 'xxx',  # Name, team, position placeholder
                #d(x, 'passing_yds'),
                #d(x, 'passing_tds'),
                #d(x, 'passing_ints'),
                #d(x, 'passing_att')-d(x, 'passing_cmp'),
                #d(x, 'rushing_yds'),
                #d(x, 'rushing_tds'),
                #d(x, 'receiving_rec'),
                #d(x, 'receiving_yds'),
                #d(x, 'receiving_tds'),
                getattr(x, 'passing_yds'),
                getattr(x, 'passing_tds'),
                getattr(x, 'passing_ints'),
                getattr(x, 'passing_att')-getattr(x, 'passing_cmp'),
                getattr(x, 'rushing_yds'),
                getattr(x, 'rushing_tds'),
                getattr(x, 'receiving_rec'),
                getattr(x, 'receiving_yds'),
                getattr(x, 'receiving_tds'),
                0, 0, 0, 0, 0,  # Kick return 12,13,14, Punt return 15,16
                #d(x, 'fumbles_lost'),
                #d(x, 'passing_twoptm')
                #+ d(x, 'rushing_twoptm')
                #+ d(x, 'receiving_twoptm'),
                #d(x, 'kicking_xpmade'),
                #d(x, 'kicking_xpmissed')
                getattr(x, 'fumbles_lost'),
                getattr(x, 'passing_twoptm')
                + getattr(x, 'rushing_twoptm')
                + getattr(x, 'receiving_twoptm'),
                getattr(x, 'kicking_xpmade'),
                getattr(x, 'kicking_xpmissed'),
                0, 0, 0, 0,  # Field goal statistics
                points,
                'xxx']
            #Try to add player's position if included in the nflgame.players
            # dictionary
            if id_number in meta:
                #result[str(x)+', '+x.team][0] = meta[str(id_number)].name
                #result[str(x)+', '+x.team][2] = meta[str(id_number)].position
                result[str(x)+', '+x.team][2] = x.player.position
                #result[str(x)+', '+x.team][26] = str(id_number)
                result[str(x)+', '+x.team][26] = x.player.player_id

        #Add in field goals and missed field goals from play-by-play results
        games = nflgame.games(year, week=week, kind=season_type)
        short, medium, longest, missed = [], [], [], []
        #SURELY THERE IS A BETTER WAY TO DO THIS,
        #BUT FOR NOW THIS METHOD IS USED THROUGHOUT
        # Count number of times each player makes a field goal less than
        # 40 yards
        plays = nflgame.combine_plays(games)
        plays30 = plays.filter(kicking_fgm__ge=1, kicking_fgm_yds__lt=40)
        for player in plays30.players().kicking():
            short.append([str(player)+', '+player.team, player.kicking_fgm])
        #Count number of times each player makes a field goal 40-49 yards
        plays = nflgame.combine_plays(games)
        plays40 = plays.filter(kicking_fgm__ge=1,
                               kicking_fgm_yds__ge=40, kicking_fgm_yds__lt=50)
        for player in plays40.players().kicking():
            medium.append([str(player)+', '+player.team, player.kicking_fgm])
        # Count number of times each player makes a field goal greater than
        # 50 yards
        plays = nflgame.combine_plays(games)
        plays50 = plays.filter(kicking_fgm__ge=1, kicking_fgm_yds__ge=50)
        for player in plays50.players().kicking():
            longest.append([str(player)+', '+player.team, player.kicking_fgm])
        # Count number of times each player misses a field goal less than
        # 40 yards
        plays = nflgame.combine_plays(games)
        plays_miss = plays.filter(kicking_fgmissed_yds__lt=40)
        for player in plays_miss.players().kicking():
            if player.kicking_fgmissed > 0:
                missed.append([
                    str(player)+', '+player.team,
                    player.kicking_fgmissed])

        #Add results from above to the results table for each player
        for each in short:
            if each[0] in result:
                result[each[0]][21] = each[1]
        for each in medium:
            if each[0] in result:
                result[each[0]][22] = each[1]
        for each in longest:
            if each[0] in result:
                result[each[0]][23] = each[1]
        for each in missed:
            if each[0] in result:
                result[each[0]][24] = each[1]
        #Update points with newly added field goal and missed field goal
        # results
        for key, val in result.items():
            val[25] += +40*val[21]+60*val[22]+80*val[23]-30*val[24]

        #Kick return statistics were not accurate with game stats data.
        #Calculating with play-by-play data instead of game data
        #Dictionary fields in question include [12],[13],[14],[15],[16]
        games = nflgame.games(year, week=week, kind=season_type)
        kick_returns, punt_returns = [], []
        plays = nflgame.combine_plays(games)
        playsKR = plays.filter(kickret_ret__ge=1)
        for player in playsKR.players():
            kick_returns.append([
                str(player)+', '+player.team,
                player.kickret_ret,
                player.kickret_yds,
                player.kickret_tds])
        plays = nflgame.combine_plays(games)
        playsPR = plays.filter(puntret_tot__ge=1)
        for player in playsPR.players():
            punt_returns.append([
                str(player)+', '+player.team,
                player.puntret_yds,
                player.puntret_tds])
        for each in kick_returns:
            if each[1] > 0 or each[2] > 0 or each[3] > 0:
                if each[0] in result:
                    result[each[0]][12] = each[1]
                    result[each[0]][13] = each[2]
                    result[each[0]][14] = each[3]
                else:
                    """
                    # I've found that sometimes a player shows up in the
                    # play-by-play that has no game stats. These have been
                    # limited primarity to lesser known defensive players that
                    # return a kick. Pretty much ignoring these cases until the
                    # day that one of these lesser known players would actually
                    # be used in FF. This will write a warning to the terminal
                    # window, but nothing else
                    """
                    print 'Failed to add %s %s and %s to %s' % (
                        each[1], each[2], each[3], each[0])
        for each in punt_returns:
            if each[1] > 0 or each[2] > 0:
                if each[0] in result:
                    result[each[0]][15] = each[1]
                    result[each[0]][16] = each[2]
                else:
                    #Same reason as the kick return above
                    print 'Failed to add %s and %s to %s' % (
                        each[1], each[2], each[0])

        #Update points with newly added kick return and punt return statistics
        for key, val in result.items():
            val[25] += -10*val[12]+1*val[13]+60*val[14]+2*val[15]+60*val[16]
        """
        #######################################################################
        #######################################################################
        ###                                                                 ###
        ###          GENERATE DEFENSIVE STATISTICS FROM PLAY BY PLAY        ###
        ###                                                                 ###
        #######################################################################
        #######################################################################
        """
        #Prepopulate a dictionary with a key for each team
        defense_results = {}
        for a in range(len(nfl_teams)):
            #defense_results[nfl_teams[a][0]] = [str(nfl_teams[a][1]),
            #   str(nfl_teams[a][0]), 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            defense_results[nfl_teams[a][0]] = [
                str(nfl_teams[a][1]),
                str(nfl_teams[a][0]),
                game_played(nfl_teams[a][0]),
                0, 0, 0, 0, 0, 0, 0, 0, 0]
        games = nflgame.games(year, week=week, kind=season_type)
        #Find defensive interceptions and interceptions for touchdowns
        plays = nflgame.combine_plays(games)
        for p in plays.filter(defense_int=True).players().defense():
            if p.defense_int > 0:
                defense_results[p.team][4] += p.defense_int
                defense_results[p.team][5] += p.defense_tds
        #Find defensive fumble recoveries and defensive fumble recoveries
        # for TD
        plays = nflgame.combine_plays(games)
        for p in plays.filter(defense_frec=True).players().defense():
            if p.defense_frec > 0:
                defense_results[p.team][6] += p.defense_frec
                defense_results[p.team][7] += p.defense_frec_tds
        #Find defensive sacks
        plays = nflgame.combine_plays(games)
        for p in players.filter(defense_sk=lambda x: x > 0).sort("defense_sk"):
            defense_results[p.team][8] += p.defense_sk
        #Find defensive safeties
        plays = nflgame.combine_plays(games)
        for p in plays.filter(defense_safe=True).players().defense():
            if p.defense_safe > 0:
                defense_results[p.team][9] += p.defense_safe
        #Find kick return touchdowns
        plays = nflgame.combine_plays(games)
        for p in plays.filter(kickret_tds=True).players():
            if p.kickret_tds > 0:
                defense_results[p.team][11] += p.kickret_tds
        #Find punt return touchdowns
        plays = nflgame.combine_plays(games)
        for p in plays.filter(puntret_tds=True).players():
            if p.puntret_tds > 0:
                defense_results[p.team][11] += p.puntret_tds

        #UGLY, UGLY, UGLY WAY FOR FINDING OPPONENT & OPPONENT SCORE
        #Key for dictionary is abbreviated team name
        #Value for dictionary is:
        # [opponent, opponent's score, opponent's defensive points]
        #ie. MIN (21) vs. CHI (14) could have the following two dictionary
        # entries:
            #defensive_points_allowed['MIN'] = ['CHI', 14, 0]
            #defensive_points_allowed['CHI'] = ['MIN', 21, 6] <-- MIN had an int_ret for a TD
        test_score = {}
        #First find opponent and opponent's total score in game
        for each in games:
            test_score[each.home] = [each.away, each.score_away, 0]
            test_score[each.away] = [each.home, each.score_home, 0]
        #For each team, find how many points were scored by DEF/ST
        for each in test_score:
            defensive_pts_allowed = int(defense_results[each][5])*6
            defensive_pts_allowed += int(defense_results[each][7])*6
            defensive_pts_allowed += int(defense_results[each][9])*2
            defensive_pts_allowed += int(defense_results[each][11])*6
            test_score[test_score[each][0]][2] = defensive_pts_allowed
        #print defense_results
        #print test_score
        for each in defense_results:
            if each in test_score:
                #defense_results[each][3] = int(test_score[each][1])
                #defense_results[each][3] += -int(test_score[each][2])
                team_total_points = int(test_score[each][1])
                team_def_points_against = int(test_score[each][2])
                team_points_against = team_total_points-team_def_points_against
                defense_results[each][3] = team_points_against
            else:
                defense_results[each][3] = 0
        #defense_results in order of:
        # [long team name, abbreviated team name, game played, points_allowed,
        # ints, int_tds, fumble recoveries, fumble_tds, sacks, safeties,
        # def_points]
        for y in defense_results:
            def_points = +200*int(defense_results[y][2])
            def_points += -10*int(defense_results[y][3])
            def_points += +45*int(defense_results[y][4])
            def_points += +60*int(defense_results[y][5])
            def_points += +45*int(defense_results[y][6])
            def_points += +60*int(defense_results[y][7])
            def_points += +20*int(defense_results[y][8])
            def_points += +45*int(defense_results[y][9])
            defense_results[y][10] = def_points

        """
        #####################################################################
        #####################################################################
        ###                                                               ###
        ###          MANUAL UPDATES FOR "STRANGE" SCORING                 ###
        ###                                                               ###
        #####################################################################
        #####################################################################
        Format for this section is `result[playername][x]` where x equals
            0: name, 1: team, 2: position, 3: pass yd, 4: pass td, 5: pass int,
            6: pass inc, 7: rush yd, 8: rush td, 9: rec rec, 10: rec yd,
            11: rec td, 12: kr, 13: kryd, 14: krtd, 15: punt yd, 16: punt td,
            17: fumble, 18: 2pt, 19: xp, 20: xp miss, 21: 1-39, 22: 40-49,
            23: 50+, 24: 40- miss, 25: total points, 26: player id number
        Format for this section is `defense_results[x]` where x equals TEAM
            0: full name, 1: TEAM, 2: game played, 3: pts. allowed, 4: int,
            5: int td, 6: fum rec, 7: fum td, 8: sacks, 9: safety,
            10: total points
        """
        if week == 15 and year == 2012 and season_type == 'REG':
            result['R.Cobb, GB'][15] = -2
            # Punt return yards changed from 1 to -2
            result['R.Cobb, GB'][25] = 210
            # Total points changed from 214 to 210 due to punt return yard
            # update
            result['F.Gore, SF'][8] = 1
            # Recovered a fumble in the end zone
            # Not really a rushing TD, but will add it there
            result['F.Gore, SF'][25] = 298
            # Total points changed from 238 to 298 due to extra touchdown
        if week == 3 and year == 2012 and season_type == 'POST':
            result['M.Ryan, ATL'][3] = 396
            result['M.Ryan, ATL'][6] = 12
            result['M.Ryan, ATL'][7] = 3
            result['M.Ryan, ATL'][25] = 468
            result['J.Jones, ATL'][9] = 11
            result['J.Jones, ATL'][10] = 182
            result['J.Jones, ATL'][25] = 516
            result['F.Gore, SF'][7] = 90
            result['F.Gore, SF'][25] = 300
            result['Jz. Rodgers, ATL'][7] = 32
            result['Jz. Rodgers, ATL'][25] = 64
            result['R.White, ATL'][9] = 7
            result['R.White, ATL'][10] = 100
            result['R.White, ATL'][25] = 214
            result['J.Snelling, ATL'][9] = 1
            result['J.Snelling, ATL'][10] = 5
            result['J.Snelling, ATL'][25] = 36
            result['H.Douglas, ATL'][9] = 3
            result['H.Douglas, ATL'][10] = 31
            result['H.Douglas, ATL'][25] = 82
        if week == 4 and year == 2012 and season_type == 'POST':
            defense_results['No D'] = [
                str('No D'),
                str('n/a'),
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            defense_results['No D'][10] = min(
                defense_results['BAL'][10]-100,
                defense_results['SF'][10]-100,
                0)
        if week == 1 and year == 2013 and season_type == 'REG':
            defense_results['PIT'][9] = 1
            defense_results['PIT'][10] += 45
            defense_results['TEN'][3] -= 2
            defense_results['TEN'][10] += 20
            # Safety against TEN not showing for PIT
            # No defensive player credited with the tackle
            defense_results['NYJ'][9] = 1
            defense_results['NYJ'][10] += 45
            defense_results['TB'][3] -= 2
            defense_results['TB'][10] += 20
            # Safety against TB not showing for NYJ
            # No defensive player credited with forced fumble
            result['M.Stafford, DET'][7] -= 5
            result['M.Stafford, DET'][25] -= 10
            defense_results['MIN'][8] -= 1
            defense_results['MIN'][10] -= 20
            # 4th Qtr, 9:58. - Play changed from a sack to a rush
            result['C.Daniel, KC'][7] += 1
            result['C.Daniel, KC'][25] += 2
            # Only one kneel at end of game
            result['M.Vick, PHI'][7] -= 2
            result['M.Vick, PHI'][25] -= 4
            # Box scores shows 54 rushing yards (not 56)
        if week == 2 and year == 2013 and season_type == 'REG':
            result['M.Vick, PHI'][7] += 11
            result['M.Vick, PHI'][25] += 22
            defense_results['SD'][8] += 1
            defense_results['SD'][10] += 20
            # Rushing attempt: -1, Sacked +1
            result['F.Jackson, BUF'][9] += 1
            result['C.Spiller, BUF'][9] -= 1
            result['F.Jackson, BUF'][10] += 12
            result['C.Spiller, BUF'][10] -= 12
            result['F.Jackson, BUF'][25] += 26
            result['C.Spiller, BUF'][25] -= 26
            # 12 yard reception was Jackson, not Spiller
            result['J.Cutler, CHI'][3] -= -2
            result['J.Cutler, CHI'][25] += 2
            result['M.Forte, CHI'][9] -= 1
            result['M.Forte, CHI'][10] -= -2
            result['M.Forte, CHI'][7] += -2
            result['M.Forte, CHI'][25] += -2
            # -2 yard pass ruled a run
            result['M.Ball, DEN'][7] -= 2
            result['M.Ball, DEN'][25] += -4
            result['D.Sproles, NO'][15] -= 2
            result['D.Sproles, NO'][25] -= 4
        if week == 3 and year == 2013 and season_type == 'REG':
            result['R.Wayne, IND'][7] += 5
            result['R.Wayne, IND'][9] -= 1
            result['R.Wayne, IND'][10] -= 5
            result['R.Wayne, IND'][25] -= 2
            result['A.Luck, IND'][3] -= 5
            result['A.Luck, IND'][25] -= 5
            #2nd quarter, 11:48; play changed from pass to rush
            defense_results['SEA'][8] -= 1
            defense_results['SEA'][10] -= 20
            #3rd quarter, 13:17; play changed from sack to rush
            result['A.Smith, KC'][7] -= 1
            result['A.Smith, KC'][25] -= 2
            #4th quarter, 0:30; rush omitted from original pbp
            result['Q.Demps, KC'][12] -= 1
            result['Q.Demps, KC'][13] -= 3
            result['Q.Demps, KC'][25] -= -7
            result['D.McCluster, KC'][12] += 1
            result['D.McCluster, KC'][13] += 3
            result['D.McCluster, KC'][25] += -7
            #4th quarter, 11:36
            result['M.Vick, PHI'][7] += 4
            result['M.Vick, PHI'][25] += 8
            #4th quarter, 1:40; play changed from a rush to a sack
            defense_results['KC'][8] += 1
            defense_results['KC'][10] += 20
            result['M.Nugent, CIN'][21] += 1
            result['M.Nugent, CIN'][25] -= 20
        if week == 4 and year == 2013 and season_type == 'REG':
            result['T.Romo, DAL'][3] += 2
            result['T.Romo, DAL'][25] += 2
            result['D.Murray, DAL'][10] += 2
            result['D.Murray, DAL'][25] += 4
            #4th quarter, 0:09; fumble recovered at DAL42, not DAL40
            result['A.Luck, IND'][3] -= 3
            result['A.Luck, IND'][25] -= 3
            result['T.Hilton, IND'][7] += 3
            result['T.Hilton, IND'][9] -= 1
            result['T.Hilton, IND'][10] -= 3
            result['T.Hilton, IND'][25] -= 2
            #1st quarter, 10:17; play changed from pass to rush
            result['M.Flynn, OAK'][17] += 1
            result['M.Flynn, OAK'][25] -= 45
            result['WAS'][6] += 1
            result['WAS'][10] += 45
            #4th quarter, 3:32; fumble
        if week == 5 and year == 2013 and season_type == 'REG':
            result['J.Nelson, GB'][12] -= 1
            result['J.Nelson, GB'][25] += 10
            #Onside kick recovery showing as a KR attempt
            result['E.Royal, SD'][15] -= 21
            result['E.Royal, SD'][25] -= 42
            result['D.Woodhead, SD'][7] += 4
            result['D.Woodhead, SD'][25] += 8
            result['D.Brees, NO'][7] -= 2
            result['D.Brees, NO'][25] -= 4
            result['V.Brown, SD'][9] -= 1
            result['V.Brown, SD'][25] -= 2
            result['K.Allen, SD'][15] += 21
            result['K.Allen, SD'][25] += 42
        if week == 6 and year == 2013 and season_type == 'REG':
            result['J.Edelman, NE'][15] -= 11
            result['J.Edelman, NE'][25] -= 22
            result['T.Pryor, OAK'][7] -= 4
            result['T.Pryor, OAK'][25] -= 8
        if week == 7 and year == 2013 and season_type == 'REG':
            pass
        if week == 14 and year == 2013 and season_type == 'REG':
            result['B.Roethlisberger, PIT'][3] += 114
            result['B.Roethlisberger, PIT'][6] += 8
            result['B.Roethlisberger, PIT'][7] += 8
            result['B.Roethlisberger, PIT'][25] += 114
            result['A.Brown, PIT'][9] += 1
            result['A.Brown, PIT'][10] += 60
            result['A.Brown, PIT'][15] += 12
            result['A.Brown, PIT'][25] += 134
            result['C.Clay, MIA'][9] += 2
            result['C.Clay, MIA'][10] += 22
            result['C.Clay, MIA'][11] += 1
            result['C.Clay, MIA'][25] += 108
            defense_results['MIA'][8] += 1
            defense_results['MIA'][10] += 20
        if week == 1 and year == 2013 and season_type == 'POST':
            result['A.Luck, IND'][8] += 1
            result['A.Luck, IND'][25] += 60
        if week == 4 and year == 2013 and season_type == 'POST':
            defense_results['No D'] = [
                str('No D'),
                str('n/a'),
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            defense_results['No D'][10] = min(
                defense_results['SEA'][10]-100,
                defense_results['DEN'][10]-100,
                0)
        sorted_result = sorted(
            result.items(), key=lambda e: e[1][25], reverse=True)
        sorted_defensive_result = sorted(
            defense_results.items(), key=lambda e: e[1][10], reverse=True)

        # Create HTML page with results
        url = 'http://www.nfl.com/players/profile?id='

        analytics = (
            '<script type="text/javascript">var _gaq = _gaq || [];_gaq.push(["'
            '_setAccount", "UA-3146554-2"]);_gaq.push(["_trackPageview"]);(fun'
            'ction() { var ga = document.createElement("script"); ga.type = "t'
            'ext/javascript"; ga.async = true;ga.src = ("https:" == document.l'
            'ocation.protocol ? "https://ssl" : "http://www") + ".google-analy'
            'tics.com/ga.js";    var s = document.getElementsByTagName("script'
            '")[0]; s.parentNode.insertBefore(ga, s);  })();</script>')
        clear_cache = (
            '<meta http-equiv="pragma" content="no-cache"><meta http-equiv="Ex'
            'pires" content="Tue,01 Dec 1990 06:30:00 GMT">')
        header = (
            '<html><head><meta http-equiv="refresh" content="30"><style type="'
            'text/css">table.gridtable {font-family: verdana,arial,sans-serif;'
            'font-size:10px;text-align:center;color:#333333;border-width:1px;b'
            'order-color: #666666;border-collapse:collapse;width:100%;}table.g'
            'ridtable th {border-width: 1px;border-style: solid;border-color: '
            '#666666;background-color: #dedede;}table.gridtable td {border-wid'
            'th: 1px;border-style: solid;border-color: #666666;background-colo'
            'r: #black;}tr.even {background-color:#FFFFFF;}tr.even:hover{backg'
            'round-color:gold;color:black;}tr.odd {background-color:#dedede;}t'
            'r.odd:hover{background-color:black;color:white;}</style>')

        with open(os.path.join(filepath, 'week%02d-%s-%s-game.html' % (
                week, year, season_type)), 'wb') as game_file:
            counter = 0

            game_file.write(
                '%s<title>Week %s NFL Player Points</title>%s%s</head>' % (
                header, week, analytics, clear_cache))
            game_file.write('<body>')
            game_file.write('<table class="gridtable">')
            game_file.write(
                '<tr><th>Name<th>Team<th><th><th>Pos<th>PaYds<th>PaTD<th>Int'
                '<th>Inc<th>RuYds<th>RuTD<th>Rec<th>ReYds<th>ReTD<th>KRa'
                '<th>KRYd<th>KRTD<th>PuYd<th>PuTD<th>FUM<th>2Pt<th>XP<th>XPM'
                '<th>FG1-39<th>FG40-49<th>FG50+<th>FGMiss<th>POINTS</tr>')
            for each in sorted_result:
                if each[1][25] != 0:
                    if counter % 2 == 0:
                        game_file.write('<tr class="even">')
                    else:
                        game_file.write('<tr class="odd">')
                    for i in range(len(each[1])-1):
                        if i == 0:
                            game_file.write(
                                '<td><a href="%s%s">%s</a></td>' % (
                                    url, each[1][26], each[1][i]))
                        elif i == 1:
                            game_file.write(
                                '<td>%s</td><td>%s</td><td>%s</td>' % (
                                    each[1][i],
                                    return_game_time(each[1][i]),
                                    nice_score(each[1][i])))
                        elif i == 25:
                            game_file.write('<td>%s</td>' % each[1][i])
                        else:
                            if each[1][i] != 0:
                                game_file.write('<td>%s</td>' % each[1][i])
                            else:
                                game_file.write('<td></td>')
                    game_file.write('</tr>')
                    counter += 1
            game_file.write('</table>')
            game_file.write('<br><br>')
            game_file.write('<table class="gridtable">')
            game_file.write(
                '<tr><th>Defense<th>Team<th><th><th>GP<th>Pts Allowed<th>INTs')
            game_file.write(
                '<th>INT TDs<th>Fum Rec<th>Fum TD<th>Sack<th>Safety')
            game_file.write('<th>POINTS</tr>')
            for each in sorted_defensive_result:
                if each[1][2] != 0:
                    if counter % 2 == 0:
                        game_file.write('<tr class="even">')
                    else:
                        game_file.write('<tr class="odd">')
                    for i in range(len(each[1])-1):
                        if i == 9:
                            game_file.write('<td>%s</td>' % each[1][i])
                        elif i == 1:
                            game_file.write(
                                '<td>%s</td><td>%s</td><td>%s</td>' % (
                                    each[1][i],
                                    return_game_time(each[1][i]),
                                    nice_score(each[1][i])))
                        else:
                            game_file.write('<td>%s</td>' % each[1][i])
                    game_file.write('</tr>')
                    counter += 1
            game_file.write('</table>')
            now = datetime.datetime.now()

            game_file.write('<p style="font-size:10px">Last updated %s</p>' % (
                now.strftime('%m/%d/%Y %I:%M%p')))
            game_file.write('</body>')
            game_file.write('</html>')

        try:
            with open(os.path.join(
                    filepath, 'week %02d %s rosters.csv' % (
                        week, year)), 'rb') as rosters_file:
                read_file = csv.reader(rosters_file)
                teams_imported = []
                team_scores = []
                for row in read_file:
                    teams_imported.append(row)
        except IOError:
            print 'No roster file "week %02d %s rosters.csv" found' % (
                week, year)
            sys.exit(1)

        for each in teams_imported:
            if each[0] != 'Team':
                temp_team = []
                temp_team.append(each[0])
                for i in range(1, len(each)):
                    temp_team.append(each[i])
                    temp_team.append(check_if_score(each[i]))
                team_scores.append(temp_team)
        for team in team_scores:
            score = 0
            for i in range(2, len(team), 2):
                score += team[i]
            team.append(score)

        #Sort scores by total points
        team_scores.sort(key=lambda x: (x[-1]), reverse=True)

        # Create HTML page with team results
        with open(os.path.join(
                filepath, 'week%02d-%s-%s-results.html' % (
                    week, year, season_type)), 'wb') as result_file:
            result_file.write(
                '%s<title>Week %s Fantasy Results</title>%s%s</head>' % (
                header, week, analytics, clear_cache))
            result_file.write('<body>')
            result_file.write('<table class="gridtable">')
            # Creates header based on:
                # 6 man roster (playoffs = 'POST') or
                # 11 man roster (regular = 'REG')
            if season_type == 'POST':
                result_file.write(
                    '<tr><th>Rank<th>Team<th>QB<th>QBpts<th>RB<th>RBpts<th>WR'
                    '<th>WRpts<th>TE<th>TEpts<th>K<th>Kpts<th>D<th>Dpts'
                    '<th>TOTAL</tr>')
            if season_type == 'REG':
                result_file.write(
                    '<tr><th>Rank<th>Team<th>QB<th><th>QB<th><th>RB<th><th>RB'
                    '<th><th>RB<th><th>WR<th><th>WR<th><th>WR<th><th>TE<th>'
                    '<th>D<th><th>K<th><th>TOTAL</tr>')
            counter = 0
            for each in team_scores:
                if counter % 2 == 0:
                    result_file.write('<tr class="even">')
                else:
                    result_file.write('<tr class="odd">')
                result_file.write('<td>%s</td>' % (counter+1))
                for i in range(len(each)-1):
                    result_file.write('<td>%s</td>' % (each[i]))
                if season_type == 'POST':
                    for j in range(len(each)-1, 13):
                        season_type.write('<td></td>')
                else:
                    for j in range(len(each)-1, 23):
                        result_file.write('<td></td>')
                result_file.write('<td>%s</td>' % (each[-1]))
                result_file.write('</tr>')
                counter += 1
            result_file.write('</table>')
            now = datetime.datetime.now()
            result_file.write(
                '<p style="font-size:10px">Last updated %s</p>' % (
                    now.strftime('%m/%d/%Y %I:%M%p')))
            result_file.write('</body>')
            result_file.write('</html>')

        if season_type == 'POST':
            #WRITE WEEK'S RESULTS (JUST TOTAL SCORE) TO A FILE TO BE
            #USED FOR CUMULATIVE SCORE COUNT
            import csv
            with open('week%02d-%s-%s-results.csv' % (
                    week, year, season_type), 'wb') as f:
                w = csv.writer(f)
                w.writerow(['Rank', 'Team', 'Total'])
                counter = 0
                for each in team_scores:
                    if season_type == 'POST':
                        w.writerow([str(counter+1), each[0], each[13]])
                    if season_type == 'REG':
                        w.writerow([str(counter+1), each[0], each[23]])
                    counter += 1

        #Different view for results:
        results_matrix = {}
        for each in result:
            results_matrix[each] = ['']*(len(teams_imported)+1)
            results_matrix[each][0] = result[each][25]
        for each in defense_results:
            results_matrix[each] = ['']*(len(teams_imported)+1)
            results_matrix[each][0] = defense_results[each][10]
        for each in results_matrix:
            i = 0
            for team in teams_imported:
                for selection in team:
                    if selection == each:
                        results_matrix[each][i+1] = results_matrix[each][0]
                        if results_matrix[each][1] == ' ':
                            results_matrix[each][1] = 1
                        else:
                            results_matrix[each][1] += 1
                        break
                    else:
                        results_matrix[each][i+1] = ' '
                i += 1

        # Create HTML page with matrix
        with open(os.path.join(
                filepath, 'week%02d-%s-%s-matrix.html' % (
                    week, year, season_type)), 'wb') as matrix_file:
            matrix_file.write(
                '%s<title>Week %s Fantasy Matrix</title>%s%s</head>' % (
                header, week, analytics, clear_cache))
            matrix_file.write('<body>')
            matrix_file.write(
                '<p style="font-size:10px">'
                'Mouse over teams for full team name'
                '</p>')
            matrix_file.write(
                '<p style="font-size:10px">Page will refresh every 3 minutes'
                ' while games are in progress.</p>')
            matrix_file.write('<table class="gridtable">')
            #Top row of matrix: player initials (hover to get player name)
            matrix_file.write(
                '<tr><th>Player<th>Pos<th><th>Points<th>'
                '<span title="# of owners">Own<span>')
            for each in teams_imported:
                if each[0] != 'Team':
                    matrix_file.write('<th><span title="%s">%s</span>' % (
                        each[0], league_owners[each[0]][0]))
            matrix_file.write('</tr>')
            #Row 1A = Full players name
            matrix_file.write(
                '<tr><th>'
                'Owner Name'
                '<th><th><th><th>')
            for each in teams_imported:
                if each[0] != 'Team':
                    matrix_file.write('<th><span title="%s">%s</span>' % (
                        each[0], league_owners[each[0]][1]))
            matrix_file.write('</tr>')
            #Second row of matrix: Score for the week
            matrix_file.write(
                '<tr><th>'
                '<span title="Total points so far">*</span>'
                '<th><th><th><th>')
            for each in teams_imported:
                if each[0] != 'Team':
                    for score in team_scores:
                        if str(each[0]) == str(score[0]):
                            matrix_file.write(
                                '<th><span title="Total points so far">'
                                '%s</span>' % (score[-1]))
            matrix_file.write('</tr>')
            #Third row of matrix:
            #How many players have played / are playing / will play
            matrix_file.write(
                '<tr><th>'
                '<span title="# played / # playing / # will play">*<span>'
                '<th><th><th><th>')
            for each in teams_imported:
                has_played, is_playing, will_play = 0, 0, 0
                if each[0] != 'Team':
                    for score in team_scores:
                        if str(each[0]) == str(score[0]):
                            for i in range(1, len(score)-1, 2):
                                if score[i] == '':
                                    will_play += 1
                                else:
                                    tn = strip_teamname(score[i])
                                    if game_current_or_past(tn) == 2:
                                        has_played += 1
                                    else:
                                        is_playing += 1
                            matrix_file.write(
                                '<th><span title="# played / # playing / # '
                                'will play">%s/%s/%s</span>' % (
                                    has_played, is_playing, will_play))
            matrix_file.write('</tr>')
            #Fourth row of matrix: similar to third row, but in percentage form
            matrix_file.write(
                '<tr><th>'
                '<span title="Percentage of week remaining">*<span>'
                '<th><th><th><th>')
            graph_list = []
            for each in teams_imported:
                time_remaining, count = 0, 0
                if each[0] != 'Team':
                    for score in team_scores:
                        if str(each[0]) == str(score[0]):
                            for i in range(1, len(score)-1, 2):
                                if score[i] == '':
                                   #game not started yet
                                    time_remaining += 1*60
                                    count += 1
                                else:
                                    tn = strip_teamname(score[i])
                                    if game_current_or_past(tn) == 2:
                                        #game completed
                                        time_remaining += 1*0
                                        count += 1
                                    else:
                                        #game in progress
                                        time_remaining += (
                                            calculate_game_remaining(tn))
                                        count += 1
                            time_total = count*60
                            percent_remain = (
                                float(time_remaining)/float(time_total))*100
                            matrix_file.write(
                                '<th>'
                                '<span title="Percentage of week remaining">'
                                '%.1f%s</span>' % (percent_remain, "%"))
                            for row in team_scores:
                                if row[0] == each[0]:
                                    score = row[-1]
                            graph_list.append(
                                (each[0], 100-percent_remain, score))
            matrix_file.write('</tr>')
            #print graph_list
            with open(os.path.join(
                    filepath, 'week%02d-%s-%s-graph.csv' % (
                        week, year, season_type)), 'ab') as graph_file:
                graph_writer = csv.writer(graph_file)
                graph_writer.writerows(graph_list)
            #Body of matrix, listed in order of QB, RB, WR, TE, K
            counter = 0
            positions = ['QB', 'RB', 'WR', 'TE', 'K']
            for j in range(len(positions)):
                for each in results_matrix:
                    if each in result:
                        # Since defenses are actually in the defense_results
                        # file, this ignores D
                        if result[each][2] == positions[j]:
                            # result[each][2] is a players position
                            # (QB, RB, WR, TE, K)
                            if results_matrix[each][1] != ' ':
                                # results_matrix[each][1] is how many teams own
                                # a player (default of ' ' is effectively 0)
                                if counter % 2 == 0:
                                    matrix_file.write('<tr class="even">')
                                else:
                                    matrix_file.write('<tr class="odd">')
                                matrix_file.write(
                                    '<td>%s</td><td>%s</td><td>%s</td>' % (
                                        each, result[each][2],
                                        return_game_time(result[each][1])))
                                for i in range(len(results_matrix[each])):
                                    matrix_file.write(
                                        '<td>%s</td>' % (
                                            results_matrix[each][i]))
                                matrix_file.write('</tr>')
                                counter += 1
            for each in results_matrix:
                if each not in result:
                    if results_matrix[each][1] != ' ':
                        if counter % 2 == 0:
                            matrix_file.write('<tr class="even">')
                        else:
                            matrix_file.write('<tr class="odd">')
                        matrix_file.write(
                            '<td>%s Defense</td><td>%s</td><td>%s</td>' % (
                                each, 'D', return_game_time(each)))
                        for i in range(len(results_matrix[each])):
                            matrix_file.write(
                                '<td>%s</td>' % results_matrix[each][i])
                        matrix_file.write('</tr>')
                        counter += 1
            #Fourth row of matrix: similar to third row, but in percentage form
            matrix_file.write(
                '<tr><th>'
                '<span title="Percentage of week remaining">*<span>'
                '<th><th><th><th>')
            graph_list = []
            for each in teams_imported:
                time_remaining, count = 0, 0
                if each[0] != 'Team':
                    for score in team_scores:
                        if str(each[0]) == str(score[0]):
                            for i in range(1, len(score)-1, 2):
                                if score[i] == '':
                                   #game not started yet
                                    time_remaining += 1*60
                                    count += 1
                                else:
                                    tn = strip_teamname(score[i])
                                    if game_current_or_past(tn) == 2:
                                        #game completed
                                        time_remaining += 1*0
                                        count += 1
                                    else:
                                        #game in progress
                                        time_remaining += (
                                            calculate_game_remaining(tn))
                                        count += 1
                            time_total = count*60
                            percent_remain = (
                                float(time_remaining)/float(time_total))*100
                            matrix_file.write(
                                '<th>'
                                '<span title="Percentage of week remaining">'
                                '%.1f%s</span>' % (percent_remain, "%"))
            #Third row of matrix:
            #How many players have played / are playing / will play
            matrix_file.write(
                '<tr><th><span title="# played / # playing / # will play">'
                '*<span><th><th><th><th>')
            for each in teams_imported:
                has_played, is_playing, will_play = 0, 0, 0
                if each[0] != 'Team':
                    for score in team_scores:
                        if str(each[0]) == str(score[0]):
                            for i in range(1, len(score)-1, 2):
                                if score[i] == '':
                                    will_play += 1
                                else:
                                    tn = strip_teamname(score[i])
                                    if game_current_or_past(tn) == 2:
                                        has_played += 1
                                    else:
                                        is_playing += 1
                            matrix_file.write(
                                '<th><span title="# played / # playing / # '
                                'will play">%s/%s/%s</span>' % (
                                    has_played, is_playing, will_play))
            matrix_file.write('</tr>')
            #Second row of matrix: Score for the week
            matrix_file.write(
                '<tr><th>'
                '<span title="Total points so far">*</span>'
                '<th><th><th><th>')
            for each in teams_imported:
                if each[0] != 'Team':
                    for score in team_scores:
                        if str(each[0]) == str(score[0]):
                            matrix_file.write(
                                '<th><span title="Total points so far">'
                                '%s</span>' % (score[-1]))
            matrix_file.write('</tr>')
            #Top row of matrix: player initials (hover to get player name)
            matrix_file.write(
                '<tr><th>Player<th>Pos<th><th>Points<th>'
                '<span title="# of owners">Own<span>')
            for each in teams_imported:
                if each[0] != 'Team':
                    matrix_file.write('<th><span title="%s">%s</span>' % (
                        each[0], league_owners[each[0]][0]))
            matrix_file.write('</tr>')

            #print team_scores
            #Fifth row of matrix:
            # experimentally extrapolate week's score based on amount remaining
            #matrix_file.write(
            #    '<tr><th>'
            #    '<span title="Experimental score">*<span>'
            #    '<th><th><th><th>')
            #for each in teams_imported:
            #    time_remaining, count = 0, 0
            #    if each[0]!='Team':
            #        for score in team_scores:
            #            if str(each[0]) == str(score[0]):
            #                for i in range(1,len(score)-1, 2):
            #                    if score[i]=='':
            #                        #game not started
            #                        time_remaining += 1*60
            #                        count += 1
            #                    else:
            #                        tn = strip_teamname(score[i])
            #                        if game_current_or_past(tn)==2:
            #                            #game completed
            #                            time_remaining += 1*0
            #                            count += 1
            #                        else:
            #                            #game in progress
            #                            time_remaining += calculate_game_remaining(tn)
            #                            count += 1
            #                time_total = count*60
            #                if time_remaining != time_total:
            #                    experiment_score = ((float(time_total)/(time_total-time_remaining))*score[-1])/11
            #                else:
            #                    experiment_score = 0
            #                matrix_file.write(
            #                   '<th><span title="Points per player">'
            #                   '%.1f</span>' % (experiment_score))
            #matrix_file.write('</tr>')
            #End of table
            matrix_file.write('</table>')
            now = datetime.datetime.now()
            matrix_file.write(
                '<p style="font-size:10px">Last updated %s</p>' % (
                    now.strftime('%m/%d/%Y %I:%M%p')))
            matrix_file.write(
                '<p style="font-size:10px">'
                'Only players that have scored are shown.</p>')
            matrix_file.write('</body></html>')

            c_teams = {}
            filename_base = 'week01-2013-REG-graph'
            filepath = os.path.dirname(os.path.abspath(__file__))
            filename = 'week%02d-%s-%s-graph.csv' % (
                week, year, season_type)
            with open(os.path.join(
                    filepath, filename), 'rb') as graph_file:
                r = csv.reader(graph_file)
                for row in r:
                    if row[0] != 'Team':
                        if row[0] not in c_teams:
                            c_teams[row[0]] = [[row[1]], [row[2]]]
                        else:
                            if row[1] not in c_teams[row[0]][0]:
                                c_teams[row[0]][0].append(row[1])
                                c_teams[row[0]][1].append(row[2])
            '''
            ax = plt.subplot(121)
            colormap = plt.cm.gist_ncar
            plt.gca().set_color_cycle(
                [colormap(i) for i in np.linspace(0, 0.9, 20)])
            for team in c_teams:
                complete = c_teams[team][0]
                score = c_teams[team][1]
                ax.plot(complete, score, label=team)
            ax.set_xlabel('Percent Complete')
            ax.set_ylabel('Points')
            ax.legend(
                loc="upper left",
                bbox_to_anchor=(1.02, 1),
                borderaxespad=0.,
                prop={'size': 10})
            '''
            ax = plt.subplot(121)
            colormap = plt.cm.gist_ncar
            plt.gca().set_color_cycle(
                [colormap(i) for i in np.linspace(0, 0.9, 20)])

            for team in c_teams:
                complete = c_teams[team][0]
                score = c_teams[team][1]
                ax.plot(complete, score, label=team)
            ax.set_xlabel('Percent Complete')
            ax.set_ylabel('Points')
            #xlim([0, 100])
            ax.set_autoscalex_on(False)
            ax.legend(
                loc="upper left",
                bbox_to_anchor=(1.02, 1),
                borderaxespad=0.,
                prop={'size': 10},
                ncol=2)
            savefig(
                os.path.join(filepath, 'week%02d-%s-%s-graph.png' % (
                    week, year, season_type)),
                bbox_extra_artists=[plt.legend])
            ax.clear()

        if season_type == 'POST':
            from totalpoints import add_all_points
            add_all_points(year, week)

        print 'Task complete.  Upload files to ftp.'

        # Attempt to upload game, matrix, results,
        # and graph image files automatically to ftp.
        upload_files_to_ftp(week, year, season_type, filepath)
        print 'sleeping for 180 seconds at %s' % (
            now.strftime('%m/%d/%Y %I:%M%p'))
        time.sleep(180)
