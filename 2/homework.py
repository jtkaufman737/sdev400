# import boto3

# s3 = boto3.client('s3')
# response = s3.list_buckets()

def gen_line_br():
    print("\n\n")

def parse_input():
    valid_input = False
    gen_line_br()

    while not valid_input:
        choice = input("Please enter your selection:")

        try:
            choice = int(choice)

            if choice in range(1,7):
                valid_input = True
                return choice
            else:
                gen_line_br()
                print("Please enter a valid selection between 1 and 6")
                gen_line_br()
        except Exception as e:
            gen_line_br()
            print("Please enter a valid selection between 1 and 6")
            gen_line_br()


def create_bucket():
    print("You have selected the new bucket operation")

def add_bucket_obj():
    print("You have selected the add item operation")

def delete_bucket_obj():
    print("You have selected the delete item operation")

def copy_bucket_obj():
    print("You've selected the copy operation.")

def download_bucket_obj():
    print("You have selected the download item operation.")

if __name__ == "__main__":
    # Condition to keep program running
    running = True
    # First option blank so array indexes match choice #s
    options = ["", create_bucket, add_bucket_obj, delete_bucket_obj,
                copy_bucket_obj, download_bucket_obj]

    while running:
        print(f"""\n\n
        Find below the S3 menu options:
            1. Create a bucket
            2. Add item to a bucket
            3. Delete item from a bucket
            4. Copy item from one bucket to another
            5. Download object from a bucket
            6. Exit program\n\n
        """)

        choice = parse_input()

        if choice == 6:
            print("You have selected the exit program operation. Goodbye!")
            running = False
        else:
            options[choice]()
