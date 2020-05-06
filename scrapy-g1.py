import scrapy
import json

'''
Essa classe será utilizada pelo parser do scrapy
com o objetivo de obter as informações do site
g1.globo.com, das três primeiras notícias
'''
class G1Spyder(scrapy.Spider):
    name = 'g1spyder'
    start_urls = ['http://g1.globo.com']
    def parse (self, response):
        posts = response.css('.feed-post')[:3] #aqui, obtemos os posts e selecionamos apenas os três primeiros
        noticias = []
        for post in posts:
            titulo = post.css('.feed-post-link::text').extract_first() #obtemos o texto do título
            descricao = post.css('.feed-post-body-resumo::text').extract_first() #obtemos o texto do subtítulo
            imagem = post.css(".bstn-fd-picture-image::attr(src)").extract_first() #obtemos o caminho da imagem, mas dessa vez usando xpath por se tratar de um elemento
            noticia = {
                'titulo': titulo,
                'descricao': descricao,
                'imagem': imagem
            }
            noticias.append(noticia)
        print(json.dumps(noticias, indent=2, ensure_ascii=False)) # no fim, printamos o json, com algumas configurações extras para facilitar a visualização - não é recomendado que se utilize o indent e o ensure_ascii=False em produção