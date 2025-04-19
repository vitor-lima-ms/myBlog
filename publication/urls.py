from django.urls import path

from publication import views

app_name = 'publication'

urlpatterns = [
    path('', views.home, name='home'),

    path('search/', views.searchPublication, name='searchPublication'),

    path('create-publication/', views.createPublication, name='createPublication'),

    path('publication/<int:id>/', views.detailsPublication, name='detailsPublication'),

    path('publication/<int:id>/comment/', views.createComment, name='createComment'),

    path('news/', views.newsPublication, name='newsPublication'),

    path('sports/', views.sportsPublication, name='sportsPublication'),

    path('entertainment/', views.entertainmentPublication, name='entertainmentPublication'),

    path('technology/', views.technologyPublication, name='technologyPublication'),

    path('health/', views.healthPublication, name='healthPublication'),

    path('other/', views.otherPublication, name='otherPublication'),
]
