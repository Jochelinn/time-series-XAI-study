import os
import pandas as pd
#from pytorch_forecasting import TimeSeriesDataSet
from torch.utils.data import Dataset

class EnergyDemandDataset(Dataset):
    def __init__(self, file, transform=None):
        self.data = pd.read_csv(file)
        
        # Drop columns that are either empty or we wont use
        self.data = self.data.drop(['generation fossil coal-derived gas', 'generation fossil oil shale', 'generation fossil peat', 
                          'generation geothermal', 'generation hydro pumped storage aggregated',  
                          'generation marine', 'generation wind offshore', 
                          'forecast solar day ahead', 'forecast wind offshore eday ahead', 
                          'forecast wind onshore day ahead', 'total load forecast', 'price day ahead'], axis=1)
        
        
        # Add up all the generation sources in a single column
        self.data['generation'] = self.data.iloc[:, 1:15].sum(axis=1)
        self.data = self.data.drop(self.data.columns[1:15], axis=1)

        self.transform = transform

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        
        if self.transform:
            row = self.transform(row)

        return row

class WeatherDataset(Dataset):
    def __init__(self, file, transform=None):
        self.data = pd.read_csv(file)

        # Drop columns that are either empty or we wont use
        self.data = self.data.drop(["wind_speed", "wind_deg", "snow_3h", "clouds_all", "weather_id", #"pressure" , "humidity", 
                           "weather_main", "weather_description", "weather_icon", "temp_min", "temp_max", "rain_3h"], axis=1)
        # Keep only the weather in Madrid
        self.data = self.data[self.data["city_name"]=="Madrid"]
        
        # Delete the "city_name" column
        self.data = self.data.drop(["city_name"], axis=1)

        # Expand the time 

        self.transform = transform

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        
        if self.transform:
            row = self.transform(row)

        return row    

class RetailStoreInventoryDataset(Dataset):
    def __init__(self, file, transform=None):
        self.data = pd.read_csv(file)
        
        # Drop columns that we wont use
        self.data = self.data.drop(["Category", "Region" , "Inventory Level", "Units Ordered", "Demand Forecast", 
                          "Weather Condition", "Competitor Pricing", "Seasonality"], axis=1)
        # Filter a single store
        self.data = self.data[self.data["Store ID"] == "S001"]
        # Filter a single product
        #self.data = self.data[self.data["Product ID"] == "P0001"]  

        self.transform = transform

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        
        if self.transform:
            row = self.transform(row)

        return row    
