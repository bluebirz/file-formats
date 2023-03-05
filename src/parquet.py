import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

target_parquet = "../outputs/sample_parquet.parquet"
people = [
    {
        "id": 1,
        "first_name": "Kenneth",
        "last_name": "Farrell",
        "occupation": "Product manager",
    },
    {
        "id": 2,
        "first_name": "Kimberly",
        "last_name": "Hood",
        "occupation": "Social worker",
    },
]
df = pd.json_normalize(people)
table = pa.Table.from_pandas(df)
pq.write_table(table, target_parquet)
