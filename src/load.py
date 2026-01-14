from sqlalchemy import create_engine
from config import DB_CONFIG

def load(df_spark):
    engine = create_engine(
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )
    df_spark.toPandas().to_sql("sales", engine, if_exists="replace", index=False)
