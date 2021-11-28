import csv

def read_column(file_name, number):
  column_data = []
  
  with open(file_name, "r") as iris:
    for line in csv.reader(iris) :
      column_data.append(line[number])
    
    column_data.pop(0)

  return column_data