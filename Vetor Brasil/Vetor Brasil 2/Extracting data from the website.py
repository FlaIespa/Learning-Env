import urllib.request as ul
from bs4 import BeautifulSoup as soup

url = 'https://app.formassembly.com/reports/view/4835029'
req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
client = ul.urlopen(req)
htmldata = client.read()
#client.close()

pagesoup = soup(htmldata, "html.parser")
itemlocator = pagesoup.find_all('thead')
itemlocator
print(pagesoup.prettify())
 #It seems to be returning the login page, so I need to create an API for my credentials.



'''

#pip install beautifulsoup4 requests lxml pandas
import requests
from bs4 import BeautifulSoup

def get_data_from_Form_Assembly(url): #defining the function that will accept the url of the website FormAssembly
    response = requests.get(url) # uses the get.method to stores the values of what is returned from the url in the variable response
    soup = BeautifulSoup(response.text,
                         "lxml")
    forms = soup.find_all('form',
                          class_="form-card__name")
    data = []

    for form in forms:
        item ={}
        item["Submitted Date"] = form.find('headers',
                                           class_="tr.slds-text-heading--label").attrs("alt") #gives me the headers of each form
        item['']
        data.append(item)
    return(data)

'''