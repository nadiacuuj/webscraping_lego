# "LEGO Sets for Adults" Catalogue Web Scraper

## Project Overview

This project is a web scraper that extracts the names of challenging LEGO sets for adults from the "LEGO - Challenging LEGO Sets for Adults" page.

- The LEGO website curates a list of challenging sets specifically aimed at adult builders.
- This script scrapes the data and saves it into a structured format (CSV), making it easy to analyze or use for recommendations.
- Additionally, the program selects and recommends a random LEGO set from the scraped list to the user, offering a quick suggestion for those looking for inspiration on their next build.

### Purpose

The purpose of this scraper is to gather a list of challenging LEGO sets designed for both young-at-heart adults, and wise-beyond-their-years children, alike. This can be used for LEGO enthusiasts or hobbyists who are looking for recommendations on complex builds. In fact, the random LEGO set recommendation feature provides an element of fun by offering a surprise suggestion from the list, helping users quickly discover their next potential build.

Additionally, it showcases how to use Python and BeautifulSoup to scrape a website that doesn’t provide an API.

## Data Description

The data uncovered by the scraper includes:
- The names of LEGO sets recommended for adult builders
- This list can be useful for hobbyists, collectors, or anyone seeking challenging LEGO sets to purchase.
- The program will also recommend a random LEGO set from the scraped data to help users make a choice.

## Website Used

The website scraped is: [LEGO - Challenging LEGO Sets for Adults](https://www.lego.com/en-us/categories/adults-welcome/article/challenging-lego-sets-to-build-for-adults).

### Why This Website Was Chosen

The LEGO website was chosen because it is publicly available but does not have a public API, so web scraping is required to extract the data efficiently.

This particular page is a static website, meaning the content is readily available in the HTML source, making it easier to scrape with only tools like BeautifulSoup. Scraping dynamic websites (where content is loaded asynchronously, such as through JavaScript) would require additional tools like Selenium for example, which simulates a web browser to load and interact with such content. While this project does not use Selenium, it presents an interesting future extension to handle more complex, dynamic websites.


## Installation

To run this scraper locally, follow these steps:

1. **Clone the repository**:
   
*(In terminal:)*  
git clone [repository URL]  
cd [project folder]

3. **Install the required dependencies**:

*(In your own IDE environment:)*  
Copy code  
*(In terminal:)*  
pip install -r requirements.txt

3. **Run the Python Script:**
4. python main.py

## Future Enhancements: 
In the future, the project can additionally be extended to scrape additional details for each LEGO set, such as:
- Price
- Recommended Age
- Number of Pieces
- User Rating

These additional details are currently not scraped because they are dynamically loaded on the page via JavaScript, which requires more advanced web scraping tools like Selenium. For this project, only BeautifulSoup is used to keep the scope focused on static content scraping. In future iterations, Selenium or similar tools may be introduced to handle dynamic content.
