import pandas as pd
import matplotlib.pyplot as plt
import boto3
from io import BytesIO

# Read the CSV file from the local filesystem
df = pd.read_csv(r"C:\Users\ravali.satla\DataEngg20Jul-10Aug\Ravali\data.csv")

# Initialize the S3 client
s3 = boto3.client('s3')

# Define the S3 bucket name
bucket_name = 'de-ravali-project3'

# Create the S3 bucket
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})

# Specify the key for the CSV file in the S3 bucket
data_file_s3_key = 'data/data1.csv'

# Upload the CSV file to the S3 bucket
s3.upload_file(r"C:\Users\ravali.satla\DataEngg20Jul-10Aug\Ravali\data.csv", bucket_name, data_file_s3_key)

# Retrieve the CSV file from the S3 bucket
s3_data = s3.get_object(Bucket=bucket_name, Key=data_file_s3_key)

# Read the CSV data from the S3 object
df = pd.read_csv(s3_data['Body'])

# Create a histogram plot of the 'Age' column
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

# Save the plot as an image file
output_file = "age_distribution.png"
plt.savefig(output_file)

# Specify the key for the plot image in the S3 bucket
s3_file_key = 'eda_results/age_distribution.png'

# Read the plot image as bytes
with open(output_file, 'rb') as f:
    file_data = f.read()

# Upload the plot image to the S3 bucket
s3.put_object(Bucket=bucket_name, Key=s3_file_key, Body=file_data)
