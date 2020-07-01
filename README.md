# Glitched Steam Spring Sale 2019 Badge
Requirements for self hosting:
- You need to have at least 1000 Steam Points.
- NO INSTALLATION REQUIREMENTS, JUST UPLOAD TO YOUR OWN HOSTING PROVIDER OR EVEN RUN LOCALLY BECAUSE THAT WORKS!



Requirements for Python Script:
- PYTHON (MAKE SURE TO INSTALL IT TO PATH! ITS A TICKBOX AT THE BEGINNING OF THE INSTALLATION!)
- You need to have at least 1000 Steam Points.
- run `pip install requests` in cmd
- run `pip install json` in cmd

Replace **key = "YOUR OAUTH TOKEN"** with your oauth token, look below for instructions. Replace **('num_levels', 'REPLACE_ME_WITH_NUMBER')** with the number of badge levels you want to craft in a row, 1 being the minimum.

## Obtaining OAUTH token:

1. Go to [Steam Points Shop](https://store.steampowered.com/points/shop).
2. Open Dev Tools (F12 or Ctrl+Shift+I) and go to the Console tab
3. Enter and execute this:
```js
javascript:(function(){prompt("Here is your access token:",$J("[data-loyaltystore]").data("loyaltystore").webapi_token);})()
```
4. Use the OAuth token in this bot, replace it with "YOUR OAUTH TOKEN HERE"





