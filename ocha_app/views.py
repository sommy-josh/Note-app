from django.shortcuts import render,redirect
from .models import NoteBook

# Create your views here.
def index(request):
    note_book =NoteBook.objects.all()
    
    return render(request, 'index.html', {'note_book':note_book})


def Add_note(request):
    if request.method=='POST':
        title = request.POST['title']
        notes = request.POST['notes']
        book = NoteBook.objects.create(title=title, notes=notes)
        book.save()

        return redirect('index')
    else:
        return render(request,'Add.html')

def Delete_note(request, pk):
    note =NoteBook.objects.get(pk=pk)
    note.delete()
    return redirect('index')




    
    
    


   

   