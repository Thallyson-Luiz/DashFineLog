from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def resize_image_django(image_django, new_width=800, optimize=True, quality=60):
    '''
    Redimensiona uma imagem usando o Pillow

    Parametros:
        image_django: Objeto ImageField do Django
        new_width: Largura da imagem nova
        optimize: Otimizar a imagem (True para otimizar, False para manter a qualidade)
        quality: Qualidade da imagem

    Ex:
        resize_image_django(image_django, new_width=800, optimize=True, quality=60)
        resize_image_django(image_django, new_width=800)

    Retorna:
        Imagem redimensionada
    '''


    # Abre a imagem direto do campo, sem .file
    image_django.open()  # garante que está aberto
    image_pillow = Image.open(image_django)

    original_width, original_height = image_pillow.size

    # Se a largura já é menor ou igual, não faz nada
    if original_width <= new_width:
        return

    # Calcula nova altura proporcional
    new_height = round(new_width * original_height / original_width)
    new_image = image_pillow.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Salva em memória
    image_io = BytesIO()
    new_image.save(image_io, format=image_pillow.format, optimize=optimize, quality=quality)
    image_io.seek(0)

    # Substitui o conteúdo do campo de imagem
    image_django.save(
        image_django.name,
        ContentFile(image_io.read()),
        save=False  # não salva o modelo ainda
    )