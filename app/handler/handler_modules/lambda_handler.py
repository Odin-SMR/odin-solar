from .download import download


def handler(event, context):
    download()

    return {
        "statusCode": 200,
        "body": "Successfully downloaded CSV and uploaded parquet file to S3",
    }
