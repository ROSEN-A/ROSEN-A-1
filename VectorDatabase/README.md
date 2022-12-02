# Milvus Vector Database
## Milvus Standalone
### Prerequisites
Check the [requirements](https://milvus.io/docs/v2.1.x/prerequisite-docker.md) for hardware and software prior to your installation.
### Download the YAML File 
> **[docker-compose.yml](./docker-compose.yml) has already been added in this directory, you can skip this step**

Download [milvus-standalone-docker-compose.yml](./docker-compose.yml) and save it as docker-compose.yml manually.
### Start Milvus
1. Start Docker Desktop
2. In the same directory as the docker-compose.yml file, start up Milvus by running:
> `sudo docker-compose up -d`
3. Check if the containers are up and running
> `sudo docker-compose ps`
4. After Milvus standalone starts, there will be three docker containers running, including the Milvus standalone service and its two dependencies.
### Stop Milvus
1. To stop Milvus standalone, run:
> `sudo docker-compose down`
2. To delete data after stopping Milvus, run:
> `sudo rm -rf  volumes`

## Milvus SDK (PyMilvus)
### Requirements
- Python 3.6 or later is required.
- Google protobuf is installed. You can install it with the command 
> `pip3 install protobuf==3.20.0`
- grpcio-tools is installed. You can install it with the command 
> `pip3 install grpcio-tools`
### Install PyMilvus via pip
> `python3 -m pip install pymilvus==2.1.3`
### Verify Installation
> `python3 -c "from pymilvus import Collection"`

### Manage Milvus Connections
Milvus supports two ports, `port 19530` and `port 9091`:
- `Port 19530` is for gRPC. It is the default port when you connect to a Milvus server with different Milvus SDKs.

- `Port 9091` is for RESTful API. It is used when you connect to a Milvus server with an HTTP client.

The example below connects to the Milvus server with host as localhost and port as `19530` or `9091`, and disconncets from it. If the connection is refused, try unblocking the corresponding port.

### Connect to a Milvus server
Construct a Milvus connection. Ensure to connect to Milvus server before any operations.
> run [connect_server.py](./connect_server.py)
### Disconnect from a Milvus server
Disconnect from a Milvus server.
> run [disconnect_server.py](./disconnect_server.py)

### Manage Metadata with MySQL
By default, Milvus uses SQLite for metadata management. But MySQL is recommended in a production environment for improved reliability.
Follow the steps below to use MySQL as metadata management service in Linux:
1. Pull the latest image of MySQL:
> `docker pull mysql:5.7`
2. Launch MySQL service. You can set your own password and port.
> `docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7`
3. Use root account and the IP of the host that runs MySQL service (<MySQL_server_host IP>) to log in MySQL. Press <ENTER> to enter the password you set in the previous step. The IP address of localhost is `127.0.0.1`.
> `mysql -h <MySQL_server_host IP> -uroot -p`
4. Enter MySQL client command line interface to create a database. Here we use `milvus` as the database name.
> `mysql> create database milvus;`

## Main Components
There are two modes for running Milvus: Standalone and Cluster. These two modes share the same features. You can choose a mode that best fits your dataset size, traffic data, and more. For now, Milvus standalone cannot be upgraded "online" to Milvus cluster.
### Milvus Standalone
**Milvus standalone** includes three components:
- **Milvus**: The core functional component.
- **etcd**: The metadata engine, which accesses and stores metadata of Milvus' internal components, including proxies, index nodes, and more.
- **MinIO**: The storage engine, which is responsible for data persistence for Milvus.
### Milvus cluster
**Milvus cluster** includes eight microservice components and three third-party dependencies. All microservices can be deployed on Kubernetes, independently from each other.
#### Microservice components
- Root coord
- Proxy
- Query coord
- Query node
- Index coord
- Index node
- Data coord
- Data node
#### Third-party dependencies
- **etcd**: Stores metadata for various components in the cluster.
- **MinIO**: Responsible for data persistence of large files in the cluster, such as index and binary log files.
- **Pulsar**: Manages logs of recent mutation operations, outputs streaming log, and provides log publish-subscribe services.
## Data Processing
- Data insertion
- Index building 
- Data query
### Data insertion
- You can specify a number of shards for each collection in Milvus, each shard corresponding to a virtual channel (_vchannel_).
- Milvus assigns each vchannel in the log broker a physical channel (_pchannel_).
- Any incoming insert/delete request is routed to shards based on the **hash value of primary key**.
- Both **DML** (data manipulation language) operations and DDL (data definition language) operations are written to the log sequence, but **DDL** operations are only assigned one channel because of their low frequency of occurrence.
### Index building
- Index building is performed by index node. To avoid frequent index building for data updates, a collection in Milvus is divided further into segments, each with its own index.
- Milvus supports building index for each **vector field**, **scalar field** and **primary field**.
- Vectors cannot be efficiently indexed with traditional tree-based indexes due to their high-dimensional nature, but can be indexed with techniques that are more mature in this subject, such as **cluster-** or **graph-based** indexes. Vectors are returned together with their corresponding primary key and fields.
### Data query
> Data query refers to the process of searching a specified collection for **k number of vectors nearest to a target vector** or for all vectors within a specified distance range to the vector.
- A collection in Milvus is split into multiple segments, and the query nodes loads indexes by segment. 
- When a search request arrives, it is broadcast to all query nodes for a concurrent search.
- Each node then prunes the local segments, searches for vectors meeting the criteria, and reduces and returns the search results.
## Schema
Schema is used to define the properties of a collection and the fields within.
### Field schema
A field schema is the logical definition of a field. It is the first thing you need to define before defining a _collection schema_ and _creating a collection_. Milvus supports **only one primary key field** in a collection.
#### Field schema properties
| Properties |                  Description                  |                                    Notes                                    |
|:----------:|:---------------------------------------------:|:---------------------------------------------------------------------------:|
|    name    | Name of the field in the collection to create |                        Data type: String. <br/>Mandatory                         |
    | dtype | Data type of the field |                                  Mandatory                                  | 
    | description | Description of the field |                         Data type: String. Optional                         |
    | is_primary | Whether to set the field as the primary key field or not | Data type: Boolean (`true` or `false`). Mandatory for the primary key field | 
    | dim | Dimension of the vector	|    Data type: Integer ∈ [1, 32768]. <br/> Mandatory for the vector field    |

#### Create a field schema
> `from pymilvus import FieldSchema`
</br> `id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, description="primary id")`
</br> `age_field = FieldSchema(name="age", dtype=DataType.INT64, description="age")`
</br> `embedding_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128, description="vector")`
#### Supported data type
`DataType` defines the kind of data a field contains. Different fields support different data types. 
- Primary key field supports:
  - INT64: numpy.int64
  - VARCHAR: VARCHAR
- Scalar field supports:
  - BOOL: Boolean (`true` or `false`)
  - INT8: numpy.int8
  - INT16: numpy.int16
  - INT32: numpy.int32
  - INT64: numpy.int64 
  - FLOAT: numpy.float32
  - DOUBLE: numpy.double 
  - VARCHAR: VARCHAR
- Vector field supports:
  - BINARY_VECTOR: Binary vector
  - FLOAT_VECTOR: Float vector
### Collection schema
  A collection schema is the logical definition of a collection. Usually you need to define the _field schema_ before defining a collection schema and _creating a collection_.
#### Collection schema properties
| Properties  |                             Description                              |                                     Notes                                      |
|:-----------:|:--------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
|    field    |                 Fields in the collection to create	                  |                                   Mandatory                                    |
| description |                    Description of the collection	                    |                        Data type: String.<br/>Optional                         |
| auto_id	 |   Whether to enable Automatic ID (primary key) allocation or not	    |                  Data type: Boolean (`true` or `false`).<br/>Optional                   |
#### Create a collection schema
Define the field schemas before defining a collection schema.

> `from pymilvus import FieldSchema, CollectionSchema`
> </br>`id_field = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, description="primary id")`
> </br> `age_field = FieldSchema(name="age", dtype=DataType.INT64, description="age")`
> </br> `embedding_field = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=128, description="vector")`
> </br> `schema = CollectionSchema(fields=[id_field, age_field, embedding_field], auto_id=False, description="desc of a collection")`

Create a collection with the schema specified:
> `from pymilvus import Collection`
> </br>`collection_name1 = "tutorial_1"`
> </br>`collection1 = Collection(name=collection_name1, schema=schema, using='default', shards_num=2)`

You can also create a collection with `Collection.construct_from_dataframe`, which automatically generates a collection schema from DataFrame and creates a collection.
> `import pandas as pd`
> </br>`df = pd.DataFrame({`
> </br>`"id": [i for i in range(nb)],`
> </br>`"age": [random.randint(20, 40) for i in range(nb)],`
> </br>`"embedding": [[random.random() for _ in range(dim)] for _ in range(nb)]`
> </br>`})`
> </br>`collection, ins_res = Collection.construct_from_dataframe(`
> </br>                              `'my_collection',`
> </br>                               `df,`
> </br>                               `primary_field='id',`
> </br>                               `auto_id=False`
> </br>                               `)`

## Create a Collection
A collection consists of one or more partitions. While creating a new collection, Milvus creates a default partition `_default`.

The following example builds a two-shard collection name `book`, with a primary key field named `book_id`, an `INT64` scalar field named `word_count`, and a two-dimensional floating-point vector field named `book_intro`. 

### Prepare Schema

> The collection to create must contain a primary key field and a vector field. INT64 and String are supported data type on primary key field.

First, prepare necessary parameters, including field schema, collection schema, and collection name. 

> `from pymilvus import CollectionSchema, FieldSchema, DataType`
> </br> `book_id = FieldSchema (`
> </br> `name = "book_id",`
> </br> `dtype=DataType.INT64,`
> </br> `is_primary=True,`
> </br> `)`
> </br> `book_name = FieldSchema (`
> </br> `name = "book_name",`
> </br> `dtype=DataType.VARCHAR,`
> </br> `max_length=200,`
> </br> `)`
> </br> `word_count = FieldSchema (`
> </br> `name = "word_count",`
> </br> `dtype=DataType.INT64,`
> </br> `)`
> </br> `book_intro = FieldSchema (`
> </br> `name = "book_intro",`
> </br> `dtype=DataType.FLOAT_VECTOR,`
> </br> `dim=2`
> </br> `)`
> </br> `schema = CollectionSchema (`
> </br> `fields=[book_id, book_name, word_count, book_intro],`
> </br> `  description="Test book search"`
> </br> `)`
> </br> `collection_name = "book"`

|                   Properties                   |                                                                                     Description                                                                                      |                                                                                                                                                                                           Notes                                                                                                                                                                                           |
|:----------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                 `FieldSchema`                  |                                            Schema of the fields within the collection to create. Refer to Schema for more information.		                                             |                                                                                                                                                                                            N/A                                                                                                                                                                                            |
|                     `name`                     |                                                                            Name of the field to create.		                                                                            |                                                                                                                                                                                            N/A                                                                                                                                                                                            |
|                    `dtype`	                    |                                                                         Data type of the field to create.		                                                                          | - Primary key field supports: <br/> - `DataType.INT64` (numpy.int64) <br/>- `DataType.VARCHAR` (VARCHAR) <br/>For scalar field: <br/>- `DataType.BOOL` (Boolean) <br/>- `DataType.INT64` (numpy.int64) <br/>- `DataType.FLOAT` (numpy.float32) <br/>- `DataType.DOUBLE` (numpy.double) <br/>For vector field: <br/>- `BINARY_VECTOR` (Binary vector) <br/>- `FLOAT_VECTOR` (Float vector) |
| `is_primary` (Mandatory for primary key field) |                                                                Switch to control if the field is primary key field.		                                                                |                                                                                                                                                                                     `True` or `False`                                                                                                                                                                                     |
|  `auto_id` (Mandatory for primary key field)   |                                                         Switch to enable or disable automatic ID (primary key) allocation.		                                                         |                                                                                                                                                                                     `True` or `False`                                                                                                                                                                                     |
|  `max_length` (Mandatory for VARCHAR field)	   |                                                                 Maximum length of strings allowed to be inserted.		                                                                  |                                                                                                                                                                                        [1, 65,535]                                                                                                                                                                                        |
|       `dim` (Mandatory for vector field)       |                                                                              Dimension of the vector.		                                                                              |                                                                                                                                                                                        [1, 32,768]                                                                                                                                                                                        |
|            `description` (Optional)            |                                            Description of the field.			                                             |                                                                                                                                                                                            N/A                                                                                                                                                                                            |
|               `CollectionSchema`               |                                            Schema of the collection to create. Refer to Schema for more information.			                                             |                                                                                                                                                                                            N/A                                                                                                                                                                                            |
|                    `fields`                    |                                            Fields of the collection to create.			                                             |                                                                                                                                                                                            N/A                                                                                                                                                                                            |
|            `description` (Optional)            |                                            Description of the collection to create.				                                             |                                                                                                                                                                                            N/A                                                                                                                                                                                            |
|          `collection_name`           |                                            Name of the collection to create.					                                             |                                                                                                                                                                                            N/A                                                                                                                                                                                            |

### Create a collection with the schema

Then, create a collection with the schema you specified above.

> `from pymilvus import Collection`
> </br> `collection = Collection(`
> </br> `name=collection_name,`
> </br> `schema=schema,`
> </br> `using='default',`
> </br> `shards_num=2,`
> </br> `properties={"collection.ttl.seconds": 15}`
> </br> `)`

|       Properties        |                                                                                     Description                                                                                      |                              Notes                              |
|:-----------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------:|
|   `using` (optional)    |                                            By specifying the server alias here, you can choose in which Milvus server you create a collection.		                                             |                               N/A                               |
| `shards_num` (optional) |                                            Number of the shards for the collection to create.		                                             |                            [1, 256]                             |
|   `properties: collection.ttl.seconds` (optional)    |                                            Collection time to live (TTL) is the expiration time of a collection. Data in an expired collection will be cleaned up and will not be involved in searches or queries. Specify TTL in the unit of seconds.	                                             |   The value should be 0 or greater. 0 means TTL is disabled.    |

