from robot.api import logger
from njsscan.njsscan import NJSScan
import json


class RoboNodeJSScan(object):
    def __init__(self):
        pass

    def run_nodejsscan_against_source(self, code_path, results_path, controls=False):
        """
        Runs NodeJSScan against Source Path with the given path for the codebase and the path for the results as arguments
        param code_path 
        """
        self.source_path = code_path
        self.results_path = results_path
        try:
            scanner = NJSScan([code_path], json=True, check_controls=controls)
        except Exception as e:
            logger.error(e)
        
        try:
            results = scanner.scan()
            if results:
                with open(results_path, 'w') as resfile:
                    resfile.write(json.dumps(results))
        except Exception as be:
            logger.error(be)

        logger.info(
            "Successfully ran NodeJSScan against the src. Please find the *.json files in the results directory"
        )

