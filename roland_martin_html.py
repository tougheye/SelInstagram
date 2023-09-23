import requests

response = requests.get('https://www.instagram.com/rolandmartinfishing_official/followers/')
with open("roland_html_text.txt",'w') as file:
    file.write(response.text)


