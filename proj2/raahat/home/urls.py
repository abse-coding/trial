from django.urls import path, include
from . import views 

urlpatterns = [
   
    path('home/', views.home, name="home"),
    # path('about/', views.about, name="about"),
    # path('knowourteam/', views.knowourteam, name="knowourteam"),
    # path('booksession/', views.booksession, name="booksession"),
    # path('payment/', views.payment, name="payment"),
    path('index/',views.index, name="index"),
    path('',views.home, name="blank"),
    path('extendsone/', views.extendsone, name="extendsone"),
    
    # This is where the real pages begin
    
    path('about/',views.about,name="about"),
    path('form/',views.form,name="form"),
    path('payment/',views.payment,name="payment"),
    path('knowourteam/',views.knowourteam,name="knowourteam"),
    
]
