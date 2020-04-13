*** Settings ***
Library  /Users/abhaybhargav/Documents/Code/Python/RoboNodeJSScan/robonodejsscan/RoboNodeJSScan.py

*** Variables ***
${CODE_PATH}  /Users/abhaybhargav/Documents/code/node/NodeGoat/
${RESULTS_PATH}  /Users/abhaybhargav/Documents/code/python/RoboNodeJSScan/test

*** Test Cases ***
Run NodeScan against Source Code
    run nodejsscan against source  ${CODE_PATH}  ${RESULTS_PATH}