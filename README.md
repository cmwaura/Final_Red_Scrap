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

1.1) PREREQ.S YOU MIGHT NEED TO KNOW BEFORE RUNNING THIS PROJECT.
-----------------------------------------------------------------
you need to have a familiarity with basic django. This project will be implemented with django 1.9 so the basic:
  1) python manage.py migrate- for initial db migrations
  2) python manage.py runserver - firing up the server on http://127.0.0.1:8000
  3) scrapy commands.
  
1.1.1) Get the project.
-----------------------
To get the project from this repo simply use the 'git' command and clone it::
    
    mkdir red_jobo #creates a new folder to compartmentalize the project
    cd red_jobo
    git clone "https://github.com/cmwaura/Final_Red_Scrap.git"
    
once  you have cloned the project simply::
    
    cd  sites
    ls  # to check whether manage.py is in the directory

1.1.2) Requirements needed for the project
-------------------------------------------

you will need the python2.7 interpreter and pip installed in the computer. you will also need the virtualenv or virtualenv wrapper installed in your computer and activated to create your env.
All the requirements have been added on the requirements.txt file in the project. Once you have the project simply::

     pip install -r requirements.txt

and all the requirements will be installed for you. For people using a Linux distro this should be enough for you. However
for people using windows you will need an extra addition of [pywin32.exe](https://sourceforge.net/projects/pywin32/). Install it to your local drive then use easy_install to add it to your environment::
 
    easy_install C:\>path\to\your\pywin32\install
    
1.2) RUNNING THE ADMIN.
-----------------------

before you try to run the admin, make sure that you are in the same directory as 'manage.py' by using ls/dir. If you are not please refer to sec 1.1.1.

Now that we are in the same directory, lets instantiate the db first. You can use whatever db you want as long as you specify on the settings.py file which database you are using. I will use the default sqlite::
    
    python manage.py migrate
    
    # now create your super user for your admin
    
    python manage.py createsuperuser #add your credentials and you are golden.
    
alright now start the django admin interface by typing::
    
    python manage.py runserver

navigate to your localhost:8000 and you should see the index page saying "hello World"

If you got till this point you are doing great!!

Access the admin interface by adding '/admin' to the url and add your credentials. you should be presented with a django admin
dashboard which is where the data will be displayed. 

something like this : 
![alt text](http://i.imgur.com/rnec5tr.png)

There are a couple of items that we can discuss in this documentation and a couple of others that i will advise you to look up 
since there is more documentation on it. For reference i will refer you to Django-Dynamic-Scraper since this project is built on that.

1.3 SCRAPER OBJECT CLASSES
--------------------------
Click on the scraper object classes in the Dynamic Scraper section. Add a name of a the class(in my case i used jobAds), then
at the bottom you will be faced  with a form similar to this one:

![alt text](http://i.imgur.com/ksbuK3c.png)

Add a base object attribute and all the other atributes after. 

1.3.1 Things to note:
---------------------
The base attribute is absolutely nessecary otherwise the spider will give you headaches and no one wants headaches. The attribute type for the base  is Base.

How to think of the base:
when scraping a objects using beautiful soup or scrapy, you always point the scraper to the vicinity that you want to get and write some piece of code along the lines of::

    for element in response.xpath('//div[@class="yay_me"):
          title = [title code here]...
          
well the base caters to the first xpath in the for-loop.

The second thing you should note when using the url of the title, you might want to add the id field of the url. Why, because later on we will automate the scraping procedure and also activate a checker that will look for repetitions of job posts based on url. If the url is already present, then the newly scraped post wont be saved in the db.

The attr type of url is 'DETAIL_PAGE_URL'.

Everything else should be tagged as standard.

1.3.2) Scraper
---------------
Once you have done the Scraper object classes and saved them , open the scraper. Add a name of what you want to call it and use the scroll down button to add the scraped obj class that you want. For status we will leave it as "MANUAL" and later automate it to "ACTIVE".

go to the scraper elements and using the scroll down button add the base with its own xpath and then add all the other attributes that you want. For reference you can use this pic;

![alt text](http://i.imgur.com/DL2eEKx.png)

This would be the dice xpath for other sites you might want to find out what their xpath is.

Things to note:

**Request page types:**

on the Request page type of the scraper, click the '+' to create a new page. Pull up the page and add main page to the page type and you should be golden.


1.3.3) Job websites
------------------
if you have a job website url that you want to scrape, go on and pull it up. On the search bar search the job you are looking for then get the url of the job in my case, i will use Dice.com. 

Now we on the last part before we run the spider. Open the job wesite link and give that bad boy a title. Then add the specific url to the job you are looking for . 

For the scraper add the name of the scraper on the drop list and then add a scraper runtime of 1. Save your work and then open the terminal.

1.4) Back to the terminal:

Go to the directory which hold the scrapy engine i.e scrapy.cfg. It should be on the same directory as django's manage.py directory. Type the following::

    scrapy crawl job_spider -a id=1 do_action=yes

at this point you will be calling the spider that is configured at the spiders.py and telling it to go to work. If everything was configured on point, then it should run and give you no log error messages. I will address the other part a little later

If things went well, then open the jobads tab in "mysites" and you should see something like this:

![alt text](http://i.imgur.com/P4FAx5u.png)

and there you have it. All the jobs scraped into your django ORM. Add a few more and play around with it.

1.4) DEBUGGING PART I:
-----------------------

So the scrape didnt work, first of all you should check to see whether you have the correct xpath and also whether the base to the xpath is right.
In the terminal type::
    $ scrapy shell "link" #link = link_you_want_to_scrape
    
    #inside the scrapy shell look for the xpath that you are interested in and type
    >>> response.xpath('//XPATH_BELONGS_HERE')

Check to see whether the desired output comes out.    

    
