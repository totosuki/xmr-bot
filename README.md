# xmr-bot
xmr-bot is a Discord bot for [nanopool](https://nanopool.org/) users, a mining pool for [Monero](https://www.getmonero.org/)<br>You can easily check the mining status on your Discord server.
# Installation
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
(Currently, only JP and EN are supported!)

3. Invite the Discord bot to the server where you want to use it (make sure to check the `bot` and `applications.commands` scopes).
![Screenshot from 2024-10-22 13-31-40](https://github.com/user-attachments/assets/739dcfc2-82b7-4bc8-a4b0-8c79ce757510)
4. Use the following command to install the required libraries
```
pip3 install -r requirements.txt
```
5. Finally, run `main.py`, and the xmr-bot will be up and running!
# Commands
## xmr-addrees
Display the set XMR address.
## xmr-balance
Displays the current XMR balance in US dollars.<br><br>
<img width="306" alt="スクリーンショット 2024-10-22 21 03 43" src="https://github.com/user-attachments/assets/b0210621-5cd3-47a4-8fff-00d6dc61cdd1"><br>
If `XMRLANG=JP`, Japanese yen will be displayed.
## xmr-hashrate
Displays the average hashrate. xmr-hashrate has several features!<br><br>
<img width="442" alt="スクリーンショット 2024-10-22 21 05 43" src="https://github.com/user-attachments/assets/642e886d-e536-486b-877f-c74287b84f3c"><br><br>
(If you do not set the “hour” parameter, it will be averaged over 2 hours.)<br><br>
`hour=0` to display the current hashrate.<br><br>
<img width="316" alt="スクリーンショット 2024-10-22 21 12 59" src="https://github.com/user-attachments/assets/b7cfb867-4aad-4c2f-ba03-fb164879a237"><br><br>
Hashrate for each Worker can also be displayed.<br>
If the member parameter is set as follows, the average hashrate for the <b>last 2 hours</b> for that worker can be displayed.<br><br>
<img width="309" alt="スクリーンショット 2024-10-22 21 01 46" src="https://github.com/user-attachments/assets/1337af03-eb87-4edf-8ef2-14309bd7f3a8"><br>
<img width="287" alt="スクリーンショット 2024-10-22 21 36 32" src="https://github.com/user-attachments/assets/ed1e33ec-73cd-4146-9d6c-7b0a82e6247d">

## xmr-help
Displays the help for the XMR bot.
## xmr-member
Displays the current mining members.<br><br>
<img width="229" alt="スクリーンショット 2024-10-22 21 20 53" src="https://github.com/user-attachments/assets/ebd0bbc0-83c5-4a70-b4ac-5d38a74faef9">
