# AWS S3 Data Analysis and Visualization

This Python script demonstrates how to perform data analysis and visualization on CSV data stored in AWS S3 buckets. The script reads a CSV file from the local filesystem, uploads it to an S3 bucket, retrieves the data from S3, performs exploratory data analysis (EDA), creates a histogram plot based on the 'Age' column, and uploads the plot image back to the S3 bucket.

## Requirements

- Python 3.x
- pandas
- matplotlib
- boto3

## Usage

1. Clone this repository:

   ```bash
   git clone <repository-url>
