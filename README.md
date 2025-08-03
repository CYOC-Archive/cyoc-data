# CYOC Data

This repository contains scripts used to collect and process data from the CYOC Archive. The goal is to extract, clean, and reformat HTML data into structured formats suitable for database import and analysis.

## Features

- Download and archive HTML data from the CYOC Archive.
- Parse and extract relevant information from HTML files.
- Reformat and export data into structured formats (e.g., CSV, JSON, or SQL).
- Utilities for cleaning and validating extracted data.

## Getting Started

### Prerequisites

- Python 3.8+ (or specify your language/environment)
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

### Usage

1. Place raw HTML files in the `input/` directory (or specify your input location).
2. Run the main data extraction script:
    ```sh
    python extract_data.py
    ```
3. Processed data will be saved in the `output/` directory.

_Replace script names and folder paths as appropriate for your project._

## Project Structure

```
cyoc-data/
├── input/           # Raw HTML files from CYOC Archive
├── output/          # Processed and formatted data
├── scripts/         # Data extraction and processing scripts
├── requirements.txt # Python dependencies
└── README.md
```

## Contact

For questions or support, please contact @HallowsEveWrite.
