import boto3
import botocore
from boto3.session import Session
from core.settings import (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
                           AWS_STORAGE_BUCKET_NAME)
from django.http import response
from rest_framework import status

from .errors import AWSDownloadError


class AWSFunctionsS3:
    def __init__(self):
        print("AWS S3 Function Class Initialised")

    def upload_file_to_s3(self, cloudFilename: str, fileobj):
        """Uploads file to S3 bucket

        Args:
            cloudFilename: Name of file in S3 bucket
            fileobj: File to be stored

        Returns:
            None -> Success
            response.JsonResponse -> Failure
        """
        try:
            session = Session(
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )

            s3 = session.resource("s3")
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
                Key=cloudFilename, Body=fileobj
            )

        except Exception:
            return response.JsonResponse(
                {"error_status": True, "success_status": False},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

    def delete_file_from_s3(self, cloudFilename: str):
        """Deletes file from S3 bucket

        Args:
            cloudFilename: Name of file in S3 bucket

        Returns:
            None -> Success
            response.JsonResponse -> Failure
        """
        try:
            session = Session(
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            )

            s3 = session.resource("s3")
            bucket = s3.Bucket(AWS_STORAGE_BUCKET_NAME)

            response = bucket.delete_objects(
                Delete={"Objects": [{"Key": cloudFilename}]}
            )

        except Exception:
            return response.JsonResponse(
                {"error_status": True, "success_status": False},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )

    def download_file_from_s3(self, cloudFilename: str, downloadFilename: str):
        """Downloads file from S3 bucket

        Args:
            cloudFilename: Name of file in S3 bucket
            downloadFilename: Name of file after download

        Returns:
            None -> Success
            response.JsonResponse -> Failure
        """
        s3 = boto3.resource("s3")

        try:
            s3.Bucket(AWS_STORAGE_BUCKET_NAME).download_file(
                cloudFilename, downloadFilename
            )

        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "404":
                return response.JsonResponse(
                    {
                        "error_status": True,
                        "success_status": False,
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            else:
                raise AWSDownloadError("Download Error, Please Try Again Later")
