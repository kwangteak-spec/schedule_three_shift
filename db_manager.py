import mysql.connector

class DBManager:
    def __init__(self):
        self.config = {
            'host': 'localhost',
            'user': 'root',             # 본인의 MySQL ID 입력
            'password': 'mysqlbig',  # MySQL 설치 시 설정한 비밀번호 입력
            'database': 'work_db'       # 앞에서 생성한 데이터베이스 이름
        }
    def get_connection(self):
        return mysql.connector.connect(**self.config)

    def fetch_staff_list(self):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM staff")
        result = cursor.fetchall()
        conn.close()
        return result

    def update_exception(self, name, date_str, exc_type, value=None, clear_types=None):
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Clear specific conflicting types if provided
        if clear_types:
            for t in clear_types:
                cursor.execute("DELETE FROM schedule_exceptions WHERE staff_name=%s AND event_date=%s AND event_type=%s", (name, date_str, t))
        
        # Simple cleanup before insert to avoid duplicates for SAME staff/date/type
        cursor.execute("DELETE FROM schedule_exceptions WHERE staff_name=%s AND event_date=%s AND event_type=%s", (name, date_str, exc_type))
        
        query = "INSERT INTO schedule_exceptions (staff_name, event_date, event_type, description) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, date_str, exc_type, str(value) if value else None))
        conn.commit()
        conn.close()

    def delete_exception(self, name, date_str, exc_type):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM schedule_exceptions WHERE staff_name=%s AND event_date=%s AND event_type=%s"
        cursor.execute(query, (name, date_str, exc_type))
        conn.commit()
        conn.close()

    def fetch_schedule_exceptions(self, year, month):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        # Fetch exceptions for the given month
        start_date = f"{year}-{month:02d}-01"
        # approximate end date handling
        if month == 12:
            end_date = f"{year+1}-01-01"
        else:
            end_date = f"{year}-{month+1:02d}-01"
            
        query = "SELECT * FROM schedule_exceptions WHERE event_date >= %s AND event_date < %s"
        cursor.execute(query, (start_date, end_date))
        result = cursor.fetchall()
        conn.close()
        return result

    def add_staff(self, name, shift_type, off_days):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO staff (name, shift_type, off_days) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, shift_type, off_days))
        conn.commit()
        conn.close()

    def update_staff(self, original_name, name, shift_type, off_days):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "UPDATE staff SET name=%s, shift_type=%s, off_days=%s WHERE name=%s"
        cursor.execute(query, (name, shift_type, off_days, original_name))
        conn.commit()
        conn.close()

    def delete_staff(self, name):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM staff WHERE name=%s"
        cursor.execute(query, (name,))
        conn.commit()
        conn.close()