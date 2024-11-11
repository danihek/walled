# walled
Python script for downloading wallpers from wallhaven.

# Usage
./walled [QUERY] [PURITY] [CATEGORY] [SORTING]

Example: ``./walled "anime" 100 010 views``

    QUERY: string without spaces or in "" that contains query
    
    PURITY: xyz - three values, that can be either 0 or 1
        X - SFW
        Y - Sketchy
        Z - NSFW - if you want to search up NSFW content you need an API key!
    
    CATEGORIES: xyz - three values, that can be either 0 or 1
        X - General
        Y - Anime
        Z - People
    
    Sorting options:  "relevance", "random", "date_added", "views", "favourites", "toplist", "hot"
