import csv
import psycopg2

DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'cyocdb'
DB_USER = 'cyocuser'
DB_PASS = 'cyocpassword'

CSV_FILE = r'output\options.csv'

def parse_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
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
                INSERT INTO chapter_option (
                    parent_id, chapter_id, option_id, option_title
                ) VALUES (%s, %s, %s, %s)
                """,
                (
                    parse_int(row['Parent ID']),
                    parse_int(row['Chapter ID']),
                    parse_int(row['Option ID']),
                    row['Option Title']
                )
            )
    conn.commit()
    cur.close()
    conn.close()
    print("Options CSV import complete.")

if __name__ == '__main__':
    main()