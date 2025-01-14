# Czech National Bank Exchange Rate Downloader

This is a simple command-line application written in Python.

## Contents

- `src/main.py`: Entry point of the application.
- `src/utils/helpers.py`: Helper functions for processing command-line arguments.
- `requirements.txt`: List of dependencies required for the project.
- `setup.py`: Configuration file for the package.

## Installation

1. Clone the repository:
   ```
   git clone <URL_REPO>
   cd my-cli-app
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application using:
```
python src/main.py [arguments]
```

## Configuration

Create a `.env` file in the root directory of the project and add the following configurations:

### Example 1: Downloading exchange rates for EUR and USD for the last 7 days

```shell
RESULT_FILE=exchange_rates.json DEBUG=True
``


### Example 2: Downloading exchange rates for GBP for the last month and outputting to standard output

```shell
python main.py --currencies EUR,USD --start_date 2023-01-01 --end_date 2023-01-07
```

## Contributing

If you want to contribute, create a pull request or open an issue.