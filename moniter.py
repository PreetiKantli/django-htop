from django.http import JsonResponse
import psutil

def htop(request):
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    data = {
        'cpu_percent': cpu_percent,
        'memory_total': memory.total,
        'memory_used': memory.used,
        'memory_free': memory.available
    }
    return JsonResponse(data)
