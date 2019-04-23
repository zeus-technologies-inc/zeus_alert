from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


User = get_user_model()


class UserCreationSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
