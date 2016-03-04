from rest_framework import serializers

from snippets.models import Analysis, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ('id', 'user_id','created','days')