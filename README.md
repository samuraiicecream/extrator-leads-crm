# CRM Lead Extractor & Data Analyzer

An automated web scraping and data extraction tool built with Python. This script automates the process of logging into a CRM system, navigating through paginated lead data (pre-enrolled students), extracting specific information, and exporting it for further analysis.

## 🚀 Features

* **Automated Authentication:** Securely logs into the CRM platform using environment variables.
* **Smart Pagination Handling:** Automatically detects and navigates through multiple pages until all data is collected.
* **Data Extraction:** Parses HTML elements to extract specific data points (e.g., Name and Email).
* **Data Structuring & Export:** Uses `pandas` to structure the scraped data and export it as a clean `.csv` file.
* **Secure by Design:** Credentials and internal URLs are completely decoupled from the codebase using `.env` files.

## 🛠️ Technologies & Tools

* **Python 3**
* **Playwright:** For robust, headless browser automation and dynamic content scraping.
* **Pandas:** For data manipulation and export.
* **python-dotenv:** For managing environment variables securely.

## ⚙️ How to Run Locally

### 1. Prerequisites
Make sure you have Python installed. Then, install the required libraries:

```bash
pip install playwright pandas python-dotenv
playwright install chromium
