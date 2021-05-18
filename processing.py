from bs4 import BeautifulSoup as BS4  
from datetime import date
import requests as req
import lxml

def scraper(url):

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

    content = req.get(url, "html.parser", headers=header ).content
    soup = BS4(content, "lxml")
    h1_raw = soup.find("h1")
    h2_raw = soup.find("h2")
    h3_raw = soup.find("h3")
    p_raw = soup.findAll("p")
    
    try:
        h1 = h1_raw.get_text()
    except Exception as e:
        h1 = "Parameter not found"

    try:
        h2 = h2_raw.get_text()
    except Exception as e:
        h2 = "Parameter not found"

    try:
        h3 = h3_raw.get_text()
    except Exception as e:
        h3 = "Parameter not found"

    try:
        p = [p.get_text() for p in p_raw]
    except Exception as e:
        p = "Parameter not found"
   
    return h1,h2,h3,p