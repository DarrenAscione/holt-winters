import matplotlib.pyplot as plt
import pcap_time
import holt_winters


def plotter(series1, series2=None, series3=None):

	if series2 == None:
		plt.plot(series1, color='green', marker='o', linestyle='solid',
	       	linewidth=2, markersize=8)

	elif series3 != None:
		plt.plot(series1, 'g.-', series2, 'bx-', series3, 'rx-')
		plt.grid(True)

	else:
		plt.plot(series1, 'g.-', series2, 'bx-')
		plt.grid(True)

	plt.show()

# data = pcap_time.get_time('test3.txt')

# series2 = data[:100] + holt_winters.holt_winters(data[1:101], 11, 20, mode='multiplicative')[0]
# plotter(pcap_time.get_time("test3.txt")[:120], series2)


list = pcap_time.get_cmd("40test_cmd2.txt")[13:]
result = pcap_time.convert_cmd(list)

list_atk = pcap_time.get_cmd("40test_cmd3.txt")
result_atk = pcap_time.convert_cmd(list_atk)
print list_atk
print result_atk
#series2 = result[20:100] + holt_winters.holt_winters(result[0:100], 6, 50, mode='multiplicative')[0]
series2 = result[:20] + holt_winters.holt_winters(result[0:20], 5, 5, mode='multiplicative')[0]

plotter(result[:25], series2, result_atk)
