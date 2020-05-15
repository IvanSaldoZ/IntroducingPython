import webbrowser
url = 'http://www.python.org/'
#webbrowser.open(url)  # открывает страницу браузера
#webbrowser.open_new(url)
#webbrowser.open_new_tab(url)

# Beautiful Soup
def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print('Links in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()