from snowflake.snowpark import Session

print("Snowpark is ready!")

# # # [myconnection]
# # # account = "myaccount"

# # # user = "jdoe"
# # # password = "******"
# # # warehouse = "my-wh"
# # # database = "my_db"
# # # schema = "my_schema"

connection_param={
"account":"erjdaal-md06260",
"user":"PremaV",
"password":"PremashreeVerma@09",
"database": "PR_DB",  # Replace with your database name
"schema": "PUBLIC" 
}

session = Session.builder.configs(connection_param).create()

print("\n\t Current Account Name: ",session.get_current_account())
print("\n\t Current Database Name: ",session.get_current_database())
print("\n\t Current Schema Name: ",session.get_current_schema())
print("\n\t Current Role Name: ",session.get_current_role())
print("\n\t Current Warehouse Name: ",session.get_current_warehouse())
print("\n\t Fully Qualifiled Schema Name: ",session.get_fully_qualified_current_schema(),"\n")

print("Session Object Type:", type(session))
session.close()

