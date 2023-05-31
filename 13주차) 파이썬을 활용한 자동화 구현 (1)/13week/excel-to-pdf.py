import win32com.client

# 엑셀 프로그램 열기 (실행과정 보이기)
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

# 파일 열기, sheet 선택
wb = excel.Workbooks.Open('C:\\_Lecture\\SJCU\\sjcu-python\\grade.xlsx')
ws = wb.Sheets('New-Sheet')
ws.Select()

# PDF로 저장 (type을 0으로 설정)
ws.ExportAsFixedFormat(0, 'C:\\_Lecture\\SJCU\\sjcu-python\\grade.pdf')

wb.Close()
excel.Quit()