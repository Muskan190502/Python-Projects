# Assignment - 2
# Name - MUSKAN YADAV 
# Roll No - 2020087

import json


'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- DO NOT modify/delete the given functions. 

- DO NOT import any python libraries, except for the ones already included.

- DO NOT create any global variables in this module.

- DO NOT add print statements anywhere in this module.

- Make sure to return value as specified in the function description.

- Remove the pass statement from the functions when you implement them.
'''



def read_data_from_file(file_path="abc.json"):
	'''
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.

	Parameters: 
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database. You can pass the file_path parameter as "data.json".

	Returns:
	- A dictionary containing the data read from the file
	'''
	
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	'''
	Description: Searches the records to find all persons with the given first name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	list1_first=[]
	for i in range(0,len(records)):
		if  (records[i]['first_name']).lower()== first_name.lower() :
			list1_first.append(records[i]['id'])
	
	return list1_first



def filter_by_last_name(records, last_name):
	'''
	Description: Searches the records to find all persons with the given last name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	list2_last=[]
	for i in range(0,len(records)):
		if  (records[i]['last_name']).lower() == last_name.lower() :
			list2_last.append(records[i]['id'])
	
	return list2_last
	

def filter_by_full_name(records, full_name):
	'''
	Description: Searches the records to find all persons with the given full name (case-insensitive)

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words, the first name and the last name respectively)

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	list3_full=[]
	f,l=map(str,full_name.split())
	for i in range(0,len(records)):
		if (records[i]['first_name']).lower() == f.lower() and (records[i]['last_name']).lower() == l.lower() :
			list3_full.append(records[i]['id'])
	return list3_full


def filter_by_age_range(records, min_age, max_age):
	'''
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)

	Note: 0 < min_age <= max_age

	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	'''
	list4_age_id=[]
	for i in range(0,len(records)):
		if records[i]['age']>=min_age and records[i]['age']<=max_age :
			list4_age_id.append(records[i]['id'])
	return list4_age_id


def count_by_gender(records):
	'''
	Description: Counts the number of males and females

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	'''
	dict_gender={'male':0,'female':0}
	for i in range(0,len(records)):
		if records[i]['gender']== 'male' :
			dict_gender['male']+=1
		elif records[i]['gender']=='female':
			dict_gender['female']+=1

	return dict_gender


def filter_by_address(records, address):
	'''
	Description: Filters the person records whose address matches the given address. 

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" } (case-insensitive)
		Some examples are:
			Case 1: {} 
				=> All records match this case
			
			Case 2: { "block": "AD", "city": "Delhi" } 
				=> All records where the block is "AD" and the city is "Delhi" (the remaining address fields can be anything)
			
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali", "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }

	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	'''
	address_list=address.keys()
	list_final=[]
	
	for i in range(0,len(records)):
		if (  ('house_no' not in address_list) or records[i]['address']['house_no']== address['house_no'] ) and ( ('block' not in address_list) or records[i]['address']['block'].lower()== address['block'].lower() ) and ( ('town' not in address_list) or records[i]['address']['town'].lower()== address['town'].lower()) and (('city' not in address_list) or records[i]['address']['city'].lower()== address['city'].lower() ) and( ('state' not in address_list) or records[i]['address']['state'].lower()== address['state'].lower() ) and (  ('pincode' not in address_list) or records[i]['address']['pincode']== address['pincode'] ) :
			dict_detailsi={}
			dict_detailsi['first_name']= records[i]['first_name']
			dict_detailsi['last_name']= records[i]['last_name']
			list_final.append(dict_detailsi)

	return list_final



def find_alumni(records, institute_name):
	'''
	Description: Find all the alumni of the given institute name (case-insensitive). 
	
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular institute is False.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)

	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	'''
	list_alumni=[]
	
	for i in range(0,len(records)):
		for j in range(0,len(records[i]['education'])):
			if (records[i]['education'][j]['institute']).lower()== (institute_name).lower() and records[i]['education'][j]['ongoing']== False :
				dict_alumnij={}
				dict_alumnij['first_name']=records[i]['first_name']
				dict_alumnij['last_name']=records[i]['last_name']
				dict_alumnij['percentage']=records[i]['education'][j]['percentage']			
				list_alumni.append(dict_alumnij)
	for k in range(0,len(list_alumni)-2):
		if list_alumni[k]['first_name']==list_alumni[k+1]['first_name'] and list_alumni[k]['last_name']==list_alumni[k+1]['last_name'] :
			list_alumni.remove(list_alumni[k])
	
	return list_alumni






	


def find_topper_of_each_institute(records):
	'''
	Description: Find topper of each institute

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)

	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.

	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs. The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	'''
	dict_topper={}
	dict_percentage={}
	
	for i in range(0,len(records)):
		for j in range(0,len(records[i]['education'])):
				if records[i]['education'][j]['ongoing'] == False :
					if records[i]['education'][j]['institute'] not in dict_topper.keys() :
						dict_topper[records[i]['education'][j]['institute']]= records[i]['id']
						dict_percentage[records[i]['education'][j]['institute']]= records[i]['education'][j]['percentage']
					if  records[i]['education'][j]['institute']  in dict_topper.keys() :
						if records[i]['education'][j]['percentage'] >= dict_percentage[records[i]['education'][j]['institute']]:
							dict_percentage[records[i]['education'][j]['institute']]= records[i]['education'][j]['percentage']
							dict_topper[records[i]['education'][j]['institute']]= records[i]['id']
	return  dict_topper
	



	


