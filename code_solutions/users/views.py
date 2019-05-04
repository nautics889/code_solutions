from users.models import User
from rest_framework import generics, mixins, permissions, response, status
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404


class UserCreateAPIView(mixins.CreateModelMixin,
                        generics.GenericAPIView):
    """
    Endpoint for creating users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserRetrieveAPIView(mixins.RetrieveModelMixin,
                          generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserUpdateAPIView(mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    #TODO:
    # implement updating logic according to AB example
    pass


class CurrentUserRetrieveUpdateAPIView(UserRetrieveAPIView, UserUpdateAPIView):
    http_method_names = ['patch', 'get']

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.request.user.pk)
        return obj

    def get(self, request, *args, **kwargs):
        print('USER: ', request.user, flush=True)
        return self.retrieve(request, *args, **kwargs)
