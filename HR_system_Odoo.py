comp_dict = {
 "emp_1" : {"Name" : "Joanne",
            "Role" : "Banker",
            "Salary" : 8000,
            "Manager" : "Angel",
            "Leave Balance" : 12,
            "Claims Made Successfully" : 0},

 "emp_2" : {"Name" : "Han",
            "Role" : "Banker",
            "Salary" : 8000,
            "Manager" : "Boba",
            "Leave Balance" : 3,
            "Claims Made Successfully" : 0},

 "man_1" : {"Name" : "Angel",
            "Role" : "Manager",
            "Salary" : 12000,
            "Employee" : "Joanne",
            "Employee_id" : "emp_1",
            "Leave Balance" : 12,
            "Claims Made Successfully" : 0},

 "man_2": {"Name": "Boba",
           "Role": "Manager",
           "Salary": 12000,
           "Employee": "Han",
           "Employee_id": "emp_2",
           "Leave Balance": 12,
           "Claims Made Successfully": 0},
}


Count_Of_Leaves_Pending = {
 "emp_1" : 2,
 "emp_2" : 0,
 "man_1" : 0,
 "man_2" : 0
}

Days_Applied_Rejected ={
 "emp_1" : [],
 "emp_2" : [],
 "man_1" : [],
 "man_2" : []
}

Days_Applied_Pending = {
 "emp_1" : ["05/12/2021","06/12/2021"],
 "emp_2" : [],
 "man_1" : [],
 "man_2" : []
}

Days_Applied_Confirmed = {
 "emp_1" : [],
 "emp_2" : ["01/01/2021", "02/01/2021", "03/01/2021", "04/01/2021", "05/01/2021", "06/01/2021", "07/01/2021", "08/01/2021", "09/01/2021"],
 "man_1" : [],
 "man_2" : []
}

Claims_Pending = {
 "emp_1" : {"taxi fare" : 20,
           "medical claims": 15,
           "misc exp" : 0},

 "emp_2" : {"taxi fare" : 20,
           "medical claims": 15,
           "misc exp" : 0},

 "man_1" : {"taxi fare" : 0,
           "medical claims": 0,
           "misc exp" : 0},

 "man_2" : {"taxi fare" : 0,
           "medical claims": 0,
           "misc exp" : 0},
}

Claims_Rejected = {
 "emp_1" : {"taxi fare" : 0,
           "medical claims": 0,
           "misc exp" : 0},

 "emp_2" : {"taxi fare" : 0,
           "medical claims": 0,
           "misc exp" : 0},

 "man_1": {"taxi fare": 0,
            "medical claims": 0,
            "misc exp": 0},

 "man_2": {"taxi fare": 0,
            "medical claims": 0,
            "misc exp": 0},
}
Claims_Confirmed = {
 "emp_1" : {"taxi fare" : 0,
           "medical claims": 0,
           "misc exp" : 0},

 "emp_2" : {"taxi fare" : 0,
           "medical claims": 0,
           "misc exp" : 0},

 "man_1": {"taxi fare": 0,
            "medical claims": 0,
            "misc exp": 0},

 "man_2": {"taxi fare": 0,
            "medical claims": 0,
            "misc exp": 0},
}

# Start program function
def start_program():
    message = "=======Welcome to Odoo, our company's self-help system.======="
    print()
    print("{:^60s}".format(message))
    main_menu()

