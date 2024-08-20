import json
import os
from os import path
from urllib.request import urlopen

def scrape(url, title) -> str:
    '''
    Scrapes the url given by `url` and saves it with name `$title.html` inside the `out` folder and returns the path to the saved file.
    '''
    # url = 'https://en.wikipedia.org/wiki/List_of_Hindu_empires_and_dynasties'

    page = urlopen(url)
    print(page)

    html_bytes = page.read()
    html = html_bytes.decode('utf-8')

    # print(html)

    out_folder = "out"
    try:
        os.makedirs(out_folder)
    except FileExistsError as e:
        pass

    # html_saved_path = path.join(out_folder, f"indian_kingdoms_wiki.html")
    html_saved_path = path.join(out_folder, f"{title}.html")

    with open(html_saved_path, "w") as f:
        f.write(html)
    
    return html_saved_path


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/List_of_Hindu_empires_and_dynasties'
    title = 'indian_kingdoms_wiki'
    # scrape(url, title)

    from bs4 import BeautifulSoup

    with open(path.join("out", f"{title}.html")) as f:
        html = f.read()
        soup = BeautifulSoup(html, "html.parser")

    kingdoms_table = soup.find("table", class_="wikitable")

    body = list(kingdoms_table)[-1]
    # with open('out/kinkdoms_table.html', 'w') as f:
    #     f.write(str(body))

    rows = body.find_all('tr')

    headers = rows[0]
    kingdoms = rows[1:]

    csv_headers = []

    for header in headers:
        # print(header)
        value: str = header.text
        value = value.strip()
        # print(f"Value: {value}")
        # print(dir(header))
        # print(header.get_text())
        if len(value) > 0:
            csv_headers.append(value)

        # print('----')

    print('csv headers: ', csv_headers)
        # print(header.get_text().strip())
    
    for kingdom in kingdoms:
        pass

