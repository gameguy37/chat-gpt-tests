"""
1. write a program in Python to interact with wikipedia's API and request a random article containing a word
provided by the user via input

2. revise this program such that it does not search wikipedia for a random article and then check for the presence
of the provided word, but instead searches for all articles using the random word and then returns one at random

3. modify the return value to be a link to the article instead of the title of the article
"""

import requests
import random
import urllib.parse


def get_random_article_with_word(word):
    # Search for articles containing the provided word
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "format": "json",
        "action": "query",
        "list": "search",
        "srsearch": word,
        "srprop": "",
        "srlimit": "500"
    }
    response = requests.get(api_url, params=params)
    data = response.json()

    # Get a random article from the search results
    articles = data['query']['search']
    if articles:
        random_article = random.choice(articles)
        article_title = random_article['title']
        article_url = "https://en.wikipedia.org/wiki/{}".format(urllib.parse.quote(article_title))
        return article_url
    else:
        return None


# Get input from the user
search_word = input("Enter a word to search for in Wikipedia articles: ")

# Request a random article containing the provided word
random_article_link = get_random_article_with_word(search_word)
if random_article_link:
    print("Random article containing the word '{}':".format(search_word))
    print(random_article_link)
else:
    print("No articles found containing the word '{}'. Please try a different word.".format(search_word))
