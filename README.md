# DHAutomaticCashSelling
What you will need to run this - 
-A node.js web server (API)
-A VPS with Python3

Run the files in the backend on your node webserver, and replace the COOKIEHERE (line 24) with your .ROBLOSECURITY COOKIE - https://roblox.fandom.com/wiki/.ROBLOSECURITY
Replace UNIVERSE ID here with your place's universe id (where the robux goes) (line 30) - https://devforum.roblox.com/t/how-do-i-get-universeid-from-placeid-roblox-api/780807
Publish it and copy web url

Open the Python bot, and replace the api.dahood.cash with your webservers weburl.
Run the bot and invite it to your server

Any questions, DM me on discord at 6Ex#6666

 ALL COMMANDS
!buy AMOUNT - calculates the price for the requested amount of da hood cash
!create - creates a ticket in the "BUYERS" category
!delete - deletes the ticket if the user made it (must be used in created ticket)
!revive - pings all open tickets to revive them (must be used by an admin)
!payments - gives a list of all payment options + links
!purchase AMOUNT - generates a custom ID for the user to purchase in-game (only can be used twice every 24 hours)


HOW AUTOMATED BUYING WORKS
-The user must choose how much da hood cash they would like. They can do !buy (amount) to check the price and stay in budget.
Example: They want 1 million da hood cash. They would type !buy 1000000 in the chat. The bot would return a price in robux. If they decide thats how much they want, then they would use the !purchase command.
They would do !purchase 1000000. Then the bot would spit out an ID and game link. They copy the ID and chat !buy (ID) in the roblox chat. It then prompts them to buy a product based on how much cash they want.
If they did !purchase 1000000, it would prompt them to spend 50 robux, as one million da hood cash is 50 robux.

This method eliminates time wasters and can make your buisness more efficient.

CREDITS
-Main credits go to 6Ex. (Discord Bot, In-Game Command Handler, Part of Web Api)
-Secondary Credits go to La Flame (critical part of web api, which creates the products the user purchases) 
