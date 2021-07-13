url(r'^register/$',views.register,name='register'),
url(r'^login',views.loginpage,name='loginpage'),
url(r'^profile/&',views.profilepage,name='profilepage'),
url(r'^search/', views.search_results, name='search_results'),