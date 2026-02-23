from rest_framework import serializers


class TranslateLotinToCyrillicSerializer(serializers.Serializer):
    text = serializers.CharField(
        max_length=255, 
        help_text="Lotin harflaridan iborat matn kiriting"
    )
    lang = serializers.CharField(
        max_length=5, 
        help_text="qaysi tilga o'kazmoqchisiz (kril/lotin)"
        )


