from decouple import config
import requests
import json

from .forms import HarvardApiForm

HARVARD_ART_URL = config('HARVARD_ART_URL')
HARVARD_API_KEY = config('HARVARD_API_KEY')


def get_art_data(title, key):
    url = HARVARD_ART_URL
    params = {'title': title, 'key': HARVARD_API_KEY}
    r = requests.get(url, params=params)
    art = r.json()
    art_list = {'art': art['results']}