### KAGGLE GRABBER

#### Mode of operation:

It grabs Kaggle top-users from [Kaggle Rankings](https://www.kaggle.com/rankings) by sending requests to:
`https://www.kaggle.com/rankings.json?group=competitions&page=3&pageSize=20` (found via Developer Tool Interface - F12).

You can choose between four groups: `Competitions`, `Datasets`, `Kernels` & `Discussion`  
and between two modes: `get all` and `page limit`.

Choosing the `get all` mode will give you the full list of participants with the folowing coloumns: 
'USERNAME', 'FULLNAME', 'LINK', 'POINTS', 'TIER'.

Choosing the `page limit` mode will also turn on the GITHUB CHECKER: 
It will check if user with the same name in 'USERNAME' coloumn exists on GitHub and will give you the full list of participants plus extra coloumns: 'GITHUB LINK', 'GITHUB LOCATION', 'GITHUB EMAIL', 'GITHUB COMPANY' if such user exists and 'null' if not.

This script requiers [Python3](https://www.python.org/), [Requests module](https://2.python-requests.org/en/master/).

#### Preparings:

[Create your token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

Just copy your token directly into the code (search for the comment marker in the code):

`headers = {"Authorization": "Token " +  "yourabcdefgh0123token"}`

#### How to launch:
* Open cmd/powershell/terminal
* `cd ~/path to script directory`
* `python3 ./kaggle-grabber.py`
* Follow further program instructions

#### If you want to make it easily executable on linux:
Make a new empty `kaggle-grabber.py` file in the directory where you want to store it with `touch kaggle-grabber.py` command

Add `#!/usr/bin/python3` at the top of the script

Copy all of the code to the new file & save it

Run: `chmod +x kaggle-grabber.py` 

Add a Directory with your script to `$PATH:` permanently by running the following in Terminal:`nano ~/.bashrc`

Add in the end of the file `PATH=$PATH:~/YOUR NEW PATH TO SCRIPT`, mark it with `##PATH##` for further needs

Save & exit wtih: `ctrl+O` `ctrl+X`

Run: `source ~/.bashrc`

Confirm changes: `echo $PATH`

You'll see the path to your new directory in the end of the line

Now you can launch it in Terminal from every directory by running: `kaggle-grabber.py` 

