# xmr-bot
xmr-bot is a Discord bot for [nanopool](https://nanopool.org/) users, a mining pool for [Monero](https://www.getmonero.org/)<br>You can easily check the mining status on your Discord server.
## Installation
Follow the steps below to use xmr-bot.<br>
1. Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications) and enable all intents.
![Screenshot from 2024-10-22 13-13-14](https://github.com/user-attachments/assets/211dd940-b113-4904-8888-fe195459d00f)
2. Clone the xmr-bot repository, create a `.env` file, and add the following.
```
TOKEN=[Your created Discord bot token]
ADDRESS=[The wallet address you use on nanopool]
XMRLANG=EN
```
If XMRLANG is set to JP, it will be changed to the Japanese version

3. Invite the Discord bot to the server where you want to use it (make sure to check the `bot` and `applications.commands` scopes).
![Screenshot from 2024-10-22 13-31-40](https://github.com/user-attachments/assets/739dcfc2-82b7-4bc8-a4b0-8c79ce757510)
4. Use the following command to install the required libraries
```
pip3 install -r requirements.txt
```
5. Finally, run `main.py`, and the xmr-bot will be up and running!
