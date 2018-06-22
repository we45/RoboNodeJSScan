## RoboNodeJSScan

Robot Framework Library for the NodeJSScan SAST Tool

**Supports Python 2.7.x for now**

### Install Instructions
* You need docker to run this program
* Pull the brakeman docker image: `docker pull abhaybhargav/nodejsscan`
* Install the RoboBrakeman Library with `pip install RoboNodeJSScan`
* Create a `.robot` file that includes the keywords used by RoboBrakeman Library


### Keywords

`run nodejsscan against source`

`| run nodejsscan against source  | source code path  | results path`

* source code path: where your ruby source code is located currently
* results path: where your results will be stored. An `.html` file and `.json` are generated as outputs