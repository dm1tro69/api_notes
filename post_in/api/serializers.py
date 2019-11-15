from rest_framework.serializers import (IntegerField, CharField, Serializer, ModelSerializer,
                                        HyperlinkedIdentityField, SerializerMethodField)
from notes.models import Note
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        queryset = model.objects.all()
        fields = ('id', 'email', 'password', 'name', 'staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        user.save()
        return user


    def update(self, instance, validated_data):
        instance.set_password(validated_data.pop('password', ''))
        return super().update(instance, validated_data)



class NoteSerializer(ModelSerializer):
    author = SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return str(obj.author.id)
    class Meta:
        model = Note
        fields = '__all__'


class ThinNoteSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='notes-detail')
    class Meta:
        model = Note
        fields = ('id', 'title', 'url')


# class NoteSerializer(Serializer):
#     id = IntegerField(read_only=True)
#     title = CharField(max_length=250, required=True)
#     text = CharField(required=False, allow_blank=True)
#
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.text = validated_data.get('text', instance.text)
#         instance.save()
#         return instance