# Chatbot function
def chatbot_menu():
  if "emp" in inp_username or "man" in inp_username:
      print("Hi " + comp_dict[inp_username]["Name"] + "," + "what would you like to find out today?")
      print("{1} : Read up on company policies")
      print("{2} : Find out about applying for leaves")
      print("{3} : Find out about applying for claims")
      print("{4} : Return to Main Menu")
      print("{0} : Log Out")
      input_chatbot = (input("Please input option 1, 2, 3 or 4 (Key 0 to exit): "))
      while input_chatbot != "1" and input_chatbot != "2" and input_chatbot != "3" and input_chatbot != "4" and input_chatbot != "0":
          print ("Please re-enter...")
          input_chatbot = (input("Please input option 1, 2, 3 or 4: "))
      else:
          if input_chatbot == "1":
              print ("\nAlright, please input the policy number that you would like to read about:")
              print("{1} : Leave Entitlement")
              print("{2} : Workplace Grievances")
              print("{3} : Flexible Work Schedule")
              policychoice = (input("Please input option 1, 2 or 3 (Key 0 to exit):"))
              while policychoice != "1" and policychoice != "2" and policychoice != "3" and policychoice != "0":
                  print ("Please re-enter...")
                  policychoice = (input("Please input option 1, 2 or 3 (Key 0 to exit):"))
              else:
                  if policychoice == "1":
                      print ("\nGenerally, you are entitled to paid annual leave if you have worked with the company for at least 3 months. You may wish to check your leave balance through our company portal or kindly approach your supervisor to find out more.")
                      print ("\nTo read up more about leave eligibility and entitlement, please visit https://www.mom.gov.sg/employment-practices/leave/annual-leave/eligibility-and-entitlement.")
                      print ("\nDo you want to continue chatting?")
                      continue_chat = input("Enter Y/N :").lower()
                      while continue_chat != "y"and continue_chat != "n":
                          print("Enter Y/N only.")
                          continue_chat = input("Enter Y/N :").lower()
                      else:
                          
                          if continue_chat == "y":
                              print()
                              chatbot_menu()
                          elif continue_chat == "n":
                              main_menu()
                  elif policychoice == "2":
                      print ("\nOh dear! If you feel victimised, you can raise your grievances and seek recourse by completing the Grievance/Complaint Lodge Form found on the company’s portal. ")
                      print ("\nYou are advised to document your concerns truthfully. Confidentiality will be maintained. Similarly, you need to ensure that matters discussed are kept confidential as well. ")
                      print ("\nOnce the form is submitted, the grievance process will be initiated and we will get in touch with you. Counselling support is also encouraged for your well-being. ")
                      print ("\nWe hope that you are doing fine!")
                      print ("\nDo you want to continue chatting?")
                      continue_chat = input("Enter Y/N: ").lower()
                      while continue_chat != "y"and continue_chat != "n":
                          print("Enter Y/N only.")
                          continue_chat = input("Enter Y/N: ").lower()
                      else:                          
                          if continue_chat == "y":
                              print()
                              chatbot_menu()
                          elif continue_chat == "n":
                              main_menu()
                  elif policychoice == "3":
                      print ("\nWork-life balance is essential to everyone and we welcome flexible work arrangements. For any arrangement, you would have to first inform your superior to attain approval. Every proposal for a Flexible Work Arrangement will be evaluated on a case-by-case basis. The following 2 types of arrangements is available:")
                      print ("\n1. Pre-approved starting and departure times may vary daily. You can arrive at work and leave at a different time each day, provided the number of hours worked each day remains the same.")
                      print ("\n2.Variations in the length of the workday (e.g., a seven-hour day followed by a ten-hour day). This type of schedule may result in a 'compressed workweek' where the total number of standard weekly hours is completed in fewer than five workdays.")
                      print ("\nDo you want to continue chatting?")
                      continue_chat = input("Enter Y/N: ").lower()
                      while continue_chat != "y"and continue_chat != "n":
                          print("Enter Y/N only.")
                          continue_chat = input("Enter Y/N :").lower()
                      else:                          
                          if continue_chat == "y":
                              print()
                              chatbot_menu()
                          elif continue_chat == "n":
                              main_menu()
                  elif policychoice == "0":
                      print ("Do you want to continue chatting?")
                      continue_chat = input("Enter Y/N: ").lower()
                      while continue_chat != "y"and continue_chat != "n":
                          print("Enter Y/N only.")
                          continue_chat = input("Enter Y/N :").lower()
                      else:                          
                          if continue_chat == "y":
                              print()
                              chatbot_menu()
                          elif continue_chat == "n":
                              main_menu()
          if input_chatbot == "2":
              print ("\nSimply head over to the 'Apply Leaves' portal, input the dates you wish to apply.")
              print ("\nUpon submission, your manager will receive your application and is now pending for approval.")
              print ("\nDo you want to continue chatting?")
              continue_chat = input("Enter Y/N: ").lower()
              while continue_chat != "y"and continue_chat != "n":
                  print("Enter Y/N only.")
                  continue_chat = input("Enter Y/N :").lower()
              else:                          
                  if continue_chat == "y":
                        print()
                        chatbot_menu()
                  elif continue_chat == "n":
                        main_menu()
          if input_chatbot == "3":
              print ("\nSimply head over to the 'Apply Claims' portal, input your claim amount and the category of claim (taxi fare, medical claims, miscellaneous expenditure).")
              print ("\nEvery employee can claim up to a maximum amount of $500 for each category. If your claim amount for the month have exceeded the limit, you will be notified.")
              print ("\nYou may wish to bring over the claim amount to the next month or claim the remaining amount left for the month.")
              print ("\nDo you want to continue chatting?")
              continue_chat = input("Enter Y/N: ").lower()
              while continue_chat != "y"and continue_chat != "n":
                  print("Enter Y/N only.")
                  continue_chat = input("Enter Y/N :").lower()
              else:                          
                  if continue_chat == "y":
                        print()
                        chatbot_menu()
                  elif continue_chat == "n":
                        main_menu()
          if input_chatbot == "4":
              main_menu()
          if input_chatbot == "0":
              print("Thank you and have a nice day!")

