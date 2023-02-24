import requests
from bs4 import BeautifulSoup

headers = {
    'cookie': 'visid_incap_1858972=ewXAlquNTUa6eBm+cyoQykO492MAAAAAQUIPAAAAAABbOGfsak9McqF1yyf85kCE; incap_ses_1309_1858972=B76xFVqAZ2zPCf5/QYEqEkO492MAAAAAs7USiXFsfDPmgBkHMfAcSA==; nlbi_1858972=HZC6eQLuhha2NXwfTxwWFAAAAAAFSR1/aCdK75YhSeJB1Fjl; frontend=ozqfc4tur46t73q5k6qikp605z; _gcl_au=1.1.881096638.1677178950; _gid=GA1.2.257028620.1677178950; _dc_gtm_UA-49207283-1=1; sc=1ADE82FD-1B15-9E65-0F76-CC5A6C5B831A; digi_user_cookie=0%3Alehh1k5l%3Ae67aa2-00513f-f5697a-0015ff-fd56a6; digi_session_cookie=8a589a5a-cb27-47e6-b22f-3ac02bb2f34a; session_id=1677178949; _fbp=fb.1.1677178950314.1449749578; reese84=3:+Q1maWYDHkZYLA0FlJP/jQ==:ZAM7w6WEch3kwXeksBvwTaBOlUj9+RhwamlD6PsADzQkI+8z5BIa8ERo9us9KahbOSmU3/dg6SIYjkPCr3obThAgZWsH23HRSBS1/ZxPx8xAytajJov0vqo5Gl4yLn2r+21W/EGlf5HlYXXiC6j7LYmcbXsDNZSFCbYgeUquGYJCtXfAT+/l+emB8qbZAJNZNHLEk+u61Qpk3TbFy7/199ojhjbY5KaxCm3NEmPg9ohymRQdz5N5/orWyox4345xaq2+IfcG+DHoY4fcdvD5jKoCf5zwD7Evjjf5svVegxMlbbQI9wReyj1/2DHzULXJwKDO2//YwFAEzoPjhQRNX2gFlxX7XEgLciK94ndpGrlE8OtMX0UyGYMcnoFfgA3mo7Dr2FUstjbItXCG8m7RsYG2d/ZQa+Haw93PfK5dM54BHAOXYUEMdltnsno9p5PFU5TANSai6w41YABm1fdrWZznvWkfJ8UG3UCavNxY5qE=:gNr9kezf3JwlDSLNtz/FkqFpGpqajJJ94jObQAk6idI=; auto=GA1.2.1935244637.1677178950; auto_gid=GA1.2.499976796.1677178955; _gat_UA-49207283-1=1; X-Store=1; _ga_SMJV1PJEMX=GS1.1.1677178954.1.0.1677178954.60.0.0; _gat=1; __utma=162514478.1935244637.1677178950.1677178955.1677178955.1; __utmc=162514478; __utmz=162514478.1677178955.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=162514478.1.10.1677178955; fp=2; lfp=2/23/2023, 9:02:29 PM; pa=1677178954994.17020.0009963152496124117comfy.ua0.40368202911172846+1; nlbi_1858972_2147483392=T847DQkVaUxuy5jKTxwWFAAAAAAzRekGpjejJJxtLgcJQNJ2; rr-testCookie=testvalue; rrpvid=850816232830529; _ga=GA1.1.1935244637.1677178950; _ga_4XXC45ZSKN=GS1.1.1677178949.1.1.1677178955.54.0.0; _userGUID=0:lehh1ouw:5vKMYP7tKS52zFqIw62A70j_Q0Us~hsa; rcuid=63f7b84c993b230064f188d7; dSesn=6b57afe1-7971-5aeb-591f-818152d3e863; _dvs=0:lehh1ouw:PaBRwz5~v9HqCRT3MhmwMJU3u4OuH4ar',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'referer': 'https://comfy.ua/notebook/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="91", "Google Chrome";v="91"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}


products = []

for page in range(1, 4):
    resp = requests.get('https://comfy.ua/notebook/?p={}', headers=headers)
    soup = BeautifulSoup(resp.content, 'html.parser')
    items = soup.find_all('div', attrs={'class': 'products-list-item__info'})
    for item in items:
        link = item.find('a', attrs={'class': 'products-list-item__name'})
        name = link.text.strip()
        product_url = link['href']
        current_price = item.find('div', attrs={'class': 'products-list-item__actions-price-current'}).text
        products.append({
            'name': name,
            'url': product_url,
            'current_price': ''.join(list(filter(str.isdigit, current_price))),
        })
    print(f'Page {page} done')
print(len(products))

