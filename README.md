# controle-seus-tweets

Conjunto de scripts simples que usam o pacote [`tweepy`](https://github.com/tweepy/tweepy) para baixar todos os tweets e likes de um usuário no Twitter. Também contém scritps que permitem remover as publicações feitas e favoritadas.

O plano aqui não é coletar dados em grande escala, mas permitir que pessoas que não têm muita intimidade com programação consigam acessar, sem muita dificuldade, tudo o que publicaram na rede social.

## O que cada programa faz?

- `download_user_tweets.py`: baixa todos os tweets de um usuário em formato CSV, juntamente com algumas informações como data, número de RTs e número de curtidas
- `download_user_likes.py`: baixa todos os likes de um usuário em formato CSV, juntamente com informações sobre o tweet original
- `delete_my_tweets.py`: deleta todos os tweets do usuário que foram publicados antes de uma data estipulada.
- `delete_my_likes.py`: deleta todos as curtidas do usuário que aconteceram antes de uma data estipulada.

## Modo de usar

### Para quem manja um pouquinho de programação

Simplesmente clone o repositório, ajuste as credenciais em `credentials.py` e rode os scripts a partir do terminal. Viva! ✨

### Para leigos

**1.** Antes de mais nada, você precisa ter o Python 3 instalado em sua máquina. Se não tem , o primeiro passo é instalar [isso aqui](https://www.python.org/downloads/)! 

** 2.** Depois, você precisa baixar esse repositório – ou seja, essa pasta – para o seu computador. Clique no **botão "clone or download", em verde,** e baixe o arquivo no formato ZIP. Descompacte em um lugar de sua preferência – sugiro a área de trabalho.

**3.** Agora, substitua os trechos entre aspas simples que estão no arquivo `credentials.py` com as suas credenciais de acesso à API do Twitter. Não sabe o que é? **Calma!** Essas credenciais são quatro senhas necessárias para acessar os dados por trás do Twitter. O único problema é que você precisa pedir acesso. Você consegue fazer isso [aqui](https://developer.twitter.com/en/application/use-case).
Deve demorar algum tempo para liberar, mas quando tiver os códigos em mãos (eles devem parecer algo como `"xSsbxEa2812313xaer"`) é só colocar cada um deles em seu devido lugar no arquivo. **Não mexa em mais nada por lá (nem nos outros arquivos)!** 

**3.** Você vai precisar mexer no terminal de comando do computador. Sem medo! Apenas abra o aplicativo `Terminal`, caso use Mac ou Linux, ou o `Prompt de comando`, caso use Windows. 

**4.** Agora que você está na famosa telinha preta, precisamos caminhar até a pasta onde os arquivos que você baixou estão salvos. Digite o comando `cd` seguido do **caminho onde você salvou a pasta**. No meu caso, salvei a pasta na área de trabalho do Mac e tive de escrever o seguinte:

  ```
  cd ~/desktop/controle-seus-tweets/
  ```

  No Windows, geralmente é algo assim:

  ```
  cd C:/Users/SeuNomeDeUsuarioAqui/Desktop/controle-seus-tweets/
  ```

  Uma maneira simples de descobrir o caminho completo é **abrir as propriedades da pasta**.

**5.** Precisamos instalar algumas coisinhas que os programas que eu escrevi exigem. Na telinha preta, digite `pip install -r requirements.txt` e aperte enter. Um monte de letras vão pular na sua tela: são outras instalações. Não se preocupe: nada disso vai derreter seu computador. Espere tudo terminar.

**6.** Agora só falta rodar os programas! Para executar o script que baixa os *likes* de um usuário no formato de tabela, por exemplo, é só só digitar o seguinte no terminal e apertar enter:

  ```
  >> python download_user_likes.py
  ```

  Siga as instruções que aparecem na tela, informando o nome de usuário. Uma nova pasta chamada `downloads` vai surgir com um novo arquivo dentro dela. Para baixar os tweets, é a mesmíssica coisa, apenas substituindo o comando por `python download_user_tweets.py` ✨

  O processo para deletar seus tweets ou likes também é semelhante.

  ```
  >> python delete_my_tweets.py
  ```

  Aperte enter e siga, novamente, as instruções na tela, informando o seu nome de usuário e, dessa vez, a data limite. Todos os tweets (ou likes) que você publicou antes dela serão permanentemente deletados.

  Deu ruim? Tente digitar `python3` em vez de `python`. Ainda deu ruim? Abra um [issue](https://github.com/RodrigoMenegat/controle-seus-tweets/issues) e me conte o que está acontecendo!

**7.** Se você quiser fazer as operações de novo, só precisa seguir esse tutorial a partir do **4º passo**. 

**8.** Que tal aproveitar que você tem o Python instalado agora e aprender programação?


## Notas importantes
Por enquanto, os scripts só conseguem acessar os 9999 likes mais recentes de um usuário. Se você quer coletar mais do que isso, sinto muito :/