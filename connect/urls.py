from django.conf.urls import url
from django.db.models.query import ValuesIterable
# from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
url(r'^register/$',views.register,name='register'),
url(r'^login',views.loginpage,name='loginpage'),
url(r'^profile/&',views.profilepage,name='profilepage'),
url(r'^search/', views.search_results, name='search_results'),
url(r'^$',views.home,name = 'home'),
url(r'^uploadImage/$',views.upload,name = 'upload'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)