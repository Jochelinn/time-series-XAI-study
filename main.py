#import lightning.pytorch as pl
#from lightning.pytorch.callbacks import EarlyStopping, LearningRateMonitor
#from lightning.pytorch.tuner import Tuner
#from pytorch_forecasting import TimeSeriesDataSet, TemporalFusionTransformer
import datasets
import display
import numpy as np
import pandas as pd

from sklearn.model_selection import TimeSeriesSplit 

#data = datasets.EnergyDemandDataset(
#    file="./time-series-XAI-study/code/data/energy_dataset.csv")


data = datasets.WeatherDataset(
    file="/home/jose/Universidad/5/TFG/time-series-XAI-study/code/data/weather_features.csv")



#data = datasets.RetailStoreInventoryDataset(
#    file="/home/jose/Universidad/5/TFG/time-series-XAI-study/code/data/retail_store_inventory.csv")


print(f"Dataset length: {len(data)}")

red = pd.DataFrame(data.data.iloc[24*10:24*11], columns=data.data.columns)

tsp = TimeSeriesSplit()


print(f"Data: {red.columns}")
display.showTime(red)

