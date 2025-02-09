import pandas as pd
import re

# Load CSV file
csv_file = "lokasi_atm.csv"
df = pd.read_csv(csv_file)

# Generate HTML file with modern design
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daftar Lokasi ATM</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            background-color: #f5f5f5;
        }

        header {
            background: #003366;
            color: white;
            padding: 1rem 0;
            margin-bottom: 2rem;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }

        h1 {
            text-align: center;
            margin-bottom: 1rem;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 2rem;
        }

        nav ul li a {
            text-decoration: none;
            color: white;
            font-size: 1.1rem;
            position: relative;
            padding: 0.5rem 0;
        }

        nav ul li a::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: -2px;
            width: 0%;
            height: 2px;
            background: white;
            transition: width 0.3s ease;
        }

        nav ul li a:hover::after {
            width: 100%;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 1rem;
        }

        .filter-container {
            margin-bottom: 1rem;
        }

        .table-container {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow: hidden;
            margin: 1rem 0;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 600px;
        }

        th, td {
            padding: 1rem;
            text-align: left;
            border-bottom: 1px solid #eee;
        }

        th {
            background-color: #f8f9fa;
            font-weight: 600;
            color: #333;
        }

        tr:hover {
            background-color: #f8f9fa;
        }

        .content-cell {
            display: flex;
            gap: 2rem;
            align-items: start;
            padding: 1rem;
        }

        .content-cell img {
            width: 300px;
            height: 300px;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .content-cell div {
            flex: 1;
        }

        .content-cell b {
            display: block;
            font-size: 1.1rem;
            color: #003366;
            margin-bottom: 1rem;
        }

        .content-cell p {
            color: #666;
            margin-bottom: 1rem;
        }

        .content-cell a {
            color: #0066cc;
            text-decoration: none;
            display: inline-block;
            margin-top: 0.5rem;
        }

        .content-cell a:hover {
            text-decoration: underline;
        }

        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
                gap: 1rem;
            }

            .table-container {
                overflow-x: auto;
            }

            .content-cell {
                flex-direction: column;
                gap: 1rem;
            }

            .content-cell img {
                width: 100%;
                height: auto;
                max-width: 300px;
            }
        }

        .image-container {
            width: 300px;
            height: 300px;
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .image-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .content-cell {
            padding: 1rem;
        }

        .content-cell b {
            display: block;
            font-size: 1.1rem;
            color: #003366;
            margin-bottom: 1rem;
        }

        .content-cell p {
            color: #666;
            margin-bottom: 1rem;
        }

        @media (max-width: 1024px) {
            .image-container {
                width: 200px;
                height: 200px;
            }
        }

        @media (max-width: 768px) {
            .image-container {
                width: 150px;
                height: 150px;
            }
        }

        .title-cell {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        
        .map-link {
            color: #0066cc;
            text-decoration: none;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 0.3rem;
        }
        
        .map-link:hover {
            text-decoration: underline;
        }
        
        .map-link i {
            font-size: 0.8rem;
        }

        /* Footer*/
        .footer {
            background: #003366; /* Warna gelap */
            color: white;
            text-align: center;
            padding: 20px 0;
            font-size: 16px;
            position: relative;
            bottom: 0;
            width: 100%;
        }

        .footer-content p {
            margin: 5px 0;
        }
        
    </style>
</head>
<body>
    <header>
        <div class="header-content">
            <h1>Sistem Informasi Geografis Bank BCA & BRI Pekanbaru</h1>
            <nav>
                <ul>
                    <li><a href="index.html">Beranda</a></li>
                    <li><a href="map.html">Peta</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="container">
        <div class="filter-container">
            <label for="filter">Filter by Bank:</label>
            <select id="filter">
                <option value="all">All</option>
                <option value="BCA">BCA</option>
                <option value="BRI">BRI</option>
            </select>
        </div>
        <div class="table-container">
            <table id="atmTable">
                <tr>
                    <th>Koordinat</th>
                    <th>Title</th>
                    <th>Informasi</th>
                    <th>Gambar</th>
                </tr>
"""

for _, row in df.iterrows():
    # Extract image tag from Content
    img_pattern = r'<img[^>]+>'
    img_match = re.search(img_pattern, row['Content'])
    content_without_img = re.sub(img_pattern, '', row['Content']) if img_match else row['Content']
    img_tag = img_match.group(0) if img_match else ''
    
    # Create map link with coordinates
    map_link = f'<a href="map.html?lat={row["Latitude"]}&lng={row["Longitude"]}&title={row["Title"]}" class="map-link"><i class="fas fa-map-marker-alt"></i> Lihat pada peta</a>'
    
    # Determine the bank from the title
    bank = "BCA" if "BCA" in row['Title'] else "BRI" if "BRI" in row['Title'] else "Other"
    
    html_content += f"""
                <tr class="atm-row" data-bank="{bank}">
                    <td style="white-space: nowrap;">
                        <div>Lat: {row['Latitude']}</div>
                        <div>Long: {row['Longitude']}</div>
                    </td>
                    <td>
                        <div class="title-cell">
                            {row['Title']}
                            {map_link}
                        </div>
                    </td>
                    <td>
                        <div class="content-cell">
                            {content_without_img}
                        </div>
                    </td>
                    <td style="width: 300px;">
                        <div class="image-container">
                            {img_tag}
                        </div>
                    </td>
                </tr>
    """

html_content += """
            </table>
        </div>
    </div>
    
    <footer class="footer">
        <div class="footer-content">
            <p>&copy; 2025 ALIF JAWA | CIHUYY</p>
            <p>Temukan lokasi bank BCA & BRI dengan mudah dan cepat.</p>
        </div>
    </footer>

    <script>
        document.getElementById("filter").addEventListener("change", function() {
            var filter = this.value.toUpperCase();
            var rows = document.querySelectorAll(".atm-row");
            
            rows.forEach(row => {
                var bank = row.getAttribute("data-bank").toUpperCase();
                if (filter === "ALL" || bank === filter) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        });
    </script>
</body>
</html>
"""

# Save to HTML file
output_file = "list.html"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_content)

# print(f"File HTML telah disimpan di {output_file}")