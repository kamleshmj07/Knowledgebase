# Data roles and services

## Database administrators
- Database admins are responsible for the overall availability and consistent performance and optimizations of databases. 
- They also implement policies, tools, and processes for backup and recovery plans to recover following a natural disaster or human-made error.
- They are also responsible for managing the security of the data in the database, granting privileges over the data, granting or denying access to users as appropriate.

## Data engineers 
- Data engineers manage infrastructure and processes for data integration across the organization, applying data cleaning routines, identifying data governance rules, and implementing data pipelines to transfer and transform data between systems.

## Data analysts
- Data analysts explore and analyze data to create visualizations and charts that enable organizations to make informed decisions.

## AI Engineer
- An AI engineer builds and integrates AI-powered features into applications and data workflows. They work with large language models (LLMs)—AI systems trained on vast amounts of text that can understand and generate human language—as well as machine learning pipelines, and data sources to enable intelligent scenarios such as chat-over-your-data, content generation, and automated classification.

## Identify data services

1. **Azure SQL**
   Azure SQL is the collective name for a family of relational database solutions based on the Microsoft SQL Server database engine. Specific Azure SQL services include:
   - **a. Azure SQL Database** – a fully managed platform-as-a-service (PaaS) database hosted in Azure.
   - **b. Azure SQL Managed Instance** – a hosted instance of SQL Server with automated maintenance, which allows more flexible configuration than Azure SQL DB but with more administrative responsibility for the owner.
   - **c. Azure SQL VM** – a virtual machine with an installation of SQL Server, allowing maximum configurability with full management responsibility.

2. **Open-source databases in Azure**
   - **a. Azure Database for MySQL** - a simple-to-use open-source database management system that is commonly used in Linux, Apache, MySQL, and PHP (LAMP) stack apps.
   - **b. Azure Database for PostgreSQL** - a hybrid relational-object database. You can store data in relational tables, but a PostgreSQL database also enables you to store custom data types, with their own nonrelational properties.

3. **Azure Cosmos DB**
   Azure Cosmos DB is a global-scale nonrelational (NoSQL) database system that supports multiple application programming interfaces (APIs), enabling you to store and manage data as JSON documents, key-value pairs, column-families, and graphs.

4. **Azure Storage**
   - **a. Blob containers** - scalable, cost-effective storage for binary files.
   - **b. File shares** - network file shares such as you typically find in corporate networks.
   - **c. Tables** - key-value storage for applications that need to read and write data values quickly.
   
   *Note: Data engineers use Azure Storage to host data lakes - blob storage with a hierarchical namespace that enables files to be organized in folders in a distributed file system.*

5. **Azure Data Factory**
   Azure Data Factory is an Azure service that enables you to define and schedule data pipelines to transfer and transform data.

6. **Microsoft Fabric**
   Microsoft Fabric is Microsoft's unified software-as-a-service (SaaS) analytics platform. It brings data engineering, data warehousing, real-time analytics, data science, and Power BI together in a single browser-based workspace on top of one shared storage layer called OneLake. You don't manage servers or clusters—you create workspaces and items, and Microsoft runs the infrastructure.

7. **Microsoft Fabric IQ**
   It enables business users and AI agents to ask questions about data in natural language, based on a shared understanding of your enterprise data.

8. **Power BI**
   Power BI is Microsoft's business intelligence and data visualization platform.

9. **Azure Databricks**
   Azure Databricks is a cloud analytics platform built on Apache Spark. It's optimized for large-scale data engineering, data science, and SQL analytics over open lakehouse formats—primarily Delta Lake. It runs as a managed service inside your Azure subscription and is a common choice for teams that need code-first Spark and notebook-based workflows.

10. **Azure Stream Analytics**
    Azure Stream Analytics is a real-time stream processing engine that captures a stream of data from an input, applies a query to extract and manipulate data from the input stream, and writes the results to an output for analysis or further processing.

11. **Azure Data Explorer**
    Azure Data Explorer is a fully managed, standalone, big data analytics platform that offers high-performance querying of log and telemetry data.

12. **Microsoft Purview**
    Microsoft Purview provides a solution for enterprise-wide data governance and discoverability. You can use Microsoft Purview to create a map of your data and track data lineage across multiple data sources and systems, enabling you to find trustworthy data for analysis and reporting.

13. **Microsoft Foundry**
    Microsoft Foundry is Microsoft's unified Azure platform-as-a-service (PaaS) for enterprise AI operations, model builders, and application development. It provides the tools, model access, and infrastructure that AI engineers—and developers more broadly—use to design, test, and deploy intelligent solutions, including chat-over-your-data applications, multi-agent workflows, and automated AI pipelines integrated with Azure data services.
