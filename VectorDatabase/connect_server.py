from pymilvus import connections,Collection,FieldSchema,DataType,CollectionSchema,utility
fmt = "\n=== {:30} ===\n"
connections.connect(
  alias="default",
  host='localhost',
  port='19530'
)

has = utility.has_collection("image")
print(f"Does collection image exist in Milvus: {has}")

# Field schema
id_field = FieldSchema(name="id",
                       dtype=DataType.INT64,
                       is_primary=True,
                       auto_id=True,
                       description="primary id"
                       )
path_field = FieldSchema(name="path",
                         dtype=DataType.VARCHAR,
                         max_length=1024
                         )
timestamp_field = FieldSchema(name="timestamp",
                              dtype=DataType.VARCHAR,
                              max_length=512
                              )
size_field = FieldSchema(name="size",
                         dtype=DataType.FLOAT
                         )
label_field = FieldSchema(name="label",
                          dtype=DataType.BOOL
                          )
vector_field = FieldSchema(name="vector",
                           dtype=DataType.FLOAT_VECTOR,
                           dim=4096,
                           description="vgg16 vector"
                           )
fields = [id_field, path_field, timestamp_field, size_field, label_field, vector_field]
# Collection schema
collection_schema = CollectionSchema(fields)

print(fmt.format("Create collection `image`"))

# Collection
collection_name = "image"
collection = Collection(
    name=collection_name,
    schema=collection_schema
)

list = utility.list_collections()
print(fmt.format(f"List collections in this Milvus instance: {list}"))

has = utility.has_collection("image")
print(f"Does collection image exist in Milvus: {has}")

print(fmt.format("Drop collection `image`"))
utility.drop_collection("image")

