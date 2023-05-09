from utils.cmd_runner import CMD_RUNNER
import requests


class GITHUB(CMD_RUNNER):
    def __init__(self):
        pass

    def clone(self, url):
        name = ("_".join(url.split("/")[-2:])).lower()
        path = f"repos/{name}"

        CMD = "git clone " + url + f" {path}"
        self.run(CMD)
        return name, path

    def check_dockerfile(self, url):
        if "https://ghp_" in url:
            ghp_key = url.split("https://ghp_")[1].split("/")[0]

        if ghp_key:
            x = url.split("/")
            headers = {"Authorization": f"token {ghp_key}"}
            api_url = f"https://api.github.com/repos/{x[3]}/{x[4]}/contents/Dockerfile"
            res: dict = requests.get(api_url, headers=headers).json()
        else:
            x = url.split("/")
            api_url = f"https://api.github.com/repos/{x[3]}/{x[4]}/contents/Dockerfile"
            res: dict = requests.get(api_url).json()

        if res.get("name"):
            if res.get("name") == "Dockerfile":
                return True
            else:
                return False
        else:
            return False

    def delete(self, path):
        CMD = f"rm -rf {path}"
        self.run(CMD)
