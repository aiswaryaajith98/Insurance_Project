from django.urls import path
from . import views

urlpatterns = [
    path('', views.Base, name='Base'),

    path('Company_Dashboard/', views.Company_Dashboard, name='Company_Dashboard'),
    path('Company_AgentDetails/', views.Company_AgentDetails, name='Company_AgentDetails'),
    path('Company_AddAgent/', views.Company_AddAgent, name='Company_AddAgent'),
    path('Company_EditAgent/', views.Company_EditAgent, name='Company_EditAgent'),
    path('Company_ClientDetails/', views.Company_ClientDetails, name='Company_ClientDetails'),
    path('Company_ClientDetails1/', views.Company_ClientDetails1, name='Company_ClientDetails1'),
    path('Company_ClientDetails2/', views.Company_ClientDetails2, name='Company_ClientDetails2'),
    path('Company_AssignAgent/', views.Company_AssignAgent, name='Company_AssignAgent'),
    path('Company_AgentTracking/', views.Company_AgentTracking, name='Company_AgentTracking'),
    # path('/', views., name=''),
    


    path('Agent_Dashboard/', views.Agent_Dashboard, name='Agent_Dashboard'),
    path('Agent_AgentProfile/', views.Agent_AgentProfile, name='Agent_AgentProfile'),
    path('Agent_ClientInfo/', views.Agent_ClientInfo, name='Agent_ClientInfo'),
    # path('/', views., name=''),
    # path('/', views., name=''),
    
    
]
