#!/usr/bin/env python3
import datetime
import requests
import sys
import re

# VARIABLES
APIKEY = "" # If you want to use NSFW purity, you need to set up API key

dateToday = datetime.date.isoformat(datetime.date.today())
availablesorting = [ "relevance", "random", "date_added", "views", "favourites", "toplist", "hot" ]
pattern = r"wallhaven-(\w+)(?:\.png|\.jpg)?"

query = ""
sorting = "relevance"   # default val
categories=111          # default val
purity=100              # default val

# FUNTIONS
def print_template():
    print("")
    print("./walled [QUERY] [PURITY] [CATEGORY] [SORTING]")

def print_example():
    print("")
    print("Example: ./walled \"anime\" 100 010 views")

def print_QUERY():
    print("")
    print("\tQUERY: string without spaces or in \"\" that contains query")

def print_PURITY():
    print("")
    print("\tPURITY: xyz - three values, that can be either 0 or 1")
    print("\t\tX - SFW")
    print("\t\tY - Sketchy")
    print("\t\tZ - NSFW - if you want to search up NSFW content you need an API key!")

def print_CATEGORIES():
    print("")
    print("\tCATEGORIES: xyz - three values, that can be either 0 or 1")
    print("\t\tX - General")
    print("\t\tY - Anime")
    print("\t\tZ - People")

def print_SORTING_OPTS():
    print("")
    print("\t Sorting options:  \"relevance\", \"random\", \"date_added\", \"views\", \"favourites\", \"toplist\", \"hot\"")

def usage():
    print_template()
    print_example()
    print_QUERY()
    print_PURITY()
    print_CATEGORIES()
    print_SORTING_OPTS()

def check_entries():
    global query, sorting, categories, purity, availablesorting  # Declare globals to use them here
    if len(sys.argv) < 2:
        print("You need to at least provide a query!")
        usage()
        exit(1)

    query = sys.argv[1]

    if query == "":
        print("You provided an empty query!")
        print_template()
        print_QUERY()
        exit(1)

    if len(sys.argv) > 2:
        purity = sys.argv[2]
        if len(purity) != 3 or not all(c in '01' for c in purity):
            print("Bad purity provided!")
            print_template()
            print_PURITY()
            exit(1)

    if len(sys.argv) > 3:
        categories = sys.argv[3]
        if len(categories) != 3 or not all(c in '01' for c in categories):
            print("Bad categories provided!")
            print_template()
            print_CATEGORIES()
            exit(1)

    # Validate sorting value
    if len(sys.argv) > 4:
        sorting = sys.argv[4]
    if sorting not in availablesorting:
        print("Bad sorting provided!")
        print_template()
        print_SORTING_OPTS()
        exit()

def wallpaper_search_api(_query):
    url = f"https://wallhaven.cc/api/v1/search?q={_query}&categories={categories}&apikey={APIKEY}&purity={purity}&sorting={sorting}"
    print(f'Starting query: {url}')
    res = requests.get(url)
    json_data = res.json()
    dl_links = []
    for wallpaper in json_data["data"]:
        dl_links.append(wallpaper["path"])
    return dl_links



# MAIN - Program starts here!

check_entries()
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
