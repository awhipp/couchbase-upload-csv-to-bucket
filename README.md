# Upload CSV file to predefined Couchbase Bucket

## Requirements

* Python 2.7.x
* Couchbase Python SDK Installed
* Couchbase Server Installed

## How To

Excute via commandline: `python cb_upload_csv.py [csv_file_path] [couchbase_url] [couchbase_bucket_name] [couchbase_username] [couchbase_password]`

Where:
* csv_file_path is the path to the CSV being uploaded
* couchbase_url is the server's couchbase url
* couchbase_bucket_name is the predefined couchbase bucket
* couchbase_username is the username of the user inserting the data
* couchbase_password is the password of the user inserting the data

ie: `python cb_upload_csv.py data.csv couchbase://localhost default admin password`
