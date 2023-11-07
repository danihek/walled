import datetime
import requests
import sys
import re

dateToday = datetime.date.isoformat(datetime.date.today())
query = sys.argv[1]

pattern = r"wallhaven-(\w+)(?:\.png|\.jpg)?"
categories=111

if len(sys.argv) > 1:
    purity=sys.argv[2]

if len(sys.argv) > 2:
    categories=sys.argv[3]

def wallpaper_search_api(_query):
	url = f"https://wallhaven.cc/api/v1/search?q={_query}&categories={categories}&apikey=j4xlcmJUGilmO37BhKx9Q2msUUuGfkLm&purity={purity}"
	res = requests.get(url)
	json_data = res.json()
	dl_links = []
	for wallpaper in json_data["data"]:
		dl_links.append(wallpaper["path"])
	
	return dl_links

waldurl = wallpaper_search_api(query)

n=0
for wall in waldurl:
	response = requests.get(wall)
	wallName = str(query)+"-"+str(n)+"-"+dateToday+str(datetime.datetime.now().minute)+".jpg"
	match = re.search(pattern, wall)
	if match:
        	extracted_id = match.group(1)
	        wallName = str(query)+str(extracted_id)+".jpg"
	file = open(wallName,'wb')
	file.write(response.content)
	print("Saved: " + wallName)
	n = n+1
