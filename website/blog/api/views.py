from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializer
from blog.models import Post


@api_view(['GET'])
def postDetailView(request, pk):
    """
    Retrieve, update or delete a blog post.
    """

    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)