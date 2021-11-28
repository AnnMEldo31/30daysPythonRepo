import os
os.environ['MPLCONFIGDIR'] = '/tmp'

from charts import create_chart
import data_storage as ds

IRIS_FILE = "day21_proj/iris.csv"
column_menu = """Enter the column you want to chart from the below given options 

  - 1 for sepal length
  - 2 for sepal width
  - 3 for petal length
  - 4 for petal width

Your selection: """
################################################################
def handle_chart(filename="graph") :

  try: 
    column_no = int(input(column_menu).strip())
    if column_no > 4 or column_no < 1 :
      raise IndexError
  except IndexError:
    print("INVALID INPUT: Out of bounds\n")
    return
  except ValueError: 
    print("INVALID INPUT: Not a number\n")
    return

  column_data = list(map(float, ds.read_column(IRIS_FILE, column_no - 1)))
  column_header = ds.read_column(IRIS_FILE, -1)

  create_chart(column_header, column_data, filename)