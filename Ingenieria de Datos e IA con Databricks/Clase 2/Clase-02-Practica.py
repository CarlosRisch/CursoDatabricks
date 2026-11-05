# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
print("Version de Apache Spark:", spark.version)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*) as Filas, sum(id) as suma
# MAGIC FROM range(10000000);

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_catalog(), current_schema();