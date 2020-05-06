# G1 Crawler

Script básico que pega informações das notícias do [g1](https://g1.globo.com).

## Requisitos

Use o [Python](https://python.org) 3 (testado com o 3.8) e o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/).

É necessário instalar o scrapy. É possível ver os passos de instalação para a sua distribuição na [documentação](https://docs.scrapy.org/en/latest/intro/install.html) deles. Se você estiver em um sistema ubuntu-based, basta usar:

```bash
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
```

E, depois das dependências instaladas, utilizar o pip para instalar o scrapy.

```bash
pip3 install scrapy
```

## Utilização

Para rodar o script, basta estar no projeto e rodar:

```bash
python3 -m scrapy runspider scrapy-g1.py
```

O scrapy é bastante verboso, então é possível desativar as informações de debug usando o parâmetro ```--debug-level=WARNING```. É possível, também, colocar a saída do json em um arquivo.

```bash
python3 -m scrapy runspider scrapy-g1.py > saida.json
```
Além disso, caso deseje mais notícias (e não só as três primeiras), o número de posts analisados pelo código é definido arbitráriamente por essa linha:
```python
posts = response.css('.feed-post')[:3] 
```
Então, é possível manipular a lista que o ```response.css``` retorna, analisando ela inteira, um elemento ou um range específico.