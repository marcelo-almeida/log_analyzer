# Log Analyzer
This program can analyze data from a database and answer predefined questions
## Requirements
* Python 3.5.2
  [download here](https://www.python.org/downloads/)
* Vagrant 1.8.5
  [download here](https://www.vagrantup.com/downloads.html)
## How to run
* Install Python 3.5.2
* Install Vagrant 1.8.5
* Clone or Download the follow repository from Udacity:

  `https://github.com/udacity/fullstack-nanodegree-vm`

* In fullstack-nanodegree-vm execute these cmd commands:

  `cd vagrant`

  `vagrant up`

  `vagrant ssh`

* It's necessary have and run the newsdata.sql from udacity's material
* Clone this repository using these git commands:

  `git init`

  `git clone https://github.com/marcelo-almeida/log_analyzer.git`

* Copy all python files to vagrant directory
* init a new vagrant session `vagrant ssh` in a terminal
* From a vagrant terminal execute this command:
  `python news.py`
* The result will be shown in the terminal
  Note: if you want record the results in a file, use save_question_and_answers()
  from the news.py file instead print_question_and_answers()
## Copyright
The database file is not available in this repository, but has been used from udacity's material

It was used the vagrant config from udacity repository

  [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm)
