import docker
from robot.api import logger
from docker.types import Mount

class RoboNodeJSScan(object):

    def __init__(self):
        self.client = docker.from_env()
        self.nodejsscan_docker = "abhaybhargav/nodejsscan"

    def run_nodejsscan_against_source(self, code_path, results_path):
        self.source_path = code_path
        self.results_path = results_path
        source_mount = Mount("/src", self.source_path, type = "bind")
        results_mount = Mount("/results", self.results_path, type = "bind")
        self.client.containers.run(self.nodejsscan_docker, mounts = [source_mount, results_mount])
        logger.info("Successfully ran NodeJSScan against the src. Please find the *.html and *.json files in the results directory")