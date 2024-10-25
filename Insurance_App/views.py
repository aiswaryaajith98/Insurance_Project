from django.shortcuts import render

def index(request):
    return render(request,'index.html')

#COMPANY
def Company_Dashboard(request):
    return render(request,'company/Company_Dashboard.html')

def Company_AgentDetails(request):
    return render(request,'company/Company_AgentDetails.html')

def Company_AddAgent(request):
    return render(request,'company/Company_AddAgent.html')

def Company_EditAgent(request):
    return render(request,'company/Company_EditAgent.html')

def Company_ClientDetails(request):
    return render(request,'company/Company_ClientDetails.html')

def Company_ClientDetails1(request):
    return render(request,'company/Company_ClientDetails1.html')

def Company_ClientDetails2(request):
    return render(request,'company/Company_ClientDetails2.html')

def Company_AssignAgent(request):
    return render(request,'company/Company_AssignAgent.html')

def Company_AgentTracking(request):
    return render(request,'company/Company_AgentTracking.html')
#AGENTS
def Agent_Dashboard(request):
    return render(request,'agent/Agent_Dashboard.html')

def Agent_AgentProfile(request):
    return render(request,'agent/Agent_AgentProfile.html')

def Agent_ClientInfo(request):
    return render(request,'agent/Agent_ClientInfo.html')





