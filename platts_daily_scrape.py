import boto3
import re
import requests
import json

from lxml import html
from lxml.cssselect import CSSSelector

months = { 'jan': '01', 'feb': '02', 'mar': '03',
           'apr': '04', 'may': '05', 'jun': '06',
           'jul': '07', 'aug': '08', 'sep': '09',
           'oct': '10', 'nov': '11', 'dec': '12'}

platts_url = "https://www.platts.com"
shipping_url = f"{platts_url}/shipping/tankers"
page = requests.get(shipping_url)
tree = html.fromstring(page.content)
sel = CSSSelector('.latest_news_headline a')
links = sel(tree)
clean_path = links[-1].get('href')

clean_page = requests.get(f"{platts_url}{clean_path}")
clean_tree = html.fromstring(clean_page.content)
report_sel = '.shippingmiddlecolwide .latest_news_headline'
report_date_sel = CSSSelector(f"{report_sel} date")
report_content_sel = CSSSelector(f"{report_sel} content")
date_line = report_date_sel(clean_tree)[0].text
date_str = re.search('(?<=--)\w+', date_line).group(0)
date = f"20{date_str[5:7]}-{months[date_str[2:5].lower()]}-{date_str[0:2]}"
report_title = f"clean-20{date}"
print(date_str)
report_text = report_content_sel(clean_tree)[0]
data = {'date': date, 'content': report_text.text}

s3 = boto3.resource('s3')
obj = s3.Object('platts-clean-tankers', report_text)
obj.put(Body=json.dumps(data))
