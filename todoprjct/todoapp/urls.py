"""
URL configuration for todoprjct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add,name='add'),
    path('done/<int:id>/', views.done, name='done'),
    path('update/<int:id>/', views.update, name='update'),
    #path('glvhome/',views.TaskListview.as_view(),name='TaskListview'),
    path('gdvdetails/<int:pk>/', views.TaskDetailview.as_view(), name='TaskDetailview'),
    path('guvupdate/<int:pk>/', views.TaskUpdateview.as_view(), name='TaskUpdateview'),
    path('gdvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='TaskDeleteview'),

]
