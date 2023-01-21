from django.shortcuts import render
from .models import Note
from django.http import HttpResponse
# Create your views here.
def get_notes(request): 
    # this func will take one object by its id 
    notes = Note.objects.all()
    context = {"Notes": notes}
    return render (request, "notes_list.html",context)

def get_id_note (request,note_id):
    #this func will display everythings 
    note = Note.objects.get(id=note_id)
    return render(request,"note_detail.html",context=note)
#NOTE: dont forget that every func we created here we have to import it in the urls

def base(request):
    return render(request='base.html')