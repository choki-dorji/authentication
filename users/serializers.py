from rest_framework import serializers
from .models import NewUser, UserProfile, Fileupload


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'user_name', 'email', 'password', 'picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
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
