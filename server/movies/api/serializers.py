from django.contrib.auth.models import User, Group

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from movies.models import Genre, Movie, Comment


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(), message="Email have already uses.")])

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})

        user.set_password(password)
        user.save()
        return user


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    """ Serializer for User model """
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'is_active', 'is_superuser', 'groups')


class GenreSerializer(serializers.ModelSerializer):
    """ Serializer for movie model """
    class Meta:
        model = Genre
        fields = ('id', 'name', 'description')


class MovieSerializer(serializers.ModelSerializer):
    """ Serializer for movie model """
    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'stars', 'description', 'created')


class CommentSerializer(serializers.ModelSerializer):
    """  Serializer for comment model """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'movie', 'comment', 'visible', 'created')
