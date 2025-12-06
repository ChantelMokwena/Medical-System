from accounts.models import AuditLog

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AuditLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Log API requests
        if request.path.startswith('/api/') and request.user.is_authenticated:
            if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
                action_map = {
                    'POST': 'create',
                    'PUT': 'update',
                    'PATCH': 'update',
                    'DELETE': 'delete'
                }
                
                AuditLog.objects.create(
                    user=request.user,
                    action=action_map.get(request.method, 'read'),
                    model_name=request.path.split('/')[2] if len(request.path.split('/')) > 2 else 'unknown',
                    ip_address=get_client_ip(request)
                )
        
        return response