import requests
import torch
from transformers import pipeline
# from newsapi import NewsApiClient


summarizer = pipeline("summarization")
# summary = summarizer(
#     """
#     America has changed dramatically during recent years. Not only has the number of 
#     graduates in traditional engineering disciplines such as mechanical, civil, 
#     electrical, chemical, and aeronautical engineering declined, but in most of 
#     the premier American universities engineering curricula now concentrate on 
#     and encourage largely the study of engineering science. As a result, there 
#     are declining offerings in engineering subjects dealing with infrastructure, 
#     the environment, and related issues, and greater concentration on high 
#     technology subjects, largely supporting increasingly complex scientific 
#     developments. While the latter is important, it should not be at the expense 
#     of more traditional engineering.

#     Rapidly developing economies such as China and India, as well as other 
#     industrial countries in Europe and Asia, continue to encourage and advance 
#     the teaching of engineering. Both China and India, respectively, graduate 
#     six and eight times as many traditional engineers as does the United States. 
#     Other industrial countries at minimum maintain their output, while America 
#     suffers an increasingly serious decline in the number of engineering graduates 
#     and a lack of well-educated engineers.
# """
# )

# print(summary)


# change URL to be top articles?
url = ('https://newsapi.org/v2/everything?q=Artificial Intelligence&from=2024-05-05&sortBy=publishedAt&apiKey={creds.news_api_key}')
response = requests.get(url).json()

# Get the URLs from the response
print(response['articles'][0]['url'])
# Scrape Data from URL


# the above code won't work because it doesn't send the full article in the content. Workaround is taking the URL provided with the api response and
# then figuring out how to scrape content from a url and then feeding that scraped content into the NLP

