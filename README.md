# Discord-Bot

This repository is dedicated to collecting custom Discord bots, each designed for specific tasks and use cases.

## Project Structure

The toolkit is organized as follows:

### src/main/

- `task_notifier_bot.py`: A Python script that sends a notification to a specific Discord channel based on the job status, then closes the bot.

## Future Plans

- `suou_yuki.py`: (Planned) A Discord bot inspired by _周防 有希_, a character from the anime _時々ボソッとロシア語でデレる隣のアーリャさん_.

## Installation Requirements

To run the scripts, you'll need the following libraries installed:

```zsh
# Install discord.py module
$ pip install discord.py
```

```text
- json
- argparse
- os
- sys
```

## Setting Up the Bot Token

To run the bots, you need to create a JSON file that stores your bot's token. Follow the steps below:

1. Create a `bot_token.json` file in the `configs` folder.

2. Inside the `bot_token.json` file, add the following structure and replace `YOUR_BOT_TOKEN` with your actual bot token:

```json
{
  "YOUR_BOT_TOKEN": "YOUR_BOT_TOKEN"
}
```

3. **Make sure the token is kept private and is not shared publicly.**

---

# Discord-Bot

本倉庫專門收集客製化的 Discord 機器人, 每個機器人都為特定任務和使用案例而設計

## 專案結構

工具包的組織結構如下:

### src/main/

- `task_notifier_bot.py`: 一個用於根據工作狀態發送通知至指定 Discord 頻道的 Python 腳本, 發送完訊息後關閉機器人

## 未來計劃

- `suou_yuki.py`: (計劃中) 靈感來自動畫 _時々ボソッとロシア語でデレる隣のアーリャさん_ 中的角色 _周防 有希_ 的 Discord 機器人

## 安裝需求

運行這些腳本, 您需要安裝以下庫:

```zsh
# 安裝 discord.py 模組
$ pip install discord.py
```

```text
- json
- argparse
- os
- sys
```

## 設定機器人 Token

要運行機器人, 您需要創建一個存儲機器人 Token 的 JSON 文件, 請按照以下步驟操作:

1. 在 `configs` 文件夾中創建一個 `bot_token.json` 文件。

2. 在 `bot_token.json` 文件中, 加入以下結構, 並將 `YOUR_BOT_TOKEN` 替換為您的實際機器人 Token:

```json
{
  "YOUR_BOT_TOKEN": "YOUR_BOT_TOKEN"
}
```

3. **確保您的 Token 保持私密, 切勿公開分享**
