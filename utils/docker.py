from utils.cmd_runner import CMD_RUNNER
import docker
from docker import APIClient
import time

client = APIClient()


class DOCKER(CMD_RUNNER):
    def __init__(self) -> None:
        pass

    async def build(self, name, path: str, msg):
        # CMD = f"docker build -t {name} {path}"
        # self._runCmd(CMD)

        streamer = client.build(decode=True, path=path, tag=name)

        logs = "🏗 **Building your app**\n\n"
        x = time.time()

        for chunk in streamer:
            if "stream" in chunk:
                for line in chunk["stream"].splitlines():
                    if "Step " in line:
                        logs += line.replace("\n", "").strip() + "\n"
                        y = time.time()
                        if y - x > 1:
                            if len(logs) > 0:
                                try:
                                    await msg.edit(logs[-500:])
                                    x = y
                                except:
                                    pass

    def run(self, name, cpu="0.1", ram="512m"):
        CMD = f"docker run -d --cpus={cpu} --memory={ram} {name}"
        self._runCmd(CMD)
