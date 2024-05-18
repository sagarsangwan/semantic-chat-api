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
        # current_user = request.user
        # current_user = User.objects.get(username=current_user)
        # current_user = UserSerializer(current_user)
        # print(current_user)
        # # add this serialized user to data as owner
        # data["owner"] = current_user.data["id"]

        # print(current_user.id)
        # data["owner"] = current_user.id
        # print(data)
        #  add this user to data as owner
        data["owner"] = request.user.id
        print(data)
        serializer = CodeRoomSerializerForCreate(data=data)
        if serializer.is_valid():
            print("valid-------------------")
            self.perform_create(serializer=serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        else:
            print("notvalid")
            print(serializer.errors)
            return Response(serializer.errors, status=500)

    def perform_create(self, serializer):
        # Save the new instance

        serializer.save(owner=self.request.user)
