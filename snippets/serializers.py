from rest_framework import serializers
from snippets.models import Analysis, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user_id  =serializers.IntegerField()
    days = serializers.IntegerField()
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Analysis.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """

        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.days = validated_data.get('days', instance.days)
        instance.save()
        return instance