from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required 
from blog.models import Post
from blog.forms import PostForm 
 
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

        # blog/views.py


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

def home(request):
    posts = Post.objects.all()  # Fetch all postse
    return render(request, 'blog/home.html', {'posts': posts,})




@login_required
def create_post(request):
    # Check if the request is a POST (user submitted data)
    if request.method == 'POST':
        # Pass the incoming POST data to our form class
        form = PostForm(request.POST)

        # Check if the form meets all model field requirements
        if form.is_valid():
            # Create a post object in memory, but don't save to the DB yet
            post = form.save(commit=False)
            # Inject the logged-in user's username into the author field
            post.author = request.user.username
            # Save the completed post object to the database
            post.save()
            # Redirect the user back to the blog home page
            return redirect('blog:home')

    else:
        # If it is a GET request, instantiate an empty form
        form = PostForm()

    context = {
        'form': form
    }
    return render(request, 'blog/post_form.html', context)

@login_required
def update_post(request, slug):
    # 1. Fetch the specific post we want to edit 
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        # 2. Pass POST data AND the existing record instance to the form
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save() # Saves the updates to the database 
            return redirect('blog:post_detail', slug=post.slug)
    else:
        # 3. Render the form pre-populated with the existing post data
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'blog/post_form.html', context)

@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)  # find the post

    if request.method == 'POST':    # user confirmed deletion
        post.delete()               # remove from database
        return redirect('blog:home')

    # GET request — just show confirmation page
    return render(request, 'blog/post_confirm_delete.html', {'post': post})