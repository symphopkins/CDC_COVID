# SARS-CoV-2 Variant Proportions ETL Pipeline

This Python script is designed to extract, transform, and load (ETL) data from the CDC (Centers for Disease Control and Prevention) API into a PostgreSQL database. It retrieves data related to variant proportions from the CDC API, performs necessary data transformations, and then loads the processed data into a PostgreSQL table.

## Installation

To run this project, ensure you have Python installed on your system. You can install the required dependencies using the `requirements.txt` file.

## Usage

1. Ensure you have a PostgreSQL database set up and running.
2. Open the `main.py` script in your preferred Python environment.
3. Update the `your_connection_string` variable with your PostgreSQL connection string.
4. Run the script.

## Citation
Ma KC, Shirk P, Lambrou AS, et al. Genomic Surveillance for SARS-CoV-2 Variants: Circulation of Omicron Lineages — United States, January 2022–May 2023. MMWR Morb Mortal Wkly Rep 2023;72:651–656. DOI: http://dx.doi.org/10.15585/mmwr.mm7224a2

## License
Apache-2.0 license
