
from django.urls import path
from home.views import home_page,save_contact,login_view

app_name='home'

urlpatterns = [
    path('', home_page ,name= "home"),
    path('contact/',save_contact,name="save_contact"),
    path('login/',login_view,name="login"),
]


