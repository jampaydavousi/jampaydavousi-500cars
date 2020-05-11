# Used Car Price Depreciation

This web service provides an interactive user interface for used car shoppers to see visialization of how 500+ used cars from 6 different makes from 2014 have made maintained their original value.

## Architecture
The asking price is provided in the used car listing.  The backend software Python obtains the MSRP from the NTSB website via JSON and verifies the data components by extracting the manufacturers specification off of the VIN number of the vehicle.  The back end software also cleans the data to make it uniform as all of the information in the used car listing is enterd by seller and is subject to typos and aliases.  

## Front End Website
It provides the car shopper the ability to filter by car make, and llustrating depreciation popular car makes including comparison of 6 different makes from 2014, and their depreciation.

## Prerequisits
1. Python version 2.7 or higher
2. Jupyter Notebook
3. Flask
4. PosgreSQL or MySQL
5. BeautifulSoup4
6. Heroku

