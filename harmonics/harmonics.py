#k means clustering on imported csv


#read csv 
#prepare file
import csv
import numpy as np
import scipy.cluster.vq as v1
#import sk


def generate_dist():
	vector4=np.loadtxt(open("readings1.csv", "rb"), delimiter=",", skiprows=1) #change_file_name
	d=np.diff(vector4,axis=0)
	seg=np.hypot(d[:,0],d[:,1])
	with open("data1.csv","w") as f:
		for ele in seg:
			print >> f,str(ele)
	
	vector4=np.loadtxt(open("readings2.csv", "rb"), delimiter=",", skiprows=1) #change_file_name
	d=np.diff(vector4,axis=0)
	seg=np.hypot(d[:,0],d[:,1])
	with open("data2.csv","w") as f:
		for ele in seg:
			print >> f,str(ele)
	


vector=[]
v=[1,2]
#v1=[]
i=0
s=""
'''
with open('out.csv','w') as f:
	with open('dataset.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
		
			row=str(row[0])
			row=row.split(',')
			v[0]=float(row[0])
			v[1]=float(row[1])
			s=s+str(v[0])+","+str(v[1])
			#print s
			print >> f,s
			s=""
			#print v
			#print("R")
			v1=v
			#print v1
			#print "V"
			vector.append(v1)
			#print vector[i]
	
			i+=1
			#print v
			#print row[2]
'''


vector=np.loadtxt(open("Book1.csv", "rb"), delimiter=",", skiprows=1)
vector=v1.whiten(vector)
#result=v1.kmeans(vector,7)
result2 , label=v1.kmeans2(vector,100)
label2=label[2:1923]
label1=label[1924:3972]



#print result2
#print label
vector3=np.loadtxt(open("dataset.csv", "rb"), delimiter=",", skiprows=1)

with open('readings1.csv','w') as f:
#with open('dataset.csv', 'rb') as csvfile:
#	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for ele in label1:
		
		#row=str(row[0])
		#row=row.split(',')
		j=result2[ele]
		s=str(j[0])+","+str(j[1])#+","+row[2]
			
		print >> f,s
		#print s
		s=""

with open('readings2.csv','w') as f:
#with open('dataset.csv', 'rb') as csvfile:
#	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for ele in label2:
		
		#row=str(row[0])
		#row=row.split(',')
		j=result2[ele]
		s=str(j[0])+","+str(j[1])#+","+row[2]
			
		print >> f,s
		#print s
		s=""



#generate distance for fourier 

generate_dist()


	
#for ele in vector3:
#	print ele

'''
for ele,row in zip(label,vector3):
	print str(row[0])+","+str(row[1])+","+str(ele)
'''
#for i in range(0,len(vector)):
	#print vector[i]
#k-means

#vector1=np.array(vector)
#print vector1

#for ele in vector:
##	print ele
#for ele in vector1:
	#print ele
#print vector
#vector=v1.whiten(vector)
#print vector
#result=v1.kmeans(vector,5)
#centroid=result

#print centroid

