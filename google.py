import json
import os
import random
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_user_agents():
  """
  Lädt die **einzige** JSON-Datei im Skriptordner und gibt die User Agents zurück.
  """
  directory = Path(".")
  json_file_path = next(directory.glob("*.json"))
  with open(json_file_path, "r") as f:
    data = json.load(f)
  return data["data"]


def search_google(search_term, user_agent):
  """
  Führt eine Google-Suche im Browser mit dem angegebenen Suchbegriff und User Agent durch.
  """
  options = webdriver.ChromeOptions()
  options.add_argument("--user-agent={}".format(user_agent))
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.google.com")
  search_box = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
  search_box.send_keys(search_term)
  search_box.submit()
  driver.quit()


def get_random_words(filename):
  """
  Liest die Textdatei und wählt 2 zufällige Wörter aus.
  """
  with open(filename, "r") as f:
    words = [line.strip() for line in f]
  return random.sample(words, 2)


def main():
  """
  Hauptfunktion, die die User Agents lädt, die Suche durchführt und die Ergebnisse ausgibt.
  """
  user_agents = get_user_agents()
  search_terms = get_random_words("diceware-dereko.txt")
  search_term = " ".join(search_terms)
  for user_agent in user_agents:
    print("Suche mit User Agent:", user_agent)
    print("Suchbegriff:", search_term)
    search_google(search_term, user_agent)
    print()


if __name__ == "__main__":
  main()