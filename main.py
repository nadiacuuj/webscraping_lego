import requests
from bs4 import BeautifulSoup
import csv
import random

def scrape_the_list(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Webpage request failed: {response.status_code}")
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all elements with the specific attribute 'data-test="article-text"'
        sets = soup.find_all(attrs={"data-test": "article-text"})
        
        # Extract the text from these elements and filter out the introduction paragraph
        set_texts = [set.text.strip() for set in sets if "LEGO®" in set.text]
        
        # We know that the actual LEGO sets start after the first one, so we skip the first item
        lego_sets = set_texts[1:12]  # Selecting sets 1 to 11
        
        # Return all sets
        return lego_sets
    
    except Exception as e:
        print(f"An error has occurred: {e}")
        return []

def main():
    url = "https://www.lego.com/en-us/categories/adults-welcome/article/challenging-lego-sets-to-build-for-adults"

    sets = scrape_the_list(url)
    
    # Write the scraped data to a CSV file
    with open('lego_sets_for_adults.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['LEGO Sets'])  # Write header
        writer.writerows([[set] for set in sets])  # Write data rows
    
    print(f"Scraped {len(sets)} LEGO sets and saved to 'lego_sets_for_adults.csv'")

    # Randomly select one of the LEGO sets to recommend to user
    if sets:
        random_set = random.choice(sets)
        print(f"Randomly selected LEGO set: {random_set}")

# Boilerplate to run the main() function
if __name__ == "__main__":
    main()