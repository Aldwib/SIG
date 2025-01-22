import folium
from folium.plugins import *
from folium import *
import pandas as pd

# Baca file CSV
csv_file = "lokasi_atm.csv"  # Ganti dengan nama file CSV Anda
data = pd.read_csv(csv_file)

# Membuat peta
map = folium.Map(location=[0.5071, 101.4478], zoom_start=13)

# Menambahkan marker untuk setiap lokasi ATM
for index, row in data.iterrows():
    
    atm_icon = folium.CustomIcon(
        icon_image="E:/Folderr/Comp-vision/SIG/images/atm1.png",  # Ganti dengan path gambar Anda
        icon_size=(34, 34)  # Ukuran ikon (sesuaikan)
    )

    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        tooltip=row['Tooltip'],
        popup=folium.Popup(row['Popup'], max_width=300),
        icon=atm_icon,
    ).add_to(map)

LayerControl().add_to(map)
map.save("map.html")