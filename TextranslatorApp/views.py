from django.shortcuts import render
from googletrans import Translator
from googletrans.models import Detected


def translator(request):
    return render(request, 'translator.html')


def translated(request):
    if request.method == "GET":
        text = request.GET.get('text')
        lang = request.GET.get('lang')

        if text and lang:
            try:
                # Connect to translator
                translator = Translator()

                # Detect language
                dt = translator.detect(text)
                dt2 = dt.lang

                # Translate the text
                translated = translator.translate(text, dest=lang)
                tr = translated.text

                d = {'translated': tr, 'ulang': dt2, 'tlang': lang}
                return render(request, 'translated.html', d)

            except Exception as e:
                error_message = f"Translation failed: {str(e)}"
                return render(request, 'translated.html', {'error_message': error_message})

        else:
            error_message = "Text or language not provided for translation."
            return render(request, 'translated.html', {'error_message': error_message})

    return render(request, 'translated.html')