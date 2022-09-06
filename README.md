Lambda CompanySave: Saves a company from a new or existing data

#invoking lambda AWS from localhost
aws lambda invoke --function-name {FUNCTION_NAME}:prd --cli-binary-format raw-in-base64-out --payload file://run/request.json run/response.json && cat run/response.json

#invoking lambda localhost
python-lambda-local src/lambda_function.py -f lambda_handler run/request.json -e run/variables.json

#packing into localhost, validade the template and generate the output.yml
sam package --output-template-file output.yaml --s3-bucket {BUCKET_NAME}

#publish into Serverless Application Repository (SAR)
sam publish --template output.yaml --region sa-east-1

#first time
sam deploy --guided
#other times
sam deploy
