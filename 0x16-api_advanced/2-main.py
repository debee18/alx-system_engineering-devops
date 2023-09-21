#!/usr/bin/python3
"""
2-main
"""
import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print("Number of post titles: {}".format(len(result)))
        else:
            print("Subreddit '{}' is invalid or there was an API request error.".format(subreddit_name))

def recurse(subreddit, hot_list=[], after=None):
    """Return top post titles recursively"""
    if after is None:
        after = ""

    user_agent = {'User-Agent': 'My Reddit Scraper'}  # Set your custom User-Agent here
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    try:
        response = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get("data")
            after = data.get("after")
            children = data.get("children")
            
            for child in children:
                title = child.get("data").get("title")
                hot_list.append(title)

            if after is not None:
                return recurse(subreddit, hot_list, after)

        return hot_list

    except requests.RequestException as e:
        print("An error occurred: {}".format(e))
        return None

if __name__ == '__main__':
    main()

