from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
import requests

class EmployeeLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is authenticated by verifying if 'employee_id' exists in the session
        is_authenticated = request.session.get('employee_id') is not None

        # If the user is not authenticated, redirect them to the login page
        if not is_authenticated:
            if request.path != reverse('login_check'):  # Assuming 'login_check' is the URL name for 'login/check/'
                return redirect(reverse('login_check'))
        
        # If the user is authenticated and tries to access the login page, redirect to the dashboard
        if is_authenticated and request.path == reverse('login_check'):
                return redirect(reverse('dash'))  # Assuming 'dash' is the URL name for the dashboard


class AuthMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
       

    def __call__(self, request):
        print(request.path) 
        print("Im Middleware")
        response=requests.get(f'{settings.SUPERADMIN_URL}superadmin/app1/api/AccountsMasterData_AppliViewsets/')
        result = response.json() if response.status_code in [200, 201] else None 
        result=result[0] if result else None
        request.session['masterData']=result.get('MasterDataImage') if result else ""
        return self.get_response(request)
        