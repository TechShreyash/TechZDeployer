import subprocess
from utils.logger import LOGGER
logger = LOGGER("CMD_RUNNER")


class CMD_RUNNER:
    def __init__(self):
        pass

    def _runCmd(self, cmd):
        logger.info("Running command: " + cmd)
        with subprocess.Popen(cmd.split(" "), stderr=subprocess.PIPE,stdout=subprocess.PIPE) as process:
            
        if results.returncode == 0:
            logger.info("Command executed successfully")
            return results.stdout
        else:
            logger.error("Command failed to execute")
            raise Exception(results.stderr)
