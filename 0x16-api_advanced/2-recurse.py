#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API and return a list of hot article titles.
    
    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): List to store the hot article titles (initially empty).
        after (str): The "after" parameter to paginate through results.

    Returns:
        list: List of hot article titles or None if the subreddit is not valid.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}  # Set a User-Agent header to mimic a web browser.

    # Define the Reddit API URL for hot posts in the given subreddit.
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    
    # Parameters for the API request.
    params = {'limit': 100, 'after': after}
    
    # Send an HTTP GET request to the Reddit API.
    response = requests.get(url, headers=headers, params=params)
    
    # Check if the request was successful.
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        
        # Extract and append the titles of hot articles to the hot_list.
        for post in posts:
            hot_list.append(post['data']['title'])
        
        # Check if there are more pages to paginate through.
        after = data.get('data', {}).get('after')
        if after is not None:
            # Recursively call the function with the 'after' parameter to get the next page.
            return recurse(subreddit, hot_list, after)
        else:
            # No more pages, return the hot_list.
            return hot_list
    elif response.status_code == 404:
        # Subreddit not found, return None.
        return None
    else:
        # Handle other API response codes as needed.
        print(f"API request failed with status code: {response.status_code}")
        return None

# Example usage:
if __name__ == '__main__':
    subreddit = 'programming'
    result = recurse(subreddit)
    if result is not None:
        print(len(result))
    else:
        print("None")

"""
Using reddit's API
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """returning top ten post titles recursively"""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

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
        return (None)
