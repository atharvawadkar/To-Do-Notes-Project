from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from . forms import AddNoteform
from .models import TodoNote



def add_note(request, form=None):
    if request.method =='GET':

        form=AddNoteform()

        return render(request,'add_note.html',{'form':form})
    else:

        form=AddNoteform(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['subject']
            description=form.cleaned_data['description']
            deadline = form.cleaned_data['deadline']
            print(subject,description,deadline)

            form.save()
    return render(request,'add_note.html')

def  get_note(request):
    qs_notes =TodoNote.objects.all()
    return render(request,'notes.html',{'qs_notes':qs_notes})



def delete_note(request):

   id=request.GET.get('id')

   if not TodoNote.objects.filter(id=id).count():
       return HttpResponse("No record found for id :")

   print("Deleting record with id ="+str(id))
   note =TodoNote.objects.get(id=id)
   note.delete()

   return HttpResponse("Record Deleted Successfullly "+str(id))

def edit_note(request):
    if request.method == "GET":
        id = request.GET.get('id')

        if not TodoNote.objects.filter(id=id).count():
            return HttpResponse("No Record Found for id: " + str(id))

        note = TodoNote.objects.get(id=id)
        data = {'subject': note.subject, 'description': note.description, 'deadline': note.deadline, 'id': id}
        # form = AddNoteForm(data)
        return render(request, 'edit_note.html', data)

    elif request.method == "POST":
        id = request.POST.get('id')
        subject = request.POST.get('subject')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')

        if not TodoNote.objects.filter(id=id).count():
            return HttpResponse("No Record Found for id: " + str(id))

        note = TodoNote.objects.get(id=id)
        note.subject = subject
        note.description = description
        note.deadline = deadline
        note.save()

        return HttpResponse("<h1>Form Submitted </h1>")