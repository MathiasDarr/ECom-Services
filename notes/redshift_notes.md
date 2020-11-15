## AWS Redshift ##

Designed for OLAP not OLTP

## Redshift Architeture ##

cluster
    - leader node
    - 1-128 compute nodes
 
 Eacch compute node has dedicated CPU
 
 DS dense storage, 
    - HDD 
 DC dense compute
    - SSD 
    - high performance
    
 Redshift spectrum
    - Query exabytes of unstructred data in S3 w/ out loading
    - Limitless concurrency
    - Horizontal scalin
    - Seperate storage & compute resources
    - Wide variety of data formats
    - Support of gzip & snappy compression
    
 Redshift replicates all data in cluser
    three copies
        - original copy in cluster
        - replica copy in cluster
        - back up to s3
 
 
 Scaling Redshift
 During scaling
    - a new cluster is created while your old one remains available for reads
    - CNAME is flipped to new cluster 
    - data moved in parallel to new nodes
    
 Redshift distribution styles
minimize data movement
- AUTO
    - redshift figures it out based on size of data
- EVEN
    - Rows distributed across slices in round-robin
- KEY
    - Rows distributed based on one column
    - Data is distibuted based on the keys in one column 
        - useful for queries w/ a specific column
    - 
- ALL 
    - Entire table is copied to every node
    - Only useful relatively slow moving, not updated frequently
        - 
 
Redshift Sort Keys
    - Rows are stored on disk in sorted order based on the column you designate as a sort key
    - Like an index
    - Makes for fast range queries
    - Choosing a sort key 
        -recency? Filtering? Joins?
       
Compound Sort keys
    -  
  
Importing / Exporting data
COPY command
    - parallelized; efficient
    - from S3, EMR, DynamoDB, remote hosts
    - S3 requires a manifest file and IAM role
UNLOAD command
    - unload from a table into files in S3
Enhanced VPC routing 
    
    
    
COPY load large amounts of data from outside of Redshift
    - if data is already in Redshift in another table, 
        - use INSERT INTO ... SELECT 
        - OR CREATE TABLE AS
        
Copy can decrypt data as it is loaded from S3
    - hardware accelerated SSL used to keep it fast
GZIP, lzop & bzip2 compression supported to speed it up further
Automatic compression option
    - Analyzes data being loaded & figures out optimal compressio nscheme for storing it
Special Case: narrow tables (lots of rows, few columns)
    - Load with a single COPY transaction if possible
    - Otherwise hidden metadata columns consume too much space
    
Redshift copy grants for cross region snapshot copies
    - let's say KMS encrypted redshift cluster and a snapshot of it
    - You want to copy that snapshot to another region for backup
In destination AWS region
    - create a KMS key if you don't have one already
    - specify a unique name for your snapshot copy grant
    - specify     
In the source AWS region
    - enable copyin g of snapshots to the copy grant you jsut created
    
Automatic Workload Managment
    - mangage which quries are snet to the concurrency scaling cluster
    - Creates up to 8 queues
    - Default 5 queus w/ even memory allocation
    - Large queries ie big hash joines
        concurrency lowered
    - small queries  
   