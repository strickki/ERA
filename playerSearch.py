import requests
import json
import pandas as pd
from openpyxl import load_workbook

auth_token = "eyJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJodHRwczovL2R1cHIuZ2ciLCJpYXQiOjE2OTUyMTk2MDEsImp0aSI6IjY5NDA2OTAzNDQiLCJleHAiOjE2OTc4MTE2MDEsInN1YiI6ImMzUnlhV05yT1RjME0wQjVZV2h2Ynk1amIyMD0ifQ.MUCxJ06uYNC-u7zVrTBhmecFxsIEriQyZ8LEAPL9ZB8mYr1eH21ufJAUwvwwWpHu0Ag7NrtKug9l57BtwePIDWdXpq7xsJkfar_BBIwu1QaKsJlxakCjk2ZHdLHRopXMLOE5k_Q9dnmwSys_Qq203tVfyETQEBfWszCdY8zO4E44_N89cg4hUszVh4khxMaXTW41nRg6UyaDbT2DV3nSzQObSiCNsotiRJxQY6zZtMupmHnbzpVMaFycNwFh865Oy0Sy8mjvXi_-hIS0Fdgml6zJLqg28FENlQwsKfaLlT2OzEl70LrG7IFgclUVrolHoDatDv39tgXv7vg5N-yg2A"


def get_data(name):
    headers = {
        "Authorization": "Bearer " + auth_token,
        "Content-type": "application/json"
    }
    data = {
        "limit":10,
        "offset":0,
        "query":name,
        "exclude":[
            
        ],
        "includeUnclaimedPlayers":True,
        "filter":{
            "lat":30.0183494,
            "lng":-95.623966,
            "rating":{
                "maxRating":None,
                "minRating":None
            }
        }
    }
    version = "v1.0"
    url = "https://api.dupr.gg/player/" + version + "/search"
    response = requests.post(url, headers=headers, json=data)
    
    if(response.status_code == 200):
        response = response.json()
    else:
        print("Error with accessing DUPR endpoint")
        exit()
    
    firstName = response['result']['hits'][0]['firstName']
    lastName = response['result']['hits'][0]['lastName']
    doublesRating = response['result']['hits'][0]['ratings']['doubles']
    singlesRating = response['result']['hits'][0]['ratings']['singles']
    
    print(firstName + ' ' + lastName + '\'s ' + 'doubles rating is: ' + doublesRating); 
    print(firstName + ' ' + lastName + '\'s ' + 'singles rating is: ' + singlesRating); 
    
    # TODO: Excel functionality 
    workbook = load_workbook(filename="ERA-Usernames.xlsx")
    sheet = workbook.active
    print(sheet["A1"].value)
   

    
get_data("rob rhett")