# Application for claims
def application_for_claims():
  while True:
      try:
          print("Here is how much you can claim for each category.")
          print("Taxi Fare      :", 500-Claims_Pending[inp_username]["taxi fare"]-Claims_Confirmed[inp_username]["taxi fare"])
          print("Medical Claims :", 500-Claims_Pending[inp_username]["medical claims"]-Claims_Confirmed[inp_username]["medical claims"])
          print("Misc Exp       :", 500-Claims_Pending[inp_username]["misc exp"]-Claims_Confirmed[inp_username]["misc exp"])
          inp_claims = float(input("\nHow much do you want to claim? (Key 0 to exit): "))
          while inp_claims>500:
              print("\nMaximum claim across each category is $500 only.\nPlease re-enter amount.")
              break
          else:              
              while inp_claims != 0 and inp_claims != '0':
                  if inp_claims < 0:
                      print("\nPlease enter positive values only. ")
                      break
                  else:
                      inp_type = input("\nWhich category would you like to claim under (taxi fare, medical claims, misc exp): ").lower()
                      while inp_type not in ['taxi fare', 'medical claims', 'misc exp']:
                          print("\nInvalid category entered.\nPlease re-enter...")
                          inp_type = input("\nWhich category would you like to claim under (taxi fare, medical claims, misc exp): ").lower()
                      else:
                          if (((comp_dict[inp_username]["Claims Made Successfully"] + inp_claims) <= 1500) and ((Claims_Pending[inp_username][inp_type] + inp_claims +Claims_Confirmed[inp_username][inp_type]) <= 500)):
                              Claims_Pending[inp_username][inp_type] += inp_claims
                              print("\nClaim is pending for approval. Thank you.")
                              break
                          elif comp_dict[inp_username]["Claims Made Successfully"] + inp_claims <= 1500:
                              print("\nInvalid claim as claims have exceeded for the month.\n")
                              break
              else:
                  main_menu()
                  break
      except ValueError:
          print("\nWrong input, please enter a value.")
          continue
  else:
      main_menu()

# Validating date
from datetime import datetime, date

def validate(date_text):
   inputdate = ""
   try:
       inputdate = datetime.strptime(date_text, "%d/%m/%Y")
   except ValueError:
       raise ValueError("Incorrect data format, should be DD/MM/YYYY")
   
   if inputdate.date() < date.today():
       raise ValueError("Input date is in the past. Please re-enter. ")
   return
   

