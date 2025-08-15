import time

import requests
from bs4 import BeautifulSoup
import os

url = "https://kpd.gddkia.gov.pl/index.php/pl/archiwalne-dane/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Znajdź wszystkie linki do plików .xlsx
links = soup.find_all("a", href=True)
xlsx_links = [link["href"] for link in links if link["href"].endswith(".xlsx")]
print(f"Znaleziono {len(xlsx_links)} plików .xlsx do pobrania.")
print(f"Linki do plików .xlsx: {xlsx_links}")




# Pobierz każdy plik
for link in xlsx_links:

    print(f"link: {link}")
    filename = link.split("/")[-1]
    file_url = link if link.startswith("http") else f"https://kpd.gddkia.gov.pl{link}"
    print(f"file url: {file_url}")
    file_data = requests.get(file_url).content


    time.sleep(10)  # Opóźnienie 1 sekundy między żądaniami, aby nie przeciążać serwera


