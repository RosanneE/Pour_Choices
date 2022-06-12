from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('create/', views.DrinksCreate.as_view(), name='create/'),
    path('list_create/', views.ListCreate.as_view(), name='list_create'),
    path('index/', views.Index.as_view(), name='index'),
    path('my_page/', views.MyPage.as_view(), name='my_page'),
    path('index/<int:pk>/', views.CocktailShow.as_view(),  name='cocktail_show'),
    path('my_page/<int:pk>/', views.ListShow.as_view(),  name='list_show'),
    path('index/<int:pk>/update/', views.CocktailUpdate.as_view(),  name='cocktail_update'),
    path('list_delete/<int:id>', views.ListDelete, name='list_delete'),
    path('ingredient_update/<int:id>', views.IngredientUpdate, name='ingredient_update'),
    path('my_page/<int:pk>/list_update/', views.ListUpdate.as_view(),  name='list_update'),
    path('ing_search/', views.ing_search, name='ingredients'),
    # path('my_page/<int:pk>/drinks/<int:drink_pk>/', views.ListDrinkAssoc.as_view(), name="list_song_assoc"),
]