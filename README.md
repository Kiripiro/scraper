# Electric Vehicles Scraper

## Overview

This project is a web scraping application developed in Python, designed to scrape electric vehicle listings from the Bymycar website.
The project was completed within a 2-hour window as part of a 48-hour challenge to demonstrate quick problem-solving and programming skills for an internship or apprenticeship opportunity.  
It was my first experience with web scraping.

## Features

- Scrapes all electric vehicle listings from Bymycar.
- Extracts relevant details such as vehicle name, price, and specifications.
- Saves the extracted data into a structured format for easy analysis.

## Requirements

- Python 3.6+
- Playwright
- BeautifulSoup4
- Requests
- Pandas (for data manipulation: creating the .csv file)

## Script Details

The `scraper.py` script performs the following steps:

1. Launches a headless browser using Playwright.
2. Navigates to the Bymycar website.
3. Parses the HTML content using BeautifulSoup.
4. Locates and extracts information on electric vehicles.
5. Handles pagination to scrape data from multiple pages.
6. Stores the extracted data in a CSV file.

### Challenges and Learning

The main challenge in this project was that the Bymycar page was not static; it loaded vehicle listings asynchronously. 
This required the use of Playwright to handle the dynamic content and load all vehicles properly.
Implementing asynchronous scraping with Playwright allowed for efficient and accurate data extraction despite the dynamic nature of the webpage. 
This project was also my first experience with web scraping, providing valuable learning in handling dynamic web content and using asynchronous programming.

## Contact

For any questions or further information, please contact:

- Alexandre Tourret: [contact@atourret.fr](mailto:contact@atourret.fr)
- LinkedIn: [Alexandre Tourret](https://www.linkedin.com/in/atourret)
