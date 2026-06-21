# Register your models here.
from django.contrib import admin
from blog.models import Post

# Define a custom interface for the Post model
class PostAdmin(admin.ModelAdmin):
    # Determine which database columns are visible in the list view
    list_display = ('title', 'author', 'category', 'created_at')

    # Enable a search bar that queries these fields
    search_fields = ('title', 'body')

    # Automatically generate the slug in the form as you type the title [3]
    prepopulated_fields = {'slug': ('title',)}

# Register the model along with its custom PostAdmin interface
admin.site.register(Post, PostAdmin)