from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from mygallary.models import newpost
from django.contrib import messages

# Create your views here.

#Home 
def home(request):
     db = newpost.objects.all().order_by('-date')
     context = {'db': db}
     return render(request, 'home/index.html',context)


#New post
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
    

#Delete post
def delete(request, id):
    db = newpost.objects.get(id=id)
    db.delete()
    messages.success(request, "Your post is deleted successfully")
    return redirect('/')


#Edit post
def edit(request, id):
    post = get_object_or_404(newpost, id=id)
    if request.method == 'POST':
        edit_caption = request.POST.get('edit-caption')
        edit_image = request.FILES.get('edit-image')
        if edit_caption or edit_image:
            post.caption = edit_caption
            if edit_image:
                post.image = edit_image
            post.save()
            print("saved!")
            return redirect('home')
    else:
        context = {'post': post, 'error': 'Oops! Something went wrong :('}
        return render(request, 'home/edit.html', context=context)
    

#Search post
def search_query(request):
    if request.method == 'GET':
        print("1st done")
        query = request.GET.get('query')
        print("2nd done")
        if query:
            print("3rd done")
            search = newpost.objects.filter( caption=query, image=query)
            print("4th done")
    return render(request, 'home/search.html', {'search': search})
    

