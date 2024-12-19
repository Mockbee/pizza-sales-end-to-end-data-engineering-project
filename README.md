### About Dataset/API Used:
This project utilizes a dataset on pizza sales, which can be accessed [here](https://drive.google.com/file/d/1i4aRieq_WDVJDGpqtZq8UW9CH8sCbaBd/view). The dataset was uploaded into Azure Blob Storage to begin the ETL pipeline process.

---

### Services Used:

1. **Azure Blob Storage:**
   - A scalable object storage solution for cloud applications.
   - Used to upload and store the raw dataset securely in Azure.

2. **Azure Data Factory (Gen II):**
   - A cloud-based data integration service to orchestrate ETL workflows.
   - Extracted the raw data, cleaned it, and transformed it into a structured CSV file.

3. **Databricks:**
   - A collaborative platform for big data and machine learning.
   - Created a Databricks cluster to process the data.
   - Transformed data into Pandas and Spark DataFrames for efficient manipulation and analytics.

4. **SQL:**
   - Used within Databricks to convert processed data into SQL format.
   - Enabled structured querying and advanced analytics.

5. **Power BI:**
   - A business analytics tool for interactive data visualization.
   - Final transformed data was exported to Power BI to create insightful dashboards and reports.

---

### Project Execution Flow:
1. **Data Upload:**
   - Raw dataset uploaded into Azure Blob Storage.

2. **ETL Process Using Azure Data Factory:**
   - Data Factory Gen II orchestrated the extraction, cleaning, and transformation of data into a clean CSV format.

3. **Data Processing in Databricks:**
   - A Databricks cluster was created to process the data.
   - Data was transformed into Pandas and Spark DataFrames.
   - SQL was used for structured querying and analysis.

4. **Visualization in Power BI:**
   - Final data exported into Power BI for creating interactive dashboards and visualizations.

---

This end-to-end pipeline demonstrates the integration of multiple services for efficient data processing, transformation, and visualization.
