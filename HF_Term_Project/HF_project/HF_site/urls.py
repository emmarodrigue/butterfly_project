from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import UserChangeView

urlpatterns = [
    path('', views.landing, name="home"),
    path('resources', views.resources, name='resources'),
    path('homelessness_in_america', views.homelessness_in_america),
    path('how_to_help', views.how_to_help, name='how_to_help'),

    # registration/login
    path('register_user', views.register_user, name='register_user'),
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),

    # account
    path('account', views.account, name='account'),
    path('edit_account', UserChangeView.as_view(), name='edit_account'),

    # resources and saved resources
    path('saved_resources', views.saved_resources, name='saved_resources'),
    path('healthcare', views.healthcare, name='healthcare'),
    path('food', views.food, name='food'),
    path('specific_populations', views.specific_populations, name='specific_populations'),
    path('answer', views.answer, name='answer'),

    # contact/report
    path('contact', views.contact, name='contact'),
    path('report', views.report, name='report'),
]

urlpatterns += staticfiles_urlpatterns()