from constance import config
from django.http import JsonResponse

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if getattr(request.user, 'is_staff', False):
            return self.get_response(request)
        if getattr(config, 'MAINTENANCE_MODE', False):
            return JsonResponse(
                {"detail": "The system is currently under maintenance. Please try again later."},
                status=503
            )
        return self.get_response(request)