import re
import os

# Define the absolute path for 01.html
file_path = os.path.join(os.getcwd(), "01.html")

with open(file_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

match = re.search(r'<a href="([^"]*data_j.xls)"', html_content)

if match:
    link_suffix = match.group(1)
    base_url = "https://www.jpx.co.jp"
    full_link = base_url + link_suffix
    print(full_link)
