# Log Analysis Project

## Brief Explanation:
This project focuses on our newly learnt SQL skills, we were challenged to write code 
to access the database news and find out three pieces of information:
- The three most popular articles
- The most popular writers
- the highest percentage of errors in one day

## How to install and run:

You need a few things to make this code work, first of all you need to download [Oracle VirtualBox](https://www.virtualbox.org/), (check troubleshooting section before installing).
after that you need to download and install [vagrant](https://www.vagrantup.com/), also you will require [git](https://git-scm.com/), and to top it all off you'll need the these files (make sure to extract to an empty folder) .

Once you have all these downloaded and installed go to the file where you extracted the fullstack-nanodegree-vm and right click on the folder, select git bash here and once it has opened run `$vagrant up`
this should initialize the download of the virtual machine. It will take a while to complete so i reccomend going off and doing something else while you wait. 
finally once its stopped throwing weird code at you and you get you git bash console back, run `vagrant ssh` to access the virtual machine. 
once inside you can type `cd /vagrant` to access all the files, just go to news-data.py and type `python news-data.py` for the code to run.

## Modifications and Contributions:

If you fancy having a look at how i did, please feel free to download and have a nose about. There are comments in the code but if you get stuck im more than happy to explain it to you. If you find any bugs please let me know!

## Troubleshooting:

I would reccomend downloading a previous version of bof Vagrant and Virtual box as I experienced trouble trying to get the latest versions to run correctly on my machine.
Also if you experience any troubles i would reccomend turning off your Onedrive as this can affect it. check out [this](https://github.com/hashicorp/vagrant/issues/9110#issuecomment-339635527) for more info.
## Views:

1. `first_answer`:
```SQL
select articles.title, count(*) as num
from articles
join log on log.path
like concat('%', articles.slug, '%')
where log.status like '%200%'
group by articles.title, log.path
order by num desc limit 3;
``` 

2. `best_author`:
```SQL
select articles.author,count (*) as num
from articles
join on log.path
like concat('%', articles.slug, '%')
group by articles.author
order by num desc;
```

3. `total`:
```SQL
select time::date, status
from log;
```

4. `failed`:
```SQL
select time, count(*) as num
from total
where status = '404 NOT FOUND'
group by time;
```

5. `allstatus`:
```SQL
select time, count(*) as num
from total
where status = '404 NOT FOUND'
or status = '200 OK'
group by time;
```

6. `count_percent`:
```SQL
select allstatus.time, allstatus.num as numall, failed.num as numfailed, failed.num::double precision/allstatus.num::double precision * 100 as percentagefailed
from allstatus,
failed
where allstatus.time = failed.time;
```

