from django.conf.urls import url, patterns
from django.contrib.auth.views import logout_then_login, login

urlpatterns = patterns('users.views',
    url(r'^login/$', login, name='users_login'),
    url(r'^logout/$', logout_then_login, name='users_logout'),
)