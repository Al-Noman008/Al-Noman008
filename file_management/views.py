from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
# Create your views here.

def upload_file(request):
    if request.method =="POST":
        form = DocumentForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()


    documents = Document.objects.all()
    return render(request,'upload.html',{'form':form, 'documents':documents})