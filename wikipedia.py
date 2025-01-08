import random
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_random_wikipedia_page():
  """
  Öffnet eine zufällige Wikipedia-Seite in Chrome.
  """
  driver = webdriver.Chrome()
  driver.get("https://de.wikipedia.org/wiki/Spezial:Zuf%C3%A4llige_Seite")
  return driver


def count_links(driver):
  """
  Zählt die Anzahl der Links auf einer Webseite.
  """
  links = driver.find_elements(By.CSS_SELECTOR, "a")
  return len(links)


def follow_random_link(driver):
  """
  Wählt einen zufälligen Link auf einer Seite und öffnet ihn.
  """
  links = driver.find_elements(By.CSS_SELECTOR, "a")
  random_link = random.choice(links)
  random_link.click()


def main():
  """
  Hauptfunktion, die die zufällige Wikipedia-Suche und das Folgen von Links wiederholt.
  """
  driver = get_random_wikipedia_page()
  for _ in range(10):  # Anzahl der Durchgänge
    print("Anzahl der Links:", count_links(driver))
    follow_random_link(driver)

  driver.quit()


if __name__ == "__main__":
  main()
