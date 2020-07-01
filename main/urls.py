from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logOut,name='logout'),
    path('user/data',views.user_data,name='user_data'),
    path('bio/building',views.bio,name='bio'),
    path('<str:username>',views.bio,name='biobulding')
]