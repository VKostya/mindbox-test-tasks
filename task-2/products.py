from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, col

spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

# Создаем DataFrame с данными о продуктах, категориях и связях между ними
data = [
    ("Продукт1", "Категория1"),
    ("Продукт2", "Категория2"),
    ("Продукт3", None),
    ("Продукт4", "Категория1"),
    ("Продукт5", None),
]

columns = ["Product", "Category"]
df = spark.createDataFrame(data, columns)

# Выбираем все пары "Имя продукта - Имя категории" и имена всех продуктов без категорий
product_category_pairs = df.filter(col("Category").isNotNull()).select(
    "Product", "Category"
)
products_without_category = df.filter(col("Category").isNull()).select("Product")

# Объединяем результаты в один DataFrame
result = product_category_pairs.union(products_without_category)

# Выводим результат
result.show()

# Закрываем сессию Spark
spark.stop()
