import csv
from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '19619890'
API_KEY = 'K9NTpICfXcA5fHTrLgTd08Q5'
SECRET_KEY = '6cQws7gP9b9HdiDef0nqPWNEXSXBw3Bm'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

with open("tk1.csv",encoding='utf-8') as f:
    content = csv.DictReader(f)
    for row in content:
        question = row['question']
        answer = row['answer']
        answerdetail = row['answerdetail']
        length = len(answer)
        detail = answer
        if length<10:
            detail = answerdetail
        print("--------------------------------------------")
        print(question,detail)
        print("keyword: ---> ", client.keyword(question, detail))
        print("--------------------------------------------")
		time.sleep(2)

