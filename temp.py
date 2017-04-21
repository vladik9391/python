
temperature=[];
with open("temperature.txt") as document:
	for line in document:
		temperature.append(int(line.strip()))



print (temperature)

avg = sum(temperature)/len(temperature)
print(avg)

temperature_deviation = []
for t in temperature:
	temperature_deviation.append(t-avg)

with open("average_temp.txt","w") as average_temp:
	average_temp.write("Temperatura medie va fi  %.2f" % avg)

with open("temp_deviation.txt","w") as temp_dev:
    for t in temperature_deviation:
    	temp_dev.write("%.2f\n" %t)
	