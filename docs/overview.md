# Project Overview

The Cognism Scraper automates the process of collecting lead information from the Cognism platform. It uses Selenium to navigate Cognism's web interface, extracts contact details, stores them in a SQLite database, and offers tools to export the data to CSV for integration with CRMs or other marketing tools.

The codebase is organised into several key modules:

- `src/utils`: helper utilities for authentication, Selenium setup, and database management.
- `src/utils_urls`: scrapes contact URLs from Cognism searches.
- `src/utils_contacts`: processes URLs to extract detailed contact information.
- `src/contact_extractors`: parsers that pull specific data points like name, email, LinkedIn URL and more.

By modularising the extraction logic, the project is easily extensible and can adapt to changes in Cognism's website structure.
