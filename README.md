# Your LinkedIn post statistics
A python script that collects data (total amount of views, likes and comments) of your LinkedIn posts.

## Prerequisites
Python 3 (tested with version 3.7.3).

Selenium library

Chrome browser and chromedriver. Please check that versions of your browser and choromederiver matches. Tested with browser version  77.0.3865.90 and correcponding chromedriver version. Chromedrivers can be downloaded from here: https://chromedriver.chromium.org/

## Running the script
python linkedinData.py

The script will ask your username and password and log in to your LinkedIn page and scroll through it. It counts amount of views, comments and likes of your posts and finally prints out the result.

Please note that the script will start Chrome in headless mode (i.e. browser not visible). Should you like to see the browser then either comment line 30 or change options.headless from True to False on the same line.

## Author
Antti Jääskö
