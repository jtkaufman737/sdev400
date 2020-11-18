# Create table, with initially specified fields to only include uniquely identifiable info
aws dynamodb create-table \
   --table-name Sensors \
   --attribute-definitions \
      AttributeName=Sensor,AttributeType=S \
   --key-schema \
      AttributeName=Sensor,KeyType=HASH \
   --provisioned-throughput \
      ReadCapacityUnits=5, WriteCapacityUnits=5 \
