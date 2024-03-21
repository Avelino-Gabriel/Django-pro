from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .forms import AddForm
from .serializers import PhotoSerializer
from .models import Contact

class PhotoListCreateView(APIView):
    name = 'photo_list_create_view'

    def get(self, request):
        photos = Contact.foto
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self, request):
       serializer = PhotoSerializer(request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
       return Response(serializer.errorS, status = status.HTTP_406_NOT_ACCEPTABLE)


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
            new_contact.img = request.FILES['foto']  # Atribuindo a imagem ao campo img
            new_contact.save()
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html', {'contacts': contact_list})
        else:
            return render(request, 'mycontacts/add.html', {'form': django_form})
    else:
        return render(request, 'mycontacts/add.html')

    