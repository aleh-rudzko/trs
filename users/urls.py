from django.conf.urls import url, patterns
from django.contrib.auth.views import logout_then_login, login
from users.forms import AuthenticationForm

urlpatterns = patterns('users.views',
    url(r'^login/$', login,
        kwargs={'template_name': 'users/login.html', 'authentication_form': AuthenticationForm}, name='users_login'),
    url(r'^logout/$', logout_then_login, name='users_logout'),
)