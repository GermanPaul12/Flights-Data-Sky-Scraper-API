# Sky Scraper - Flight Search App

Sky Scraper is a Python application that allows you to search for flight information using the Sky Scrapper API. This application helps you find flight prices and other related information for various destinations from a specified origin airport.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- API key and host details for the Sky Scrapper API. You can obtain these by signing up on their website.

## Getting Started

### Installation

1. Clone this repository to your local machine using:
`git clone https://github.com/GermanPaul12/Flights-Data-Sky-Scraper-API.git`
2. Navigate to the project directory:
`cd Flights-Data-Sky-Scraper-API`

### Configuration

1. Create a `creds.py` file in the project directory.

2. Inside `creds.py`, define your API key and host as follows:

```python
X_RapidAPI_Key = "your-api-key"
X_RapidAPI_Host = "your-api-host"
```

### Usage

To use the Sky Scraper application:

1. Modify the `querystring` in the `main.py` file to specify your search criteria, including the originSkyId, travelDate, and currency.
2. Run the application: `python3 main.py`

The application will make a request to the Sky Scrapper API and retrieve flight information for your specified criteria. The data will be appended to a data.csv file in the project directory.

You can access the flight data in the data.csv file, which includes information such as the country ID, country name, price, currency, timestamp, and image URL.
