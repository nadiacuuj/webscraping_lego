# ETHICS.md

## Purpose of Data Collection

The purpose of this project is to collect publicly available information about LEGO sets for adults from the official LEGO website. This data is collected solely for educational and research purposes to demonstrate web scraping techniques and to provide a list of challenging LEGO sets for adult builders.

We are collecting this data to build a structured, accessible list of LEGO sets for young-at-heart adults and wise-beyond-their-years children alike, showcasing web scraping methodologies for static websites and demonstrating how such data can be retrieved and processed in real-world applications.

## Data Sources and robots.txt

- The target webpage is: [LEGO - Challenging LEGO Sets for Adults](https://www.lego.com/en-us/categories/adults-welcome/article/challenging-lego-sets-to-build-for-adults).
- The website's `robots.txt` file was checked to ensure scraping is allowed for the targeted content. We have ensured that our scraping does not violate any terms and conditions outlined by LEGO.
  - URL for robots.txt: [https://www.lego.com/robots.txt](https://www.lego.com/robots.txt)
  
We only scrape publicly accessible pages that do not explicitly prohibit scraping, and we respect any limitations specified in the `robots.txt` file.

## Collection Practices

- **Respect for Website Resources**: We have implemented rate limiting to ensure that the scraper does not overload the LEGO website with too many requests in a short period of time.
- **No Bypassing Protections**: The scraper does not attempt to bypass password protections, CAPTCHA challenges, or other security measures.
- **Static Content**: We only scrape static content (LEGO set names). We have intentionally avoided scraping dynamic content such as price, recommended age, and number of pieces, as they require advanced tools like **Selenium** to handle JavaScript-loaded content. Future extensions of this project may use such tools, but for now, we are focusing on static content using **BeautifulSoup**.

## Data Handling and Privacy

- **No Collection of PII (Personally Identifiable Information)**: This project does not collect any user data or PII. The data collected is strictly limited to publicly available information about LEGO sets.
- **Secure Data Storage**: Any data collected is securely stored in a local CSV file for educational purposes. If sensitive or private data is accidentally scraped, it will be excluded from version control by adding it to the `.gitignore` file to ensure that it is not inadvertently shared or published.

## Data Usage

- The data collected through this project is used solely for educational and research purposes. It is not used for commercial gain, nor is it sold or shared with third parties.
- The purpose of the data is to provide a curated list of challenging LEGO sets for adults, helping users and developers learn about web scraping techniques.

## Ethical Considerations

- This project adheres to ethical guidelines for web scraping, including compliance with the website’s `robots.txt` file and implementing rate limiting to minimize disruption to the website’s resources.
- We avoid scraping sensitive or personal information and respect the legal boundaries and terms set by the website. All scraped data is for educational purposes and complies with ethical web scraping standards.