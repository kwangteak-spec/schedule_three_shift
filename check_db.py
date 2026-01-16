from db_manager import DBManager
import datetime

db = DBManager()
conn = db.get_connection()
cursor = conn.cursor(dictionary=True)

print("--- Table Structure: schedule_exceptions ---")
cursor.execute("DESCRIBE schedule_exceptions")
for row in cursor.fetchall():
    print(row)

print("\n--- Recent EXTRA_HOURS entries ---")
cursor.execute("SELECT * FROM schedule_exceptions WHERE event_type='EXTRA_HOURS'")
for row in cursor.fetchall():
    print(row)

conn.close()
