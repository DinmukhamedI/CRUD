from django.urls import path
from . import views

urlpatterns = [
    path('', views.story, name='story'),
    path('exists', views.exists, name='exists'),
    path('create', views.create, name='create'),
    path('create2', views.create2, name='create2'),
    path('<int:pk>', views.DetailView1.as_view(), name='story_detail'),
    path('<int:pk>/update', views.UpdateView1.as_view(), name='story_update'),
    path('<int:pk>/delete', views.DeleteView1.as_view(), name='story_delete'),
    path('exists/<int:pk>', views.DetailView2.as_view(), name='exists_detail'),
    path('exists/<int:pk>/update', views.UpdateView2.as_view(), name='exists_update'),
    path('exists/<int:pk>/delete', views.DeleteView2.as_view(), name='exists_delete'),
]