'''
Funções utilitárias compartilhadas entre os vários scripts
'''

import credentials
import csv
import datetime
import pandas as pd
import tweepy


def validate_date(date_text):
  '''
  Verifica se a data entrada pelo usuário
  está no foramto YYYY-MM-DD. Se não estiver,
  levanta uma exeção com mensagem de erro.
  '''

  try:
    datetime.datetime.strptime(date_text, '%Y-%m-%d')

  except ValueError:
    raise ValueError("A data não está no formato YYYY-MM-DD. Execute o programa novamente.")

def login():
  '''
  Autentica e loga no twitter usando as facilidades
  built-in do Tweepy.
  '''

  auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
  auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
  api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

  print("Autenticado como: %s" % api.me().screen_name)

  return api

def fetch_tweets(api, username):
  '''
  Baixa todos os tweets do usuário
  determinado em 'username'
  '''

  tweets_dict = {}  
  all_tweets = []

  new_tweets = api.user_timeline(username, tweet_mode='extended', count=200)

  all_tweets.extend(new_tweets)

  # Salva o id do tweet antigo menos um
  oldest = all_tweets[-1].id - 1

  while len(new_tweets) > 0:   # Continua pegando tweets até a requisição retornar nada

      # Todos as requests posteriores usam max_id "para avançar no tempo"
      new_tweets = api.user_timeline(username, tweet_mode='extended', count=200, max_id=oldest)

      all_tweets.extend(new_tweets)

      # Atualiza o id
      oldest = all_tweets[-1].id - 1

  # Transform the tweepy tweets into a 2D array that will populate the csv
  output = [ 
                [ tweet.id, 
                  tweet.created_at, 
                  tweet.created_at.strftime("%d-%m-%Y %H:%M:%S"), 
                  tweet.full_text,
                  tweet.retweet_count,
                  tweet.favorite_count,
                  username ] for tweet in all_tweets
          ]

  for sublist in output:
    sublist.append(username)


  return output

def fetch_favs(api, username):
  '''
  Pega os tweets favoritados
  pelo usuário 'username' e retorna
  uma lista com os respectivos ids.
  '''

  output = tweepy.Cursor(api.favorites, id=username, tweet_mode="extended").items(9999)

  output = [ 
                [ tweet.id, 
                  tweet.created_at, 
                  tweet.created_at.strftime("%d-%m-%Y %H:%M:%S"), 
                  tweet.full_text,
                  tweet.retweet_count,
                  tweet.favorite_count,
                  username ] for tweet in output
          ]

  return output

def filter_tweets(start, tweets):
  '''
  Usa o dataframe com todos os tweets
  e a data de corte, depois da qual os
  tweets devem ser mantidos, para gerar
  uma lista com os ids das publicações
  devem ser removidas.
  '''


  now = datetime.datetime.now()
  start_date = pd.to_datetime(start, format = "%Y-%m-%d")

  # Filtra intervalo de tweets que quero manter
  keep_dates = pd.date_range(start=start_date, end=now)
  keep_dates = [str(date)[:10] for date in keep_dates]

  # Cria uma lista de ids cujo tweet deve ser mantido
  tweets_to_delete = [ tweet[0] for tweet in tweets if str(pd.to_datetime(tweet[1]))[:10] not in keep_dates ]

  return tweets_to_delete

def save_csv(output, fpath):

  '''
  Salva os tweets que estão em 'output',
  gerados pela função fetch_tweets, em
  um arquivo csv determinado por fp.
  '''

  with open(fpath, "w+") as file:
    writer = csv.writer(file)
    writer.writerow(["id","datetime","created_at","text","retweet_count", "favorite_count", "username"])
    writer.writerows(output)