# Application for leaves function
def application_for_leaves():
    print("Currently, you can claim up to", str(comp_dict[inp_username]["Leave Balance"] - Count_Of_Leaves_Pending[inp_username]), "days of leave.")
    while True:
       try:
           inp_leaves = int(input("How many days of leaves do you want to apply for? (Key 0 to exit): "))
           if inp_leaves < 0:
                   print("Please enter positive value only. ")
                   return application_for_leaves()           
           elif inp_leaves != 0:               
                if ((comp_dict[inp_username]["Leave Balance"] - Count_Of_Leaves_Pending[inp_username] - inp_leaves) < 0):
                    print("Invalid Entry. Total number of leaves applied EXCEEDS total remaining leave balance and pending leaves")
                    print("Please try again.")
                    return application_for_leaves()
                else:
                    x = 0
                    while x < inp_leaves:
                        inp_date = input("Enter the date you would like to take leave on (DD/MM/YYYY): ")
                        try:
                            validate(inp_date)
                        except ValueError as e:
                            print(e)
                            continue
                        while len(inp_date) != 10:
                            print("Please enter the correct format.")
                            inp_date = input("Enter the date you would like to take leave on (DD/MM/YYYY): ")
                        else: 
                            if ((inp_date in Days_Applied_Pending[inp_username]) or (inp_date in Days_Applied_Confirmed[inp_username])):
                                print("\nThis date has already been entered before. Kindly enter another day instead.")
                                inp_leaves += 1
                            else:
                                Days_Applied_Pending[inp_username].append(inp_date)
                                Count_Of_Leaves_Pending[inp_username] += 1
        
                            x += 1
                    print("\nThese are the leaves pending for approval: ")
                    print(Days_Applied_Pending[inp_username])
                    print("\nThese are the leaves confirmed: ")
                    print(Days_Applied_Confirmed[inp_username])
                    input_continue = input("Would you like to return back to the Main Menu? (Enter Y/N only): ").lower()
                    while input_continue != "y" and input_continue != "n":
                        print("Invalid input (Y/N only): ")
                        input_continue = input("Would you like to return back to the Main Menu? (Enter Yes/No only): ").lower()
                    else:
                        if input_continue == "y":
                            main_menu()
                            break
                        elif input_continue == "n":
                            return application_for_leaves()
           else:
               main_menu()
               break
       except:
           print ("\nWrong input, please enter a value.")
           continue
    else:
      main_menu()

# Approval for claims function
def approval_for_claims():
 print("Here are", comp_dict[inp_username]["Employee"] + "'s", "pending amount for claims")
 emp_id_value = comp_dict[inp_username]["Employee_id"]
 print("Taxi Fare      :", Claims_Pending[emp_id_value]["taxi fare"])
 print("Medical Claims :", Claims_Pending[emp_id_value]["medical claims"])
 print("Misc Expenses  :", Claims_Pending[emp_id_value]["misc exp"])
 print("")
 list = ["taxi fare", "medical claims", "misc exp"]
 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):").lower()
 while (input_category != '0'):
     if input_category in list:
         if (input_category == "taxi fare" and Claims_Pending[emp_id_value]["taxi fare"] >0) :
             input_choice = input("Please key in Y/N: ").lower()
             if input_choice == "y":
                 Claims_Confirmed[emp_id_value]["taxi fare"] += Claims_Pending[emp_id_value]["taxi fare"]
                 comp_dict[emp_id_value]["Claims Made Successfully"] += Claims_Pending[emp_id_value]["taxi fare"]
                 Claims_Pending[emp_id_value]["taxi fare"] = 0
                 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):")
                 continue
             elif (input_choice == "n"):
                 Claims_Rejected[emp_id_value]["taxi fare"] += Claims_Pending[emp_id_value]["taxi fare"]
                 Claims_Pending[emp_id_value]["taxi fare"] = 0
                 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):")
                 continue

         elif (input_category == "medical claims" and Claims_Pending[emp_id_value]["medical claims"] >0):
             input_choice = input("Please key in Y/N: ").lower()
             if input_choice == "y":
                 Claims_Confirmed[emp_id_value]["medical claims"] += Claims_Pending[emp_id_value]["medical claims"]
                 comp_dict[emp_id_value]["Claims Made Successfully"] += Claims_Pending[emp_id_value]["medical claims"]
                 Claims_Pending[emp_id_value]["medical claims"] = 0
                 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):")
                 continue
             elif (input_choice == "n"):
                 Claims_Rejected[emp_id_value]["medical claims"] += Claims_Pending[emp_id_value]["medical claims"]
                 Claims_Pending[emp_id_value]["medical claims"] = 0
                 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):")
                 continue

         elif (input_category == "misc exp" and Claims_Pending[emp_id_value]["misc exp"] >0):
             input_choice = input("Please key in Y/N: ").lower()
             if input_choice == "y":
                 Claims_Confirmed[emp_id_value]["misc exp"] += Claims_Pending[emp_id_value]["misc exp"]
                 comp_dict[emp_id_value]["Claims Made Successfully"] += Claims_Pending[emp_id_value]["misc exp"]
                 Claims_Pending[emp_id_value]["misc exp"] = 0
                 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):")
                 continue
             elif (input_choice == "n"):
                 Claims_Rejected[emp_id_value]["misc exp"] += Claims_Pending[emp_id_value]["misc exp"]
                 Claims_Pending[emp_id_value]["misc exp"] = 0
                 input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):").lower()
                 continue
         else:
             print("There's nothing to claim for this category.")
             input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):").lower()

     else:
         print("Please enter taxi fare, medical claims or misc exp only")
         input_category = input("Select category for approval (taxi fare, medical claims, misc exp)(Key 0 to exit):").lower()
         continue

 else:
     print()
     print("**PENDING**")
     print(comp_dict[inp_username]["Employee"] + "'s " + "Taxi Fare        :", Claims_Pending[emp_id_value]["taxi fare"])
     print(comp_dict[inp_username]["Employee"] + "'s " + "Medical Expenses :",Claims_Pending[emp_id_value]["medical claims"])
     print(comp_dict[inp_username]["Employee"] + "'s " + "Misc Expenses    :", Claims_Pending[emp_id_value]["misc exp"])

     print("\n**CONFIRMED**")
     print(comp_dict[inp_username]["Employee"] + "'s " + "Taxi Fare        :", Claims_Confirmed[emp_id_value]["taxi fare"])
     print(comp_dict[inp_username]["Employee"] + "'s " + "Medical Expenses :",Claims_Confirmed[emp_id_value]["medical claims"])
     print(comp_dict[inp_username]["Employee"] + "'s " + "Misc Expenses    :", Claims_Confirmed[emp_id_value]["misc exp"])

     print("\n**REJECTED**")
     print(comp_dict[inp_username]["Employee"] + "'s " + "Taxi Fare        :", Claims_Rejected[emp_id_value]["taxi fare"])
     print(comp_dict[inp_username]["Employee"] + "'s " + "Medical Expenses :",Claims_Rejected[emp_id_value]["medical claims"])
     print(comp_dict[inp_username]["Employee"] + "'s " + "Misc Expenses    :", Claims_Rejected[emp_id_value]["misc exp"])
     print()
     main_menu()
     
