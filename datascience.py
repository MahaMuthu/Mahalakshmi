import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
rn=pd.read_csv("Social_Network_Ads.csv")
rn.pad()
print("First five values in a file:",rn.head())
sns.lineplot(rn["EstimatedSalary"],rn["Purchased"])

