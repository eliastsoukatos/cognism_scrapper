# Cognism Scraper

A Python-based automation tool that collects high-quality B2B leads from the [Cognism](https://www.cognism.com/) platform. The scraper logs into Cognism, extracts contact URLs, gathers enriched details for each lead and stores everything in a local SQLite database that can be exported to CSV or connected to your CRM workflow.

## Features

- **Lead URL scraping** &ndash; Automatically navigates Cognism search results and captures contact URLs for further processing.
- **Contact enrichment** &ndash; Parses each contact page to extract names, roles, email addresses, phone numbers, LinkedIn URLs and company information.
- **Duplicate filtering** &ndash; Deduplicates URLs before scraping to avoid processing the same lead twice.
- **Database storage** &ndash; Saves all collected data in `contacts.db` for easy retrieval and auditing.
- **CSV export** &ndash; Exports the complete contact database to `contacts_export.csv` for seamless import into CRMs or marketing tools.
- **Configurable delays** &ndash; Environment variables allow you to tweak wait times and batch sizes for reliable automation.

## Use Cases

- Populate your CRM with fresh leads for outbound campaigns.
- Enrich existing lead lists with additional data points such as company size or location.
- Automate repetitive data collection tasks for sales development representatives.

## Tech Stack

- **Python 3** with Selenium for browser automation
- **SQLite** for lightweight, file-based data storage
- **BeautifulSoup / lxml** for HTML parsing
- **dotenv** for configuration via environment variables

## Quick Start

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `example.env` to `.env` and update with your Cognism credentials.

3. Run the application and follow the prompts:

   ```bash
   python main.py
   ```

Check the [docs](./docs) directory for more detailed usage and architecture information.

## Project Structure

```
├── src/                    # Core scraper modules
├── examples/               # Sample HTML and usage examples
├── docs/                   # Project documentation
├── data/                   # Placeholder for exported CSV files or datasets
├── requirements.txt        # Python dependencies
├── CONTRIBUTING.md         # Contribution guidelines
└── LICENSE                 # MIT license
```

## Benefits

By automating contact collection and enrichment, this project helps sales and marketing teams:

- Save time on manual data entry
- Build richer lead profiles for more targeted outreach
- Integrate scraped data into existing CRM pipelines

Feel free to open issues or submit pull requests to improve the project. Happy scraping!
