from utils.cmd_runner import CMD_RUNNER


class DOCKER(CMD_RUNNER):
    def __init__(self) -> None:
        pass

    def build(self, name, path: str):
        CMD = f"docker build -t {name} {path}"
        self._runCmd(CMD)

    def run(self, name, cpu="0.1", ram="512m"):
        CMD = f'docker run -d --cpus={cpu} --memory={ram} {name}'
        self._runCmd(CMD)
