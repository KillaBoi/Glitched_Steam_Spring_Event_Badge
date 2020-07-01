# Glitched Steam Spring Sale 2019 Badge
Requirements for self hosting:
- NONE, JUST UPLOAD TO YOUR OWN HOSTING PROVIDER OR EVEN RUN LOCALLY BECAUSE THAT WORKS!



Requirements for Python Script:
 -PYTHON (MAKE SURE TO INSTALL IT TO PATH! ITS A TICKBOX AT THE BEGINNING OF THE INSTALLATION!)
- You need to have at least 1000 Steam Points.
- run `pip install requests` in cmd
- run `pip install json` in cmd

Replace **key = "YOUR OAUTH TOKEN"** with your oauth token, look below for instructions. Replace **('num_levels', 'REPLACE_ME_WITH_NUMBER')** with the number of badge levels you want to craft in a row, 1 being the minimum.

## Obtaining OAUTH token:

View the video [HERE](https://www.youtube.com/watch?v=0_Bf4GOFAr0)

Nagivate to a emoticon that you haven't purchased yet and open it.

Next, press F12 and go to Network. Clear the page so that there is nothing there.

Then go ahead and purchase the item. You should see 3 requests to v1?access_token=... the access_token is your OAuth token.

Use the OAuth token in this bot, replace it with "YOUR OAUTH TOKEN HERE"





