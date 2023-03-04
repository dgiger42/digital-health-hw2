import psycopg2

# Establish a connection to the remote PostgreSQL database
conn = psycopg2.connect(
    host="172.16.34.1",
    port=5432,
    database="mimic",
    user="mimic_demo",
    password="mimic_demo"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
# cursor.execute("SELECT * FROM mimic.mimiciii limit 10")
# cursor.execute("show tables")


# cursor.execute("""
#  SELECT * FROM pg_catalog.pg_tables;
# """)

cursor.execute("""
SELECT subject_id, hadm_id, text 
FROM mimiciii.noteevents 
WHERE category = 'Discharge summary'
LIMIT 10
""")




# Fetch the results
results = cursor.fetchall()

# Print the results
print('results')
for row in results:
    print(row)
    print("\n\n")

# print(f'{results = }')

# Close the cursor and connection
cursor.close()
conn.close()