from django.urls import path
from . import views

app_name = 'concessionnaire'

urlpatterns = [
    # Endpoints obligatoires
    path('concessionnaires/', views.ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', views.ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/', views.VehiculeListByConcessionnaireView.as_view(), name='vehicule-list-by-concessionnaire'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/<int:pk>/', views.VehiculeDetailView.as_view(), name='vehicule-detail'),
    # Endpoint bonus
    path('users/', views.UserCreateView.as_view(), name='user-create'),
]
