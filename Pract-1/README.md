# Review Analysis Project

This project processes customer reviews from multiple CSV files, calculates the average ratings for each product, and generates a summary report.

## Project Structure

- [`app.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FAdvPython%2FPract-1%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/AdvPython/Pract-1/app.py"): Main script to process the reviews and generate the summary report.
- [`summary.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FAdvPython%2FPract-1%2Fsummary.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/AdvPython/Pract-1/summary.txt"): Output file containing the summary of the reviews.
- `F1.csv`, `F2.csv`, `F3.csv`, `F4.csv`, `F5.csv`: Input CSV files containing customer reviews.

## Requirements

- Python 3.x
- pandas library

## Setup

1. Clone the repository or download the project files.
2. Ensure you have Python 3.x installed on your machine.
3. Install the required library using pip:
    ```sh
    pip install pandas
    ```

## Usage

1. Place all the CSV files (`F1.csv`, `F2.csv`, `F3.csv`, `F4.csv`, `F5.csv`) in the same directory as [`app.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FAdvPython%2FPract-1%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/AdvPython/Pract-1/app.py").
2. Run the [`app.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FAdvPython%2FPract-1%2Fapp.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/AdvPython/Pract-1/app.py") script:
    ```sh
    python app.py
    ```
3. The script will generate a [`summary.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FAdvPython%2FPract-1%2Fsummary.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/AdvPython/Pract-1/summary.txt") file with the following information:
    - Total number of reviews processed.
    - Total number of valid reviews.
    - Total number of invalid reviews.
    - Top 3 products with the highest average ratings.

## Example Output

The [`summary.txt`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fworkspaces%2FAdvPython%2FPract-1%2Fsummary.txt%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/workspaces/AdvPython/Pract-1/summary.txt") file will look like this:

```plaintext
The Total Number of reviews processed: 50
The Total Number of valid reviews 49
The Total Number of invalid reviews 1
Product ID: P0000000001, Average Rating: 4.8
Product ID: P0000000002, Average Rating: 4.2
Product ID: P0000000004, Average Rating: 3.6