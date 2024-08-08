import os

def main():
    print("Hi from Docker")
    bucket_name = os.environ["INPUT_BUCKET"]
    bucket_region = os.environ["INPUT_BUCKET-REGION"]
    bucket_url = "http://" + bucket_name + "/hi"
    print(f''::set-output name=bucket-url::{bucket_url}')

main()