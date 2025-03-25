import requests
from bs4 import BeautifulSoup

# Step 1: Define the target website URL
url = "https://example-blog.com"  # Replace with a real website

# Step 2: Send an HTTP request and get the response
response = requests.get(url)

# Step 3: Check if the request was successful
if response.status_code == 200:
    # Step 4: Parse the webpage content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Step 5: Find all article titles
    articles = soup.find_all("h2", class_="post-title")  # Adjust based on the website's HTML
    
    print("\n🔹 Blog Articles:")
    for article in articles:
        title = article.get_text(strip=True)
        link = article.a["href"] if article.a else "No link available"
        print(f"📌 {title} - {link}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
