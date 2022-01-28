from django.urls import path, include
from posts.views import PostListView, PostListViewAPI, PostDetailViewAPI


urlpatterns = [
    path('', PostListView.as_view()),
    path('api/v1/posts/', PostListViewAPI.as_view(), name="post_list_api"),
    path('api/v1/posts/<int:pk>/', PostDetailViewAPI.as_view(), name="post_detail_api"),
    path('api/auth/', include('rest_framework.urls')),
]