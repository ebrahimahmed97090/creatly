from django.conf.urls import url
from users import views

app_name = 'users'
urlpatterns = [
    url(r'^users/', views.usershome, name='users_home'),
    url(r'^pbuilder/', views.pagebuilder, name='page_builder'),
    url(r'^/', views.user_logout, name='log_out'),

]
