import os

import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def build_course_tbl():
    try:
        course_tbl = dynamodb.create_table(
            TableName = 'Courses',
            KeySchema = [
                {
                    "AttributeName": "Subject",
                    "KeyType": "HASH"
                },
                {
                    "AttributeName": "CourseID",
                    "KeyType":"RANGE"
                }
            ],
            AttributeDefinitions = [
                {
                    "AttributeName": "CourseID",
                    "AttributeType": "S"
                },
                {
                    "AttributeName": "Subject",
                    "AttributeType": "S"
                }
            ],
            ProvisionedThroughput = {
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

    except Exception as e:
        print(f"Error building table: {e}")

def run_ui():
    print("Welcome to the course catalog.\n\n")
    table = dynamodb.Table('Courses')
    search_done = False

    while not search_done:
        subject = None
        catalog_no = None
        next = None

        # Repeats subject question until valid input is received
        while not subject:
            subject = input("Please enter the 2-4 letter subject abbreviation: ")

            # Quick validation of proper values
            if len(subject) not in range(2,5):
                subject = None

        # Repeats catalog question until valid input is received
        while not catalog_no:
            try:
                catalog_no = int(input("Please enter the numeric course number: "))
            except Exception as e:
                print(f"Error gathering input: {e}")

        # Process search criteria
        try:
            response = table.query(
                KeyConditionExpression=Key('Subject').eq(subject)
            )

            response = list(
                filter(lambda x: x['CatalogNbr'] == catalog_no, response['Items'])
            )

            response_title = response[0]["Title"]

            print(f'The title of your selected course is: {response_title}')
        except Exception as e:
            print(f"Sorry, no matches found for these search criteria: {e} \n\n")


        # Process logic if they want to perform additional searches
        while next not in ["n","y"]:
            next = input("Would you like to search for another title? (Y or N)").lower()

            if next == "y":
                catalog_no = None
                subject = None
            elif next == "n":
                search_done = True
                print("\n\n Thank you for using the course catalog.")
                return
            else:
                pass

def delete_tbl():
    try:
        table = dynamodb.Table('Courses')
        table.delete()
    except Exception as e:
        print(f'Error deleting table: {e}')

if __name__ == "__main__":
    """
    For use resetting table during this trials and building out the logic,
    can wipe the table then rebuild by calling commented function below
    """
    # Delete table
    # delete_tbl()

    # Rebuild table
    # build_course_tbl()

    run_ui()
        
