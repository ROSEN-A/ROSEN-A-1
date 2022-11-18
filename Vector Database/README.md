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



