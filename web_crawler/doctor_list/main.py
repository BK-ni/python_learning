import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


result_dict = {}
url = "https://wd.vghtpe.gov.tw/gm/Fpage.action?muid=513"
headers = {"Cookie": "JSESSIONID=CF0BD11EBE9E59691D19C1842334BF35"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

a_tags = soup.find_all("a", class_="list-group-item-action d-flex align-items-stretch justify-content-between align-items-center p-2 px-3 top_link")
for a_tag in a_tags:
    try:
        anchor_text = a_tag.get_text().strip()
        key, value = anchor_text.split(maxsplit=1)
        result_dict[value] = key
        href = a_tag.get("href")
        response = requests.get(href)
        ability = BeautifulSoup(response.text, "html.parser")
        sixth_tr = ability.find("div", class_="table-responsive ckeditor").find_all("tr")[5]
        p_text = sixth_tr.find_all('td')[1].find('p')
        print(p_text)
        print(href)
    except ValueError as e:
        print(f"Error processing text '{anchor_text}': {e}")

    except Exception as e:
        print(f"Un expected error occurred: {e}")
print(result_dict)

# 進入到各醫生個人版，將其'專長學科'存成新的{key: value}

df = pd.DataFrame(list(result_dict.items()), columns=['名字', '職稱'])
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
print("CSV 文件已成功保存。")



