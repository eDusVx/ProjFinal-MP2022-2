   
   # Foi feito um deploy do sistema portanto é possível acessar pelo endereço: https://ristorante12.herokuapp.com/  :+1:
O projeto foi feito utilizando Python 3.10.7 e o framework de desenvolvimento web Django.

Para compilar o programa localmente:

1) Abrir o arquivo do código,instalar os arquivos necessários abrindo um terminal integrado a pasta principal e digitando:

    pip install -r requirements.txt

2) Criar um ambiente virtual com o comando:
 
    mkvirtualenv nome_do_ambiente_vitual

3) Para iniciar o ambiente virtual:

    workon nome_do_ambiente_vitual

4) Instalar novamente as dependencias,mas agora no ambiente virtual:

    pip install -r requirements.txt

5) Rodar o projeto com:

    py manage.py runserver

6) Será gerado um link HTTPS,basta colá-lo no navegador para rodar o sistema
