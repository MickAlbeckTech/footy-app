import requests
import bs4
import selenium
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()



#team page on nrl.com can be accessed by a unique number eg Souths is 5000005.
#Url is https://www.nrl.com/players?competition=111&team=500005
team_urls = {
    "south-sydney-rabbitohs": "https://www.nrl.com/players?competition=111&team=500005",
    "Broncos": "https://www.nrl.com/players?competition=111&team=500011",
    "Bulldogs": "https://www.nrl.com/players?competition=111&team=500010",
    "Cowboys": "https://www.nrl.com/players?competition=111&team=500012",
    "Dolphins": "https://www.nrl.com/players?competition=111&team=500723",
    "Dragons": "https://www.nrl.com/players?competition=111&team=500022",
    "Eels": "https://www.nrl.com/players?competition=111&team=500031",
    "Knights": "https://www.nrl.com/players?competition=111&team=500003",
    "Panthers": "https://www.nrl.com/players?competition=111&team=500014",
    "Raiders": "https://www.nrl.com/players?competition=111&team=500013",
    "Roosters": "https://www.nrl.com/players?competition=111&team=500001",
    "Manly": "https://www.nrl.com/players?competition=111&team=500002",
    "Sharks": "https://www.nrl.com/players?competition=111&team=500028",
    "Storm": "https://www.nrl.com/players?competition=111&team=500021",
    "Titans": "https://www.nrl.com/players?competition=111&team=500004",
    "Warriors": "https://www.nrl.com/players?competition=111&team=500032",
    "Tigers": "https://www.nrl.com/players?competition=111&team=500023"
}
dict_of_teams = {}
dict_of_players = {}
#loop through team urls
for team in team_urls:
    #go to team page that has all their players
    driver.get(team_urls[team])

    time.sleep(20)
    #find all the individual players in the team
    player_names = driver.find_elements(By.CLASS_NAME, "card-themed-hero__name")

    list_of_players = []
    #add each player to the team list_of_players
    for player in player_names:
        #extract string of player's name from webdriver object
        player_name = player.text.replace("\n", " ")
        list_of_players.append(player_name)


    #TODO: now we have list_of_players for current team, iterate through list and go to each player's page and extract weight, height, age, image?
    # and store in dictionary under player name (instead of dict of team: list of players)
    # eg {"Alex Johnston": ["185 cm", "95 kg", "31", "url-of-image ????"],
    #     "Fatty Smith": ["156 cm", 150 kg", "25", "url-of-image ????"]}
    for player_name in list_of_players:
        #create list to eventually go into dict_of_players
        player_stats = []
        #url needs player names in format name-name-name
        player_name_for_url = player_name.replace(" ", "-")
        print(player_name_for_url)
        # create url to go to player's page
        player_url = "https://www.nrl.com/players/nrl-premiership/" + team + "/" + player_name_for_url + "/"
        print(player_url)
        driver.get(player_url)

        # TODO: format of players name in url is not always name-name-name eg Campbell Graham is not working

        # search for height data
        try:
            player_height = driver.find_element(By.XPATH, "//*[contains(text(), ' cm')]")
            print(player_height.text)
            player_stats.append(player_height.text)
        except:
            print("no height data for this player")
            player_stats.append("no height data for this player")

        # search for weight data
        try:
            player_weight = driver.find_element(By.XPATH, "//*[contains(text(), ' kg')]")
            print(player_weight.text)
            player_stats.append(player_weight.text)
        except:
            print("no weight data for this player")
            player_stats.append("no weight data for this player")

        dict_of_players[player_name] = player_stats
        print(dict_of_players)


#TODO: convert cm and kg to feet/inches and stones/lbs, and store that info in player_stats as well

#TODO: how to store the dictionary of players without losing the info as soon as program finishes??

#TODO: use csv or json to store data for each player

#TODO: store this info (and a photo?) somehow so that we don't have to access nrl.com for each user request

