
def get_time(fname):
	fname = "../data/TIME/" + fname
	with open(fname) as file:
		content = file.readlines()
		lines = [line.rstrip("\n").split("\t")[1] for line in content] 
	return lines

