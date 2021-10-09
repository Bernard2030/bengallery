from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.Home,name = 'Home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^single_image/(\d+)',views.single_image,name ='single_image'),
    url(r'^location/(\d+)',views.search_by_location,name ='search_by_location'),
    url(r'^category/(\d+)',views.search_by_category,name ='search_by_category'),
    # url('category/<str:poll_id>', views.search_by_category, name="search_by_category")
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)