from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum, col

spark = SparkSession.builder.appName("processamento_vendas").getOrCreate()

df = spark.read.csv("data/vendas_grande.csv", header=True, inferSchema=True)

print("Schema inferido automaticamente:")
df.printSchema()

print(f"Total de linhas: {df.count()}")

receita_por_categoria = (
    df.withColumn("valor_total", col("preco") * col("quantidade"))
      .groupBy("categoria")
      .agg(_sum("valor_total").alias("receita_total"))
      .orderBy(col("receita_total").desc())
)

receita_por_categoria.show()

# Também dá para usar SQL puro, registrando o DataFrame como uma "tabela" temporária:
df.createOrReplaceTempView("vendas")
resultado_sql = spark.sql("""
    SELECT categoria, SUM(preco * quantidade) AS receita_total
    FROM vendas
    GROUP BY categoria
    ORDER BY receita_total DESC
""")
resultado_sql.show()

receita_por_categoria.write.mode("overwrite").parquet("data/receita_por_categoria_parquet")
df.write.mode("overwrite").parquet("data/vendas_grande_parquet")

spark.stop()
