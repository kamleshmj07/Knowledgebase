# Real-Time Intelligence with Microsoft Fabric

![Real-Time Intelligence Core](https://learn.microsoft.com/en-in/training/wwl/get-started-kusto-fabric/media/real-time-intelligence-core.png#lightbox)

## Understand events and streams
- Events are records of things that happen in a system. 
- A stream is essentially a sequence of events, typically ordered by the time an event occurred.

## Components of real-time analytics solutions
1. **Real-time data ingestion**: Collect data from multiple sources simultaneously, as information is generated. For example: database changes from change data capture, sensors, applications, system logs, and APIs.
2. **Stream processing**: Transform and analyze data while it flows from sources to destinations. This includes filtering, aggregating, joining with other data sources, and detecting patterns with minimal latency.
3. **Low-latency storage**: Use specialized databases and storage systems designed to handle high-velocity data writes and provide fast query responses.
4. **Interactive dashboards**: Create visualizations that update automatically as new data arrives, show current state and trends in real-time.
5. **Automated decision making**: Set up event-driven rules and triggers that can initiate actions, send alerts, or start workflows based on real-time conditions.

## Eventstreams for data ingestion and transformation
Eventstreams are a way to bring real-time events into Fabric, to transform them, and then route data to a destination.

## Data destinations in eventstreams
You can load the data from your stream into the following destinations: a KQL database in an Eventhouse, Lakehouse, a derived stream, Fabric Activator, or a custom endpoint.

## Data transformation in a KQL database in Eventhouse with update policies
When directly ingesting data into a KQL database, data first lands in the database, then can be transformed using update policies. This is different from eventstream transformations that occur during stream processing, before routing data to a destination.

Update policies are automation mechanisms triggered when new data is written to a table. They run a query to transform ingested data and save the result to a destination table.

## Store and query real-time data
Within an eventhouse, you can create:
- **KQL databases**: Real-time optimized data stores that host a collection of tables, stored functions, materialized views, shortcuts and data streams.
- **KQL querysets**: Collections of KQL queries that you can use to work with data in KQL database tables. A KQL queryset supports queries written using Kusto Query Language (KQL) or a subset of the Transact-SQL language.

## Kusto Query Language (KQL)
KQL is specifically designed for analyzing large volumes of structured, semi-structured, and unstructured data with exceptional performance. KQL databases are optimized for time-series data and index incoming data by ingestion time and partition it for optimal query performance. KQL is the same language used in Azure Data Explorer, Azure Monitor Log Analytics, Microsoft Sentinel, and in Microsoft Fabric.

## Automate data processing with management commands
Beyond basic querying, you can automate data processing through management commands including:
- **Update policies**: Automatically transform incoming data and save it to different tables as it arrives.
- **Materialized views**: Precalculate and store summary results for faster queries.
- **Stored functions**: Save frequently used query logic that you can reuse across multiple queries.

## Visualize real-time data
You can create a Real-Time Dashboard in a workspace and then configure its source, or you can create one directly from a KQL queryset in an eventhouse.

## Automate actions
Activator is a technology in Microsoft Fabric that enables automated processing of events that trigger actions. For example, you can use Activator to notify you by email when a value in an Eventstream deviates from a specific range or to run a notebook to perform some Spark-based data processing logic when a Real-Time Dashboard is updated.

Use Activator to:
- Initiate marketing actions when product sales drop.
- Send notifications when temperature changes could affect perishable goods.
- Flag real-time issues affecting the user experience on apps and websites.
- Trigger alerts when a shipment hasn't been updated within an expected time frame.
- Send alerts when a customer's account balance crosses a certain threshold.
- Respond to anomalies or failures in data processing workflows immediately.
- Run ads when same-store sales decline.
- Alert store managers to move food from failing grocery store freezers before it spoils.
