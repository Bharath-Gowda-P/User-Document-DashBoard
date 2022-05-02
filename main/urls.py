from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views 
# from .views import CustomLoginView

urlpatterns = [
    path('', views.index, name="index"),
    # path('login', CustomLoginView.as_view(), name="login"),
    path('login', views.user_login, name = "login"),
    path('logout/', views.logout_view, name="logout"), 
    path('signup', views.signup, name="signup"),
    path('add', views.add, name="add"),
    path('download/<int:id>', views.download, name="download"),
    path('viewdoc/<int:id>', views.viewdoc, name="viewdoc"),
    path('home', views.home, name="home"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)