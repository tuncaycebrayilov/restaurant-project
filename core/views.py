from django.shortcuts import render, redirect
from datetime import date, timedelta, datetime
from .models import MenuItem, BlogPost, Reservation

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {'posts': posts})

def blog_detail(request, pk):
    post = BlogPost.objects.get(id=pk)
    return render(request, 'blog-detail.html', {'post': post})

def reservation(request):
    error = None

    if request.method == "POST":
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        reservation_date = request.POST.get('date')
        time_value = request.POST.get('time')
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests')

        today = date.today()
        max_date = today + timedelta(days=180)

        opening_time = datetime.strptime("17:00", "%H:%M").time()
        closing_time = datetime.strptime("23:00", "%H:%M").time()

        selected_date = date.fromisoformat(reservation_date)
        selected_time = datetime.strptime(time_value, "%H:%M").time()

        if selected_date < today:
            error = "You cannot select a past date."

        elif selected_date > max_date:
            error = "Reservations are available up to 6 months ahead."

        elif selected_time < opening_time or selected_time > closing_time:
            error = "Reservations are available between 17:00 and 23:00 only."

        elif selected_date == today and selected_time <= datetime.now().time():
            error = "You cannot select a past time."

        else:
            Reservation.objects.create(
                full_name=full_name,
                email=email,
                date=selected_date,
                time=selected_time,
                guests=guests,
                special_requests=special_requests
            )

            # Redirect instead of render
            return redirect('reservation_success')

    return render(request, 'reservation.html', {'error': error})

def menu(request):
    items = MenuItem.objects.all()
    return render(request, 'menu.html', {'items': items})

def reservation_success(request):
    return render(request, 'reservation-success.html')