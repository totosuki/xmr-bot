# xmr-bot
xmr-botは、[monero](https://www.getmonero.org/)のマイニングプールである[nanopool](https://nanopool.org/)ユーザー向けの、Discordボット。<br>
Discordサーバーで、簡単にマイニング状況を確認できます。
## 使い方
以下の手順で、xmr-botを使用することが出来ます。<br>
1. [DiscordのDeveloper Potal](https://discord.com/developers/applications)でボットを作成し、intentsを全てオンにする。
2. xmr-botリポジトリをcloneして`.env`というファイルを作り、以下のように記述する。
```
TOKEN=[作成したDisocrdボットのトークン]
ADDRESS=[nanopoolで使用しているwalletアドレス]
```
3. Discordボットを使いたいサーバーに招待する。（scopeは`bot`と`applications.commands`にチェックを入れてください）
4. 最後に、`main.py`を実行したらxmr-botが動きます！
