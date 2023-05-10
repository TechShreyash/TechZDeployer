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

        logs = ""
        x = time.time()

        for chunk in streamer:
            if "stream" in chunk:
                for line in chunk["stream"].splitlines():
                    if '->' in line:
                        print(line.split("->")[0].replace("\n", "").strip() + "\n\n")
                        logs += line.split("->")[0].replace("\n", "").strip() + "\n\n"
                        y = time.time()
                        if y - x > 2:
                            await msg.edit(logs[-500:])
                            x = y

    def run(self, name, cpu="0.1", ram="512m"):
        CMD = f"docker run -d --cpus={cpu} --memory={ram} {name}"
        self._runCmd(CMD)
