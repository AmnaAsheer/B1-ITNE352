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
