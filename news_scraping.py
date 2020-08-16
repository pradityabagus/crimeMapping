import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup as bs

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# scraping parameters
startyear = 2020
endyear = 2020

startmonth = 7
endmonth = 7

startday = 1
endday = 1

page = 1

for year in range(startyear,endyear+1):
    for month in range(startmonth,endmonth+1):
        for day in range(startday,endday+1):
            req = urllib.request.Request('https://www.jpnn.com/indeks?id=276&d='+str(day)+'&m='+str(month)+'&y='+str(year)+'&tab=all&page='+str(page), headers={'User-Agent': 'Mozilla/5.0'})

            data = urllib.request.urlopen(req, context=ctx).read().decode()
            bsData = bs(data, 'html.parser')

            links = bsData.select('#content-utama > div.kolom-kiri > div.border-box > div > ul > li > div.content-description > div > h2 > a')

            for link in links:
                print(link['href'])
            