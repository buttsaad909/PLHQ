
# coding: utf-8

# In[ ]:


from django.urls import path
from playerhq import views

app_name = 'playerhq'

urlpatterns = [
    path('playerhq/', views.index, name='index'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('game/<slug:game_name_slug>/', views.game, name='game'),
    #path('<slug:game_name_slug>/review/', views.review, name='reviews'),
    path('category/<slug:category_name_slug>/', views.category, name='category'),
    path('category/<slug:category_name_slug>/review/', views.review, name= 'review'),
]

