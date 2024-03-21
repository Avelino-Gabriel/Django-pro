from rest_framework.serializers import ModelSerializer
from mycontacts.models import Contact

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'image']