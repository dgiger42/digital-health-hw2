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


# cursor.execute("""
#  SELECT * FROM pg_catalog.pg_tables;
# """)

cursor.execute("""
SELECT text 
FROM mimiciii.noteevents 
WHERE category = 'Discharge summary'
LIMIT 10
""")



# Fetch the results
results = cursor.fetchall()

# Print the results
print('results')
for row in results:
    print('#' * 100)
    print('#' * 100)
    print('#' * 100)
    print('\n\n')
    # print(row)
    print(row[0])
    print("\n\n\n\n")


# Close the cursor and connection
cursor.close()
conn.close()
# breakpoint()