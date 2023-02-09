from django.shortcuts import redirect, get_object_or_404
from links.models import Link
# Create your views here.

def redirect_view(request, pk):
    link_object = get_object_or_404(Link, pk=pk)
    return redirect(link_object.original_url)