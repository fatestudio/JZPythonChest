import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

if __name__ == '__main__':
    # Sample data
    data = {'Column1': [1, 2, 3, 4, 5], 'Column2': ['A', 'B', 'C', 'D', 'E']}

    # Create a pyarrow.Table
    table = pa.Table.from_pandas(pd.DataFrame(data))

    # Output Parquet file path
    output_file = 'example.parquet'

    # Write the table to the Parquet file
    with pq.ParquetWriter(output_file, table.schema) as writer:
        writer.write_table(table)
