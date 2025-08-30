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


    # Abre a imagem e obtem suas dimensões
    image_pillow = Image.open(image_django.file)
    original_width, original_height = image_pillow.size

    # Para caso a imagem seja menor que a largura desejada
    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    # Redimensionando a imagem
    new_height = round(new_width * original_height / original_width) # Calculando a nova altura
    new_image = image_pillow.resize((new_width, new_height), Image.Resampling.LANCZOS) # Redimensionando a imagem


    image_io = BytesIO() # Criando um buffer para salvar a imagem
    new_image.save(image_io, format=image_pillow.format, optimize=optimize, quality=quality) # Salvando a imagem

    # Atualizando a imagem no Django
    image_django.save(
        image_django.name,
        ContentFile(image_io.getvalue()),
        save=False  
    )

    return new_image