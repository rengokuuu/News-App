from turtle import title
from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.


def home(request):
    newsapi = NewsApiClient(api_key="8a92847a26414185997b8fe1b78704a9")
    headlines = newsapi.get_top_headlines(sources='bbc-news, the-verge')
    articles = headlines['articles']
    desc = []
    title = []
    image = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        title.append(article['title'])
        image.append(article['urlToImage'])

    mylist = zip(title, desc, image)
    context = {
        'mylist': mylist
    }

    return render(request, 'newsapp/index.html', context)
