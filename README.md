# modelo

Serverless lambda functions to read a query from postgres and read data from dynamodb

I decided to hardcode some values, although it can be configured to be less dynamic.

For Postgres, I used an sample event.json which will be a sample payload that can be used to do dynamic queries and also the DB credentials are set at the yaml file so it can be more dynamic too
For Dynamodb, I decided to hardcode the table that we want to read the data, but the table can be set to be dynamic. Also, it is using the current settings of the aws user to pull the dynamo db, which could be configured later to be a bit more dynamic
