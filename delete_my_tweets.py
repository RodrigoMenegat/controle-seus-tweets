'''
Script para apagar todos os meus tweets mais antigos que determinada data
'''
import datetime
import pandas as pd
import tweepy
import utils


def delete_tweets(api, tweet_ids):

  '''
  Deleta os tweets cujos números
  identificadores estão na lista
  tweet_ids
  '''

  # Começa a deletar:
  delete_count = 0

  for tweet_id in tweet_ids:

      try:
          api.destroy_status(tweet_id)
          print(tweet_id, 'deletado!')
          delete_count += 1

      except:
          print(tweet_id, 'não pode ser deletado!')

  print('Pronto!', delete_count, 'tweets foram deletados, ao todo.')


##########################
### Execução principal ###
##########################

def main():

  username = input("Digite o seu usuário do Twitter, sem a arroba, e aperte < ENTER >. Exemplo: jack\n")

  start = input("Digite a data antes da qual os tweets devem ser deletados, no formato YYYY-MM-DD, e aperte < ENTER >.\n")

  utils.validate_date(start)

  input(f"ATENÇÃO: todos os tweets anteriores à {start} serão deletados. Pressione < ENTER > para continuar.")

  api = utils.login()

  tweets = utils.fetch_tweets(api, username)
  tweets = utils.filter_tweets(start, tweets)
  
  delete_tweets(api, tweets)

if __name__ == "__main__":
  main()


