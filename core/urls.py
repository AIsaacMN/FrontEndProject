from django.urls import path

from .views import LoginView, HomeView, RegisterView, GroupListView, GroupView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('groups/', GroupListView.as_view(), name="list-groups"),
    path('', HomeView.as_view(), name="home"),
    path('groups/<str:key>', GroupView.as_view(), name="group")
]
