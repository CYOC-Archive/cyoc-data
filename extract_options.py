import os
import csv
import sys
import re
from bs4 import BeautifulSoup

def extract_chapter_id(link):
    match = re.search(r'chapter_(\d+)', link)
    if match:
        return match.group(1)
    return ''

def extract_options_from_html(file_path):
    options = []
    parent_id = extract_chapter_id(os.path.basename(file_path))

    with open(file_path, 'r', errors="ignore") as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Extract options from <ul id="subchapters" ...>
        subchapters_ul = soup.find('ul', id='subchapters')
        if subchapters_ul:
            for li in subchapters_ul.find_all('li'):
                a = li.find('a', href=True)
                if a:
                    chapter_id = extract_chapter_id(a['href'])
                    option_title = a.get_text(strip=True)
                    options.append({
                        'Parent ID': parent_id,
                        'Chapter ID': chapter_id,
                        'Option ID': '',  # No option ID for these, leave blank
                        'Option Title': option_title
#                        'Type': 'subchapter'  # <-- Flag as subchapter
                    })

        # Extract options from <ul class="subchapter-list suggested-list">
        suggested_ul = soup.find('ul', class_='subchapter-list suggested-list')
        if suggested_ul:
            for li in suggested_ul.find_all('li'):
                a = li.find('a', href=True)
                if a:
                    # Option ID from id attribute, e.g. id="suggested_499818"
                    option_id = ''
                    if a.has_attr('id'):
                        match = re.search(r'suggested_(\d+)', a['id'])
                        if match:
                            option_id = match.group(1)
                    option_title = a.get_text(strip=True)
                    chapter_id = ""
                    options.append({
                        'Parent ID': parent_id,
                        'Chapter ID': chapter_id,
                        'Option ID': option_id,
                        'Option Title': option_title
#                        'Type': 'option'  # <-- Flag as option
                    })
    return options

def extract_all_options_to_csv(input_folder, output_csv):
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a valid directory.")
        return

    os.makedirs(os.path.dirname(output_csv), exist_ok=True)

    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'Parent ID',
            'Chapter ID', 
            'Option ID', 
            'Option Title', 
#            'Type'  # <-- Add Type field to CSV
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
                options = extract_options_from_html(file_path)
                for option in options:
                    writer.writerow(option)
                print(f"Processed: {filename}")

    print(f"Extraction complete. CSV saved to: {output_csv}")

if __name__ == "__main__":
    # You can run with command-line args or hardcode paths here
    if len(sys.argv) == 3:
        input_folder = sys.argv[1]
        output_csv = sys.argv[2]
    else:
        input_folder = "input/interactives"
        output_csv = os.path.join("output", "options.csv")
    
    extract_all_options_to_csv(input_folder, output_csv)
