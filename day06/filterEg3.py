import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

avg = statistics.mean(data)

print("avg is " + str(avg))

data_g_a = list(filter(lambda x: x > avg, data))

print("data is more than avg is: " + str(data_g_a))