from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from links.models import Link
from .forms import LinkForm
# Create your views here.

def redirect_view(request, pk):
    link_object = get_object_or_404(Link, pk=pk)
    return redirect(link_object.original_url)

def create_view(request):
    if request.method == "GET":
        form = LinkForm()
        return render(request, 'links/link_form.html', {'form': form})
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            link_object = form.save()
        shorten_url = request.scheme + "://" + request.get_host() + "/" + link_object.id
        return render(request, 'links/link_confirmation.html', context={ "shorten_url" : shorten_url })
