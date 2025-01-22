import folium
from folium.plugins import *
from folium import *
import pandas as pd

# Data lokasi untuk bank dan ATM
lokasi_atm_list = [
    {
        "lokasi": [0.535616948748213, 101.4408593952205],  # Koordinat lokasi 1
        "tooltip": "ATM Bank BCA A. Yani, Pekanbaru",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/E:/Folderr/Comp-vision/SIG/images/Bank BCA A. Yani.png" 
                         width="200"><br>
            <b>ATM Bank BCA A. Yani</b><br>
            <p>
            Lokasi: Jl. Jend. Ahmad Yani No.41 C, Kota Baru, Kec. Pekanbaru Kota, Kota Pekanbaru, Riau 28113<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
        # "icon_color": "blue",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5298348953911128, 101.44714816749695],  # Koordinat lokasi baru
        "tooltip": "ATM Bank BCA 4266 Plaza Sukaramai",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM Bank BCA 4266 Plaza Sukaramai.png" 
                         width="200"><br>
            <b>ATM Bank BCA 4266 Plaza Sukaramai</b><br>
            <p>
            Lokasi: Jl. Jend. Sudirman, Sukaramai, Kec. Pekanbaru Kota, Kota Pekanbaru, Riau 28111<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
        # "icon_color": "blue",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5304492237446169, 101.41977976564557],  # Koordinat lokasi baru
        "tooltip": "ATM BCA Wira Kencana",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM BCA Wira Kencana.jpg" 
                         width="200"><br>
            <b>ATM BCA Wira Kencana</b><br>
            <p>
            Lokasi: Jl. Soekarno - Hatta No.56, Labuh Baru Tim., Kec. Payung Sekaki, Kota Pekanbaru, Riau 28291<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
        # "icon_color": "blue",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.4985930249548644, 101.45487352146594],  # Koordinat lokasi baru
        "tooltip": "ATM Bank BCA 2907-RSIA Syafira",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM Bank BCA 2907-RSIA Syafira.png" 
                         width="200"><br>
            <b>ATM Bank BCA 2907-RSIA Syafira</b><br>
            <p>
            Lokasi: Jl. Jend. Sudirman, Tengkerang Tengah, Kec. Pekanbaru Kota, Kota Pekanbaru, Riau 28115<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
        # "icon_color": "blue",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5324745669193345, 101.44814685215337],  # Koordinat lokasi baru
        "tooltip": "ATM Bank BCA 6544-Senapelan",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM Bank BCA 6544-Senapelan.png" 
                         width="200"><br>
            <b>ATM Bank BCA 6544-Senapelan</b><br>
            <p>
            Lokasi: Lobby Senapelan Plaza, Jl. Jend. Sudirman No. 121, Rintis, Kec. Lima Puluh, Kota Pekanbaru, Riau 28111<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
        # "icon_color": "blue",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.536026381691666, 101.44551671167665],  # Koordinat lokasi baru
        "tooltip": "BRI Unit Juanda",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/BRI Unit Juanda.jpg" 
                         width="200"><br>
            <b>BRI Unit Juanda</b><br>
            <p>
            Lokasi: Jl. Ir. H. Juanda No.81-83, Sago, Kec. Senapelan, Kota Pekanbaru, Riau 28155<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5266026764023216, 101.44723811101905],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Unit Sudirman",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/bri unit sudirman.jpg" 
                         width="200"><br>
            <b>Bank BRI Unit Sudirman</b><br>
            <p>
            Lokasi: Jl. Jend. Sudirman, Sukaramai, Kec. Pekanbaru Kota, Kota Pekanbaru, Riau 28156<br>
            Buka jam 08.00–16.00<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5285256, 101.4390289],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Unit Pasar Kodim",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Bank BRI Unit Pasar Kodim.png" 
                         width="200"><br>
            <b>Bank BRI Unit Pasar Kodim</b><br>
            <p>
            Lokasi: Jl. Cempaka No.88 A, RT.002/RW.002, Padang Bulan, Kec. Senapelan, Kota Pekanbaru, Riau 28281<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5172272, 101.4178318],  # Koordinat lokasi baru
        "tooltip": "Bank BRI UNIT Sigunggung",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Bank BRI UNIT Sigunggung.jpg" 
                         width="200"><br>
            <b>Bank BRI UNIT Sigunggung</b><br>
            <p>
            Lokasi: Jl. Dharma Bakti No.4, Labuh Baru Bar., Kec. Payung Sekaki, Kota Pekanbaru, Riau 28292<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.5231103672517159, 101.44223053866102],  # Koordinat lokasi baru
        "tooltip": "Bank BRI KCP Ahmad Yani",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Bank bri kcp ayani.jpg" 
                         width="200"><br>
            <b>Bank BRI KCP Ahmad Yani</b><br>
            <p>
            Lokasi: Jl. Jend. Ahmad Yani, Tanah Datar, Kec. Pekanbaru Kota, Kota Pekanbaru, Riau 28293<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.4676157, 101.4044837],  # Koordinat lokasi baru
        "tooltip": "Bank BRI & BCA Delima",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/atm bri delima.png" 
                         width="200"><br>
            <b>	ATM BRI & BCA Alfamart</b><br>
            <p>
            Lokasi: Jl. Delima, RT.01/RW.02, Tampan, Kec. Tampan, Kota Pekanbaru, Riau 28292<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a><br>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.48172199314575, 101.41846972997268],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Soekarno-Hatta",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/atm bri Soekarno-Hatta.png" 
                         width="200"><br>
            <b>BRI - Unit Kota Bertuah</b><br>
            <p>
            Lokasi: Jl. Soekarno - Hatta No.174, Delima, Kec. Tampan, Kota Pekanbaru, Riau 28292<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    {
        "lokasi": [0.48057124821529784, 101.41874971526678],  # Koordinat lokasi baru
        "tooltip": "ATM BRI Indomaret Fresh",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM bri indomaret fresh.png" 
                         width="200"><br>
            <b>Indomaret Plus Sukarno Hatta</b><br>
            <p>
            Lokasi: Jl. Sukarno Hatta No. 1 A-D, Sidomulyo Timur, Marpoyan Damai, Pekanbaru City, Riau 28282<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
        # "icon_color": "green",
        # "icon_text_color": "white",
    },
    #  baris kode iseng ajah
    # {
    #     "lokasi": [0.4989230706488193, 101.41563236858819],  # Koordinat lokasi baru
    #     "tooltip": "Universitas Muhammadiyah Riau",
    #     "popup": """
    #     <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
    #         <img src="E:/Folderr/Comp-vision/SIG/images/umri.png" 
    #                      width="200"><br>
    #         <b>Universitas Muhammadiyah Riau</b><br>
    #         <p>
    #         Simpang Komersil Arengka (SKA, Jl. Tuanku Tambusai, Delima, Kec. Tampan, Kota Pekanbaru, Riau 28290<br>
    #         Tutup jam 21:00<br>
    #         </p>
    #         <a href="https://daftar.umri.ac.id/" target="_blank" style="color: blue; text-decoration: underline;">Ayo Klik aku, klik aku</a>
    #     </div>
    #     """,
    #     "icon_color": "green",
    #     "icon_text_color": "yellow",
    # },
]

data = []
for atm in lokasi_atm_list:
    data.append({
        "Latitude": atm["lokasi"][0],
        "Longitude": atm["lokasi"][1],
        "Tooltip": atm["tooltip"],
        "Popup": atm["popup"].strip()  # Menghapus whitespace berlebih
    })

df = pd.DataFrame(data)

# Simpan ke file CSV
df.to_csv("lokasi_atm.csv", index=False)
print("Data berhasil disimpan ke lokasi_atm.csv!")