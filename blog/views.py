from django.shortcuts import render
 
# Hardcoded data 
posts = [
  {
    'title': 'Getting started with Django',
    'excerpt': 'Django is a high-level Python web framework that encourages rapid development.',
    'category': 'Tutorial',
    'author': 'Your name',
    'date': '2026-03-10',
  },
  {
    'title': 'Understanding the MTV pattern',
    'excerpt': 'Model, Template, View — how Django structures the separation of concerns.',
    'category': 'Concepts',
    'author': 'Your name',
    'date': '2026-02-17',
  },
  {
    'title': 'Django ORM basics',
    'excerpt': 'Query your database with Python — no SQL required.',
    'category': 'Deep dive',
    'author': 'Your name',
    'date': '2026-01-24',
  },
]
 
 
def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)
 
 
def about(request):
    return render(request, 'blog/about.html')
 
 
def post_detail(request, pk):
    context = {'pk': pk}
    return render(request, 'blog/post_detail.html', context)

#from django.http import HttpResponse

#def home(request):
        #return HttpResponse("Welcome to My Blog!")
 
#def about(request):
        #return HttpResponse("About: I am learning Django in Year 1.")
 
#def post_detail(request, pk):
        #return HttpResponse(f"Post #{pk}: Coming soon!")