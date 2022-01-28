from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from posts.serializers import PostSerializer
from posts.models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = "posts"
    template = 'posts/list.html'


class PostListViewAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    peermission_class = (AllowAny,)


class PostDetailViewAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

''' REST API '''
# def json_list_published_posts(request):
#     posts = Post.objects.filter(status='published')
#     return JsonResponse({
#         "posts":[{
#             "title": p.title, "slug": p.slug,
#             "id": p.id, "published": p.when_published,
#         }
#         for p in posts]
#     })
