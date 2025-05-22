from bs4 import BeautifulSoup
import os
import datetime

# Input and output files
html_file = 'Tracks.html'
tracks_folder = 'Tracks'
output_file = 'Tracks_modified.html'

# Load HTML
with open(html_file, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

count_updated = 0

# Look at each <li> and read its data-src attribute
for li in soup.find_all('li'):
    data_src = li.get('data-src')
    if data_src and data_src.endswith('.mp3'):
        mp3_filename = os.path.basename(data_src)
        full_path = os.path.join(tracks_folder, mp3_filename)

        if os.path.exists(full_path):
            modified_time = os.path.getmtime(full_path)
            date_str = datetime.datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d')
            li['data-modified'] = date_str
            count_updated += 1
            print(f"✔ {mp3_filename} → data-modified={date_str}")
        else:
            print(f"⚠ File not found: {full_path}")

# Save the modified HTML
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(str(soup.prettify()))

print(f"\n✅ Done. {count_updated} songs updated with data-modified.")
