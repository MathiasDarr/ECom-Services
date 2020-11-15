import psycopg2
#Amazon Redshift connect string 
conn_string = "dbname='dev' port='5439' user='admin' password='Password1' host='redshift-stack-redshiftcluster-1125c9ub6jpn1.cvsnwns8y832.us-west-2.redshift.amazonaws.com'"  
#connect to Redshift (database should be open to the world)
con = psycopg2.connect(conn_string);
#sql="""COPY %s FROM '%s' credentials 
#      'aws_access_key_id=%s; aws_secret_access_key=%s'
#       delimiter '%s' FORMAT CSV %s %s; commit;""" % 
#      (to_table, fn, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,delim,quote,gzip)

