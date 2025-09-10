import re
import urllib.request

JPX_BASE_URL = "https://www.jpx.co.jp"
JPX_PAGE_URL = JPX_BASE_URL + "/markets/statistics-equities/misc/01.html"

with urllib.request.urlopen(JPX_PAGE_URL) as f:
    html_content = f.read().decode()

match = re.search(r'<a href="([^"]*data_j.xls)"', html_content)
link_suffix = match.group(1)
csv_link = JPX_BASE_URL + link_suffix

with urllib.request.urlopen(csv_link) as f:
    with open("data_j.xls", "wb") as g:
        g.write(f.read())
