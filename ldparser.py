import requests
from bs4 import BeautifulSoup

def get_product_name(ld_number):
    # Construct the initial URL with the LD number
    initial_url = f"https://www.londondrugs.com/{ld_number}.html"

    # Send a GET request to fetch the redirected page
    response = requests.get(initial_url, allow_redirects=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the redirected page
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Find the product information within the HTML
        product_info = soup.find("h1", class_="product-name")
        
        # Extract the product name if found
        if product_info:
            return product_info.text.strip()

    return None

# Get LD number input from the user
ld_number = input("Enter the LD number: ")

# Get product name using the LD number
product_name = get_product_name(ld_number)

# Print the product name if available
if product_name:
    print(product_name)
else:
    print("Product information not found.")
