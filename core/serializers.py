from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from . import models

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id','username','password', 'email','first_name','last_name']

class UserSerializer(BaseUserSerializer):
    username = serializers.CharField()
    address_line1 = serializers.CharField(source='address.line1')
    address_city = serializers.CharField(source='address.city')
    address_state = serializers.CharField(source='address.state')
    address_pincode = serializers.CharField(source='address.pincode')
    profile_picture = serializers.ImageField(source='profile_picture.image')
    password = serializers.CharField(write_only=True)
    profile = serializers.PrimaryKeyRelatedField(queryset=models.Profile.objects.all(), source='user_profile.profile')

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'email',
            'password', 'address_line1', 'address_city', 'address_state',
            'address_pincode', 'profile_picture', 'profile']

    def create(self, validated_data):
        print(validated_data)        
        address = validated_data.pop("address")
        profile_picture = validated_data.pop("profile_picture")
        profile = validated_data.pop("user_profile")['profile']
        
        user = UserCreateSerializer.create(UserCreateSerializer(), validated_data)
        user_profile = models.UserProfile()
        user_profile.user = user
        user_profile.profile = profile
        user_profile.save()

        address["user_id"] = user.id
        address = AddressSerializer.create(AddressSerializer(), address)

        profile_picture["user_id"] = user.id
        profile_picture = ProfilePictureSerializer.create(ProfilePictureSerializer(), profile_picture)

        return user

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = ['user_id', 'line1', 'city', 'state', 'pincode']

class ProfilePictureSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = models.ProfilePicture
        fields = ['user_id', 'first_name', 'last_name', 'image']
