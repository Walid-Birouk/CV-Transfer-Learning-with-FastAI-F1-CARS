import requests
import json
import os
import urllib.request

def get_photos(query, per_page=200):
    api_key = 'ac03afb07facef2181bf47696a3e459b'
    base_url = "https://api.flickr.com/services/rest/"

    params = {
        'method': 'flickr.photos.search',
        'api_key': api_key,
        'text': query,
        'tags': "formula 1",
        'tag_mode': 'all',
        'format': 'json',
        'nojsoncallback': 1,
        'per_page': per_page,
        'sort': 'relevance'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def get_image_url(photo):
    return f"https://farm{photo['farm']}.staticflickr.com/{photo['server']}/{photo['id']}_{photo['secret']}.jpg"

def download_image(url, dirname, filename):
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    urllib.request.urlretrieve(url, f"{dirname}/{filename}.jpg")

def search_and_download_images(keywords):
    for keyword in keywords:
        print(f"Searching images for {keyword}...")
        photos = get_photos(keyword)['photos']['photo']
        for i, photo in enumerate(photos):
            url = get_image_url(photo)
            print(f"Downloading image {i} from {url}...")
            download_image(url, keyword, f"{keyword}_{i}")

search_and_download_images(["Ferrari", "Mclaren", "Red Bull", "Renault", "Mercedes"])