import base64
import io
from rest_framework.decorators import api_view
from rest_framework.response import Response
from deep_translator import GoogleTranslator
from gtts import gTTS

@api_view(['POST'])
def translate_text(request):
    try:
        # Get data from React
        text = request.data.get('text')
        source_lang = request.data.get('source_lang', 'auto')
        target_lang = request.data.get('target_lang', 'en')
        
        if not text:
            return Response({'error': 'Please provide text'}, status=400)

        # Step 1: Translate Text
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)

        # Step 2: Generate Audio (Text-to-Speech)
        audio_base64 = ""
        try:
            tts = gTTS(text=translated, lang=target_lang)
            fp = io.BytesIO()
            tts.write_to_fp(fp)
            fp.seek(0)
            audio_base64 = base64.b64encode(fp.read()).decode('utf-8')
        except Exception as e:
            print("Audio generation failed:", e)

        # Step 3: Send Final Response
        return Response({
            'status': 'success',
            'translated_text': translated,
            'audio_data': audio_base64
        })
        
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)