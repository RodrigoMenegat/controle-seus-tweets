'''
Esse programa salva os tweets mais recentes - todos que a API do twitter 
permite acessar - de um usuário em um arquivo de texto.
'''

import datetime
import os
import utils



def main():

  username = input("Digite o nome do usuário que você quer baixar, sem a arroba, e aperte < ENTER >. Exemplo: jack\n")

  api = utils.login()

  output = utils.fetch_tweets(api, username)

  if not os.path.exists("downloads/"):
    os.makedirs("downloads/")

  now = str(datetime.datetime.now()).replace(" ", "-").replace(":", "-")
  fpath = "downloads/tweets-by-" + username + "-" + now + ".csv"

  utils.save_csv(output, fpath)

  print("Pronto!")

if __name__ == "__main__":
  main()


