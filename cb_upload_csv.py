import csv, sys, uuid, json
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

if len(sys.argv) == 6:
	print "Opening file: " + sys.argv[1]
	with open(sys.argv[1]) as f:
		reader = csv.reader(f)
		cluster = Cluster(sys.argv[2])
		authenticator = PasswordAuthenticator(sys.argv[4], sys.argv[5])
		cluster.authenticate(authenticator)
		bucket = cluster.open_bucket(sys.argv[3])

		isHeader = True
		headerRow = []
		for row in reader:
			if isHeader:
				headerRow = row
				isHeader = False
				print headerRow
			else:
				id = str(uuid.uuid4())
				obj = {}
				for i in range(len(headerRow)):
					obj[headerRow[i]] = row[i]
				# print json.dumps(obj)
				bucket.insert(id, json.dumps(obj))
		bucket.n1ql_query('CREATE PRIMARY INDEX ON ' + sys.argv[3]).execute();
else:
	print "Improper use. Not enough arguments. Requires 2:"
	print "python cb_upload_csv.py [csv_file_path] [couchbase_url] [couchbase_bucket_name] [couchbase_username] [couchbase_password]"
	print "ie: python cb_upload_csv.py data.csv couchbase://localhost default admin password"
