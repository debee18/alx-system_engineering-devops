#!/usr/bin/python3
"""
Using reddit's API
"""
import requests

# Initialize 'after' as None for the first request
after = None

def recurse(subreddit, hot_list=[]):
    """Return top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent, allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return None

# Example usage
if __name__ == "__main__":
    subreddit_name = "python"  # Replace with the desired subreddit
    titles = recurse(subreddit_name)
    if titles:
        for i, title in enumerate(titles[:10], start=1):
            print(f"{i}. {title}")
    else:
        print("Invalid subreddit or API request error.")

