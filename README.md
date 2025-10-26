# Discord Bot for Jetson GPIO


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