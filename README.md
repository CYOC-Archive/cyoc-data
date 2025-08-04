# CYOC Data

This repository contains scripts used to collect and process data from the CYOC Archive. The goal is to extract, clean, and reformat HTML data into structured formats suitable for database import and analysis.

## Data
To start you will need a copy of the CYOC dataset from the Internet Archive.
 - https://archive.org/details/cyocnet

Place the contents of the `interactives/` directory into the `input/` directory of this project.

## Features

- Download and archive HTML data from the CYOC Archive.
- Parse and extract relevant information from HTML files.
- Reformat and export data into structured formats (e.g., CSV, JSON, or SQL).
- Utilities for cleaning and validating extracted data.

## Getting Started

### Prerequisites

- Python 3.8+ (or specify your language/environment)
- Docker
- Required Python packages (see `requirements.txt` if available)

### Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/CYOC-Archive/cyoc-data.git
    cd cyoc-data
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Data Extract

1. Place raw HTML files in the `input/` directory (or specify your input location).
2. Run the main data extraction script, you can leave the options as default if running in the root directory:
    ```sh
    python extract_data.py <input directory> <Output CSV>
    python extract_options.py <input directory> <Output CSV>
    ```
3. Processed data will be saved in the `output/` directory.

## Database
The `docker-compose.yml` has some basic configuration for a postgres database, this is purely for analytics. Don't run this in production.

1. Run the database with the following command.
    ```sh
    docker compose up
    ```
2. Connect to the database and run the database schema in `schema/schema.sql`
3. Run the load python files to populate the data, the order matters
    ```sh
    python load_data.py
    python load_options.py
    ```
4. Processed data will be saved in the postgres database.

## Project Structure

```
cyoc-data/
├── input/           # Raw HTML files from CYOC Archive
├── output/          # Processed and formatted data
├── requirements.txt # Python dependencies
└── README.md
```

## Contact

For questions or support, please contact @HallowsEveWrite.
