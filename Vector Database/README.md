# Milvus Vector Database
## Milvus Standalone
### Prerequisites
Check the [requirements](https://milvus.io/docs/v2.1.x/prerequisite-docker.md) for hardware and software prior to your installation.
### Download the YAML File 
> [docker-compose.yml](./docker-compose.yml) has already been added in this directory, you can skip this step

Download [milvus-standalone-docker-compose.yml](./docker-compose.yml) and save it as docker-compose.yml manually.
### Start Milvus
1. Start Docker Desktop
2. In the same directory as the docker-compose.yml file, start up Milvus by running:
> sudo docker-compose up -d
3. Check if the containers are up and running
> sudo docker-compose ps
4. After Milvus standalone starts, there will be three docker containers running, including the Milvus standalone service and its two dependencies.
### Stop Milvus
1. To stop Milvus standalone, run:
> sudo docker-compose down
2. To delete data after stopping Milvus, run:
> sudo rm -rf  volumes

## Milvus SDK (PyMilvus)
### Requirements
- Python 3.6 or later is required.
- Google protobuf is installed. You can install it with the command 
> pip3 install protobuf==3.20.0
- grpcio-tools is installed. You can install it with the command 
> pip3 install grpcio-tools.
### Install PyMilvus via pip
> python3 -m pip install pymilvus==2.1.3
### Verify Installation
> python3 -c "from pymilvus import Collection"

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
