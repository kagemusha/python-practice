


page = requests.get(shipping_url)
soup = BeautifulSoup(page.content, 'html.parser')
links = soup.select('.latest_news_headline a')
clean_path = links[-1]['href']

clean_page = requests.get(f"{platts_url}{clean_path}")
clean_soup = BeautifulSoup(clean_page.content, 'html.parser')
report_sel = '.shippingmiddlecolwide .latest_news_headline'

date_line = clean_soup.select(f"{report_sel} date")[0].get_text()
date_str = re.search('(?<=--)\w+', date_line).group(0)
date = f"20{date_str[5:7]}-{months[date_str[2:5].lower()]}-{date_str[0:2]}"

report = clean_soup.select(f"{report_sel} content")[0].get_text()
data = {'date': date, 'content': report}

file_name = f"clean-20{date}"

s3 = boto3.resource('s3')
obj = s3.Object('platts-clean-tankers', file_name)
obj.put(Body=json.dumps(data))
