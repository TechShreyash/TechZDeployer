import uvloop
import subprocess
from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram import filters

uvloop.install()
app = Client(
    "techzdeployer",
    "23636845",
    "d757ec9d2b7f09f474947ad3a2befd00",
    bot_token="6221266001:AAFvwYhd4xgzSCFdHf2Q6b8C_aacGbG1Cgk",
)

with open("cmds/deploy.txt") as f:
    DEPLOY_CMD = f.read().splitlines()
with open("cmds/update.txt") as f:
    UPDATE_CMD = f.read().splitlines()


def run_cmd(cmd):
    subprocess.run(cmd.split(" "))


@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply_text("Bot is working")


@app.on_message(filters.command("deploy"))
async def deploy(client: Client, message: Message):
    GIT_REPO_URL = message.text.split(" ")[1]
    CONTAINER_NAME = GIT_REPO_URL.split("/")[-2:]
    CONTAINER_NAME = CONTAINER_NAME[0] + "-" + CONTAINER_NAME[1]
    REPO_DIR = "/repos/" + CONTAINER_NAME.replace("-", "_").lower()

    for cmd in DEPLOY_CMD:
        cmd = (
            cmd.replace("GIT_REPO_URL", GIT_REPO_URL)
            .replace("CONTAINER_NAME", CONTAINER_NAME)
            .replace("REPO_DIR", REPO_DIR)
        )
        run_cmd(cmd)


@app.on_message(filters.command("update"))
async def udpate(client: Client, message: Message):
    GIT_REPO_URL = message.text.split(" ")[1]
    CONTAINER_NAME = GIT_REPO_URL.split("/")[-2:]
    CONTAINER_NAME = CONTAINER_NAME[0] + "-" + CONTAINER_NAME[1]
    REPO_DIR = "/repos/" + CONTAINER_NAME.replace("-", "_").lower()

    for cmd in UPDATE_CMD:
        cmd = (
            cmd.replace("GIT_REPO_URL", GIT_REPO_URL)
            .replace("CONTAINER_NAME", CONTAINER_NAME)
            .replace("REPO_DIR", REPO_DIR)
        )
        run_cmd(cmd)


app.run()
