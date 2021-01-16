from django.urls import path,include



# from django.contrib import admin



from . import views

urlpatterns=[
    path('info/', views.view1, name="view1"),
    path('login/',views.login_view,name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logoutview, name="logout"),
]