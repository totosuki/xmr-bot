# xmr-bot
xmr-botは、[monero](https://www.getmonero.org/)のマイニングプールである[nanopool](https://nanopool.org/)ユーザー向けの、Discordボット。<br>
Discordサーバーで、簡単にマイニング状況を確認できます。
## 使い方
以下の手順で、xmr-botを使用することが出来ます。<br>
1. [DiscordのDeveloper Potal](https://discord.com/developers/applications)でボットを作成し、intentsを全てオンにする。<br><br>
![Screenshot from 2024-10-22 13-13-14](https://github.com/user-attachments/assets/211dd940-b113-4904-8888-fe195459d00f)
3. xmr-botリポジトリをcloneして`.env`というファイルを作り、以下のように記述する。
```
TOKEN=[作成したDisocrdボットのトークン]
ADDRESS=[nanopoolで使用しているwalletアドレス]
```
3. Discordボットを使いたいサーバーに招待する。（scopeは`bot`と`applications.commands`にチェックを入れてください）<br><br>
![Screenshot from 2024-10-22 13-31-40](https://github.com/user-attachments/assets/739dcfc2-82b7-4bc8-a4b0-8c79ce757510)
4. 以下のコマンドを利用し、ライブラリをインストールする。
```
pip3 install -r requirements.txt
```
5. 最後に、`main.py`を実行したらxmr-botが動きます！
