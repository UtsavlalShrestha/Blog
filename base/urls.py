from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog_add/', views.blog_add, name='blogadd'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signupUser, name="signup"),
    path('readblog/<int:id>', views.readblog, name="readblog"),
    path('delete/<int:id>', views.delete, name="delete"),
    # path('edit/<int:id>', views.edit, name="edit"),

]