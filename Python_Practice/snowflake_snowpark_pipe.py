from snowflake.snowpark import Session
from snowflake.snowpark.functions import col, flatten

print("Snowpark is ready!")


connection_param={
"account":"elnonyn-cl75100",
"user":"Dileep",
"password":"Dileep123455555@@",
"database": "AZURE_SNOW_PIPE",  # Replace with your database name
"schema": "AZURE_SNOWFLAKE_SH" 
}

session = Session.builder.configs(connection_param).create()

print("\n\t Current Account Name: ",session.get_current_account())
print("\n\t Current Database Name: ",session.get_current_database())
print("\n\t Current Schema Name: ",session.get_current_schema())
print("\n\t Current Role Name: ",session.get_current_role())
print("\n\t Current Warehouse Name: ",session.get_current_warehouse())
print("\n\t Fully Qualifiled Schema Name: ",session.get_fully_qualified_current_schema(),"\n")

# To view full table
export_df=session.table("reltio_raw_json")
# export_df.show(1)
print("new")
export_select=export_df.select_expr("DATA:attributes:FirstName")


# export_select=export_df.select_expr("DATA:attributes:FirstName").alias("F_Name")
# result_df=export_select.select(col("F_Name")["value"])
export_select.show()

print("Session Object Type:", type(session))
session.close()

