# xmr-bot
xmr-bot is a Discord bot for [nanopool](https://nanopool.org/) users, a mining pool for [Monero](https://www.getmonero.org/)<br>You can easily check the mining status on your Discord server.
## How to Use
Follow the steps below to use xmr-bot.<br>
1. Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and enable all intents.
2. Clone the xmr-bot repository, create a `.env` file, and add the following.
```
TOKEN=[Your created Discord bot token]
ADDRESS=[The wallet address you use on nanopool]
XMRLANG=EN
```
If XMRLANG is set to JP, it will be changed to the Japanese version

3. Invite the Discord bot to the server where you want to use it (make sure to check the `bot` and `applications.commands` scopes).
4. Use the following command to install the required libraries
```
pip3 install -r requirements.txt
```
5. Finally, run `main.py`, and the xmr-bot will be up and running!
