from django.conf.urls import url

from django.contrib.auth.views import LogoutView
from .views import (
    login_page,
    insription,
    invite_vue
)

urlpatterns = [
    url(r'^login/$', login_page, name='login'),
    url(r'^inscription/invite/$', invite_vue, name='invite'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^inscription/$', insription, name='inscription'),
]