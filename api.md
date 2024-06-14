# Catalogs

Types:

```python
from unitycatalog.types import CatalogInfo, CatalogListResponse, CatalogDeleteResponse
```

Methods:

- <code title="post /catalogs">client.catalogs.<a href="./src/unitycatalog/resources/catalogs.py">create</a>(\*\*<a href="src/unitycatalog/types/catalog_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/catalog_info.py">CatalogInfo</a></code>
- <code title="get /catalogs/{name}">client.catalogs.<a href="./src/unitycatalog/resources/catalogs.py">retrieve</a>(name) -> <a href="./src/unitycatalog/types/catalog_info.py">CatalogInfo</a></code>
- <code title="patch /catalogs/{name}">client.catalogs.<a href="./src/unitycatalog/resources/catalogs.py">update</a>(name, \*\*<a href="src/unitycatalog/types/catalog_update_params.py">params</a>) -> <a href="./src/unitycatalog/types/catalog_info.py">CatalogInfo</a></code>
- <code title="get /catalogs">client.catalogs.<a href="./src/unitycatalog/resources/catalogs.py">list</a>(\*\*<a href="src/unitycatalog/types/catalog_list_params.py">params</a>) -> <a href="./src/unitycatalog/types/catalog_list_response.py">CatalogListResponse</a></code>
- <code title="delete /catalogs/{name}">client.catalogs.<a href="./src/unitycatalog/resources/catalogs.py">delete</a>(name, \*\*<a href="src/unitycatalog/types/catalog_delete_params.py">params</a>) -> <a href="./src/unitycatalog/types/catalog_delete_response.py">object</a></code>

# Schemas

Types:

```python
from unitycatalog.types import SchemaInfo, SchemaListResponse, SchemaDeleteResponse
```

Methods:

- <code title="post /schemas">client.schemas.<a href="./src/unitycatalog/resources/schemas.py">create</a>(\*\*<a href="src/unitycatalog/types/schema_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/schema_info.py">SchemaInfo</a></code>
- <code title="get /schemas/{full_name}">client.schemas.<a href="./src/unitycatalog/resources/schemas.py">retrieve</a>(full_name) -> <a href="./src/unitycatalog/types/schema_info.py">SchemaInfo</a></code>
- <code title="patch /schemas/{full_name}">client.schemas.<a href="./src/unitycatalog/resources/schemas.py">update</a>(full_name, \*\*<a href="src/unitycatalog/types/schema_update_params.py">params</a>) -> <a href="./src/unitycatalog/types/schema_info.py">SchemaInfo</a></code>
- <code title="get /schemas">client.schemas.<a href="./src/unitycatalog/resources/schemas.py">list</a>(\*\*<a href="src/unitycatalog/types/schema_list_params.py">params</a>) -> <a href="./src/unitycatalog/types/schema_list_response.py">SchemaListResponse</a></code>
- <code title="delete /schemas/{full_name}">client.schemas.<a href="./src/unitycatalog/resources/schemas.py">delete</a>(full_name) -> <a href="./src/unitycatalog/types/schema_delete_response.py">object</a></code>

# Tables

Types:

```python
from unitycatalog.types import TableInfo, TableListResponse, TableDeleteResponse
```

Methods:

- <code title="post /tables">client.tables.<a href="./src/unitycatalog/resources/tables.py">create</a>(\*\*<a href="src/unitycatalog/types/table_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/table_info.py">TableInfo</a></code>
- <code title="get /tables/{full_name}">client.tables.<a href="./src/unitycatalog/resources/tables.py">retrieve</a>(full_name) -> <a href="./src/unitycatalog/types/table_info.py">TableInfo</a></code>
- <code title="get /tables">client.tables.<a href="./src/unitycatalog/resources/tables.py">list</a>(\*\*<a href="src/unitycatalog/types/table_list_params.py">params</a>) -> <a href="./src/unitycatalog/types/table_list_response.py">TableListResponse</a></code>
- <code title="delete /tables/{full_name}">client.tables.<a href="./src/unitycatalog/resources/tables.py">delete</a>(full_name) -> <a href="./src/unitycatalog/types/table_delete_response.py">object</a></code>

# Volumes

Types:

```python
from unitycatalog.types import VolumeInfo, VolumeListResponse, VolumeDeleteResponse
```

Methods:

- <code title="post /volumes">client.volumes.<a href="./src/unitycatalog/resources/volumes.py">create</a>(\*\*<a href="src/unitycatalog/types/volume_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/volume_info.py">VolumeInfo</a></code>
- <code title="get /volumes/{name}">client.volumes.<a href="./src/unitycatalog/resources/volumes.py">retrieve</a>(name) -> <a href="./src/unitycatalog/types/volume_info.py">VolumeInfo</a></code>
- <code title="patch /volumes/{name}">client.volumes.<a href="./src/unitycatalog/resources/volumes.py">update</a>(name, \*\*<a href="src/unitycatalog/types/volume_update_params.py">params</a>) -> <a href="./src/unitycatalog/types/volume_info.py">VolumeInfo</a></code>
- <code title="get /volumes">client.volumes.<a href="./src/unitycatalog/resources/volumes.py">list</a>(\*\*<a href="src/unitycatalog/types/volume_list_params.py">params</a>) -> <a href="./src/unitycatalog/types/volume_list_response.py">VolumeListResponse</a></code>
- <code title="delete /volumes/{name}">client.volumes.<a href="./src/unitycatalog/resources/volumes.py">delete</a>(name) -> <a href="./src/unitycatalog/types/volume_delete_response.py">object</a></code>

# TemporaryTableCredentials

Types:

```python
from unitycatalog.types import GenerateTemporaryTableCredentialResponse
```

Methods:

- <code title="post /temporary-table-credentials">client.temporary_table_credentials.<a href="./src/unitycatalog/resources/temporary_table_credentials.py">create</a>(\*\*<a href="src/unitycatalog/types/temporary_table_credential_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/generate_temporary_table_credential_response.py">GenerateTemporaryTableCredentialResponse</a></code>

# TemporaryVolumeCredentials

Types:

```python
from unitycatalog.types import GenerateTemporaryVolumeCredentialResponse
```

Methods:

- <code title="post /temporary-volume-credentials">client.temporary_volume_credentials.<a href="./src/unitycatalog/resources/temporary_volume_credentials.py">create</a>(\*\*<a href="src/unitycatalog/types/temporary_volume_credential_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/generate_temporary_volume_credential_response.py">GenerateTemporaryVolumeCredentialResponse</a></code>

# Functions

Types:

```python
from unitycatalog.types import FunctionInfo, FunctionListResponse, FunctionDeleteResponse
```

Methods:

- <code title="post /functions">client.functions.<a href="./src/unitycatalog/resources/functions.py">create</a>(\*\*<a href="src/unitycatalog/types/function_create_params.py">params</a>) -> <a href="./src/unitycatalog/types/function_info.py">FunctionInfo</a></code>
- <code title="get /functions/{name}">client.functions.<a href="./src/unitycatalog/resources/functions.py">retrieve</a>(name) -> <a href="./src/unitycatalog/types/function_info.py">FunctionInfo</a></code>
- <code title="get /functions">client.functions.<a href="./src/unitycatalog/resources/functions.py">list</a>(\*\*<a href="src/unitycatalog/types/function_list_params.py">params</a>) -> <a href="./src/unitycatalog/types/function_list_response.py">FunctionListResponse</a></code>
- <code title="delete /functions/{name}">client.functions.<a href="./src/unitycatalog/resources/functions.py">delete</a>(name) -> <a href="./src/unitycatalog/types/function_delete_response.py">object</a></code>
