import requests
import json
from bs4 import BeautifulSoup

def view_url_data(data):
    headlines = []
    headlines.append(get_cnn_headline("https://cnnphilippines.com"))
    headlines.append(get_abscbn_headline("https://news.abs-cbn.com/news"))
    headlines.append(get_rappler_headline("https://rappler.com"))

    print('headlines', headlines)
    return headlines


def get_cnn_headline(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    return {
        "url": url + soup.select(".cpmedium-header a")[0]['href'],
        "headline": soup.select(".cpmedium-header a")[0].text
    }

def get_abscbn_headline(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    print('>',soup.select(".news-title a")[0].text)
    return {
        "url": url + soup.select(".news-title a")[0]['href'],
        "headline": soup.select(".news-title a")[0].text
    }

def get_rappler_headline(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    print('>', soup.find('h3'))
    h3 =  soup.find('h3')
    parent = h3.find_parent()
    return {
        "url": url + parent['href'],
        "headline": h3.text
    }

def update_json_file():
    with open('news.json', 'r') as json_file:
        data = json.load(json_file)
        updated_data = view_url_data(data)

    with open('news.json', 'w') as json_file:
        json_file.write(json.dumps(updated_data, indent=4))


if __name__ == '__main__':
    update_json_file()