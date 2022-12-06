#using module 'requests'
import requests
from bs4 import BeautifulSoup
#request to the page
page = requests.get('https://app.formassembly.com/reports/view/4835013')

#store the text response and the status code of the code
txt = res.text
status = res.status_code

print(txt, res.status_code)

#Using library beautiful soup - this library provides simple methods for navigating, searching, and modifying a DOM tree

#Extract title page
soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text # gets you the text of the <title>(...)</title>

#Extract body of page
page_body = soup.body

#Extract head of page
page_head = soup.head

print(page_title, page_head, page_head)

parameters = "Name"