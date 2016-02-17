THE RED SCRAP PROJECT DJANGO EDITION
====================================

1.0) INTRODUCTION AND BACKGROUND [motivation].
----------------------------------------------
The motivation of this project was from the fact that alot of unemployed people out there search exhaustively on different
job boards trying to find that perfect job. I personally didnt like the fact that there so many job boards, some which may
specialize on a specific sector of the industry but may lack the jobs that you wanted to apply for even though they were 
available on other job boards. The whole process is also exhausting and actually takes alot from the candidate who is looking
for that perfect job. So I decided to extend the Red scrap project that i had done with scrapy to a django version that collects
all the jobs from a specific link and can be programmed to collect it periodically.

1.1) HOW IT WORKS.
------------------
This is a back-end process that has implemented a Solr instance to create a search bar that queries the backend data. However, for this to work you as a programmer need to specify what you want in the jobad_text.txt. I added an example of a hyperlink text object but I leave the rest to you. On top of that you need to add the Solr instance into your environment and build the index. If you feel that solr isnt the search engine you want, feel free to change it to whatever you want i.e Whoosh, Elastic beanstalk etc.

if you have read this far [here is a gift for you my good friend](http://imgur.com/gallery/2RHOuPi). Who says documentation has to be strict.. Bet half of you laughed and the other half got kind of happy-frustrated. 

The project uses Django, Scrapy and Django-Dynamic-Scraper to scrape the links you provide. It then uses, Django Celery and Kombu for creating/executing cron tasks and transport respectively. 

1.1) PREREQS YOU MIGHT NEED TO KNOW BEFORE RUNNING THIS PROJECT.
-----------------------------------------------------------------
you need to have a familiarity with basic django. This project will be implemented with django 1.9 so the basic:
  1) python manage.py migrate- for initial db migrations
  2) python manage.py runserver - firing up the server on http://127.0.0.1:8000
  
1.1.1) Get the project.
-----------------------
To get the project from this repo simply use the 'git' command and clone it::

    git clone "https://github.com/cmwaura/Final_Red_Scrap.git"

1.1.2) Requirements needed for the project
-------------------------------------------

you will need the python2.7 interpreter and pip installed in the computer. you will also need the virtualenv or virtualenv wrapper installed in your computer and activated to create your env.
All the requirements have been added on the requirements.txt file in the project. Once you have the project simply::

     pip install -r requirements.txt

and all the requirements will be installed for you. For people using a Linux distro this should be enough for you. However
for people using windows you will need an extra addition of [pywin32.exe](https://sourceforge.net/projects/pywin32/). Install it to your local drive then use easy_install to add it to your environment::

    easy_install C:\>path\to\your\pywin32\install
    
