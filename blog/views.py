
from .models import Blog
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        sender_name = request.POST['firstname']
        sender_email = request.POST['senderemail']
        sender_subject = request.POST['subject']

        message = " username: {} \n user mail: {} \n user message: {}".format(
            sender_name, sender_email, sender_subject)
        send_mail('Salut', message, sender_email, [
            'sectiacasatineretului@gmail.com'])
        return render(request, 'home/home.html', {'success': 'Multumim pentru mesaj!'})
    else:
        return render(request, 'home/home.html')


def blog(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def posts(request, pk_id):
    posts = get_object_or_404(Blog, pk=pk_id)
    return render(request, 'posts/posts.html', {'posts': posts})


def desprenoi(request):
    return render(request, 'blog/desprenoi.html')
