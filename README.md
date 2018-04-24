# Logs Analysis Project
## Project Description:
This project is a report tool that connects to a database, uses SQL queries to analyze the data, and prints out the answers to some questions. 

### PreRequisites:
- [Python3](https://www.python.org/)
- [Vagrant](https://www.vagrantup.com/)
- [VirtualBox](https://www.virtualbox.org/)



### Getting started:
1. Install python
2. Install Vagrant and VirtualBox

### The virtual machine:

There are a couple of different ways you can download the VM configuration.You can download and unzip this file: [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder. Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm. Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory. From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM.

### Download the data:

Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine. To build the reporting tool, you'll need to load the site's data into your local database. To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. Once you have the data loaded into your database, connect to your database using `psql -d news` and explore the tables using the `\dt` and `\d table` commands and select statements.

### Create the necessary tables and views:

Create view pop using `create view pop as Select title, count(*) as views from articles, log where log.path = concat('/article/', articles.slug) group by articles.title order by views desc;` 

### Run the queries:

Inside the virtual machine, run the tool using `python newsdb.py`