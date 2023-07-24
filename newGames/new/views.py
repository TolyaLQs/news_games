from django.shortcuts import render
from .models import News
# Create your views here.

def index(request):
    # if request.POST:
    #     if 'search' in request.POST and request.POST['search']:
    #         search = request.POST['search']
    #         search(request, search)

    news = []

    try:
        news = News.objects.all().filter(published=True).order_by('-pub_add')[0:20]
        id_user = request.user.id
        for new in news:
            new.check_like_user(id_user)
    except:
        print('not user')

    context = {
        'news': news,
    }
    return render(request, 'new/index.html', context)


def hot_news(request):
    pass


def categories_news(request):
    pass


def category_news(request):
    pass


def news_page(request):
    pass

