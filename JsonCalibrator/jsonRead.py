f = open('전국금연구역표준데이터.json', 'r', encoding='utf-8')
data = f.read()  # .replace("\"\"","\"")
f.close()
print(data[2332000:2332200])