# Approval for leaves for managers function
def approval_for_leaves():
  print("Here are", comp_dict[inp_username]["Employee"] + "'s", "pending leaves:")
  emp_id_value = comp_dict[inp_username]["Employee_id"]
  print("Date of pending leaves:", Days_Applied_Pending[emp_id_value])
  print()
  while True:
      choice = input("Approve all of the pending leaves? (Please key in Y/N only)(Key 0 to exit): ").lower()
      if choice == "n":
          specific_date = input("Reject all of the pending leaves? (Please key in Y/N only): ")
          if specific_date == "n":
              while True:
                  date_reject = input("Which date you want to reject?(dd/mm/yyyy)(Key 0 to exit): ")
                  if date_reject in Days_Applied_Pending[emp_id_value]:
                      Days_Applied_Pending[emp_id_value].remove(date_reject)
                      Days_Applied_Rejected[emp_id_value].append(date_reject)
                      print(date_reject, "is being rejected.")
                      print()
                      print("CURRENT PENDING DATE OF LEAVES")
                      print(comp_dict[inp_username]["Employee"] + "'s " + "Pending date of leaves are: ",Days_Applied_Pending[emp_id_value])
                      print("\nCONFIRMED DATE OF LEAVES")
                      print(comp_dict[inp_username]["Employee"] + "'s " + "Confirmed date of leaves are: ",Days_Applied_Confirmed[emp_id_value])
                      print("\nREJECTED DATE OF LEAVES")
                      print(comp_dict[inp_username]["Employee"] + "'s " + "Rejected date of leaves are: ",Days_Applied_Rejected[emp_id_value])
                      print("\nTOTAL NUMBER OF LEAVES")
                      print(comp_dict[inp_username]["Employee"] + "'s " + "Total number of leaves are: ",len(Days_Applied_Confirmed[emp_id_value]))
                      continue
                  elif date_reject == "0":
                      break 
                  else:
                      print("No such date")
                      continue
          elif specific_date == "y":
              Days_Applied_Rejected[emp_id_value] += Days_Applied_Pending[emp_id_value]
              Days_Applied_Confirmed[emp_id_value].clear()
              Days_Applied_Pending[emp_id_value].clear()
              print("All of the pending leaves have been rejected.")
              print()
              print("\nCURRENT PENDING DATE OF LEAVES")
              print(comp_dict[inp_username]["Employee"] + "'s " + "Pending date of leaves are: ",Days_Applied_Pending[emp_id_value])
              print("\nCONFIRMED DATE OF LEAVES")
              print(comp_dict[inp_username]["Employee"] + "'s " + "Confirmed date of leaves are: ",Days_Applied_Confirmed[emp_id_value])
              print("\nREJECTED DATE OF LEAVES")
              print(comp_dict[inp_username]["Employee"] + "'s " + "Rejected date of leaves are: ",Days_Applied_Rejected[emp_id_value])
              print("\nTOTAL NUMBER OF LEAVES")
              print(comp_dict[inp_username]["Employee"] + "'s " + "Total number of leaves are: ",len(Days_Applied_Confirmed[emp_id_value]))
              print()
              main_menu()
              break
      elif choice == "y":
          Days_Applied_Confirmed[emp_id_value] += Days_Applied_Pending[emp_id_value]
          Days_Applied_Rejected[emp_id_value].clear()
          Days_Applied_Pending[emp_id_value].clear()
          print("All of the pending leaves have been confirmed successfully.")
          print()
          print("CURRENT PENDING DATE OF LEAVES")
          print(comp_dict[inp_username]["Employee"] + "'s " + "Pending date of leaves are: ",Days_Applied_Pending[emp_id_value])
          print("\nCONFIRMED DATE OF LEAVES")
          print(comp_dict[inp_username]["Employee"] + "'s " + "Confirmed date of leaves are: ",Days_Applied_Confirmed[emp_id_value])
          print("\nREJECTED DATE OF LEAVES")
          print(comp_dict[inp_username]["Employee"] + "'s " + "Rejected date of leaves are: ",Days_Applied_Rejected[emp_id_value])
          print("\nTOTAL NUMBER OF LEAVES")
          print(comp_dict[inp_username]["Employee"] + "'s " + "Total number of leaves are: ",len(Days_Applied_Confirmed[emp_id_value]))
          print()
          main_menu()
          break
      elif choice == "0":
          return start_program()
          break
      else:
          print("Please key Y/N only: ")
          continue
  
