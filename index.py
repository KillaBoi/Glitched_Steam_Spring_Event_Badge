import requests
import json

defid = "73000"
key = "YOUR OAUTH TOKEN"

url = 'https://api.steampowered.com/ILoyaltyRewardsService/RedeemPointsForBadgeLevel/v1/'
data=[('access_token', key), ( 'defid', defid), ('num_levels', 'REPLACE_ME_WITH_NUMBER')]

x = requests.post(url, data = data)

if "communityitemid" in (x.text):
    print("Success!")
else:
    print("Failure, check to see if your inputs are correct!")

