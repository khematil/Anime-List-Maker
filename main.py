"""
Author: Kyle Hematillake --> k.hematillake@gmail.com
Date: 2021-08-27

"""


import requests


#Code Snippet from: . . .

def findByName(search):

    key = 0

    url = "https://jikan1.p.rapidapi.com/search/anime"


    headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
    'x-rapidapi-key': "b8bf8c37c3msh7b576ecd25a7611p13b689jsn7558bf6c60cf"
    }
    querystring = {"q": search}

    headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
    'x-rapidapi-key': "b8bf8c37c3msh7b576ecd25a7611p13b689jsn7558bf6c60cf"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.json()

    resultsDict = {}

    for i in result['results']:
        resultsDict["#"+str(key)] = {"title": i['title'], "rating": i["score"]}
        key+=1
        if key == 10:
            break

    return resultsDict
