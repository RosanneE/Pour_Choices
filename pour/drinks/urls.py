from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.DrinksCreate.as_view(), name='create/'),
    path('index/', views.Index.as_view(), name='index'),
      path('my_page/', views.MyPage.as_view(), name='my_page'),
    # path('my_lists/', views.MyLists.as_view(), name='my_lists'),
    path('index/<int:pk>/', views.CocktailShow.as_view(),  name='cocktail_show'),
    path('index/<int:pk>/update/', views.CocktailUpdate.as_view(),  name='cocktail_update'),
    path('ing_search/', views.ing_search, name='ingredients'),
]