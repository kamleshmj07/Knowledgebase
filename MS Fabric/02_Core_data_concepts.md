# Core data concepts

You can classify data as structured, semi-structured, or unstructured.

## Structured data
Structured data is data that adheres to a fixed schema. Structured data is often stored in a database in which multiple tables can reference one another by using key values in a relational model.

## Semi-structured data
Semi-structured data is information that has some structure, but which allows for some variation between entity instances. One common format for semi-structured data is JavaScript Object Notation (JSON).

## Unstructured data
Not all data is structured or even semi-structured.

## Data stores
Organizations typically store data in structured, semi-structured, or unstructured format to record details of entities (for example, customers and products), specific events (such as sales transactions), or other information in documents, images, and other formats. The stored data can then be retrieved for analysis and reporting later.

There are two broad categories of data stores in common use:
* File stores
* Databases

## File Stores
Some common file formats are discussed below:

1. **Delimited text files**
2. **JavaScript Object Notation (JSON)**
3. **Extensible Markup Language (XML)**
4. **Binary Large Object (BLOB)**
5. **Optimized file formats (parquet, avro, delta lake)**
   * **Parquet** is a columnar data format and the de facto standard for modern data lakehouses.
   * **Avro** is a row-based format. 
   * **Delta Lake** is an open-source storage format that builds on Parquet by adding a transaction log.

## Databases
* **Relational databases**
* **Nonrelational databases**
  * **Key-value databases** in which each record consists of a unique key and an associated value, which can be in any format.
  * **Document databases**, which are a specific form of key-value database in which the value is a JSON document (which the system is optimized to parse and query).
  * **Column family databases**, which store tabular data comprising rows and columns, but you can divide the columns into groups known as column-families. Each column family holds a set of columns that are logically related together.
  * **Graph databases**, which store entities as nodes with links to define relationships between them.

## Transactional data processing
A transactional system records transactions that encapsulate specific events that the organization wants to track. The work performed by transactional systems is often referred to as Online Transactional Processing (OLTP).

OLTP solutions rely on a database system in which data storage is optimized for both read and write operations in order to support transactional workloads in which data records are created, retrieved, updated, and deleted (often referred to as CRUD operations). These operations are applied transactionally, in a way that ensures the integrity of the data stored in the database:
* Atomicity
* Consistency 
* Isolation 
* Durability 

## Analytical data processing
Analytical data processing typically uses read-only (or read-mostly) systems that store vast volumes of historical data or business metrics.

## Organizing data with the medallion architecture		
A common pattern for organizing data in a lakehouse is the medallion architecture, which uses three layers:
* **Bronze:** raw data ingested as-is from source systems, with no transformations applied, preserving the original records for reprocessing.
* **Silver:** cleansed and conformed data, with duplicates removed and data types standardized.
* **Gold:** aggregated, business-ready data modeled for specific reporting and analytics use cases.
