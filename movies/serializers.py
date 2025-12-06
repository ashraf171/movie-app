from rest_framework import serializers
from .models import Genre,Actor,Movie,Review

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
    genres_id=serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        write_only=True,many=True
    )
    actors_id=serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        write_only=True,many=True
    )
    class Meta:
        model=Movie
        fields=['id','title','description','release_year','rating','genres','actors','created_at','updated_at','genres_id','actors_id']
        read_only_fields=['created_at','updated_at']

    def create(self, validated_data):
    # خذ IDs من الـ request
       genres_ids = self.context['request'].data.get('genres_id', [])
       actors_ids = self.context['request'].data.get('actors_id', [])

    # أنشئ الفيلم بدون العلاقات
       movie = Movie.objects.create(**validated_data)

    # أضف العلاقات Many-to-Many
       movie.genres.set(genres_ids)
       movie.actors.set(actors_ids)

       return movie


def update(self, instance, validated_data):
    # خذ IDs من الـ request
    genres_ids = self.context['request'].data.get('genres_id', None)
    actors_ids = self.context['request'].data.get('actors_id', None)

    # عدّل القيم الأساسية
    for attr, value in validated_data.items():
        setattr(instance, attr, value)
    instance.save()

    # لو المستخدم أرسل genres_id → حدّث العلاقة
    if genres_ids is not None:
        instance.genres.set(genres_ids)

    # لو أرسل actors_id → حدّث العلاقة
    if actors_ids is not None:
        instance.actors.set(actors_ids)

    return instance
