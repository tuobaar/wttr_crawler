# Wttr.in Crawler and REST API

This program crawls weather information from the URL https://wttr.in/ and stores them in a sqlite database every 30 minutes. Included is a REST API for accessing aggregated weather information such average/maximum/minimum temperature and wind speed for specified date(s).


## Technologies and modules:

- python3
- sqlite3
- flask
- sys
- signal
- time
- datetime
- requests
- bs4 (beautifulsoup4)

Some modules are already part of the python3 install package. Other modules/packages can be installed through `pip install package_name` or `pip3 install package_name` .

### Database
The sqlite database is created the first time the program is executed and skipped on subsequent program executions.   
The database 'weather_archive.db' contains a table 'weather' with the following columns:  

`Temperature INT, Wind_Speed INT, Date DATE, Time TIME` 

## Program features:

1. Crawls weather data from url every 30 minutes specific to the current location.
2. Handles requests errors.
3. Handles technical errors/changes on the site that result in crawling 'unknown' data.
4. Handles internet/network disconnection errors during requests to url. The program keeps running waiting for the connection to get fixed, and continues afterwards. To see this feature instantly, temporarily disconnect the internet connection on the device before running the program. Then reconnect afterwards to continue crawling data.
5. When the program is terminated, the first 5 latest weather-entries are displayed.


## Installation:
1. Click on the [download](https://gitlab.com/zigpos/coding-tasks/challenges/archive-weather-data-kpipien/-/archive/main/archive-weather-data-kpipien-main.zip) button/symbol on main project page on GitLab and download zip file.
2. Extract the downloaded zip file to a preferred location on your computer.
3. Open `command console/prompt` or `terminal`, navigate to the location of the extracted folder/files and install all packages in `requirements.txt` using pip as follows:

   `>>> pip install -r requirements.txt`   
   `>>> pip3 install -r requirements.txt`
   

## How to use:

This program has a crawler that crawls weather data into a database and a REST API to access aggregated weather information from the database.
1. The crawler can be launched by entering the following in a `command console/prompt` or `terminal`:

   `>>> python wttr_crawler.py`  
   `>>> python3 wttr_crawler.py`

2. To access the database with the REST API, run:

   `>>> python rest_api.py`  
   `>>> python3 rest_api.py`

## Sample Database:
Since it takes time to populate the database `weather_archive.db` created at first run, a sample database `sample.db` has been provided to 
immediately try out the REST API. If that is necessary, then:

1. Copy `sample.db` from the `sample_database` directory to the main project directory.
2. Rename `sample.db` to `weather_archive.db`, then try out the REST API.
3. When done with the trials, you can delete the database file.

## Unit Test:
Some unit tests have been provided for some endpoints/functions in `rest_api.py`
Note that the testcase was for aggregated temperature calculations only. Some lines of code were also stripped out from 
the original functions. You can compare `rest_api.py` in the main folder `wttr_crawler` and `rest_api_functions.py` in the subdirectory
`unittest`.

To access the unit tests:

1. Open `command console/prompt` or `terminal`.
2. Navigate to unittest directory/folder.
3. Run one of the following commands and observe the results:

   `>>> python -m unittest test.py`  
   `>>> python3 -m unttest test.py`
4. You can further exploit the test by changing the values in `test.py`.
5. You can also change the database name from `weather_archive_valid.db` to `weather_archive_invalid.db` This however may 
 not be important, as invalid characters are not usually stored in the database.
