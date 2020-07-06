## RoboNodeJSScan

Robot Framework Library for the NodeJSScan SAST Tool

**Supports Python 3.x only**

### Currently version 1.2

### Install Instructions
* You need docker to run this program
* Install the RoboNodeJSScan Library with `pip install RoboNodeJSScan`
* Create a `.robot` file that includes the keywords used by RoboNodeJSScan Library

#### Update
* Includes update that works with NodeJSScan with Semgrep Support.
* Directly leverages the `njsscan` Python API without needing additional docker containers, etc 


### Keywords

`run nodejsscan against source`

`| run nodejsscan against source  | source code path  | results file | controls (optional) |`

* source code path: where your ruby source code is located currently
* results file needs to be an absolute path with the file name that you want to generate results in. It generates as a JSON file
* controls - enables nodejsscan's `check_controls` feature that additionally operates as a passive scanner for HTTP Header security configs and so on. 
