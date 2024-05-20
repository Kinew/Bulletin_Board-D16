from django.urls import path
from news_portal import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('advert/', views.AdvertList.as_view(), name= 'advert_list'),
    path('advert/create/', views.AdvertCreate.as_view(), name='advert_create'),
    path('<int:pk>/edit/', views.AdvertUpdate.as_view(), name='advert_update'),
    path('<int:pk>/delete/', views.AdvertDelete.as_view(), name='advert_delete'),
]
