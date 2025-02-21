import folium
from folium.plugins import *
from folium import *
import pandas as pd

# Data lokasi untuk bank dan ATM
lokasi_atm_list = [
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
    },
    {
        "lokasi": [0.536026381691666, 101.44551671167665],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Unit Juanda",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/BRI Unit Juanda.jpg" 
                         width="200"><br>
            <b>Bank BRI Unit Juanda</b><br>
            <p>
            Lokasi: Jl. Ir. H. Juanda No.81-83, Sago, Kec. Senapelan, Kota Pekanbaru, Riau 28155<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo <br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
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
            - Informasi Saldo <br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
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
            - Informasi Saldo <br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
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
            - Informasi Saldo <br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.5231103672517159, 101.44223053866102],  # Koordinat lokasi baru
        "tooltip": "Bank BRI KCP Ahmad Yani",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Bank BCA A. Yani.png" 
                         width="200"><br>
            <b>Bank BRI KCP Ahmad Yani</b><br>
            <p>
            Lokasi: Jl. Jend. Ahmad Yani No.41 C, Kota Baru, Kec. Pekanbaru Kota, Kota Pekanbaru, Riau 28113<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo <br>
            - Customer Service
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.48172199314575, 101.41846972997268],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Soekarno-Hatta",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/atm bri Soekarno-Hatta.png" 
                         width="200"><br>
            <b>Bank BRI Unit Kota Bertuah</b><br>
            <p>
            Lokasi: Jl. Soekarno - Hatta No.174, Delima, Kec. Tampan, Kota Pekanbaru, Riau 28292<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo <br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="https://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
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
    },
    {
        "lokasi": [0.4239468,101.4377786],  # Koordinat lokasi 1
        "tooltip": "ATM BRI",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Jl. Kaharuddin Nst di batalyon.png" 
                         width="200"><br>
            <b>ATM BRI</b><br>
            <p>
            Lokasi: Simpang Tiga, Kec. Bukit Raya, Kota Pekanbaru, Riau 28283<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.4773509,101.4067191],  # Koordinat lokasi baru
        "tooltip": "ATM Indomaret Delima 1",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/bri indomaret delima.png" 
                         width="200"><br>
            <b>ATM Indomaret Delima 1</b><br>
            <p>
            Lokasi: Jl. Delima No.24, Delima, Kec. Tampan, Kota Pekanbaru, Riau 28292<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.4642594,101.4001326],  # Koordinat lokasi baru
        "tooltip": "ATM BRI Indomaret Subrantas 360",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM BRI Indomaret subrantas 360.png" 
                         width="200"><br>
            <b>ATM BRI Indomaret Subrantas 360</b><br>
            <p>
            Lokasi: Jl. HR. Soebrantas, Delima, Kec. Tampan, Kota Pekanbaru, Riau 28293<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.46367687748319586, 101.40140100504804],  # Koordinat lokasi baru
        "tooltip": "ATM BRI Indomaret Spg. Purwodadi Pekanbaru",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Indomaret Spg. Purwodadi Pekanbaru.png" 
                         width="200"><br>
            <b>ATM BRI Indomaret Spg. Purwodadi Pekanbaru</b><br>
            <p>
            Lokasi: Jl. Purwodadi Ujung, Sidomulyo Bar., Kec. Tampan, Kota Pekanbaru, Riau 28293<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.463145, 101.453322],  # Koordinat lokasi baru
        "tooltip": "ATM BCA Indomaret Kaharuddin Nasution 105",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM BCA Indomaret Kaharuddin Nasution 105.png" 
                         width="200"><br>
            <b>ATM BCA Indomaret Kaharuddin Nasution 105</b><br>
            <p>
            Lokasi: Simpang Tiga, Kec. Bukit Raya, Kota Pekanbaru, Riau<br>
            Buka jam 07.00–23.00<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.46113735883579127, 101.40189050683874],  # Koordinat lokasi baru
        "tooltip": "ATM BCA Swalayan D'Seven",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Swalayan D'Seven.png" 
                         width="200"><br>
            <b>ATM BCA Swalayan D'Seven</b><br>
            <p>
            Lokasi : Sidomulyo Bar., Kec. Tampan, Kota Pekanbaru, Riau 28294<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.4645533,101.3714302],  # Koordinat lokasi baru
        "tooltip": "Indomaret SPBU PRIMA PUTRA PABAN",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/Indomaret SPBU PRIMA PUTRA PABAN.png" 
                         width="200"><br>
            <b>Indomaret SPBU PRIMA PUTRA PABAN</b><br>
            <p>
            Lokasi: Simpang Baru, Kec. Tampan, Kota Pekanbaru, Riau 28293<br>
            Buka 24 jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.5209476, 101.4198492],  # Koordinat lokasi baru
        "tooltip": "ATM BCA BIG LAND - Pekanbaru",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM BCA BIG LAND - Pekanbaru.png" 
                         width="200"><br>
            <b>ATM BCA BIG LAND - Pekanbaru</b><br>
            <p>
            Lokasi: Jl. Soekarno - Hatta No.8, Labuh Baru Bar., Kec. Payung Sekaki, Kota Pekanbaru, Riau 28291<br>
            Buka jam 09.00-17.00<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.44811446462005416, 101.41773559917709],  # Koordinat lokasi baru
        "tooltip": "ATM BCA PERTAMINA",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/ATM BCA pertamina.png" 
                         width="200"><br>
            <b>ATM BCA PERTAMINA</b><br>
            <p>
            Lokasi: Jl. Soekarno - Hatta, Sidomulyo Bar., Kec. Tampan, Kota Pekanbaru, Riau 28294<br>
            Buka jam 07.00-23.00<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.5172108757411183, 101.42297327062687],  # Koordinat lokasi baru
        "tooltip": "BCA KCP Kas Durian",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/BCA KCP Kas Durian.png" 
                         width="200"><br>
            <b>BCA KCP Kas Durian</b><br>
            <p>
            Lokasi: Jl. Durian No.64, Labuh Baru Tim., Kec. Payung Sekaki, Kota Pekanbaru, Riau 28291<br>
            Buka jam 09.00-17.00<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo <br>
            - Customer Service
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    # Lokasi survey langsung -------
    {
        "lokasi": [0.4676157, 101.4044837],  # Koordinat lokasi baru
        "tooltip": "ATM BCA Delima",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/images/atm bca delima.jpg" 
                         width="200"><br>
            <b>	ATM BCA Alfamart</b><br>
            Buka ? jam<br>
            <p>
            Lokasi: Jl. Delima, RT.01/RW.02, Tampan, Kec. Tampan, Kota Pekanbaru, Riau 28292<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.5304166839239566, 101.44209714204648],  # Koordinat lokasi baru
        "tooltip": "ATM BCA & BRI Pasar kodim",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/mesin atm bca&bri, pasar kodim.jpg" 
                         width="200"><br>
            <b>ATM Bank BCA</b><br>
            <p>
            Lokasi: Jl. Jend. Ahmad Yani No.43, Padang Bulan, Kec. Senapelan, Kota Pekanbaru, Riau 28155<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            - Setor Tunai (BCA)
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a><br>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.501997, 101.423809],  # Koordinat lokasi baru
        "tooltip": "Mesin ATM BCA",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/mesin atm bca, jl nangka.jpg" 
                         width="200"><br>
            <b>ATM Bank BCA</b><br>
            <p>
            Lokasi: Jl. Tuan Tambusai No.18J,K,L, Labuh Baru Tim., Kec. Payung Sekaki, Kota Pekanbaru, Riau 28292<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.506257, 101.436936],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Unit Tuanku Tambusai Pekanbaru",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/bank atm bri, jl tuanku.jpg" 
                         width="200"><br>
            <b>Bank BRI Unit Tuanku Tambusai</b><br>
            <p>
            Lokasi: Jl. Tuanku Tambusai No.22, Labuh Baru Tim., Kec. Sukajadi, Kota Pekanbaru, Riau 28122<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.525302, 101.434421],  # Koordinat lokasi baru
        "tooltip": "Mesin ATM BRI Melur",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/mesin atm bri, jl melur.jpg" 
                         width="200"><br>
            <b>ATM Bank BCA</b><br>
            <p>
            Lokasi: Jl. Melur No.103, Harjosari, Kec. Sukajadi, Kota Pekanbaru, Riau 28156<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.527508, 101.434490],  # Koordinat lokasi baru
        "tooltip": "Mesin ATM BCA Melur Swalayan",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/mesin atm bca, melur swalayan.jpg" 
                         width="200"><br>
            <b>ATM Bank BCA</b><br>
            <p>
            Lokasi: Jl. Melur-Pekanbaru, Harjosari, Kec. Sukajadi, Kota Pekanbaru, Riau 28156<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
    {
        "lokasi": [0.480041, 101.434597],  # Koordinat lokasi baru
        "tooltip": "Bank BRI KK Bukit Raya",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/bank atm bri, bukit raya.jpg" 
                         width="200"><br>
            <b>Bank BRI KK Bukit Raya</b><br>
            <p>
            Lokasi: Jl. Sidomulyo Tim., Kota Pekanbaru, Riau<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.45707402696870386, 101.45271692154765],  # Koordinat lokasi baru
        "tooltip": "Bank BRI KCP Simpang Tiga",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/bank atm bri, KCP simpang3.jpg" 
                         width="200"><br>
            <b>Bank BRI KCP Simpang Tiga</b><br>
            <p>
            Lokasi: Jl. Kharudin Nasution No.171 E-F, Riau 29352<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.44265529695190275, 101.44926425525068],  # Koordinat lokasi baru
        "tooltip": "Bank BRI Unit Marpoyan",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/bank atm bri, kcp marpoyan.jpg" 
                         width="200"><br>
            <b>Bank BRI Unit Marpoyan</b><br>
            <p>
            Lokasi: Jl. Kaharuddin Nst No.292B, Perhentian Marpoyan, Kec. Marpoyan Damai, Kota Pekanbaru, Riau 28284<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo<br>
            - Setor Tunai <br>
            - Customer Service
            </p>
            <a href="http://bri.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BRI</a>
        </div>
        """,
    },
    {
        "lokasi": [0.437723, 101.455343],  # Koordinat lokasi baru
        "tooltip": "ATM BCA Pasir Putih",
        "popup": """
        <div style="font-family: Arial; font-size: 12px; line-height: 1.5;">
            <img src="E:/Folderr/Comp-vision/SIG/survey langsung/mesin atm bca, pasir putih.jpg" 
                         width="200"><br>
            <b>ATM BCA Pasir Putih</b><br>
            <p>
            Lokasi: CFQ4+34G Tanah Merah, Kabupaten Kampar, Riau<br>
            Buka ? jam<br>
            Layanan: <br>
            - Penarikan Tunai<br>
            - Transfer Antar Rekening<br>
            - Informasi Saldo
            </p>
            <a href="https://www.bca.co.id/" target="_blank" style="color: blue; text-decoration: underline;">Kunjungi Situs BCA</a>
        </div>
        """,
    },
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
df.to_csv("sumber data/lokasi_atm.csv", index=False)
print("Data berhasil disimpan ke lokasi_atm.csv!")