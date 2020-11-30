# Create table, with initially specified fields to only include uniquely identifiable info
aws dynamodb create-table \
   --table-name Sensors \
   --attribute-definitions \
      AttributeName=Sensor,AttributeType=S \
   --key-schema \
      AttributeName=Sensor,KeyType=HASH \
   --provisioned-throughput \
      ReadCapacityUnits=5,WriteCapacityUnits=5


# This was how to add a singular result from a JSON file


# This was how to absorb results 2-20 from a JSON file
aws dynamodb batch-write-item --request-items file://week_two/sensors.json
