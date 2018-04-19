
def get_time(fname):
	fname = "../data/TIME/" + fname
	with open(fname) as file:
		next(file)
		lines = [float(line.rstrip("\n").split("\t")[1])*(10**6) for line in file] 
	return lines
	
