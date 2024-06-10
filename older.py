import requests
import creds

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2024-06-05&'
       'sortBy=popularity&'
       'apiKey={creds.news_api_key}')
response = requests.get(url).json()
print(response)