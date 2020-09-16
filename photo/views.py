from django.shortcuts import redirect, render
from .forms import *

def index(request):
	form = PhotoPostForm()

	if request.method == "POST":
		form = PhotoPostForm(request.POST, request.FILES)
		if form.is_valid():
			photo = form.save(commit=False)
			photo.user = request.user
			form.save()
			return redirect('index')
	
	photos = Photo.objects.order_by('-id')

	context = {
		"form": form,
		"photos": photos
	}
	return render(request, "photo/index.html", context)