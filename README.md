# Mission to Mars
This repo contains files for an application that scrapes the web to get the latest information about the mission to mars. This has three major parts:
1. The flask app 
1. The index.html file 
1. Mars webscrapping file

## File Organization
All files are stored in the **Mission_to_Mars** main folder. 

* In this folder there is the **mission_to_mars jupyter notebook** that contains the code for the mars webscraping portion. There is a chromedriver that is used for the scrape and the **mars_scrape.py** file which is essential the same code as the jupyter notebook file. 
  
* The **mars_scrape.py** file defines a function that scrapes the web for data on the mission to mars. 

* There is a **static folder** which contains css styling info for the HTML.

* The **templates folder** contains the **index.html** file  

* Finally the **app.py** file contains the flask app that uses the a function defined in the **mars_scrape.py** file to crape the web for mars data then updated this to a MongoDB database. The app then pulls from this database to populate the html file where the data is vizualized in a web page.
