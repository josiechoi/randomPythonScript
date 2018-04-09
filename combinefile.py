#Modified script from https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python
#to combine log files  (Apr 2018. JC) 



import glob

pattern='*.log'

read_files=glob.glob(pattern)

with open("result.txt","wb") as outfile:
	for f in read_files:
		with open(f,"rb") as infile:
			outfile.write(infile.read())


	
