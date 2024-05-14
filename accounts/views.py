from rest_framework.response import Response
from .models import UserProfile
from rest_framework import viewsets, generics
from .serializer import UserProfileSerializer, UserSerializer, CompleteUserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .custom_permissions import IsOwner
from rest_framework.decorators import action


def update_user_social_data(strategy, *args, **kwargs):
    response = kwargs["response"]
    backend = kwargs["backend"]
    user = kwargs["user"]
    print(user)
    user_profile = UserProfile.objects.filter(user=user)

    # check if user already exists
    # if user exists, update the fields
    # else create a new user
    if not user_profile:
        print("user does not exist------------------")
        if response["picture"]:
            url = response["picture"]
            userProfile_obj = UserProfile()
            userProfile_obj.user = user
            userProfile_obj.picture = url
            userProfile_obj.save()
    else:
        print("user exists------------------")
        if response["picture"]:
            url = response["picture"]
            userProfile_obj = user.profile
            print(userProfile_obj)
            userProfile_obj.picture = url
            userProfile_obj.save()


class UserDetailViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    # send current user data to frontend for profile page without pk
    @action(detail=False, methods=["get"])
    def current_user(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=200)
