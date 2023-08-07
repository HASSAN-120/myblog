from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, ContactMessage
from .forms import ContactForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Save the contact message to the database
            ContactMessage.objects.create(name=name, email=email, message=message)

            # Optionally, you can add code here to send an email notification to yourself
            # or the site administrators regarding the new contact message.

            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')