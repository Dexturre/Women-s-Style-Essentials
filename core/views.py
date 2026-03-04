from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-created_at')[:3]  # Spotlight favorites
    return render(request, 'index.html', {
        'categories': categories,
        'products': products
    })

def blog(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'blog.html', {
        'categories': categories,
        'products': products
    })

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    products = category.products.all().order_by('-created_at')
    return render(request, 'category_detail.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def about(request): return render(request, 'about.html')
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not name or not email or not message:
            messages.error(request, 'Please fill in all required fields correctly.')
            return render(request, 'contact.html')

        # Construct Email
        full_message = f"Message from: {name} ({email})\n\nSubject: {subject}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                f"New Contact Form Submission: {subject}",
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Thank you! Your message has been sent successfully. We will get back to you soon.')
        except Exception as e:
            messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')

    return render(request, 'contact.html')

def privacy(request): return render(request, 'privacy.html')
def disclosure(request): return render(request, 'disclosure.html')
