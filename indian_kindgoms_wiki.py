import json
import os
from os import path
import sys
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

    csv_headers = csv_headers[:-1]

    print('csv headers: ', csv_headers)
        # print(header.get_text().strip())
    
    csv_rows = []
    for i, kingdom in enumerate(kingdoms):
        # if i != 3:
        #     continue
        krow = []
        if len(kingdom) != 14:
            raise Exception(f'expected <tr> with len 14. Got with len: {len(kingdom)}')
        # print(kingdom)
        # print(dir(kingdom))
        # print(next(kingdom))
        extracted_kingdom_row_texts = []
        for i, kdata in enumerate(kingdom):
            # print(f'idx: {i}. data: {kdata.get_text()}. type: {kdata.__class__}')

            # print(len(kdata))
            value: str = kdata.get_text()
            value = value.strip()
            extracted_kingdom_row_texts.append(value)
            # if len(value) > 0:
            #     krow.append(value)
            
            # print(value)
        if len(extracted_kingdom_row_texts) != 14:
            raise Exception(f'expected 14 values to be extracted. Got: {len(extracted_kingdom_row_texts)}')
        # print(extracted_kingdom_row_texts)
        for idx, t in enumerate(extracted_kingdom_row_texts):
            if idx in [1, 3, 5, 7, 9, 11]:
                krow.append(t)
        csv_rows.append(krow)
        # print(kingdom)
        # if i == 5:
        #     break
        # break
    # sys.exit(1)

    print(csv_rows)

    # sys.exit(1)

    print(f'Parsed {len(csv_rows)} kingdoms.')

    non_conforming_indices = []

    for idx, row in enumerate(csv_rows):
        if len(row) != 6:
            print('-'*20)
            print(f'Index: {idx}. Len: {len(row)}')
            print(row)
            print('-'*20)
            non_conforming_indices.append(idx)
            continue
        if idx == 56:
            print('+'*20)
            print(row)
            print('+'*20)
        part_of: str = row[5]
        part_of = part_of.replace('\n', '\xa0')
        part_of = part_of.split('\xa0')
        part_of = list(filter(lambda n : n != '', part_of))
        part_of = ','.join(part_of)
        row[5] = part_of

        languages: str = row[4]
        languages = languages.replace('\n', '\xa0')
        languages = languages.split('\xa0')
        languages = list(filter(lambda n : n != '', languages))
        languages = ','.join(languages)
        row[4] = languages

        # print(part_of)

    # csv_data = [csv_headers]
    print(f'Non conforming Indices: {non_conforming_indices}')

    out_csv_path = path.join('out', 'kingdoms.csv')

    with open(out_csv_path, 'wt') as f:
        import csv
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        writer.writerows(csv_rows)
    
    print(f'data written to {out_csv_path}')



