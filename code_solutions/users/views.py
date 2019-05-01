from users.models import User
from rest_framework import generics, mixins, permissions, response, status
from users.serializers import UserSerializer


class UserCreateAPIView(mixins.CreateModelMixin,
                        generics.GenericAPIView):
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
