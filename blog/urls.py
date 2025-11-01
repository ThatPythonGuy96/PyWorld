from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogHomeView.as_view(), name='home'),
    path('<int:id>', views.BlogDetailView.as_view(), name='detail'),
    path('blog/create', views.CreateBlogView.as_view(), name='create'),
] 