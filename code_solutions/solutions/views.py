from rest_framework import generics, mixins, response, status, permissions
from solutions.models import Solution, Topic
from solutions.serializers import SolutionSerializer, SolutionListSerializer, TopicSerializer


class SolutionsListAPIView(generics.ListAPIView):
    """
    Endpoint for fetching list of existing solutions
    """
    queryset = Solution.objects.all().only("title", "price", 'topics')
    permission_classes = (permissions.AllowAny,)
    serializer_class = SolutionListSerializer


class SolutionRetrieveAPIView(mixins.RetrieveModelMixin,
                              generics.GenericAPIView):
    queryset = Solution.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SolutionSerializer

    def get_object(self, slug):
        obj = Solution.objects.get(slug=slug)
        return obj

    def get(self, request, slug):
        solution = self.get_object(slug)
        serializer = self.serializer_class(solution)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class SolutionsCreateAPIView(mixins.CreateModelMixin,
                             generics.GenericAPIView):
    """
    Endpoint for creating solutions
    """
    queryset = Solution.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = SolutionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SolutionsUpdateDeleteAPIView(mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin,
                                   generics.GenericAPIView):
    """
    Endpoint for updating and deleting solutions
    """
    queryset = Solution.objects.all()
    permission_classes = (permissions.IsAuthenticated)
    serializer_class = SolutionSerializer


class TopicListAPIView(generics.ListCreateAPIView):
    """
    Endpoint for fetching list of existing topics
    """
    queryset = Topic.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TopicSerializer


class TopicRetriveAPIView(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = TopicSerializer

    def get_object(self, slug):
        obj = Topic.objects.get(slug=slug)
        return obj

    def get(self, request, slug):
        topic = self.get_object(slug)
        serializer = self.serializer_class(topic)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

