'''
Let's create a spider that scrapes emails and passwords, and phone numbers.
make it argparse to be able to input websites to scrape.

open all links from the mainpage and scrape that aswell.
'''

from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string
import argparse

current_links = []


def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url

def handle_local_links(url,link):
    if link.startswith('/'):
        return ''.join([url,link])
    else:
        return link

def get_links(url):
    xyz = []
    try:
        resp = requests.get('https://christopherek.dev')
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        print(soup)
        links = [link.get('href') for link in soup.find_all('a')]
        links = [handle_local_links(url,link) for link in links]
        links  = [str(link.encode('ascii') for link in links)]
        print(str(links))
        return links
        #links = [current_links.append(link) for link in links if url in links]
        
    except TypeError as e:
        print(e)
        print("Got a Typerror")
        return []
    except IndexError as e:
        print(e)
        return []
    except AttributeError as e:
        print(e)
        return []
    except Exception as e:
        print(str(e))
        return []
def get_emails(url):
    pass

def main():
    parser = argparse.ArgumentParser(
    description='Web-Scraper for emails- Enter single or list of addresses')
    #Add group so either U or u is required.
    group = parser.add_mutually_exclusive_group(required=True)
    #Arg for list of urls
    group.add_argument('--urllist', '-U', metavar="",help='Input location to list with urls, 1 url per line. Example -U ~/folder/list.txt')
    #Single url. (https://google.coom)
    group.add_argument('--url', '-u', metavar="",help='Input single url, Example -u https://google.com')
    args = parser.parse_args()
    
    if not args.urllist:
        pass

    current_links.append('https://christophereek97@gmail.com')
    how_many = 2
    p = Pool(processes=how_many)
    data = p.map(get_links, [link for link in current_links])
    data = [url for url_list in data for url in url_list]
    p.close()
    with open('urls.txt', 'w') as f:
        f.write(str(data))

if __name__ == "__main__":
       main()
