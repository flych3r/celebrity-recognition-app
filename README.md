# Celebrity Recognition App

This app will use your default AWS Credentials
You will need to setup the following services:

* an `s3 bucket` with public read access
* a `dynamodb table` with `img_path` as a primary key
* create a `lambda function` using the `lambda.py`, that triggers when putting `jpg` files on the previous `s3 bucket`

Before running, set the following environment variables:

`export CELEBS_BUCKET=<s3-bucket-name>`
`export CELEBS_TABLE=<dynamodb-table-name>`

run the command: `streamlit run App.py --server.enableCORS=true`
