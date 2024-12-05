from django.db.models import Avg
from django.shortcuts import render, redirect
from .models import Rating
import requests
import re
from django.core.mail import send_mail
from django.conf import settings
import threading
import time

# Create your views here.

def check_nvidia_driver():
    url = "https://www.nvidia.com/Download/processFind.aspx?psid=101&pfid=816&osid=12&lid=1&whql=1&lang=en-us&ctk=0"
    response = requests.get(url)
    match = re.search(r'<td class="gridItem">(\d+\.\d+)</td>', response.text)
    if match:
        return match.group(1)
    return None

latest_version = check_nvidia_driver()

def send_update_emails(new_version):
    emails = Rating.objects.values_list('email', flat=True).distinct()
    subject = "New NVIDIA Driver Update Available"
    for email in emails:
        unsubscribe_link = f"https://nvidiarch.jleuthardt.com/unsubscribe?email={email}"
        message = f"A new NVIDIA driver version {new_version} is available. Please update to the latest version and rate on NVIDIArch.\n\nTo unsubscribe, click here: {unsubscribe_link}"
        send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

def periodic_check():
    global latest_version
    while True:
        new_version = check_nvidia_driver()
        if new_version and new_version != latest_version:
            send_update_emails(new_version)
            latest_version = new_version
        time.sleep(1800)  # Sleep for 30 minutes

# Start the periodic check in a separate thread
thread = threading.Thread(target=periodic_check)
thread.daemon = True
thread.start()

def unsubscribe(request):
    email = request.GET.get('email')
    if email:
        Rating.objects.filter(email=email).update(email='')
    return render(request, 'unsubscribe.html')

def home(request):
    ratings = Rating.objects.all()
    average_ratings = Rating.objects.values('driver').annotate(avg_rating=Avg('rating')).order_by('-avg_rating')
    return render(request, 'home.html', {'ratings': ratings, 'average_ratings': average_ratings, 'latest_version': latest_version})

def add_rating(request):
    if request.method == 'POST':
        driver = request.POST['driver']
        name = request.POST.get('name', 'Anonymous')
        rating = request.POST['rating']
        comment = request.POST['comment']
        date = request.POST.get('date', '')
        distro = request.POST.get('distro', '')
        email = request.POST.get('email', '')
        
        Rating.objects.create(driver=driver, name=name, rating=rating, comment=comment, date=date, distro=distro, email=email)
        return redirect('home')
    
    return render(request, 'addrating.html', {'latest_version': latest_version})

