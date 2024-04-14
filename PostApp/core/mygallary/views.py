from django.shortcuts import render, redirect
from mygallary.models import newpost
from django.contrib import messages

# Create your views here.
def home(request):
     db = newpost.objects.all().order_by('-date')
     context = {'db': db}
    #  return render(request, 'home/index.html', context=context)
     return render(request, 'home/index.html',context)

def form(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        np = newpost(caption=caption, image=image)
        np.save()
        db = newpost.objects.all()
        messages.success(request, "Your post is uploaded successfully")
       
        
        return redirect('/')  
    else:
        return render(request, 'home/form.html')
