'''
Script para desfazer todos os likes do Twitter
'''
import datetime
import pandas as pd
import tweepy
import utils


def delete_favs(api, tweet_ids):
  '''
  Desfavorita todos os tweets cujo id
  está na lista tweet_ids.
  '''

  unlike_count = 0
  for tweet_id in tweet_ids:

    try:
      api.destroy_favorite(tweet_id)
      print(tweet_id, "descurtido!")
      unlike_count += 1

    except:
      print(tweet_id, 'não pode ser descurtido!')

  print("Pronto!", unlike_count, "tweets foram desafavoritados, ao todo")

def main():

  username = input("Digite o seu nome de usuário, sem a arroba, e aperte < ENTER >. Exemplo: jack\n")

  start = input("Digite a data antes da qual os favoritos devem ser deletados, no formato YYYY-MM-DD, e aperte < ENTER >.\n")

  utils.validate_date(start)

  input(f"ATENÇÃO: todos os favoritos anteriores à {start} serão deletados. Pressione < ENTER > para continuar.")

  api = utils.login()

  favs = utils.fetch_favs(api, username)
  favs = utils.filter_tweets(start, favs)

  delete_favs(api, favs)

if __name__ == '__main__':
  main()