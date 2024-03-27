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
            print(file)
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
            foto = request.FILES.get('foto')
            if foto:
                new_contact.foto = foto
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
    contact = Contact.objects.get(id=id) 
    return render(request, 'mycontacts/edit.html', {'contact': contact})

def update(request, id):
    vfoto = request.FILES.get('foto')
    vnome = request.POST.get('name')
    vrelation = request.POST.get('relation')
    vphone = request.POST.get('phone')
    vemail = request.POST.get('email')

    contact = Contact.objects.get(id=id)
    etc(contact.foto.name) 
    if vfoto:
        contact.foto = vfoto
    contact.name = vnome
    contact.relation = vrelation
    contact.phone = vphone
    contact.email = vemail
    contact.save()
    return redirect(show)
    