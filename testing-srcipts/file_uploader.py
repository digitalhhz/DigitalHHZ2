from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "10.0.105.60:9000",
        access_key="minio-user-kilab",
        secret_key="minio-user-kilab",
        secure=False
    )

    # Make 'file_uploader' bucket if not exist.
    found = client.bucket_exists("fileuploader")
    if not found:
        client.make_bucket("fileuploader")
    else:
        print("Bucket 'fileuploader' already exists")

    # Upload 'file_uploader.py' as object name
    # 'file_uploader.py' to bucket 'file_uploader'.
    client.fput_object(
        "fileuploader", "file_uploader.py", "./file_uploader.py",
    )
    print(
        "'file_uploader.py' is successfully uploaded as "
        "object 'file_uploader.py' to bucket 'fileuploader'."
    )


if _name_ == "_main_":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
