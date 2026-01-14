from extract import extract
from transform_spark import transform
from load import load

def run_pipeline():
    df = extract()
    df_t = transform(df)
    load(df_t)
    print("ETL Pipeline executed successfully")

if __name__ == "__main__":
    run_pipeline()
