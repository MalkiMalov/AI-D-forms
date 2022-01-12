import difflib
from limitedRecord import rec

def words_similarity(a,b):
	seq = difflib.SequenceMatcher(None,a,b)
	d = seq.ratio()*100
	return d

def fields_values(s,fields):
	try:
		temp=s.split()
		all=s.split() #all the text in list (split by words)
		print(all)
		fields_from_string=[]
		field_indexes=[]
		l1=0
		l2=1
		max_similarity=[88,"field"]
		prev_index=0
		while l1 <len(temp):
			while l2<len(temp):
				for f in fields:
					similarity=words_similarity(f," ".join(temp[l1:l2]))
					if similarity>=max_similarity[0]:
						max_similarity=[similarity,f]
				if max_similarity[1]!="field": #found an exist field
					fields_from_string+=[max_similarity[1]] #add field name to the list
					field_indexes+=[[prev_index+l1,l2-l1]]
					print(temp)
					print(l1,l2,temp[l1:l2])

					all=all[:prev_index+l1]+max_similarity[1].split()+all[prev_index+l2:]

					temp = temp[l2:]
					prev_index += l2
					print(all[l1+prev_index:l2+prev_index],max_similarity)
					max_similarity=[88,"field"] #initial
					l1=0
					l2=1
				else:
					l2+=1
			l1+=1
			l2=l1+1

		fields=[x.split() for x in fields_from_string]
		print(field_indexes)
		print(fields)
		fields_dict={}
		for i in range(len(fields)-1):
			index=field_indexes[i][0]
			field=" ".join(all[index:field_indexes[i][1]+index])
			value = " ".join(all[field_indexes[i][1]+index:field_indexes[i+1][0]])
			fields_dict[field]=value

		print (field_indexes)
		index=field_indexes[-1][0]
		field = " ".join(all[index:field_indexes[-1][1] + index])
		value = " ".join(all[field_indexes[-1][1] + index:])
		fields_dict[field]=value

		return fields_dict
	except: print("error")


def fill_box(self,fields,fields_dict):
	try:
		rec()
		f = open("text_from_speech.txt", "r")
		s = f.readline()

		full_dict = fields_values(s, fields)
		print(dict)
		for f in fields:
			if f in full_dict.keys():
				if full_dict[f].isdigit():
					self.ids[fields_dict[f]].text = full_dict[f]
				else:
					self.ids[fields_dict[f]].text = full_dict[f][::-1]
	except: print("error")





"""
fields={"שם פרטי", "שם משפחה", "גיל","תז","תעודת זהות","מגדר","מין"}
s="שם פרטי חיים שם מישפחה לוי תעודת זהות 322222 מיגדר זכר"
dict=fields_values(s,fields)
print(dict)"""
