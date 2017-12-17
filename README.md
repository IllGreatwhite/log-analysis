# Log Analysis Project

## Brief Explanation:
This project focuses on our newly learnt SQL skills, we were challenged to write code 
to access the database news and find out three pieces of information:
- The three most popular articles
- The most popular writers
- the highest percentage of errors in one day

## How to install and run:

You need a few things to make this code work, first of all you need to download:
+ [Oracle VirtualBox](https://www.virtualbox.org/) (check troubleshooting section before installing).
+ [vagrant](https://www.vagrantup.com/).
+ [git](https://git-scm.com/).
+ [this vagrantFile](https://github.com/udacity/fullstack-nanodegree-vm).
+ the files in this repository

After downloading and installing this folow these steps:

1. Go to your downloads and extract the vagrantFile and the files in this repository to your prefered destination. for this example we will use Desktop.
make sure to save these files inside the vagrant file.

2. once everything is in the correct location, right click on vagrant file and select 'git bash here' 

3. once its open, run `$ vagrant up` and wait for the machine to install, it will take a while

4. After the machine has successfully installed you will get your git bash command line back. now enter `$ vagrant ssh` and this will log you into your virtual machine. You can navigate through your linked files using ls. when ready cd into the vagrant file and check that news.sql is there and news-data.py.

5. To connect to the database, type in the command `psql -d news -f newsdata.sql`, this will connect you to the database. Once connected type `psql news` toenter the database where you can add the views listed below.

6. Once you have created all the views you can either exit the database to the virtual machine or open a new window, it doesnt matter, all you have to do is run python news-data.py in your virtual machine commandline to see the results of the code.

## Modifications and Contributions:

If you fancy having a look at how i did, please feel free to download and have a nose about. There are comments in the code but if you get stuck im more than happy to explain it to you. If you find any bugs please let me know!

## Troubleshooting:

I would reccomend downloading a previous version of bof Vagrant and Virtual box as I experienced trouble trying to get the latest versions to run correctly on my machine.
Also if you experience any troubles i would reccomend turning off your Onedrive as this can affect it. check out [this](https://github.com/hashicorp/vagrant/issues/9110#issuecomment-339635527) for more info.
## Views:

1. `first_answer`:
```SQL
create view first_answer as
select articles.title, count(*) as num
from articles, log
where log.path = concat('/article/', articles.slug)
group by articles.title, log.path
order by num desc limit 3;
``` 

2. `best_author`:
```SQL
create view best_author as
select authors.name, count(*) as views
       from authors, articles, log
       where authors.id = articles.author
         and log.path = concat('/article/', articles.slug)
       group by authors.name
       order by views desc;
```

3. `total`:
```SQL
create view total as
select time::date, status
from log;
```

4. `failed`:
```SQL
create view failed as
select time, count(*) as num
from total
where status = '404 NOT FOUND'
group by time;
```

5. `allstatus`:
```SQL
create view allstatus as
select time, count(*) as num
from total
where status = '404 NOT FOUND'
or status = '200 OK'
group by time;
```

6. `count_percent`:
```SQL
create view count_percent as
select allstatus.time, allstatus.num as numall, failed.num as numfailed, failed.num::double precision/allstatus.num::double precision * 100 as percentagefailed
from allstatus,
failed
where allstatus.time = failed.time;
```

