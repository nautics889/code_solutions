from django.urls import path
from solutions.views import (SolutionsCreateAPIView,
                             SolutionsUpdateDeleteAPIView,
                             SolutionsListAPIView,
                             SolutionRetrieveAPIView)

urlpatterns = [
    path('', SolutionsListAPIView.as_view(), name='solutions_list'),
    path('create/', SolutionsCreateAPIView.as_view(), name='create_solution'),
    path('update-delete/', SolutionsUpdateDeleteAPIView.as_view(), name='update_delete_solution'),
    path('<slug:slug>/', SolutionRetrieveAPIView.as_view(), name='retrieve_solution'),
]
