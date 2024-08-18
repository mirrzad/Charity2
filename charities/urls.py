from django.urls import path

from . import views

urlpatterns = [
    path('benefactors/', views.BenefactorRegistration.as_view(), name='benefactor-register'),
    path('charities/', views.CharityRegistration.as_view(), name='charities-register'),
    path('tasks/', views.Tasks.as_view(), name='task-create-list'),
    path('tasks/<int:task_id>/request/', views.TaskRequest.as_view(), name='task-request'),
    path('tasks/<int:task_id>/response/', views.TaskResponse.as_view(), name='task-response'),
    path('tasks/<int:task_id>/done/', views.DoneTask.as_view(), name='task-done'),
]
