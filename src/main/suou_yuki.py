import asyncio
import random

import discord
from discord.ext import commands

# 設定並創建第一個 Bot 實例
intents1 = discord.Intents.default()
intents1.message_content = True  # 啟用獲取訊息內容的權限
bot1 = commands.Bot(command_prefix="!", intents=intents1)  # 使用 "!" 作為指令前綴

# 設定並創建第二個 Bot 實例
intents2 = discord.Intents.default()
intents2.message_content = True  # 啟用獲取訊息內容的權限
bot2 = commands.Bot(command_prefix="", intents=intents2)  # 不使用指令前綴


# 定義第一個 Bot 的事件和指令
@bot1.event
async def on_ready():  # type: ignore
    print(f"Bot 1 已登入為 {bot1.user}")  # 當 Bot 1 完成登入時，在控制台顯示訊息


# 食物清單，用於隨機選擇
food = [
    "控肉飯",
    "陽春麵",
    "蛋花麵",
    "鐵板燒",
    "肉羹麵",
    "沙拉",
    "鍋燒麵",
    "臭豆腐",
    "麵包",
    "火鍋",
    "泡麵",
    "自助餐",
    "粥",
    "麥當勞",
    "肯德基",
    "摩斯",
    "拉亞",
]


@bot1.command()
async def 吃飯(ctx):
    EatFood = random.sample(food, 1)[0]  # 隨機選擇一種食物
    await ctx.send(EatFood + "！")  # 回覆選擇的食物名稱


# 定義第二個 Bot 的事件和指令
@bot2.event
async def on_ready():
    print(f"Bot 2 已登入為 {bot2.user}")  # 當 Bot 2 完成登入時，在控制台顯示訊息


@bot2.event
async def on_message(message):
    # 確保機器人不會回應自己的訊息
    if message.author == bot2.user:
        return

    # 檢查訊息內容並觸發相應的回應
    if "有希" in message.content:
        await message.channel.send("待った待った！")
    elif "艾莉" in message.content:
        await message.channel.send("お兄ちゃんがアーリャさんに寝取られた！")

    # 允許命令處理器在不使用前綴時繼續工作
    await bot2.process_commands(message)


# 啟動兩個 Bot
async def main():
    await asyncio.gather(bot1.start("機器人1的TOKEN"), bot2.start("機器人2的TOKEN"))


# 運行事件循環
asyncio.run(main())
