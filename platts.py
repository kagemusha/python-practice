import requests


base_url = "https://www.platts.com/shippingcommentary/Tankers/957_"

#10347404
offset = 2700
last_article_num = 10355733
article_list = [10355733]

i = 1
while len(article_list) < 50:
  num = last_article_num - offset + i
  url = f"{base_url}{num}"
  r = requests.get(url)
  if r.status_code == 200:
    last_article_num = num
    article_list.append(num)
    i += offset
    print(url)
  else:
    num = last_article_num - offset - i
    url = f"{base_url}{num}"
    r = requests.get(url)
    if r.status_code == 200:
      last_article_num = num
      article_list.append(num)
      i += offset
      print(url)



