from rest_framework import serializers

from musician import models


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = (
            "id",
            "first_name",
            "last_name",
            "instrument",
            "age",
            "date_of_applying",
            "is_adult",
        )
