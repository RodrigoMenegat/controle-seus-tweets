# controle-seus-tweets

Conjunto de scripts simples que usam o pacote [`tweepy`](https://github.com/tweepy/tweepy) para baixar todos os tweets e likes de um usuário no Twitter. Também contém scritps que permitem remover as publicações feitas e favoritadas.

O plano aqui não é coletar dados em grande escala, mas permitir que pessoas que não têm muita intimidade com programação consigam acessar, sem muita dificuldade, tudo o que publicaram na rede social.

## Modo de usar

Primeiro, substitua as variáveis em `credentials.py` com as suas credenciais de acesso à [API do Twitter](https://developer.twitter.com/en/application/use-case)

Simplesmente clone esse repositório e execute os scripts a partir da linha de comando. 

Para garantir que você tem os pacotes necessários instalados (as únicas dependências são o `pandas` e o `tweepy`), pode ser útil executar `pip install -r requirements.txt` antes de tentar rodar os programas. 

O exemplo abaixo mostra como executar, a partir de um terminal Unix, o programa que faz download de todos os likes de um usuário:

```
>> cd controle-seus-tweets
>> python download_user_likes.py
```

Siga as instruções que aparecem na tela, informando o nome de usuário. Um sub-diretório chamado `downloads` vai surgir com um arquivo CSV dentro dele ✨

O processo para deletar seus tweets ou likes também é semelhante.

```
>> cd controle-seus-tweets
>> python delete_my_tweets.py
```

Siga, novamente, as instruções na tela, informando o seu nome de usuário e, dessa vez, a data limite. Todos os tweets (ou likes) que você publicou antes dela serão permanentemente deletados.

## O que cada script faz?

- `download_user_tweets.py`: baixa todos os tweets de um usuário em formato CSV, juntamente com algumas informações como data, número de RTs e número de curtidas
- `download_user_likes.py`: baixa todos os likes de um usuário em formato CSV, juntamente com informações sobre o tweet original
- `delete_my_tweets.py`: deleta todos os tweets do usuário que foram publicados antes de uma data estipulada.
- `delete_my_likes.py`: deleta todos as curtidas do usuário que aconteceram antes de uma data estipulada.

## Notas importantes
Por enquanto, os scripts só conseguem acessar os 9999 likes mais recentes de um usuário. Se você quer coletar mais do que isso, sinto muito :/