#Student Database
#*********************************************************************
**********
#*********************************************************************
**********
#Helper functions
#*********************************************************************
**********
def input_records():
 '''
 Inputs from user and returns a list of records.
 Each record is itself a list
 '''
 print('\nEnter nothing in name field to exit')
 rec_lst=[]
 while True:
 name=input('\nEnter student\'s name: ')
 if name=='':
 break
 roll=input('Enter roll number: ')
 marks=input('Enter sessional marks: ')
 rec_lst+=[[name,roll,marks]]
 return rec_lst
def print_records(rec_lst):
 '''
 Prints all records on screen.
 '''
 if rec_lst==[]:
 print('\nNo record found.')
 return
 print('\nS.No. Name ',' Roll No. ',' Marks\n')
 count=0
 for record in rec_lst:
 count+=1
 print(f'{count:3} {record[0]:20} {record[1]:6}
{record[2]:3}')
def save_records(rec_lst,mode):
 '''
 Writes record(s) to the file StudentDB.txt
 '''
 with open('StudentDB.txt',mode) as f:
 for record in rec_lst:
 f.write(str(record)+'\n')
def read_all_records():
 '''
 Reads and returns as list all records from the file StudentDB.txt.
 Each record is itself a list.
 '''
 with open('StudentDB.txt','a+') as f:
 f.seek(0)
 rec_lst=[]
 for record in f:
 rec_lst+=[eval(record.strip())]
 return rec_lst
def search_rec_lst(fd, val):
 '''
 Searches a record on field fd containing the string val.
 fd=0, searches a name,
 fd=1, searches a roll number.
 Returns the record(s) as a list.
 '''
 with open('StudentDB.txt','a+') as f:
 rec_lst=[]
 f.seek(0)
 for record in f:
 rec=eval(record.strip())
 if val in rec[fd]:
 rec_lst+=[rec]
 return rec_lst
def search_rec_index(fd, val):
 '''
 Searches a record on field fd containing the string val.
 fd=0, searches a name,
 fd=1, searches a roll number
 returns the index of the first occurence of the searched record.
 '''
 with open('StudentDB.txt','a+') as f:
 rec_lst=[]
 f.seek(0)
 index=0
 for record in f:
 rec=eval(record.strip())
 if val in rec[fd]:
 return index
 index+=1
#*********************************************************************
**********
#Main functions
#*********************************************************************
**********
def print_menu():
 '''
 Prints the menu.
 '''
 print('NED University of Engineering & Technology')
 print('Department of Computer & Information Systems Engineering')
 print('FE - Batch 2019')
 print('CS-115 Computer Programming')
 print('Sessional Marks')

print('**********************************************************\n')
 print('1. Enter records')
 print('2. View records')
 print('3. Search record')
 print('4. Delete records')
 print('5. Sort records')
 print('6. Result statistics')
 print('7. Exit')
def enter_records():
 '''
 Allows user to enter one or more new record(s).
 '''
 rec_lst=input_records()
 choice=input('\nPress \'y\' to save record(s): ')
 if choice=='y':
 save_records(rec_lst,'a')
 print('Records saved successfully!\n')
def view_records():
 '''
 Allows user to view all records.
 '''
 rec_lst=read_all_records()
 print_records(rec_lst)
def search_records():
 '''
 Allows user to search for a record.
 A record can be searched on name or roll number.
 It prints all records containing the searched value.
 '''
 choice=input('Press 1 to search by name; 2 to search by roll
number: ')
 if choice=='1':
 value=input('Enter name to be searched: ')
 rec_lst=search_rec_lst(0,value)
 elif choice=='2':
 value=input('Enter roll no. to be searched: ')
 rec_lst=search_rec_lst(1,value)
def delete_records():
 '''
 Allows user to delete a record.
 A record can be searched on name or roll number.
 It deletes the first occurrence of the record containing the
value.
 '''
 choice=input('Press 1 to search by name; 2 to search by roll
number: ')
 if choice=='1':
 value=input('Enter name to be searched: ')
 index=search_rec_index(0,value)
 elif choice=='2':
 value=input('Enter roll no. to be searched: ')
 index=search_rec_index(1,value)
 rec_lst=read_all_records()
 rec_lst.pop(index)
 save_records(rec_lst,'w')
 print('\nRecord deleted successfully\n')
def sort_records():
 '''
 Allows user to sort records.
 Records can be sorted on name or roll number or marks.
 The sorted list can be saved if the user opts for it,
 overwriting the original file.
 '''
 print('Select a field to sort records.')
 choice=input('Press 1 to sort by names; 2 to sort by roll numbers,
3 to sort by marks: ')
 rec_lst=read_all_records()
 if choice=='2' or choice=='3':
 rec_lst.sort(key=lambda x:int(x[int(choice)-1]))
 else:
 rec_lst.sort(key=lambda x:x[int(choice)-1])
 print_records(rec_lst)
 choice=input('\nPress \'y\' to save changes: ')
 if choice=='y':
 save_records(rec_lst,'w')
 print('Changes saved successsfully!\n')

def print_result_stats():
 '''
 Prints average, maximum and minimum marks.
 Also prints standard deviation.
 '''
 #Find and print the following
 print('\nMinimum marks: ')
 print('Maximum marks: ')
 print('Class average: ')
 print('Standard deviation: ')
while True:
 print_menu()
 choice=input('\nSelect an option/number: ')
 if choice=='7':
 break
 elif choice=='1':
 enter_records()
 elif choice=='2':
 view_records()
 elif choice=='3':
 search_records()
 elif choice=='4':
 delete_records()
 elif choice=='5':
 sort_records()
 elif choice=='6':
 print_result_stats()
 else:
 print('Enter valid choice')
 y=input('\nPress \'y\' to continue and any other key to exit: ')
 if y!='y':
 break
