from bs4 import BeautifulSoup, NavigableString

# Load original file
with open("Tracks.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML to extract <li> tags
soup = BeautifulSoup(html_content, "html.parser")
track_list_ul = soup.find("ul", class_="track-list")
li_elements = track_list_ul.find_all("li", recursive=False)

# Sort <li> tags by data-title
sorted_lis = sorted(li_elements, key=lambda li: li.get("data-title", "").lower())

# Preferred attribute order
attribute_order = [
    "data-src", "data-title", "data-author", "data-category",
    "data-century", "data-date-composed", "data-modified", "data-comments"
]

# Build compact, single-line <li> entries
formatted_lis = []
for li in sorted_lis:
    attrs = {k: li[k] for k in attribute_order if li.has_attr(k)}
    attr_str = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    title = li.contents[0].strip() if isinstance(li.contents[0], NavigableString) else ""
    hover_box = li.find("div", class_="hover-box")
    hover_text = hover_box.decode_contents().strip() if hover_box else ""
    hover_html = f'<div class="hover-box">{hover_text}</div>' if hover_box else ""

    formatted_li = f'<li {attr_str}>{title}{hover_html}</li>\n'
    formatted_lis.append(formatted_li)

# Stitch together: before <ul>, <li>s, after </ul>
before_ul = html_content.split('<ul class="track-list">')[0] + '<ul class="track-list">\n\n'
after_ul = html_content.split('</ul>')[-1]

# Final HTML with a blank line between each <li>
final_html = before_ul + "\n".join(formatted_lis) + "\n</ul>" + after_ul

# Write to output
with open("Tracks_sorted_clean.html", "w", encoding="utf-8") as out:
    out.write(final_html)

print("✅ Final clean file saved as Tracks_sorted_clean.html")
