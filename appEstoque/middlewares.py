import logging

logger = logging.getLogger('custom')

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        logger.info('O middleware foi executado: Obtendo requisição...')

        if 'X-Meu_Header' in request.headers:
            request.session['meu_header'] = request.headers['X-Meu-Header']
            logger.info('Valor do cabeçalho armazenado na sessão: %s', request.session['meu_header'])
        
        response = self.get_response(request)

        logger.info('O middleware foi executado: Obtendo resposta...')

        return response
    