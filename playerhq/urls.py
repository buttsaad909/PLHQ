
# coding: utf-8

# In[ ]:


from django.urls import path
from playerhq import views

app_name = 'playerhq'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]

