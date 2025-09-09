import requests
from bs4 import BeautifulSoup

url='https://www.atyeti.com/'
response=requests.get(url)
print(response)
soup = BeautifulSoup(response.content,'html.parser')
links = soup.find_all('a')  # Find all <a> (anchor) tags
# To get the href attribute (URL) of each link:
for link in links:
    print(link.get('href'))

from urllib.parse import urljoin 

from urllib.parse import urljoin
base_url='https://www.atyeti.com/'
for link in links:
    href=urljoin(base_url,link.get('href'))
    print(href)
images = soup.find_all('img')
# images = soup.find_all('img')  
for img in images:
    print(img.get('src'))
from PIL import Image 
from PIL import Image
Image.open(r"C:\Users\ramka\OneDrive - Atyeti Inc\Desktop\6653588.jpg")
import requests 
# from bs4 import Beautiful

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
import base64
from PIL import Image  # Import Image from PIL pillow
 
# Sample URL of the webpage (replace with the actual URL you want to scrape)
url = 'https://www.atyeti.com/'
 
# Request the webpage
response = requests.get(url)
 
# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
 
# Find all <img> tags
images = soup.find_all('img')
 
# Loop through the images and get their 'src' attributes (image URLs)
for img in images:
    img_url = img.get('src')
 
    if img_url:
        # Check if the source is a base64 or data URI
        if img_url.startswith('data:image'):
            # Handle base64 image data
            try:
                # Extract the base64 part after 'data:image/...;base64,' and decode it
                img_data = img_url.split(",")[1]
                img_data = base64.b64decode(img_data)
 
                # Create a file-like object from the binary data
                img = Image.open(BytesIO(img_data))
 
                # Plot the image
                plt.imshow(img)
                plt.axis('off')  # Hide axes
                plt.show()
            except Exception as e:
                print(f"Error decoding base64 image: {e}")
 
        elif img_url.startswith('http') or img_url.startswith('https'):
            # For normal image URLs, download the image using requests
            try:
                img_response = requests.get(img_url)
                img = mpimg.imread(BytesIO(img_response.content))  # Read from the content of the image
                plt.imshow(img)
                plt.axis('off')  # Hide axes
                plt.show()
            except Exception as e:
                print(f"Error downloading image: {e}")
 
        elif img_url.startswith('/'):  # Handle relative URLs (e.g., /static/image.jpg)
            # Combine relative URL with base URL to form the full URL
            img_url = url + img_url
            try:
                img_response = requests.get(img_url)
                img = mpimg.imread(BytesIO(img_response.content))  # Read from the content of the image
                plt.imshow(img)
                plt.axis('off')  # Hide axes
                plt.show()
            except Exception as e:
                print(f"Error downloading image from relative URL: {e}")
        else:
            print(f"Skipping invalid image URL: {img_url}")

