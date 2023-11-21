import requests
import json

request = requests.get('https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard')

print(request.json())