import os 
s='detected_face\\Nazeer.266.44.jpg'
s2=os.path.split(s)
print(s2[-1])
s3=s2[-1].split('.')
print(s3[-3])

