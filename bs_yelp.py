import requests
from bs4 import BeautifulSoup

def yelp_bs(url):
    urls = list()
    for i in range(0, 250,10):
    	link = url + '&start=' + str(i)
    	urls.append(link)

    names = list()
    for url in urls:
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        # print(soup.prettify())

        links = soup.find_all("a", class_ = "link__09f24__1kwXV link-color--inherit__09f24__3PYlA link-size--inherit__09f24__2Uj95")
        links = links[-10:]
        for link in links:
            names.append(link.get('name'))

    return(names)

corona = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Corona%2C%20Queens%2C%20NY')
chandler = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Chandler%2C%20AZ')
chelsea = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Chelsea%2C%20NY')
elmhurst = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Elmhurst%2C%20Queens%2C%20NY')
gainsville = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Gainesville%2C%20FL')
jackson_heights = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Jackson%20Heights%2C%20Queens%2C%20NY')
north_corona = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=North%20Corona%2C%20Queens%2C%20NY')
scottsdale = yelp_bs('https://www.yelp.com/search?cflt=restaurants&find_loc=Scottsdale%2C%20AZ')

queens = corona + north_corona + elmhurst + jackson_heights

queens = list(set(queens))