# Main menu function
def main_menu():
  if "emp" in inp_username:
     print()
     print("Hi " + comp_dict[inp_username]["Name"] + "," + "what would you like to do today?")
     print("{1} : Apply for Claims")
     print("{2} : Apply for Leaves")
     print("{3} : HR Chatbot")
     print("{0} : Log Out")
     input_choice = input("Enter your choice (Key 0 to exit): ")
     while input_choice != "1" and input_choice != "2" and input_choice != "3"  and input_choice != "0":
         print("Invalid input, please re-enter.")
         input_choice = input("Enter your choice (Key 0 to exit): ")
     else:
         if input_choice == "1":              #APPLICATION FOR CLAIMS
             application_for_claims()
         elif input_choice == "2":             #APPLICATION FOR LEAVES
             application_for_leaves()
         elif input_choice == "3":
             print()
             chatbot_menu()
         else:
             print("Thank you and have a nice day!")


  elif "man" in inp_username:
      print("\nHi " + comp_dict[inp_username]["Name"] + "," + "what would you like to do today?")
      print("{1} : Approve Claims")
      print("{2} : Approve Leaves")
      print("{3} : Apply for Claims")
      print("{4} : Apply for Leaves")
      print("{5} : HR Chatbot")
      print("{0} : Log Out")
      input_choice = (input("Enter your choice (Key 0 to exit): "))
      while input_choice != "1" and input_choice != "2" and input_choice != "3"  and input_choice != "4" and input_choice != "5" and input_choice != "0":
         print("Invalid input, please re-enter.")
         input_choice = input("Enter your choice (Key 0 to exit): ")
      else:   
          if input_choice == "1":  # Approval for Claims
              approval_for_claims()
          elif input_choice == "2":  # Approval for leaves
              approval_for_leaves()
          elif input_choice == "3":
              application_for_claims()
          elif input_choice == "4":
              application_for_leaves()
          elif input_choice == "5":
              chatbot_menu()
          else: 
              print("Thank you and have a nice day!")

# This is where the program starts
while True:
   try:
       inp_username = input("Enter your id to begin: ")
       while inp_username not in comp_dict:
           print("Invalid entry. Please try again.")
           inp_username = input("Enter your id to begin: ")
       start_program()
   except:
       print("Invalid entry. Please try again.")
       inp_username = input("Enter your id to begin: ")
       start_program()
