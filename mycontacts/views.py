from django.shortcuts import get_object_or_404, render, redirect
from .forms import AddForm
from .models import Contact
import os
from django_senai.settings import BASE_DIR

def etc(arquivo):
    path = f'{BASE_DIR}/media'
    dir = os.listdir(path)
    for file in dir:
        if file == arquivo:
            os.remove(f'{path}/{file}')

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        django_form = AddForm(request.POST, request.FILES)
        if django_form.is_valid():
            new_contact = django_form.save(commit=False)
            new_contact.save()
            return redirect(show)
        else:
            return render(request, 'mycontacts/add.html', {'form': django_form})
    else:
        return render(request, 'mycontacts/add.html')
    
def delete(request, contact_id):
    contact = get_object_or_404(Contact, id = contact_id)
    if request.method == 'POST':
            # Se o formulário foi submetido, exclua o contato
            etc(contact.foto.name)
            contact.delete()
            # Redireciona para uma página de confirmação ou outra página após a exclusão
            return redirect(show)
    return render(request, 'mycontacts/delete.html', {'contact': contact})

def editar(request, id):
    if request.method == 'POST':
        contact = Contact.objects.get(id=id)
        django_form = AddForm(request.POST, request.FILES, instance=contact)
        if django_form.is_valid():
            django_form.save()
            if request.POST.get('delete'):
                etc(contact.foto.name) 
                contact.foto = None

            contact.save()
            return redirect(show)
    else:
        contact = Contact.objects.get(id=id) 
        return render(request, 'mycontacts/edit.html', {'contact': contact})


    
    