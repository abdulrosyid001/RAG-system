import pandas as pd
from sqlalchemy import create_engine
import re

db_host="localhost"
db_name="magang"
db_user="postgres"
db_password="indojayaraya"
db_port=5432

# Buat engine SQLAlchemy
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)

# Query ambil postingan
query = """
SELECT *
FROM posts
WHERE caption IS NOT NULL
ORDER BY posted_at DESC
"""

# Load ke DataFrame
df_posts = pd.read_sql(query, engine)

print(f"✅ Berhasil load {len(df_posts)} postingan")
print(df_posts)

output_path = "D:/Kuliah/Magang Datains/instagrapi/df_posts.csv"

df_posts.to_csv(
    output_path,
    index=False
)

print(f"💾 DataFrame berhasil disimpan ke {output_path}")
