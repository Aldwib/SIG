import folium
from folium.plugins import *
from folium import *
import pandas as pd

# Baca file CSV
csv_file = "lokasi_atm.csv"
data = pd.read_csv(csv_file)

# Custom CSS dan JavaScript untuk sidebar
custom_css = """
<style>
.sidebar {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 9999;  /* Ditingkatkan untuk memastikan selalu di atas */
    top: 0;
    right: 0;
    background-color: white;
    overflow-x: hidden;
    transition: all 0.5s ease;
    padding-top: 60px;
    box-shadow: -2px 0 5px rgba(0,0,0,0.1);
}

.sidebar.active {
    width: 400px;
}

.sidebar-content {
    opacity: 0;
    padding: 20px;
    transition: opacity 0.3s ease;
    margin-top: 6px;  /* Tambahkan margin agar konten tidak tertutup header */
}

.sidebar-content img {
    width: 360px;
    }

.sidebar.active .sidebar-content {
    opacity: 1;
    display: block;
}

.sidebar-header {
    display: flex;
    justify-content: space-between;

    padding: 20px;
    background-color: #4CAF50;
    color: white;
    position: fixed;
    width: 400px;  /* Sesuaikan dengan lebar sidebar */
    top: 0;
    right: -400px;  /* Sembunyikan di luar layar */
    z-index: 10000;
    transition: right 0.5s ease;
}

.sidebar.active .sidebar-header {
    right: 0;  /* Tampilkan saat active */
}

.menu-btn {
    position: fixed;
    z-index: 9998;
    right: 20px;
    top: 20px;
    background: white;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    display: flex;
    align-items: center;
}

.menu-btn i {
    font-size: 20px;
}

/* Tambahkan style untuk konten */
.atm-info {
    padding: 15px;
    background: #f9f9f9;
    border-radius: 8px;
    margin-bottom: 15px;
}

.atm-info img {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 15px;
}

.atm-info h4 {
    margin: 0 0 10px 0;
    color: #333;
}

.atm-info p {
    margin: 5px 0;
    color: #666;
}
</style>
"""

custom_js = """
<script>
function toggleSidebar() {
    document.getElementById("mySidebar").classList.toggle("active");
}

function updateSidebarContent(content, title) {
    document.getElementById("sidebarTitle").innerHTML = title;
    document.getElementById("sidebarContent").innerHTML = content;
    document.getElementById("mySidebar").classList.add("active");
}

// Tambahkan event listener untuk menutup sidebar ketika klik di luar
document.addEventListener('click', function(e) {
    if (!e.target.closest('.sidebar') && 
        !e.target.closest('.leaflet-marker-icon') &&
        !e.target.closest('.menu-btn')) {
        document.getElementById("mySidebar").classList.remove("active");
    }
});
</script>
"""

# Membuat peta
map = folium.Map(location=[0.5071, 101.4478], zoom_start=13)

# Update bagian pembuatan marker
for index, row in data.iterrows():
    # Buat marker dengan tooltip dan tanpa popup
    marker = folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        tooltip=row['Title'],  # Menampilkan title di sebelah marker
        icon=folium.CustomIcon(
            icon_image="icon/0.png",
            icon_size=(40, 40)
        )
    )
    
    # Tambahkan event listener untuk marker
    element = Element(f"""
        <script>
            (function() {{
                setTimeout(function() {{
                    var marker = document.getElementsByClassName('leaflet-marker-icon')[{index}];
                    if (marker) {{
                        marker.addEventListener('click', function() {{
                            // Reset semua marker ke default icon
                            var markers = document.querySelectorAll('.leaflet-marker-icon');
                            markers.forEach(function(m) {{
                                m.src = 'icon/0.png';
                            }});
                            
                            // Set icon selected untuk marker yang diklik
                            this.src = 'icon/atm.png';
                            
                            // Update sidebar
                            updateSidebarContent(
                                `{row['Content']}`,
                                '{row['Title']}'
                            );
                        }});
                    }}
                }}, 1000);
            }})();
        </script>
    """)
    
    marker.add_to(map)
    map.get_root().html.add_child(element)

# Menambahkan HTML elements untuk sidebar
sidebar_html = """
<div class="menu-btn" onclick="toggleSidebar()">
    <i class="fa fa-bars"></i>
</div>
<div id="mySidebar" class="sidebar">
    <div class="sidebar-header">
        <h3 id="sidebarTitle">ATM Information</h3>
        <span class="close-btn" onclick="toggleSidebar()">&times;</span>
    </div>
    <div class="sidebar-content" id="sidebarContent">
        <div class="atm-info">
            Select an ATM location to view details
        </div>
    </div>
</div>
"""

# Menambahkan Font Awesome untuk ikon
font_awesome = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
"""

# Menggabungkan semua HTML elements
map.get_root().html.add_child(folium.Element(font_awesome + custom_css + custom_js + sidebar_html))

# Menambahkan layer control
LayerControl().add_to(map)

# Menyimpan peta
map.save("map.html")