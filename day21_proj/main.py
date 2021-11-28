import handle_chart as hc

USER_MENU = '''Please select one of the below given options:

- Enter 'c' to chart a new graph.
- Enter 'd' to chart a new graph with a name
- Enter 'q' to quit.

Your selection: '''

while True :
  choice = input(USER_MENU).strip().lower()

  if choice == 'c' :
    hc.handle_chart()
  elif choice == 'd':
    file_name = input("Enter the filename: ")
    hc.handle_chart(file_name)
  elif choice == 'q' :
    break
  else :
    print("INVALID INPUT: Not one of the choices\n")