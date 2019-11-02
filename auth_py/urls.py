from django.conf.urls import url, include
from auth_py.views import  logout, login, registration, user_profile
from auth_py import url_reset

urlpatterns= [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="registration"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^password_reset/', include(url_reset))
]