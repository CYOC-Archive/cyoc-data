import os
import csv
import sys
import base64
import re
from bs4 import BeautifulSoup

def extract_chapter_id(link):
    match = re.search(r'chapter_(\d+)\.html', link)
    if match:
        return match.group(1)
    return ''

def extract_data_from_html(file_path):
    try:
        with open(file_path, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')

            chapter_text = soup.find('p', id='chapter-text')
            chapter_date = soup.find('span', class_='chapter-date')
            chapter_author = soup.find('span', class_='chapter-author')
            prev_link = soup.find('a', id='previouschapterlink')
            chapter_title_tag = soup.find('h2', class_='title')

            # Base64 encode the HTML content of chapter_text
            if chapter_text:
                html_content = chapter_text.decode_contents().strip()
                encoded_chapter_text = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
            else:
                encoded_chapter_text = ''

            prev_link_href = prev_link['href'] if prev_link and 'href' in prev_link.attrs else ''
            prev_chapter_id = extract_chapter_id(prev_link_href)

            # Extract current chapter ID from filename
            current_chapter_id = extract_chapter_id(os.path.basename(file_path))

            # Extract chapter title
            chapter_title = chapter_title_tag.get_text(strip=True) if chapter_title_tag else ''

            chapter_author_id = ''
            if chapter_author:
                author_link = chapter_author.find('a')
                if author_link and 'href' in author_link.attrs:
                    match = re.search(r'user_(\d+)\.html', author_link['href'])
                    if match:
                        chapter_author_id = match.group(1)

            return {
                'Filename': os.path.basename(file_path),
                'Current Chapter ID': current_chapter_id,
                'Chapter Date': chapter_date.get_text(strip=True) if chapter_date else '',
                'Author ID': chapter_author_id,
                'Author': chapter_author.get_text(strip=True) if chapter_author else '',
                'Previous Chapter Link': prev_link_href,
                'Previous Chapter ID': prev_chapter_id,
                'Chapter Title': chapter_title,
                'Chapter Text (base64)': encoded_chapter_text
            }
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def extract_all_html_to_csv(input_folder, output_csv):
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a valid directory.")
        return

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Filename',
            'Current Chapter ID',
            'Chapter Date',
            'Author ID',
            'Author',
            'Previous Chapter Link',
            'Previous Chapter ID',
            'Chapter Title',
            'Chapter Text (base64)'
        ]
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            quoting=csv.QUOTE_ALL,  # <-- Quote all fields
            escapechar='\\',        # <-- Escape special characters
            doublequote=True
        )
        writer.writeheader()

        for filename in os.listdir(input_folder):
            if filename.endswith('.html'):
                file_path = os.path.join(input_folder, filename)
                data = extract_data_from_html(file_path)
                if data:
                    writer.writerow(data)
                    print(f"Processed: {filename}")

    print(f"Extraction complete. CSV saved to: {output_csv}")

if __name__ == "__main__":
    # You can run with command-line args or hardcode paths here
    if len(sys.argv) == 3:
        input_folder = sys.argv[1]
        output_csv = sys.argv[2]
    else:
        input_folder = "input/interactives"
        output_csv = os.path.join("output", "output.csv")

    extract_all_html_to_csv(input_folder, output_csv)
