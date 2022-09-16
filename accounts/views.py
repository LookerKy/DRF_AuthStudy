from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([AllowAny])
def test_api(request):
    current_sit = get_current_site(request)
    print(current_sit)

    return Response({"hello": "hi"}, status=status.HTTP_200_OK)


