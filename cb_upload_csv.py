import csv, sys, uuid, json
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

if len(sys.argv) == 6:
	fileName = sys.argv[1]
	clusterName = sys.argv[2]
	bucketName = sys.argv[3]
	username = sys.argv[4]
	password = sys.argv[5]

	with open(fileName) as f:
		reader = csv.reader(f)
		cluster = Cluster(clusterName)
		authenticator = PasswordAuthenticator(username, password)
		cluster.authenticate(authenticator)
		bucket = cluster.open_bucket(bucketName)

		isHeader = True
		headerRow = []
		for row in reader:
			if isHeader:
				headerRow = row
				isHeader = False
			else:
				id = str(uuid.uuid4())
				obj = {}
				for i in range(len(headerRow)):
					obj[headerRow[i]] = row[i]
				bucket.insert(id, obj)
		bucket.n1ql_query('CREATE PRIMARY INDEX ON ' + bucketName).execute();
else:
	print "Improper use. Not enough arguments. Requires 2:"
	print "python cb_upload_csv.py [csv_file_path] [couchbase_url] [couchbase_bucket_name] [couchbase_username] [couchbase_password]"
	print "ie: python cb_upload_csv.py data.csv couchbase://localhost default admin password"
