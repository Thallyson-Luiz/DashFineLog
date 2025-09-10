import os
from django.conf import settings

def domain_context(request):
    """
    Função context processor para injetar as variáveis de ambiente relacionadas ao domínio no contexto de todos os templates.

    Essa função é usada como um context processor para fornecer duas variáveis de ambiente ao contexto de todos os templates:

    - **DOMAIN_HOST**: O host do domínio, obtido da variável de ambiente 'DOMAIN_HOST'. Por padrão, é '127.0.0.1'.
    - **PORT**: A porta do domínio, obtida da variável de ambiente 'PORT'. Por padrão, é '8000'.

    Essas variáveis de ambiente são úteis para construir URLs absolutas em todos os templates do projeto.

    Retorna um dicionário contendo as variáveis de ambiente acima mencionadas.
    
    """
    domain_host = os.getenv('DOMAIN_HOST', '127.0.0.1')
    port = os.getenv('PORT', '8000')
    
    # Determine protocol based on DEBUG mode
    protocol = 'http' if settings.DEBUG else 'https'
    
    # Build full URL
    if settings.DEBUG:
        base_url = f"{protocol}://{domain_host}:{port}"
    else:
        base_url = f"{protocol}://{domain_host}"
    
    return {
        'DOMAIN_HOST': domain_host,
        'BASE_URL': base_url,
        'API_BASE_URL': base_url,
    }
