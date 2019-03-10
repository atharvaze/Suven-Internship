import pandas as pd

unsorted=pd.read_csv("sample.csv")

print("The existing data base is\n",unsorted)

ch=int(input("\nChoose the row you want to be sorted\n1-Name\n2-Age\n3-GPA\n4-Salary\nEnter your choice= "))

if(ch==1):
	sorted1=unsorted.sort_values(by=['Name'])
	sorted1.to_csv("sorted.csv")
	print("Above Database has been Sorted and saved")
	sorted=pd.read_csv("sorted.csv")
	print("The sorted data base is\n",sorted)

elif(ch==2):
	sorted1=unsorted.sort_values(by=['Age'])
	sorted1.to_csv("sorted.csv")
	print("Above Database has been Sorted and saved")
	sorted=pd.read_csv("sorted.csv")
	print("The sorted data base is\n",sorted)
elif(ch==3):
	sorted1=unsorted.sort_values(by=['GPA'])
	sorted1.to_csv("sorted.csv")
	print("Above Database has been Sorted and saved")
	sorted=pd.read_csv("sorted.csv")
	print("The sorted data base is\n",sorted)
elif(ch==4):
	sorted1=unsorted.sort_values(by=['Salary'])
	sorted1.to_csv("sorted.csv")
	print("Above Database has been Sorted and saved")
	sorted=pd.read_csv("sorted.csv")
	print("The sorted data base is\n",sorted)

else:
	print("Invalid Input!\nTry Again")
