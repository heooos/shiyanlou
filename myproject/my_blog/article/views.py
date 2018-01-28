from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse('Hello World,Django')

def detail(request):
    post = Article.objects.all()
    str = ''
    for item in post:
        str += ('title = {title},category={category},date_time = {date_time},content={content}\n'.format(title=item.title,category=item.category,date_time = item.date_time,content=item.content))
    return HttpResponse(str)

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})
