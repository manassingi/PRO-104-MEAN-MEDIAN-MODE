import csv
with open("mydata.csv",newline="")as f:

  reader=csv.reader(f)
  file_data= list(reader)
file_data.pop(0)
newdata=[]
num= file_data[i]
for i in range(len(file_data)):
  num= file_data[i][1]
  newdata.append(float(num))
  