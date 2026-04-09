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

2. Environment Setup
For security reasons, credentials and URLs are not hardcoded. You need to create a .env file in the root directory with your own target parameters:

Snippet de código
URL_SISTEMA=[https://your-target-login-url.com](https://your-target-login-url.com)
USUARIO_SISTEMA=your_email@domain.com
SENHA_SISTEMA=your_secure_password
URL_CRM=[https://your-target-crm-url-with-filters.com](https://your-target-crm-url-with-filters.com)
3. Execution
Run the main script to start the extraction process:

Bash
python extrator_visitas.py
Note: A sample file (modelo_visitantes.csv) is included to demonstrate the expected output format.

🛡️ Disclaimer
This project was developed for automation and data analysis purposes. All sensitive routes, company domains, and credentials have been hidden using environment variables to ensure security and follow industry best practices.


Para subir esse arquivo novo para o GitHub, o processo é o mesmo que você acabou de fazer:

1. Salve o arquivo `README.md`
2. `git add README.md`
3. `git commit -m "docs: add project README"`
4. `git push`

O que achou dessa estrutura? Podemos seguir para organizar o repositório do seu sistema de cont
