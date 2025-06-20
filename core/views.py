from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ColorBlindTest
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_protect

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    stats = {
        'total_tests': ColorBlindTest.objects.count(),
        'recent_tests': ColorBlindTest.objects.filter(
            created_at__gte=timezone.now() - timedelta(days=30)
        ).count(),
        'accuracy_rate': 98
    }
    return render(request, 'index.html', {'stats': stats})

@login_required
def dashboard(request):
    context = {
        'user': request.user,
        'tests': ColorBlindTest.objects.filter(user=request.user).order_by('-created_at')
    }
    return render(request, 'dashboard.html', context)

@csrf_protect
def analyze_colorblind(request):
    if request.method == 'POST':
        fundus_image = request.FILES.get('fundus_image')
        erg_data = request.FILES.get('erg_data')
        
        if fundus_image:
            # Create test record
            test = ColorBlindTest.objects.create(
                user=request.user,
                fundus_image=fundus_image,
                erg_data=erg_data,
                result_type='Processing',
                severity='Unknown',
                confidence=0
            )
            
            try:
                # Process image (placeholder for AI model)
                result = {
                    'type': 'Deuteranopia',
                    'severity': 'Moderate',
                    'confidence': 85
                }
                
                # Update test with results
                test.result_type = result['type']
                test.severity = result['severity']
                test.confidence = result['confidence']
                test.save()
                
                return JsonResponse({
                    'success': True,
                    'result': result
                })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': str(e)
                })
                
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_protect
def analyze_blood(request):
    if request.method == 'POST':
        # Your blood analysis logic here
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