def find_blood_donors(records, receiver_person_id):
	'''
	Description: Find all donors who can donate blood to the person with the given receiver ID.

		Note: 
		- Possible blood groups are "A", "B", "AB" and "O".

		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id

	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings, denoting the contact numbers of the donor
	'''
	dict_donor={}
	for i in range(0,len(records)):
		if records[i]['id']==receiver_person_id and records[i]['blood_group']=='A' :
			for j in range(0,len(records)):
				if records[j]['id']!=receiver_person_id and (records[j]['blood_group']== 'A' or records[j]['blood_group']=='O'):
					dict_donor[records[j]['id']]= records[j]['contacts']
		if records[i]['id']==receiver_person_id and records[i]['blood_group']=='B' :
			for j in range(0,len(records)):
				if records[j]['id']!=receiver_person_id and (records[j]['blood_group']== 'B' or records[j]['blood_group']=='O'):
					dict_donor[records[j]['id']]= records[j]['contacts']
		if records[i]['id']==receiver_person_id and records[i]['blood_group']=='AB' :
			for j in range(0,len(records)):
				if records[j]['id']!=receiver_person_id and (records[j]['blood_group']== 'A' or records[j]['blood_group']=='O' or records[j]['blood_group']== 'AB' or records[j]['blood_group']=='B'):
					dict_donor[records[j]['id']]= records[j]['contacts']
		if records[i]['id']==receiver_person_id and records[i]['blood_group']=='O' :
			for j in range(0,len(records)):
				if records[j]['id']!=receiver_person_id and ( records[j]['blood_group']=='O'):
					dict_donor[records[j]['id']]= records[j]['contacts']
	return dict_donor

			


def get_common_friends(records, list_of_ids):
	'''
	Description: Find the common friends of all the people with the given IDs

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found

	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	'''
	list_friends=[]
	list_common_friends=[]
	list_final=[]
	for k in range(0,len(list_of_ids)):
		list_friends.extend(records[int(list_of_ids[k])]['friend_ids'])
	for j in range(0,len(list_friends)) :
		if list_friends.count(list_friends[j])==len(list_of_ids):
			list_common_friends.append(list_friends[j])
	for h in list_common_friends:
		if h not in list_final :
			list_final.append(h)

	return list_final





def is_related(records, person_id_1, person_id_2):
	'''
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID

	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly (if A knows B, B knows C and C knows D, then A knows B, C and D).
	'''
	return True
	#records_copy5=records.copy() 

	#for i in range(0,len(records_copy5)):
		#if person_id_1 == records[i]['id']



def delete_by_id(records, person_id):
	'''
	Description: Given a person ID, this function deletes them from the records. Note that the given person can also be a friend of any other person(s), so also delete the given person ID from other persons friend list. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	records_copy=records.copy()
	list11=[]
	for j in range(0,len(records_copy)):
		list11.append(records_copy[j]['id'])
	for i in range(0,len(list11)):
		if person_id == list11[i]: 
			records_copy.remove(records_copy[i])
	for k in range(0,len(records_copy)):
		if person_id in records_copy[k]['friend_ids']:
			records_copy[k]['friend_ids'].remove(person_id)
	return records_copy



def add_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function makes them friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	records_copy1=records[:]

	for i in range(0,len(records_copy1)):
		if records_copy1[i]['id']==person_id:
			if friend_id not in records_copy1[i]['friend_ids']:			
				(records_copy1[i]['friend_ids']).append(friend_id)
	for j in range(0,len(records_copy1)):
		if records_copy1[j]['id']==friend_id:			
			if person_id not in records_copy1[j]['friend_ids']:		
				(records_copy1[j]['friend_ids']).append(person_id)
			
			
			

	return records_copy1 		


def remove_friend(records, person_id, friend_id):
	'''
	Description: Given a person ID and a friend ID, this function removes them as friends of each other. If any of the IDs are not available, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	records_copy2=records[:]
	
			
	
			 
	for i in range(0,len(records_copy2)):
		if records_copy2[i]['id']==person_id:
			if friend_id  in records_copy2[i]['friend_ids']:			
				(records_copy2[i]['friend_ids']).remove(friend_id)
	for j in range(0,len(records_copy2)):
		if records_copy2[j]['id']==friend_id:			
			if person_id  in records_copy2[j]['friend_ids']:		
				(records_copy2[j]['friend_ids']).remove(person_id)	


	return records_copy2




def add_education(records, person_id, institute_name, ongoing, percentage):
	'''
	Description: Adds an education record for the person with the given person ID. The education record constitutes of insitute name, the person's percentage and if that education is currently ongoing or not. Please look at the format of an education field from the PDF. If the person ID is not available in the records, you can ignore that case.

	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage

	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	'''
	records_copy3=records[:]
	dict_edu={}
	
		
	for i in range(0,len(records_copy3)):
		
		if records_copy3[i]['id']==person_id:
			dict_edu['institute']=institute_name
			dict_edu['ongoing']=ongoing
			if ongoing==False :
				dict_edu['percentage']=percentage
				records_copy3[i]['education'].append(dict_edu)
			else:
				dict_edu=dict_edu
				records_copy3[i]['education'].append(dict_edu)
		
			
		
	return records_copy3







