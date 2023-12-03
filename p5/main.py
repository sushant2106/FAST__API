from fastapi import FastAPI, HTTPException
import boto3
from botocore.exceptions import ClientError

app = FastAPI()

# AWS S3 configuration
AWS_ACCESS_KEY_ID = "your_access_key_id"
AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
AWS_REGION_NAME = "your_region"
S3_BUCKET_NAME = "your_bucket_name"

# Initialize S3 client
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION_NAME)


@app.get("/download/{file_key}")
async def get_presigned_url(file_key: str):
    try:
        # Generate a pre-signed URL for the file in S3
        # url = s3.generate_presigned_url(
        #     'get_object',
        #     Params={
        #         'Bucket': S3_BUCKET_NAME,
        #         'Key': file_key,
        #     },
        #     ExpiresIn=3600  
        # )
        return {"presigned_url": "url"}
    except ClientError as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


# from fastapi import FastAPI, HTTPException, Depends
# from fastapi.responses import RedirectResponse
# import boto3
# from botocore.exceptions import ClientError

# app = FastAPI()

# # AWS S3 configuration
# AWS_ACCESS_KEY_ID = "your_access_key_id"
# AWS_SECRET_ACCESS_KEY = "your_secret_access_key"
# AWS_REGION_NAME = "your_region"
# S3_BUCKET_NAME = "your_bucket_name"

# # Initialize S3 client
# s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION_NAME)


# def get_presigned_url(file_key: str):
#     try:
#         # Generate a pre-signed URL for the file in S3
#         url = s3.generate_presigned_url(
#             'get_object',
#             Params={
#                 'Bucket': S3_BUCKET_NAME,
#                 'Key': file_key,
#             },
#             ExpiresIn=3600  # Set the expiration time of the URL (in seconds)
#         )
#         return url
#     except ClientError as e:
#         raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


# @app.get("/download/{file_key}")
# async def download_file(file_key: str):
#     presigned_url = get_presigned_url(file_key)
#     return RedirectResponse(url=presigned_url, status_code=302)
