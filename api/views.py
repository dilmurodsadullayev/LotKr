from django.shortcuts import render
from api.serializers import TranslateLotinToCyrillicSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from .latin_to_cyrillic import latin_to_cyrillic
from .cyrillic_to_latin import cyrillic_to_latin
import api.validation_text_lang as validation_text_lang
# Create your views here.

class TranslateLotinToCrylic(APIView):

    @swagger_auto_schema(
        operation_description="Lotin tildagi so'zni kirill tiliga o'tkazish",
        request_body=TranslateLotinToCyrillicSerializer,
        responses={201: TranslateLotinToCyrillicSerializer}

    )

    

    def post(self, request):
        text = request.data.get("text", "")
        lang = request.data.get("lang", "")
        print(text, lang)

        if not text.strip() or not validation_text_lang.is_valid_text(text, lang):
            return Response(
                {"Message": "Iltimos, to‘g‘ri matn kiriting"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if lang.lower() == "kril":
            translation = latin_to_cyrillic(text)

            msg = {
                "text": text,
                "lang": lang,
                "translation": translation
            }
            return Response(msg, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": "Iltimos, 'kril' yoki 'lotin' tilini tanlang"}, status=status.HTTP_400_BAD_REQUEST)


class TranslateCrylicToLotin(APIView):

    @swagger_auto_schema(
        operation_description="Kirill tildagi so'zni lotin tiliga o'tkazish",
        request_body=TranslateLotinToCyrillicSerializer,
        responses={201: TranslateLotinToCyrillicSerializer}

    )

    

    def post(self, request):
        text = request.data.get("text", "")
        lang = request.data.get("lang", "")
        print(text, lang)

        if not text.strip() or not validation_text_lang.is_valid_text(text, lang):
            return Response(
                {"Message": "Iltimos, to‘g‘ri matn kiriting"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if lang.lower() == "lotin":
            translation = cyrillic_to_latin(text)

            msg = {
                "text": text,
                "lang": lang,
                "translation": translation
            }
            return Response(msg, status=status.HTTP_201_CREATED)
        else:
            return Response({"Message": "Iltimos, 'kril' yoki 'lotin' tilini tanlang"}, status=status.HTTP_400_BAD_REQUEST)
        

    
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)