import os
import shutil
import uvloop
from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram import filters
from utils import GITHUB, DOCKER, inc_user, repo_count, CMD_RUNNER
import time

uvloop.install()
app = Client(
    "techzdeployer",
    "23636845",
    "d757ec9d2b7f09f474947ad3a2befd00",
    bot_token="6221266001:AAFvwYhd4xgzSCFdHf2Q6b8C_aacGbG1Cgk",
)


@app.on_message(filters.command(["start", "help"]) & filters.private)
async def start(client: Client, message: Message):
    await message.reply_text(
        """**💠 TechZDeployer - Deploy Your Apps For Free**

🧲 **Two Apps For Free**
- 0.1 core cpu
- 512 mb ram

♻️ **How To Use?**

**1.** Get github link of your repo
**2.** Your repo must contain a valid docker file
**3.** Send /deploy <repo-link> to Deploy your app
**4.** Done. Your app will get deployed on our server
"""
    )


@app.on_message(filters.command("deploy") & filters.private)
async def deploy(client: Client, message: Message):
    try:
        if repo_count(message.from_user.id) >= 2:
            return await message.reply_text(
                "❌ **You already have deployed your two free apps**\n\nContact @TechZBots_Support for more"
            )

        path = None
        url = message.text.split(" ")[1]
        if not url.startswith("https://github.com"):
            if not url.startswith("https://ghp"):
                await message.reply_text("❗️ **Not a valid github url**")
                return

        if not GITHUB.check_dockerfile(url):
            await message.reply_text("❗️ **Dockerfile not found**")
            return

        msg = await message.reply_text("🔄 **Cloning your repo**")
        name, path = GITHUB.clone(url)
        time.sleep(1)

        try:
            await msg.edit_text("🏗 **Building your app**")
        except:
            pass
        await DOCKER.build(name, path, msg)
        time.sleep(3)

        try:
            await msg.edit_text("🏃 **Starting your app**")
        except:
            pass
        DOCKER.run(name)
        inc_user(message.from_user.id, name, url)
        time.sleep(2)
        GITHUB.delete(path)

        await msg.edit_text("✨ **Your app has been deployed succesfully**")

    except Exception as e:
        await message.reply_text(str(e))
        if path:
            GITHUB.delete(path)


@app.on_message(filters.command("removeall") & filters.user(1693701096))
async def removeall(_, message):
    CMD_RUNNER._runCmd("bash rm_docker.sh")
    await message.reply_text("Removed All Images And Containers")


def rm_cache():
    try:
        shutil.rmtree("repos")
        os.mkdir("repos")
    except Exception as e:
        print(e)


rm_cache()
print("Starting bot")
app.run()
