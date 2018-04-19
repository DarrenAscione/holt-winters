import matplotlib.pyplot as plt
import pcap_time


def plotter(series):
	plt.plot(series, color='green', marker='o', linestyle='solid',
        	linewidth=2, markersize=8)
	plt.grid(True)
	plt.show()

plotter(pcap_time.get_time("test3.txt")[:100])
