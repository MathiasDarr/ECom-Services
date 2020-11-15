###  What is a data warehouse ###


* A data warehouse is a central repository of data.
* Data flows into a data warehouse from transactional systems, relation databases

### Data warehouse architecture ###

* comprised of tiers
    - top tier is fron end client that prsents results through reporting, analysis & data mining tools
    - middle tier consists of the analytics engine used to access & analyze the dat
    - Bottom tier is the database server, where data is loaded and stored 
        - Data is stored in two different types of ways, 
            1) data that is accssed frequently is stored in fast storage such as SSD drives
            2) data that is infrequently accessed is stored ina cheap object store, such as S3.
        - Warehouse will automatically ensure that frequently accessed data is moved into the fast storage  

