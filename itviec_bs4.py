import bs4
import requests
import pandas as pd

resp = requests.get("https://itviec.com/it-jobs/python/?per_page=100")
tree = bs4.BeautifulSoup(resp.text, features="html.parser")
div = tree.find_all("h2", attrs={"class": "title"})
links = []
names = []
for line in div:
    a = line.find_all("a")
    link = "https://itviec.com" + "".join([href["href"] for href in a])
    names.append((line.text).replace("\n", ""))
    links.append((link))
itviec = pd.DataFrame(zip(names, links), columns=["names", "links"])
itviec.to_csv("itviec.csv")
itviec = pd.DataFrame([links])


def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val, val)


itviec.style.format(make_clickable)
