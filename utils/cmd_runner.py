import subprocess
from utils.logger import LOGGER

logger = LOGGER("CMD_RUNNER")


class CMD_RUNNER:
    def __init__(self):
        pass

    def run(cmd):
        logger.info("Running command: " + cmd)
        results = subprocess.run(cmd.split(" "), capture_output=True, text=True)
        if results.returncode == 0:
            logger.info("Command executed successfully")
            return results.stdout
        else:
            logger.error("Command failed to execute")
            raise Exception(results.stderr)
