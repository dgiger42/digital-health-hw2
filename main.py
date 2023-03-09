import psycopg2
import json






# FINDING UMLS SYNONYMS (starting with a given CUI - need to find CUI first):
# can find CUI with `str like 'whatever was entered'`

#select distinct str from MRCONSO where CUI = "C0242379" and SUPPRESS = 'N' limit 30;
















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


def get_discharge_summaries():
    # get column names


    # should probably limit fields eventually...
    # NEED TO REMOVE LIMIT
    cursor.execute(f"""
    SELECT {','.join(col_names)}
    FROM mimiciii.noteevents 
    WHERE category = 'Discharge summary'
    LIMIT 5
    """)


cursor.execute("""
SELECT column_name FROM information_schema.columns where table_name = 'noteevents'
""")

res1 = cursor.fetchall()
col_names = [x[0] for x in res1]

get_discharge_summaries()

# Fetch the results
results = cursor.fetchall()
all_row_dicts = []

# Print the results
# print('results')
for row in results:
    # print('#' * 100)
    # print('#' * 100)
    # print('#' * 100)
    # print('\n\n')
    # # print(row)
    # print(row[0])
    # print("\n\n\n\n")

    row_dict = {name: val for (name, val) in zip(col_names, row)}

    row_dict['chartdate'] = str(row_dict['chartdate'])
    x = 42
    all_row_dicts.append(row_dict)


dataset_file = 'MIMIC_notes.json'
with open(dataset_file, 'w') as f:
    json.dump(all_row_dicts, f)

# all_row_dicts_json = json.dumps(all_row_dicts)


# Close the cursor and connection
cursor.close()
conn.close()
# breakpoint()