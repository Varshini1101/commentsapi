from rest_framework import serializers
from core.models import Comments

class commentserializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = (
            
            'email',
            
            'comment',
            'comment_time',
        )