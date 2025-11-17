from django.contrib import admin
from blog.models import Post,Category 

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'creat_date'
    empty_value_display="-empty"
    list_display = ('title' ,'counted_view','status','published_date','creat_date')
    list_filter = ('status',)
    search_fields = ['title','content'] 
    
@admin.register(Category)
class Category(admin.ModelAdmin):
    pass
    
