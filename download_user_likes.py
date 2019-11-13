'''
Script para desfazer todos os likes do Twitter
'''
import datetime
import os
import utils


def unfav_tweets(api, tweet_ids):
  '''
  Desfavorita todos os tweets cujo id
  está na lista tweet_ids.
  '''

  for tweet_id in tweet_ids:
    api.destroy_favorite(tweet_id)

def main():

  username = input("Digite o seu nome de usuário, sem a arroba, e aperte < ENTER >. Exemplo: @jack\n")

  api = utils.login()

  favs = utils.fetch_favs(api, username)

  if not os.path.exists("downloads/"):
    os.makedirs("downloads/")

  now = str(datetime.datetime.now()).replace(" ", "-").replace(":", "-")
  fpath = "downloads/favs-by-" + username + "-" + now + ".csv"

  utils.save_csv(favs, fpath)

if __name__ == '__main__':
  main()