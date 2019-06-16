from django.urls import path
from solutions.views import (SolutionsCreateAPIView,
                             SolutionsUpdateDeleteAPIView,
                             SolutionsListAPIView,
                             SolutionRetrieveAPIView,
                             TopicListAPIView,
                             TopicRetriveAPIView)

urlpatterns = [
    path('', SolutionsListAPIView.as_view(), name='solutions_list'),
    path('create/', SolutionsCreateAPIView.as_view(), name='create_solution'),
    path('update-delete/', SolutionsUpdateDeleteAPIView.as_view(), name='update_delete_solution'),
    path('topics/', TopicListAPIView.as_view(), name='topic_list'),
    path('topics/<slug:slug>/', TopicRetriveAPIView.as_view(), name='retrieve_topic'),
    path('<slug:slug>/', SolutionRetrieveAPIView.as_view(), name='retrieve_solution'),
]
