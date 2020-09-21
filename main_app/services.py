from decouple import config
import requests
import json

from .forms import HarvardApiForm

HARVARD_ART_URL = config('HARVARD_ART_URL')
HARVARD_API_KEY = config('HARVARD_API_KEY')


def get_art_data(title):
    url = f"{HARVARD_ART_URL}&title={title}&apikey={HARVARD_API_KEY}"
    print(url)
    params = {'title': title, 'api_key': HARVARD_API_KEY}
    r = requests.get(url)
    print(r)
    art = r.json()
    return {'baseimageurl': art['records'[0]['images'[0]['baseimageurl']]] , 'title': art['records'[0]['title']] }