import pandas as pd
import pyarrow.parquet as pq

target_parquet = "outputs/sample_parquet.parquet"
print(">> using `pandas`")
df = pd.read_parquet(target_parquet)
print(df)
print(">> using `pyarrow.parquet`")
pq = pq.read_table(target_parquet)
print(pq)
