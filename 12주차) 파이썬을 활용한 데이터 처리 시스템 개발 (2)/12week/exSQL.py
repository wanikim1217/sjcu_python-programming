import sqlite3
import sys

'''
CREATE TABLE data (
    id INTEGER AUTO_INCREMENT,
    time datetime DEFAULT current_timestamp,
    kor INTEGER,
    math INTEGER,
    grade char(1), 
    PRIMARY KEY(id)
)
'''

# 데이터베이스 파일명
DATABASE_FILE = "grade.db"

# 데이터베이스 연결 후 Cursor 획득
sqlite3 = sqlite3.connect(DATABASE_FILE)

# 테이블 생성
try:
    cursor = sqlite3.cursor()
    cursor.execute("DROP TABLE IF EXISTS data")
    cursor.execute("CREATE TABLE data (id INTEGER PRIMARY KEY AUTOINCREMENT, time datetime DEFAULT current_timestamp, kor INTEGER, math INTEGER, grade char(1))")
    sqlite3.commit()
except:
    sqlite3.rollback()
    sqlite3.close()
    sys.exit("테이블 생성 실패")

# CSV 파일을 읽어서 데이터베이스에 기록
fp = open("grade.csv", "r", encoding="utf-8")
if not fp:
    sys.exit("파일 읽기 실패")
    
fp.readline() # 첫 줄은 읽기만 하고 무시
for line in fp:
    line = line.strip()
    kor, math, grade = line.split(",")
    try:
        cursor.execute("INSERT INTO data (kor, math, grade) VALUES (?, ?, ?)", (kor, math, grade))
    except:
        sqlite3.rollback()
        sqlite3.close()
        sys.exit("데이터 삽입 실패")

sqlite3.commit()
fp.close()

# 학점(grade)이 A인 데이터를 모두 조회
try:
    cursor = sqlite3.cursor()
    cursor.execute("SELECT * FROM data WHERE grade = 'A' and kor > 95 and math > 95")
    rows = cursor.fetchall()
    print("A인 데이터 개수: {0}".format(len(rows)))
    print(rows)
except:
    sqlite3.rollback()
    sqlite3.close()
    sys.exit("데이터 조회 실패")

# 데이터베이스 연결 종료
sqlite3.close()
print("Done")