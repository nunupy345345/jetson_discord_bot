# Discord Bot for Jetson GPIO

このプロジェクトは、Jetson Orin Nano と 磁気リードスイッチ を用いて、
ドアの「開閉」をリアルタイムに検知し、Discordに自動通知するIoTシステムです。

JetsonのGPIOピンを使ってセンサー入力を読み取り、Python（discord.py ＋ Jetson.GPIO）でイベントを検出すると、Dockerコンテナ内のBotがDiscordのチャンネルに「ドアが開きました」「ドアが閉まりました」とメッセージを送信します。

環境構築にはDockerを用いており、JetPack 5系で動作確認をしました。
スラッシュコマンド /status で、現在のドア状態も確認できます。
## Discord bot TOKENの取得の仕方など
dicord developer portalでBotを作成し、TOKENを取得してください。
bot->restart TOKEN で確認できます。


channel IDを取得するには、Discordの設定で開発者モードを有効にし、通知したいチャンネルを右クリックして「IDをコピー」を選択してください。
.envファイルに以下のように設定してください。

```
DISCORD_BOT_TOKEN=あなたのBotトークン
DISCORD_CHANNEL_ID=通知したいチャンネルのID
```

## botのpermission

botには以下のpermissionが必要です。

- Send Messages
- Use Slash Commands
- View Channel

Permissions Integer : 2147494912
以下のURLでbotをサーバーに招待できます。
```
https://discord.com/oauth2/authorize?client_id=あなたのBotのClient ID&permissions=2147494912&scope=bot%20applications.commands
```
## 実行方法

```bash
docker compose up -d --build
```

## 使用機材
- [磁気リードスイッチ](https://www.amazon.co.jp/dp/B08XZ28DR9?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
- [Jetson orion Nano developer kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#intro)
- [micro SD card](https://www.amazon.co.jp/dp/B08PTPTMH5?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
