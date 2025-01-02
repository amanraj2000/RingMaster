from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path("login/", views.login, name="login"),
    path('mark_spam/', views.mark_spam, name='mark_spam'),
    path('search_name/<str:name>/', views.search_by_name, name='search_by_name'),
    path('search_phone_number/<str:phone_number>/', views.search_by_phone_number, name='search_by_phone_number'),
]
