from . import views
from django.urls import path
urlpatterns = [
    path('', views.add, name='add'),
    # path('details', views.details, name='details')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('cbrhome/', views.TaskListView.as_view(), name='cbrhome'),
    path('cbrdetail/<int:pk>/', views.TaskDetailView.as_view(),name='cbrdetail'),
    path('cbrupdate/<int:pk>/', views.TaskUpdateView.as_view(),name = 'cbrupdate'),
    path('cbrdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbrdelete'),

]