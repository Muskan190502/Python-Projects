# Name - MUSKAN YADAV
# Roll No - 2020087

'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries. You may only import a2.py.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the function when you implement it.

- Do not create any global variables in this module.
'''


# Write the code here for creating an interactive program.


import a2 
import json

list_queries={'read_data_from_file':1,'filter_by_first_name':2,'filter_by_last_name':3,'filter_by_full_name':4,'filter_by_age_range':5,'count_by_gender':6,'filter_by_address':7,'find_alumni':8,'find_topper_of_each_institute':9,'find_blood_donors':10,'get_common_friends':11,'is_related':12,'delete_by_id':13,'add_friend':14,'remove_friend':15,'add_education':16}
def main():
	
	print('\n\t\t\t\tHello!\n')
	print('\t\t\tHere is the list of queries.\n')
	print('\t\tQuery Number \t |'+'\t\t\tQuery Name')
	print('-'*80)
	for i in list_queries.keys():
		print('\t\t'+str(list_queries[i])+'\t\t |'+'\t\t\t'+str(i))

	
	while True :
		
		x=int(input('Enter the Query Code(Enter -1 to stop):'))
		
		if x in range(1,17):
			if x==1:
				
				records=a2.read_data_from_file()
				print(records)
			if x==2:
				first_name=input('Enter first name: ')
				print('The list of IDs of persons having first name as '+first_name+' is:') 
				print(a2.filter_by_first_name(records,first_name))
				a=a2.filter_by_first_name(records,first_name)
			if x==3:
				last_name=input('Enter last name: ')
				print('The list of IDs of persons having last name as '+last_name+' is:')
				print(a2.filter_by_last_name(records,last_name))
				b=a2.filter_by_last_name(records,last_name)
			if x==4:
				full_name=input('Enter full name: ')
				print('The list of IDs of persons having full name as '+full_name+' is:')
				print(a2.filter_by_full_name(records,full_name))
				c=a2.filter_by_full_name(records,full_name)
			if x==5:
				min_age=int(input('Enter the minimum age: '))
				max_age=int(input('Enter the maximum age:'))
				print('The list of IDs of person having their age in the range: '+str(min_age)+'-'+str(max_age)+' : ')
				print(a2.filter_by_age_range(records,min_age,max_age))
				d=a2.filter_by_age_range(records,min_age,max_age)
			if x==6:
				print('The total number of males and females in the records are: ')
				print(a2.count_by_gender(records))
				e=a2.count_by_gender(records)
			if x==7 :
				address1={}
				address1['house_no']=input('Enter the house number: ')
				address1['block']=input('Enter the block: ')
				address1['town']=input('Enter the town: ')
				address1['city']=input('Enter the city: ')
				address1['state']=input('Enter the state: ')
				address1['pincode']=input('Enter the pincode: ')
				if address1['house_no']=='':
					del address1['house_no']
				if address1['block']=='':
					del address1['block']
				if address1['town']=='':
					del address1['town']
				if address1['city']=='':
					del address1['city']
				if address1['state']=='':
					del address1['state']
				if address1['pincode']=='':
					del address1['pincode']

				print('The first and last names of people having the given address respectively are: ')
				print(a2.filter_by_address(records,address1))
				f=a2.filter_by_address(records,address1)
			if x==8 :
				institute_name=input('Enter the name of institute: ')
				print('The details of the alumni of '+ institute_name +' institute are:  ')
				print(a2.find_alumni(records,institute_name))
				g=a2.find_alumni(records,institute_name)
			if x==9:
				print('The  list of toppers is: ')
				print(a2.find_topper_of_each_institute(records))
				h=a2.find_topper_of_each_institute(records)
			if x==10:
				receiver_person_id=int(input('Enter the receiver persons id: '))
				print('The contact details of the potential donors are:  ')
				print(a2.find_blood_donors(records,receiver_person_id))
				j=a2.find_blood_donors(records,receiver_person_id)
			if x==11:
				list_of_ids=input('Please enter space separated IDs:  ')
				list_of_ids1=list_of_ids.split()
				print('The list of common friends: ')
				print(a2.get_common_friends(records,list_of_ids1))
				k=a2.get_common_friends(records,list_of_ids1)
			if x==12:
				print(a2.is_related)
			if x==13:
				person_id=int(input('Enter the person ID: '))
				print('The new updated records are: ')
				print(a2.delete_by_id(records,person_id))
				records=a2.delete_by_id(records,person_id)
			if x==14:
				person_id1=int(input('Enter the person ID: '))
				friend_id=int(input('Enter the friend ID: '))
				print('The new updated records are: ')
				print(a2.add_friend(records,person_id1,friend_id))
				records= a2.add_friend(records,person_id1,friend_id)
			if x==15:
				person_id2=int(input('Enter the person ID: '))
				friend_id2=int(input('Enter the friend ID: '))
				print('The new updated records are: ')
				print(a2.remove_friend(records,person_id2,friend_id2))
				records=a2.remove_friend(records,person_id2,friend_id2)
			if x==16:
				person_id=int(input('Enter the person ID: '))
				institute_name= input('Enter the name of the institute: ')
				ongoing1=input('Enter ongoing status: ')
				if ongoing1.lower()=='False'.lower():
					ongoing=False
					percentage=float(input('Enter the percentage: '))
					print('The new updated records are: ')
					print(a2.add_education(records,person_id,institute_name,ongoing,percentage))
					records=a2.add_education(records,person_id,institute_name,ongoing,percentage)
				elif ongoing1.lower()=='True'.lower():
					ongoing=True
					percentage=0
					print('The new updated records are: ')
					print(a2.add_education(records,person_id,institute_name,ongoing,percentage))
					records=a2.add_education(records,person_id,institute_name,ongoing,percentage)

		elif x== -1:
			break
		else:
			print('Enter valid code.Try again.')
	print('Thanks.\nNice to meet you.')


main()










		 
	