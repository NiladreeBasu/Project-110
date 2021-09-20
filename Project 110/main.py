import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)

    mean = st.mean(dataSet)

    return mean

def showFig(meanList):
    df = meanList
    mean = st.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean], y = [0,1], mode = 'lines', name = 'mean'))
    fig.show()

def setup():
    meanList = []
    for i in range(0,100):
        setofmeans = randomSetOfMean(100)
        meanList.append(setofmeans)
    showFig(meanList)
    mean = st.mean(meanList)
    mode = st.mode(meanList)
    median = st.median(meanList)
    sd = st.stdev(meanList)
    print(mean)
    print(mode)
    print(median)
    print(sd)

setup()