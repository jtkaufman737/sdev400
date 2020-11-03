import os
from random import randint

import boto3

# Below are interfaces to boto3, AWS SDK
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# Used for spacing/line breaks for readability
standard_spaces = "\n\n         "


def parse_input():
    """
    Main function for error handling & collecting user options from the cli menu
    """

    valid_input = False

    # keeps menu running until exited
    while not valid_input:
        choice = input(f"{standard_spaces} Please enter your selection: ")

        try:
            choice = int(choice)

            if choice in range(1,8):
                valid_input = True
                return choice
            else:
                print(f"{standard_spaces} Please enter a valid selection between 1 and 7")
        except Exception as e:
            print(f"{standard_spaces} Please enter a valid selection between 1 and 7")


def list_buckets():
    """
    Read operation for buckets user has access to
    """

    buckets = [bucket["Name"] for bucket in s3_client.list_buckets()["Buckets"]]
    return buckets


def select_bucket():
    """
    Of listed buckets accepts user input to return a selected bucket,
    used elsewhere in CRUD operations
    """

    buckets = list_buckets()
    print(f"{standard_spaces} Available buckets are: {', '.join(buckets)}")

    try:
        b = input(f"{standard_spaces} Please enter the name if your target bucket EXACTLY: ")

        if b in buckets:
            print(f"{standard_spaces} Great - {b} selected")
            return b
        else:
            raise Exception()
    except Exception as e:
        print(f"{standard_spaces} Please enter a valid bucket.")
        return None


def create_bucket():
    """
    Creates a new AWS bucket
    """

    fname = False
    lname = False
    rand_id = randint(100000,999999)

    print("""
    You have selected the new bucket operation.

    To create a new s3_client bucket, we will need your first and last name.

    """)

    while not fname or not lname:
        fname = input(f"{standard_spaces} Enter your first name below:")
        lname = input(f"{standard_spaces} Enter your last name below:")

    print(f"{standard_spaces} Great, thank you {fname} {lname}.")

    bucket = f"{fname}{lname}-{rand_id}".lower()

    try:
        b = s3_client.create_bucket(Bucket=bucket)
        print(f'{standard_spaces} Success! Bucket {bucket} created at {b["ResponseMetadata"]["HTTPHeaders"]["location"]}')
    except Exception as e:
        print(e)


def add_bucket_obj():
    """
    Creates new object in a specified bucket
    """
    buckets = list_buckets()
    target_bucket = None
    target_file = None

    print(f"{standard_spaces} You have selected the add item operation. Your available buckets are: { ', '.join(buckets) }")

    while not target_bucket:
        target_bucket = select_bucket()

    while not target_file:
        try:
            files = [f for f in os.listdir('.') if os.path.isfile(f) and '.py' not in f]
            file = input(f"{standard_spaces} Files available for upload are {', '.join(files)}. Please enter the EXACT name of the file you wish to upload.")

            if file in files:
                target_file = s3_client.upload_file(file, target_bucket, file)
                print(f"{standard_spaces} Great, {file} uploaded successfully to {target_bucket}")
                return
            else:
                raise Exception()
        except Exception as e:\
            print(f"{standard_spaces} Error processing file: {e} ")


def delete_bucket_obj():
    """
    Deletes object from a bucket
    """

    target_bucket = None
    target_file = None

    print(f"{standard_spaces} You have selected the delete item operation")

    while not target_bucket:
        target_bucket = select_bucket()

    while not target_file:
        target_file = input(f"{standard_spaces} Please enter the file name you wish to remove from {target_bucket} ")

    try:
        s3_resource.Object(target_bucket, target_file).delete()
        print(f"{standard_spaces} Success! file {target_file} deleted from {target_bucket}")
    except Exception as e:
        print(f"{standard_spaces} Failed to delete file...{e}")


def delete_bucket():
    """
    Empties, then deletes, AWS storage bucket
    """

    target_bucket = None
    print(f"{standard_spaces} Delete bucket operation selected.")

    while not target_bucket:
        target_bucket = select_bucket()

    try:
        all = s3_resource.buckets.all()

        # isolate our bucket by checking name
        for bucket in all:
            if bucket.name == target_bucket:
                target_bucket = bucket

        # have to empty items before deleting container
        for item in target_bucket.objects.all():
            item.delete()

        target_bucket.delete()

        print(f"{standard_spaces} Success! {target_bucket.name} deleted.")
    except Exception as e:
        print(f"{standard_spaces} Error deleting bucket: {e}")


def copy_bucket_obj():
    """
    Copies object from a source bucket to a target bucket
    """

    source_bucket = None
    target_bucket = None
    file = None

    print(f"{standard_spaces} You've selected the copy operation.")

    while not source_bucket:
        print(f"{standard_spaces} First select the bucket from which you will be copying a file")
        source_bucket = select_bucket()

    while not target_bucket:
        print(f"{standard_spaces} Now select the bucket that you are copying the file to.")
        target_bucket = select_bucket()

    while not file:
        file = input(f"{standard_spaces} Enter the file that you wish to copy ")

    try:
        s3_resource.Object(target_bucket, file).copy({
            'Bucket': source_bucket,
            'Key': file
        })

        print(f"{standard_spaces} Success! {file} copied to {target_bucket}")
    except Exception as e:
        print(f"{standard_spaces} Error copying file: {e}")


def download_bucket_obj():
    """
    Locally downloads a bucket object to Cloud9
    """
    target_file = None
    target_bucket = None

    print(f"{standard_spaces} You have selected the download item operation.")

    while not target_bucket:
        target_bucket = select_bucket()

    while not target_file:
        target_file = input(f"{standard_spaces} Please enter the file name you wish to download ")

    try:
        s3_resource.Bucket(target_bucket).download_file(target_file, target_file)
        print(f"{standard_spaces} Success! {target_file} downloaded")
    except Exception as e:
        print(f"{standard_spaces} Error downloading file: {e}")

if __name__ == "__main__":
    """
    Main script which runs when file is executed, runs menu and contains
    control flow logic to call the other functions as needed
    """

    # Condition to keep program running
    running = True
    # First option blank so array indexes match choice #s
    options = ["", create_bucket, add_bucket_obj, delete_bucket_obj,
                delete_bucket, copy_bucket_obj, download_bucket_obj]

    while running:
        print(f"""\n\n
        Find below the s3_client menu options:
            1. Create a bucket
            2. Add item to a bucket
            3. Delete item from a bucket
            4. Delete bucket
            5. Copy item from one bucket to another
            6. Download object from a bucket
            7. Exit program\n\n
        """)

        choice = parse_input()

        if choice == 7:
            print(f"{standard_spaces} You have selected the exit program operation. Goodbye!")
            running = False
        else:
            options[choice]()
