# import of third-party library
import requests

# URL
URL = "https://bold.dk/fodbold/stillinger/premier-league"

# Request to bold.dk
response = requests.get(URL)

# Save text from respone to index.html file
with open("index.html", "w") as file:
    file.write(response.text)
