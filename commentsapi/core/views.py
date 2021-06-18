from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from core.models import Comments
from core.serializers import commentserializer
from rest_framework.decorators import api_view
from rest_framework import permissions

permission_classes = [permissions.AllowAny]

@api_view(['GET', 'POST', 'DELETE'])
def core_list(request):

    if request.method == 'GET':
        comments = Comments.objects.order_by('-comment_time')
        comment = request.GET.get('comment', None)
        if comment is not None:
            comments = comments.filter(feed__icontains=comment)
        
        comments_serializer = commentserializer(comments, many=True)
        return JsonResponse(comments_serializer.data, safe=False)

    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = commentserializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

