import pandas as pd
import random 
import statistics
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
populationmean=statistics.mean(data)
print("Mean Of Population",str(populationmean))


def randomSetOfMean(counter):
    dataSet=[]
    for i in range(0,counter):
       randomIndex=random.randint(0,len(data)-1)
       value=data[randomIndex]
       dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean

def show_fig(mean_list):
    df=mean_list
    fig = ff.create_distplot([df],["reading_time"],show_hist="false")
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= randomSetOfMean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    meanOfSamplingDistribution=statistics.mean(mean_list)
    print("Mean Of Sampling Distribution",meanOfSamplingDistribution)
setup()