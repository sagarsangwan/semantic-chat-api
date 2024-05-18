from rest_framework import viewsets, permissions, status
from .serializers import CodeRoomSerializer, CodeRoomSerializerForCreate
from .models import CodeRoom
from rest_framework.response import Response
from accounts.serializer import UserSerializer
from django.contrib.auth.models import User

# from .serializers


class CodeRoomViewsets(viewsets.ModelViewSet):

    queryset = CodeRoom.objects.all()
    serializer_class = CodeRoomSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        data = request.data
        data["owner"] = request.user.id
        serializer = CodeRoomSerializerForCreate(data=data)
        if serializer.is_valid():
            self.perform_create(serializer=serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            return Response(serializer.errors, status=500)

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)
