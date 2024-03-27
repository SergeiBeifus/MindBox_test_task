from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, when, col


def find_product_category_pairs(dataframe):
    products_with_categories = dataframe.filter(col("Category").isNotNull() & col("Product").isNotNull())
    products_without_categories = dataframe.filter(col("Category").isNull() & col("Product").isNotNull())

    product_category_pairs = products_with_categories.select("Product", "Category")

    all_pairs = product_category_pairs.union(
        products_without_categories.select("Product", col("Product").alias("Category"))
    )

    return all_pairs


# Пример использования
if __name__ == "__main__":
    session = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

    columns = ["Product", "Category"]
    # Example DataFrame
    data = [("Product A", "Category 1"),
            ("Product B", "Category 2"),
            ("Product C", "Category 1, Category 3"),
            ("Product D", None),
            ("Product E", "Category 2"),
            (None, "Category 2")]

    products_dataframe = session.createDataFrame(data, columns)
    products_dataframe = products_dataframe.withColumn("Category", explode(
        split(when(products_dataframe["Category"].isNull(), "no Category").otherwise(products_dataframe["Category"]),
              ", ")))
    result = find_product_category_pairs(products_dataframe)
    result.show()

    session.stop()
