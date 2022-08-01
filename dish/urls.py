from unicodedata import name

from django.urls import path

from . import views

app_name = 'dish'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexClassView.as_view(), name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('item/', views.item, name='item'),
    path('add', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
