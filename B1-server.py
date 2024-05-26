import socket
import json
import os
import threading
import requests
countries = {
    "Australia": "au",
    "New Zealand": "nz",
    "Canada": "ca",
    "United Arab Emirates": "ae",
    "Saudi Arabia": "sa",
    "United Kingdom": "gb",
    "United States": "us",
    "Egypt": "eg",
    "Morocco": "ma",
}
languages = {
    "Arabic": "ar",
    "English": "en"
}

categories = {
    "Business": "business",
    "Entertainment": "entertainment",
    "General": "general",
    "Health": "health",
    "Science": "science",
    "Sports": "sports",
    "Technology": "technology"
}

sources = [
    {"name": "Source A", "country": "US", "description": "Description A", "url": "http://example.com/a", "category": "General", "language": "English"},
    {"name": "Source B", "country": "GB", "description": "Description B", "url": "http://example.com/b", "category": "Business", "language": "English"}
]
NEWS_API_KEY = 'd4b3d0b1675f48709625f2ce6cd2aea4'
BASE_URL = 'https://newsapi.org/v2/'
HOST = '127.0.0.1'
PORT = 65432

def get_allnews(endpoint, params):
    params['apiKey'] = NEWS_API_KEY
    response = requests.get(BASE_URL + endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'error', 'message': 'Unnable to fetch data'}