from rest_framework import serializers
from .models import Genre,Actor,Movie,Review
from django.contrib.auth.models import User
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['id','name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields=['id','name','birth_year','country']


class MovieSerializer(serializers.ModelSerializer):
    genres=GenreSerializer(read_only=True,many=True)
    actors=ActorSerializer(read_only=True,many=True)
    genres_ids=serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        write_only=True,many=True
    )
    actors_ids=serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        write_only=True,many=True
    )
    class Meta:
        model=Movie
        fields=['id','title','description','release_year','rating','genres','actors','created_at','updated_at','genres_ids','actors_ids']
        read_only_fields=['created_at','updated_at']

    def create(self, validated_data):
    
       genres_ids = validated_data.pop('genres_ids')
       actors_ids = validated_data.pop('actors_ids')

    
       movie = Movie.objects.create(**validated_data)

    
       movie.genres.set(genres_ids)
       movie.actors.set(actors_ids)

       return movie


    def update(self, instance, validated_data):
    
        genres_ids = validated_data.pop('genres_id',None)
        actors_ids = validated_data.pop('actors_id',None)

    
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

    
        if genres_ids is not None:
            instance.genres.set(genres_ids)

    
        if actors_ids is not None:
            instance.actors.set(actors_ids)

        return instance




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=['id','user','movie','rating','comment','created_at']
        read_only_fields=['created_at']



from django.contrib.auth.models import User
from rest_framework import serializers

class RigesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("this email allready used !")
        return value

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
