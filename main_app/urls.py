from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pops/', views.pops_index, name='index'),
    path('pops/<int:pop_id>/', views.pops_detail, name='detail'),
    path('pops/create/', views.PopCreate.as_view(), name='pops_create'),
    path('pops/<int:pk>/update/', views.PopUpdate.as_view(), name='pops_update'),
    path('pops/<int:pk>/delete/', views.PopDelete.as_view(), name='pops_delete'),
    path('pops/<int:pop_id>/add_dusting/', views.add_dusting, name='add_dusting'),
    path('pops/<int:pop_id>/assoc_group/<int:group_id>/', views.assoc_group, name='assoc_group'),
    path('groups/', views.GroupList.as_view(), name='groups_index'),
    path('groups/<int:pk>/', views.GroupDetail.as_view(), name='groups_detail'),
    path('groups/create/', views.GroupCreate.as_view(), name='groups_create'),
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name='groups_update'),
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name='groups_delete'),
]