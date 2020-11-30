from django.urls import path
from . import views

app_name = 'person'
urlpatterns = [
    path('', views.PersonMain.as_view(), name='index'),
    path('create/', views.PersonCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.PersonUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.PersonDelete.as_view(), name='delete'),
]
