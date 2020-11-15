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
    
 