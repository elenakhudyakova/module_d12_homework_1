from django.urls import path
from .views import NewsList, NewsItem, Search, CreatePost, EditPost, DeletePost, add_subscribe, del_subscribe

app_name = 'news'
urlpatterns = [
  path('', NewsList.as_view()),
  path('<int:pk>', NewsItem.as_view()),
  path('search', Search.as_view()),
  path('add', CreatePost.as_view()),
  path('<int:pk>/edit', EditPost.as_view()),
  path('<int:pk>/delete', DeletePost.as_view()),
  path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('category/', Subscribers),
]