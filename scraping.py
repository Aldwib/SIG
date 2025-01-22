import overpy
import csv

# Buat instance Overpass API
api = overpy.Overpass()

# Kueri untuk mencari ATM di Pekanbaru (dalam Indonesia)
query = """
[out:json];
area["name"="Indonesia"]->.countryArea;
area["name"="Pekanbaru"](area.countryArea)->.cityArea;
node["amenity"="atm"](area.cityArea);
out body;
"""

# Eksekusi query
result = api.query(query)

# Tampilkan hasil jumlah data
print(f"Jumlah ATM ditemukan: {len(result.nodes)}")

# Simpan hasil ke file CSV
with open("atm_pekanbaru.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Country", "City", "Latitude", "Longitude"])
    for node in result.nodes:
        writer.writerow(["ATM", "Indonesia", "Pekanbaru", node.lat, node.lon])

print("Data berhasil disimpan ke atm_pekanbaru.csv")


# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import StaleElementReferenceException  # Import this exception
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# import time
# import pandas as pd
# from bs4 import BeautifulSoup

# filename = "data"
# link = "https://www.google.com/maps/search/ATM+BRI/@0.4852171,101.4050156,16z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDExNS4wIKXMDSoASAFQAw%3D%3D"

# browser = webdriver.Chrome()
# record = []
# e = []
# le = 0

# def Selenium_extractor():
#     action = ActionChains(browser)
#     e = []
#     record = []
#     le = 0

#     while True:
#         a = browser.find_elements(By.CLASS_NAME, "hfpxzc")  # Ambil elemen terbaru
#         print(f"Jumlah elemen ditemukan: {len(a)}")

#         if le > 20:  # Batas untuk menghentikan scroll jika tidak ada elemen baru
#             break

#         try:
#             scroll_origin = ScrollOrigin.from_element(a[-1])  # Elemen terakhir
#             action.scroll_from_origin(scroll_origin, 0, 1000).perform()
#             time.sleep(2)
#         except IndexError:
#             print("Tidak ada elemen untuk di-scroll")
#             break

#         if len(a) > len(e):  # Cek jika elemen baru muncul
#             le = 0
#         else:
#             le += 1

#     # Loop untuk klik pada setiap elemen
#     for i in range(len(a)):
#         a = browser.find_elements(By.CLASS_NAME, "hfpxzc")  # Refresh elemen sebelum klik
#         try:
#             action.move_to_element(a[i]).perform()
#             a[i].click()
#             time.sleep(2)
#         except StaleElementReferenceException:
#             print("Stale element detected, skipping...")
#             continue
#         except Exception as ex:
#             print(f"Error: {ex}")
#             continue

#         source = browser.page_source
#         soup = BeautifulSoup(source, 'html.parser')
#         try:
#             Name_Html = soup.findAll('h1', {"class": "DUwDvf fontHeadlineLarge"})
#             name = Name_Html[0].text
#             if name not in e:
#                 e.append(name)
#                 divs = soup.findAll('div', {"class": "Io6YTe fontBodyMedium"})
#                 phone = next((div.text for div in divs if div.text.startswith("+")), "Not available")
#                 address = divs[0].text if divs else "Not available"
#                 website = next((div.text for div in divs if "." in div.text[-4:]), "Not available")
#                 print([name, phone, address, website])
#                 record.append((name, phone, address, website))
#                 df = pd.DataFrame(record, columns=['Name', 'Phone number', 'Address', 'Website'])
#                 df.to_csv(filename + '.csv', index=False, encoding='utf-8')
#         except Exception as ex:
#             print(f"Error during parsing: {ex}")
#             continue


# browser.get(str(link))
# time.sleep(20)
# Selenium_extractor()