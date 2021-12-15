from django.shortcuts import render

# Create your views here.

def view_index(request):
    print(request.POST.get("titlee"))
    context = {"name": "Max", "title": "lalala"}
    return render(request, 'index.html', context)

def create_articles_view(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        user = {
            "name": "Maksat",
            "age": 21,
            "address": "Mars"
        }
        context = {
            "title": request.POST.get("title"),
            "content": request.POST.get("content"),
            "author": request.POST.get("author"),
            "user":user
        }


        return render(request, 'article_view.html', context)