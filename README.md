# SciHub Batch Downloader

## Overview

The SciHub Automatic Downloader is a Python script that automates the process of downloading research papers using Digital Object Identifiers (DOIs) stored in a CSV file. It utilizes the `scidownl` module to query SciHub and retrieve the papers.

## Prerequisites

- Python 3
- Required Python packages (install using `pip install scidownl pandas`):
  - `scidownl`: Python module for interacting with SciHub
  - `pandas`: Data manipulation library for reading and processing CSV files

## Usage

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/SciHub-Batch-Downloader.git
   ```

2. **Navigate to the Directory**

   ```bash
   cd SciHub-Batch-Downloader
   ```

3. **Install Required Packages**

   ```bash
   pip install scidownl pandas
   ```

4. **Prepare the CSV File**

   - Create a CSV file containing a column named `DOI` with the DOIs of the papers you want to download. Save it in the `input` directory.

5. **Run the Script**

   - Open a terminal or command prompt and run:

     ```bash
     python download_papers.py
     ```

   - The script will prompt you for the name of the CSV file (including extension). For example, if your file is named `my_papers.csv`, you would enter `my_papers.csv`.

   - The script will then start downloading the papers from SciHub.

6. **Retrieve Downloaded Papers**

   - Once the script completes, the downloaded PDFs will be available in the `output` directory.

## Example CSV File

```csv
DOI
10.1234/abcd
10.5678/efgh
10.9123/ijkl
```

## Important Notes

- Ensure that the DOIs in your CSV file are valid and formatted correctly.
- The downloaded PDFs will be saved in the `output` directory with filenames corresponding to the DOIs (e.g., `10.1234_abcd.pdf`).

## Acknowledgements

- This script utilizes the `scidownl` module, which interacts with SciHub. Please be mindful of the terms of service of both SciHub and the publishers.

## License

This project is licensed under the MIT License.