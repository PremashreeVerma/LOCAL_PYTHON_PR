from snowflake.snowpark import Session
from snowflake.snowpark.functions import *


print("Snowpark is ready!")

# snowflake credential
connection_param={
"account":"erjdaal-md06260",
"user":"PremaV",
"password":"PremashreeVerma@09",
"database": "pR_DB",  # Replace with your database name
"schema": "PUBLIC" 
}

session = Session.builder.configs(connection_param).create()

# details receive from snowflake account
print("\n\t Current Account Name: ",session.get_current_account())
print("\n\t Current Database Name: ",session.get_current_database())
print("\n\t Current Schema Name: ",session.get_current_schema())
print("\n\t Current Role Name: ",session.get_current_role())
print("\n\t Current Warehouse Name: ",session.get_current_warehouse())
print("\n\t Fully Qualifiled Schema Name: ",session.get_fully_qualified_current_schema(),"\n")

# To view full table
emp_df=session.table("json_table")
emp_df.show()

# To select one column
emp_select=emp_df.select("JSON_DATA")
emp_select.show()

emp_select=emp_df.select_expr("JSON_DATA:first_name","JSON_DATA:last_name")
emp_select.show()

emp_renamed = emp_select.rename({
    "JSON_DATA:FIRST_NAME": "F_NAME",
    "JSON_DATA:LAST_NAME": "L_NAME"
})

emp_renamed.show()
# a_dict={'"JSON_DATA:first_name"':'F_Name','"JSON_DATA:fast_name"':'L_Name'}
# for key, value in a_dict.items():
#     emp_dict=emp_select.withColumnRenamed(col(key),value)
#     emp_select=emp_dict
# emp_dict.show()

# emp_df da
print(type(emp_df))

# session datatype
print("Session Object Type:", type(session))
session.close()

