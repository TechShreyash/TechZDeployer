import os
import shutil
import uvloop
from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram import filters
from utils import GITHUB, DOCKER

uvloop.install()
app = Client(
    "techzdeployer",
    "23636845",
    "d757ec9d2b7f09f474947ad3a2befd00",
    bot_token="6221266001:AAFvwYhd4xgzSCFdHf2Q6b8C_aacGbG1Cgk",
)


@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text("Bot is working")


@app.on_message(filters.command("deploy") & filters.user(1693701096))
async def deploy(client: Client, message: Message):
    try:
        path = None
        url = message.text.split(" ")[1]
        if not url.startswith("https://github.com"):
            if not url.startswith("https://ghp"):
                await message.reply_text("Not a valid github url")
                return

        if not GITHUB.check_dockerfile(url):
            await message.reply_text("Dockerfile not found")
            return

        message = await message.reply_text("Cloning your repo")
        name, path = GITHUB.clone(url)

        try:
            await message.edit_text("Building your app")
        except:
            pass
        DOCKER.build(name, path)

        try:
            await message.edit_text("Starting your app")
        except:
            pass
        DOCKER.run(name)
        GITHUB.delete(path)

        await message.edit_text("Your app has been deployed succesfully")

    except Exception as e:
        await message.reply_text(str(e))
        if path:
            GITHUB.delete(path)


def rm_cache():
    try:
        shutil.rmtree("repos")
        os.mkdir("repos")
    except Exception as e:
        print(e)


rm_cache()
print("Starting bot")
app.run()
