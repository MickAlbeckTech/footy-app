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
    "Souths": "https://www.nrl.com/players?competition=111&team=500005",
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
dict_of_teams ={}
#loop through team urls
for team in team_urls:
    #go to team page that has all their players
    driver.get(team_urls[team])

    time.sleep(20)
    #find all the individual players in the team
    player_names = driver.find_elements(By.CLASS_NAME, "card-themed-hero__name")

    list_of_players = []
    #add each player to the team list_of_players
    #TODO: maybe here instead of creating dict of team:players, I can just use team name, player name in url and go straight to player info and scrape weight etc from there and store that under player name
    for player in player_names:
        print(player.text.replace("\n", " "))
        list_of_players.append(player.text.replace("\n", " "))

    #add team and players to dictionary in format "team": list of players
    dict_of_teams[team] = list_of_players
    #end up with dictionary of all teams with lists of players
print(dict_of_teams)

    # with open("broncos.txt", "w", encoding="utf-8") as file:
    #     for player in player_names:
    #         print(player.text)
    #         #program is seeing players as 'adam', then 'reynolds' then 'ben', then 'hunt', etc
    #         file.writelines(player.text)




#TODO: how to store the dictionary of club: list_of_players without losing the info as soon as program finishes??
#TODO or maybe now use the dictionary to access each player and scrape their page for height, weight, age and image, in this same script and store all that under player name?

#TODO: use csv or json to store list of players for each club
#TODO: then use club and player's name to access their page like this https://www.nrl.com/players/nrl-premiership/broncos/payne-haas
#TODO: get their age, weight, height with Beautiful Soup or Selenium??
#TODO: store this info (and a photo?) somehow so that we don't have to access nrl.com for each user request