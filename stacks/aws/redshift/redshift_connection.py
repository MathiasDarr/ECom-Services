import psycopg2

# Amazon Redshift connect string
conn_string = "dbname='dev' port='5439' user='admin' password='Password1' host='redshift-stack-redshiftcluster-1125c9ub6jpn1.cvsnwns8y832.us-west-2.redshift.amazonaws.com'"
# connect to Redshift (database should be open to the world)
# connection = psycopg2.connect(conn_string);
# cursor = connection.cursor()
# query = "select * from shoes;"
# cursor.execute(query)
# records = cursor.fetchall()
# print("Print each row and it's columns values")
# for row in records:
#     print("shoetype = ", row[0], )
#     print("color = ", row[1])


create_users_table = '''create table users(
userid integer not null distkey sortkey,
username char(8),
firstname varchar(30),
lastname varchar(30),
city varchar(30),
state char(2),
email varchar(100),
phone char(14),
likesports boolean,
liketheatre boolean,
likeconcerts boolean,
likejazz boolean,
likeclassical boolean,
likeopera boolean,
likerock boolean,
likevegas boolean,
likebroadway boolean,
likemusicals boolean);'''

create_venues_table = '''create table venue(
venueid smallint not null distkey sortkey,
venuename varchar(100),
venuecity varchar(30),
venuestate char(2),
venueseats integer);'''

create_category_table = '''create table category(
catid smallint not null distkey sortkey,
catgroup varchar(10),
catname varchar(10),
catdesc varchar(50));'''

create_date_table = '''create table date(
dateid smallint not null distkey sortkey,
caldate date not null,
day character(3) not null,
week smallint not null,
month character(5) not null,
qtr character(5) not null,
year smallint not null,
holiday boolean default('N'));
'''

create_event_table = '''create table event(
eventid integer not null distkey,
venueid smallint not null,
catid smallint not null,
dateid smallint not null sortkey,
eventname varchar(200),
starttime timestamp);
'''

create_listing_table = '''create table listing(
listid integer not null distkey,
sellerid integer not null,
eventid integer not null,
dateid smallint not null  sortkey,
numtickets smallint not null,
priceperticket decimal(8,2),
totalprice decimal(8,2),
listtime timestamp);
'''

create_sales_table = '''create table sales(
salesid integer not null,
listid integer not null distkey,
sellerid integer not null,
buyerid integer not null,
eventid integer not null,
dateid smallint not null sortkey,
qtysold smallint not null,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp);'''

create_table_commands = [create_date_table, create_event_table, create_sales_table, create_users_table,
                         create_listing_table, create_venues_table, create_category_table]


with psycopg2.connect(conn_string) as conn:
    with conn.cursor() as curs:
        for command in create_table_commands:
            curs.execute(command)

copy_users_command = "copy moves from 's3://dakobed-redshift-sample-data/data/allusers_pipe.txt'"
copy_sales_command = "copy sales from 's3://dakobed-redshift-sample-data/data/sales_tab.txt'"
copy_events_command = "copy event from 's3://dakobed-redshift-sample-data/data/allevents_pipe.txt'"
copy_listings_command = "copy listing from 's3://dakobed-redshift-sample-data/data/listings_pipe.txt'"
copy_category_command = "copy category from 's3://dakobed-redshift-sample-data/data/category_pipe.txt'"
copy_venue_commadn = "copy venue from 's3://dakobed-redshift-sample-data/data/venue_pipe.txt'"
copy_date_command = "copy date from 's3://dakobed-redshift-sample-data/data/date2008_pipe.txt'"

copy_commands = [copy_date_command, copy_category_command, copy_events_command, copy_sales_command, copy_venue_commadn,
                 copy_listings_command, copy_users_command]


with psycopg2.connect(conn_string) as conn:
    with conn.cursor() as curs:
        for command in copy_commands:
            curs.execute(command)
