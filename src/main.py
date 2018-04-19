import holt_winters
import pcap_time
import plot

def main():
	file1 = pcap_time.get_time("40test_norm.txt")
	file2 = pcap_time.get_time("50test_norm.txt")

	diff = []
	for i in xrange(min(len(file1), len(file2))):
		diff.append(abs(float(file1[i]) - float(file2[i]))*1000)

	series = diff[:300] + holt_winters.holt_winters(diff[:3000], 26, 20, mode='additive')[0]

	plot.plotter(diff[:320], series)

main()
