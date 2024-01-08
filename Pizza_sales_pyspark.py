# Databricks notebook source
dbutils.fs.mount(
  source = "wasbs://rawdata@pizzasalesrishabh.blob.core.windows.net",
  mount_point = "/mnt/transformeddata",
  extra_configs = {"fs.azure.account.key.pizzasalesrishabh.blob.core.windows.net":"c/eCR4XurA07gN3swIo6rO5KA4QYHINyuSw6h9y4fgZQ5WNYBlHcuqnWxTIJr7O+QUWT7xzz8cYE+AStNp0Mjw=="})

# COMMAND ----------

dbutils.fs.ls("/mnt/tranformeddata")

# COMMAND ----------

df = spark.read.format("csv").options(header='True',inferSchema ='True').load('dbfs:/mnt/tranformeddata/pizzasales1.csv')

# COMMAND ----------

display(df)

# COMMAND ----------

df.head()

# COMMAND ----------

df.createOrReplaceTempView("pizza_sales_analysis")

# COMMAND ----------

# MAGIC %sql 
# MAGIC select * from pizza_sales_analysis

# COMMAND ----------

# MAGIC %sql
# MAGIC select
# MAGIC order_id,
# MAGIC pizza_id,
# MAGIC quantity,
# MAGIC date_format(order_date,"MMM") as month_name,
# MAGIC date_format(order_date,"EEEE" ) as day_name,
# MAGIC hour(order_time) order_time,
# MAGIC unit_price,
# MAGIC total_price,
# MAGIC pizza_size,
# MAGIC pizza_category,
# MAGIC pizza_name
# MAGIC from pizza_sales_analysis
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select
# MAGIC count(distinct order_id) as order_id,
# MAGIC sum(quantity) as quantity,
# MAGIC date_format(order_date,"MMM") as month_name,
# MAGIC date_format(order_date,"EEEE" ) as day_name,
# MAGIC hour(order_time) order_time,
# MAGIC sum(unit_price) as unit_price,
# MAGIC sum(total_price) as total_price,
# MAGIC pizza_size,
# MAGIC pizza_category,
# MAGIC pizza_name
# MAGIC from pizza_sales_analysis
# MAGIC group by 3,4,5,8,9,10

# COMMAND ----------


