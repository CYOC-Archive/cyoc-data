import csv
import sys
import psycopg2
from datetime import datetime

# Database connection settings
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'cyocdb'
DB_USER = 'cyocuser'
DB_PASS = 'cyocpassword'

CSV_FILE = r'output\output.csv'

csv.field_size_limit(100000000)

def parse_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def parse_timestamp(value):
    try:
        # Format: "01/01/2002 17:41"
        return datetime.strptime(value, "%m/%d/%Y %H:%M")
    except Exception:
        return None

def main():
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()

    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur.execute(
                """
                INSERT INTO chapter (
                    chapter_id, chapter_date, user_id, username, parent_chapter_id,
                    tags, chapter_title, chapter_text_base64
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    parse_int(row['Chapter ID']),
                    parse_timestamp(row['Chapter Date']),
                    parse_int(row['User ID']),
                    row['Username'],
                    parse_int(row['Parent Chapter ID']),
                    row['Tags'],
                    row['Chapter Title'],
                    row['Chapter Text (base64)'],
                )
            )
    conn.commit()
    cur.close()
    conn.close()
    print("CSV import complete.")

if __name__ == '__main__':
    main()