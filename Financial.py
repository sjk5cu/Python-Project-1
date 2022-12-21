#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:20:30 2022

@author: *
"""

import numpy as np
import pandas as pd
from pathlib import Path

# Directory of this file
this_dir = Path('/Users/*/Desktop/All/Financials/CSV').resolve().parent

# Read in all Excel files from folder
parts = []

for path in (this_dir).rglob("*.csv"):
    part = pd.read_csv(path)
    parts.append(part)
    

# Combine the DataFrames from each file into a single DataFrame # pandas takes care of properly aligning the columns
df = pd.concat(parts)

#Combining Chase and Apple csv value with different heads
df["Amount"] = df["Amount"].fillna(df["Amount (USD)"] * -1)
df.drop(['Memo','Amount (USD)','Purchased By','Clearing Date','Post Date'], axis = 1, inplace = True)



# Reorganizing columns so amount is at the end
cols = df.columns.tolist()
cols = cols[:4] + cols[5:3:-1]
df = df[cols]

# Replacing some text
df["Type"]= df["Type"].replace("Sale","Purchase")
df = df.sort_values(by= "Transaction Date")

df.to_excel("2022 Transactions.xlsx", sheet_name="Output", startrow=0, startcol=0, index=True, header=True, na_rep="<NA>", inf_rep="<INF>")
