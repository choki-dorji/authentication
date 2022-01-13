from rest_framework import serializers
from .models import NewUser, UserProfile, Fileupload
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth import get_user_model

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'user_name', 'email', 'password', 'picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # def create(self, validated_data):
    #     user = User.objects.create(user_name = validated_data['user_name'], password = validated_data['password'], email = validated_data['email'], picture = validated_data['picture'])
    #     return user

    def create(self, validated_data):
        ##password hash
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserProfileSerializers(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = UserProfile
        fields = "__all__"

class FileuploadSerializers(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model = Fileupload
        fields = "__all__"