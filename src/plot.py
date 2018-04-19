import matplotlib.pyplot as plt
import pcap_time
import holt_winters


def plotter(series1, series2=None):
	#plt.plot(series1, color='green', marker='o', linestyle='solid',
    #    	linewidth=2, markersize=8, series2, color='red', marker='x')

	plt.plot(series1, 'g.-', series2, 'rx-')
	plt.grid(True)
	plt.show()

data = pcap_time.get_time('test3.txt')

series2 = data[:100] + holt_winters.holt_winters(data[1:101], 11, 20, mode='multiplicative')[0]
plotter(pcap_time.get_time("test3.txt")[:120], series2)


