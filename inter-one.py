import csv
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics
import random
df = pd.read_csv("Math_mark.csv")
data = df["Math_score"].tolist()
# fig = ff.create_distplot([data],["Math score"],show_hist = False)
# fig.show()
mean = statistics.mean(data)
print(f"Mean: {mean}")
print(f"Standard-Deviation: {statistics.stdev(data)}")

def random_set_of_mean(counter):
    data_set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return(mean)
mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)
stand_dev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print(f"Mean: {mean}, Standard-Deviation: {stand_dev}")
#Math-mark
first_sd_start, first_sd_end = mean - stand_dev, mean + stand_dev
second_sd_start, second_sd_end = mean - (2*stand_dev), mean + (2*stand_dev)
third_sd_start, third_sd_end = mean - (3*stand_dev), mean + (3*stand_dev)
# fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
# fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [first_sd_start,first_sd_start], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [second_sd_start,second_sd_start], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [third_sd_start,third_sd_start], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.17], mode = "lines", name = "MEAN"))
# fig.show()
#Math-mark2
df = pd.read_csv("Math_marks2.csv")
data = df["Math_score"].tolist()
mean_of_sample = statistics.mean(data)
fig = ff.create_distplot([data], ["mean of sample 1"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample,mean_of_sample], y = [0,0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_sd_start,first_sd_start], y = [0,0.17], mode = "lines", name = "ONE SD START"))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = "lines", name = "ONE SD END"))
fig.add_trace(go.Scatter(x = [second_sd_start,second_sd_start], y = [0,0.17], mode = "lines", name = "TWO SD START"))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.17], mode = "lines", name = "TWO SD END"))
fig.add_trace(go.Scatter(x = [third_sd_start,third_sd_start], y = [0,0.17], mode = "lines", name = "THREE SD START"))
fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.17], mode = "lines", name = "THREE SD END"))
fig.show() 
print(f"Mean1: {mean_of_sample}")
#Math-marks3
df = pd.read_csv("Math_marks3.csv")
data = df["Math_score"].tolist()
mean_of_sample = statistics.mean(data)
fig = ff.create_distplot([data], ["mean of sample 2"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample,mean_of_sample], y = [0,0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_sd_start,first_sd_start], y = [0,0.17], mode = "lines", name = "ONE SD START"))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = "lines", name = "ONE SD END"))
fig.add_trace(go.Scatter(x = [second_sd_start,second_sd_start], y = [0,0.17], mode = "lines", name = "TWO SD START"))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.17], mode = "lines", name = "TWO SD END"))
fig.add_trace(go.Scatter(x = [third_sd_start,third_sd_start], y = [0,0.17], mode = "lines", name = "THREE SD START"))
fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.17], mode = "lines", name = "THREE SD END"))
fig.show()
print(f"Mean2: {mean_of_sample}")
#Math-marks4
df = pd.read_csv("Math_marks4.csv")
print(f"Z-SCORE: {(mean_of_sample-mean)/stand_dev}")
data = df["Math_score"].tolist()
mean_of_sample = statistics.mean(data)
fig = ff.create_distplot([data], ["mean of sample 3"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample,mean_of_sample], y = [0,0.17], mode = "lines", name = "MEAN OF SAMPLE"))
fig.add_trace(go.Scatter(x = [first_sd_start,first_sd_start], y = [0,0.17], mode = "lines", name = "ONE SD START"))
fig.add_trace(go.Scatter(x = [first_sd_end,first_sd_end], y = [0,0.17], mode = "lines", name = "ONE SD END"))
fig.add_trace(go.Scatter(x = [second_sd_start,second_sd_start], y = [0,0.17], mode = "lines", name = "TWO SD START"))
fig.add_trace(go.Scatter(x = [second_sd_end,second_sd_end], y = [0,0.17], mode = "lines", name = "TWO SD END"))
fig.add_trace(go.Scatter(x = [third_sd_start,third_sd_start], y = [0,0.17], mode = "lines", name = "THREE SD START"))
fig.add_trace(go.Scatter(x = [third_sd_end,third_sd_end], y = [0,0.17], mode = "lines", name = "THREE SD END"))
fig.show()
print(f"Mean3: {mean_of_sample}")