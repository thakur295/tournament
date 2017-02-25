# Tournament-Results

## Introduction
Developing a database schema to store the game matches between players. Python code to query the given data and determine the winners of various games by Swiss System.

## Documents
* tournament.py : This file includes the basic functions required to evaluate and find the winner.
* tournament_test.py : This file Tests all the possible outcomes and raises an exception if conditions are not fulfilled.
* tournament.sql: This contains all the basic queries required in the project.

## Installtion
1. Install Virtual Box from: https://www.virtualbox.org/wiki/Downloads
2. Install Vagrant from: https://www.vagrantup.com/downloads.html
3. Start the virtual machine by using `vigrant up` command in your terminal.
4. After downloading all necessary files then login to the Linux Vm using `vagrant ssh` command in terminal.

## Steps To Run The Application:
1. Open terminal for Mac or Linux and Git Bash for Windows to run the application.
2. Change the directory to the cloned folder by using `cd /vagrant/tournament`
3. Now type `psql` in your terminal
4. Import the given sql file using `\i tournament.sql` command.
5. Run the file using `python tournament_test.py` command

