from django.urls import path
from.views import(
    CourseView,
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView
   # my_fbv
)

app_name='courses'
urlpatterns=[
    #path('',my_fbv,name='courses-list'),
    path('',CourseListView.as_view(), name='courses-list'),
    path('<int:id>/',CourseView.as_view(), name='course-detail'),
    path('create/',CourseCreateView.as_view(),name='courses-create'),
    path('<int:id>/update/',CourseUpdateView.as_view(), name='courses-update'),
     path('<int:id>/delete/',CourseDeleteView.as_view(), name='courses-delete'),
]