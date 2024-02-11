from django.urls import path
from . import views


app_name = 'food'
urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),
    path('items/',views.items,name='items'),
    # path('<int:item_id>/',views.detail,name='detail'), # FBV
    path('<int:pk>/',views.FoodDetailView.as_view(),name='detail'), # CBW
    # add item
    # path('add/',views.create_item,name='create_item'),
    path('add/',views.ItemCreateView.as_view(),name='create_item'),
    # edit item
    path('update/<int:item_id>/',views.update_item,name='update_item'),
    # delete item
    path('delete/<int:item_id>/',views.delete_item,name='delete_item'),
]