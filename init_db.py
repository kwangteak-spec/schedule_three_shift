import mysql.connector

def init_db():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'mysqlbig'
    }
    
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS work_db")
        cursor.execute("USE work_db")
        
        # Create staff table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS staff (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                shift_type VARCHAR(10) NOT NULL,
                off_days VARCHAR(100)
            )
        """)
        
        # Create schedule_exceptions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schedule_exceptions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                staff_name VARCHAR(100) NOT NULL,
                event_date DATE NOT NULL,
                event_type VARCHAR(50) NOT NULL,
                description TEXT
            )
        """)
        
        # Sample staff members (7 people)
        sample_staff = [
            ('김철수', 'A', '6,0'), # Sat, Sun (0=Mon, 6=Sun in Python logic, but app.py uses (calendar.weekday + 1) % 7)
            ('이영희', 'B', '6,0'), # Let's assume 0=Sun, 6=Sat for off_days as commonly used
            ('박지민', 'C', ''),
            ('최수연', 'N', '6,0'),
            ('정진우', 'A', '6,0'),
            ('강다현', 'B', '6,0'),
            ('윤성호', 'C', '')
        ]
        
        # Clear existing staff to avoid duplicates during init
        cursor.execute("DELETE FROM staff")
        
        cursor.executemany(
            "INSERT INTO staff (name, shift_type, off_days) VALUES (%s, %s, %s)",
            sample_staff
        )
        
        conn.commit()
        print("Database 'work_db' initialized successfully with 7 sample staff members.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    init_db()
