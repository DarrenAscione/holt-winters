def get_time(fname):
	fname = "../data/TIME/" + fname
	with open(fname) as file:
		next(file)
		lines = [line.rstrip("\n").split("\t")[3] for line in file] 
	return lines

def get_cmd(fname):
	fname = "../data/TIME/" + fname
	with open(fname) as file:
		next(file)
		lines = [line.rstrip("\n").split("\t")[3] for line in file] 
	return lines


def convert_cmd(list):
	result = []
	pointer = 0.0
	for row in list:
		if 'Retransmission' in row:
			print row
			pointer -= 6.0
			result.append(pointer)
		elif '(0x4c)' in row:
			pointer += 2.0
			result.append(pointer)
		elif '(0x4d)' in row:
			pointer -= 2.0
			result.append(pointer)
		else:
			print row
			pointer -= 6.0
			result.append(pointer)
	return result

#list = get_cmd("40test_cmd.txt")
#result = convert_cmd(list)


file3 = get_cmd('40test_cmd3.txt')
print convert_cmd(file3)

# file1 = get_time("40test_norm.txt")
# file2 = get_time("50test_norm.txt")

# diff = []
# for i in xrange(min(len(file1), len(file2))):
# 	diff.append(abs(float(file1[i]) - float(file2[i])))

# print diff

# print len(file1)
# print len(file2)
