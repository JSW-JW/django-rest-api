from rest_framework import serializers

from ..models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'id',
            'user',
            'content',
            'image'
        )

    def validate_content(self, content):
        if len(content) > 1000:
            raise serializers.ValidationError("Content is too long.")

        return content

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)

        if image is None and content is None:
            raise serializers.ValidationError("Content or image is required")
        return data