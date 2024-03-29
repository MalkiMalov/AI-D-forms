#Fill the fields in the GUI
import difflib
from limitedRecord import rec

#The function returns the similarity percent between 2 words
def words_similarity(a,b):
	seq = difflib.SequenceMatcher(None,a,b)
	d = seq.ratio()*100
	return d

#The function recieves text and expected feilds' names, and returns a dictionary with the value of each field
def fields_values(s,fields):
	try:
		temp=s.split() #Split the text to words in list
		all=s.split() #All the text in list (split by words)
		fields_from_string=[]
		field_indexes=[]
		l1=0
		l2=1
		max_similarity=[88,"field"]
		prev_index=0
		#Go through the text, and find the fields positions in it
		while l1 <len(temp): 
			while l2<len(temp):
				for f in fields: #Go through the expected fields
					similarity=words_similarity(f," ".join(temp[l1:l2]))
					if similarity>=max_similarity[0]: #Found better similarity between a field and part of the string
						max_similarity=[similarity,f]
				if max_similarity[1]!="field": #Found an existing field
					fields_from_string+=[max_similarity[1]] #Add field name to the list
					field_indexes+=[[prev_index+l1,l2-l1]] #Add field position to indexes list

					all=all[:prev_index+l1]+max_similarity[1].split()+all[prev_index+l2:] #Optimize the field name (to the expected name) in the final string 

					temp = temp[l2:]
					prev_index += l2
					max_similarity=[88,"field"] #Initial the max similarity for the next field
					l1=0
					l2=1
				else: #Still not a field's name, keep going through the text
					l2+=1
			l1+=1
			l2=l1+1

		fields=[x.split() for x in fields_from_string]
		fields_dict={} #Initial a dictionary of the fields and their values
		for i in range(len(fields)-1): #Get each field and its' corresponding value in the original text
			index=field_indexes[i][0]
			field=" ".join(all[index:field_indexes[i][1]+index])
			value = " ".join(all[field_indexes[i][1]+index:field_indexes[i+1][0]])
			fields_dict[field]=value
                #Handle the last fiels and its' value
		index=field_indexes[-1][0]
		field = " ".join(all[index:field_indexes[-1][1] + index])
		value = " ".join(all[field_indexes[-1][1] + index:])
		fields_dict[field]=value

		return fields_dict
	except: print("error") #An error occured

#Fill the fields with their values in the GUI
def fill_box(self,fields,fields_dict):
	try:
		rec() #Turn on the record from limitedRecord.py and make the text from the speech recognition
		f = open("text_from_speech.txt", "r") #The text from the speech recognition
		s = f.readline()
		full_dict = fields_values(s, fields) #Get the dictionary of the fields and their values, according to the given text
		for f in fields: #Go through the expected fields
			if f in full_dict.keys(): #Found an existing field
				if full_dict[f].isdigit(): #If the value is a digit - add it normally to the matching field in the GUI
					self.ids[fields_dict[f]].text = full_dict[f]
				else: #If the value is not a digit - add it in reverse to the matching field in the GUI (dealing with HEBREW text)
					self.ids[fields_dict[f]].text = full_dict[f][::-1]
	except: print("error") #An error occured





