from django.urls import path
from .views import ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CommunityView, Home, Movies, CategoryView, LikeView, AddCommentView

urlpatterns = [
    path('community/', CommunityView.as_view(), name='community'),
    path('', Home, name='Home'),
    path('movies/', Movies, name='movies'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/del/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:c>', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),
]
