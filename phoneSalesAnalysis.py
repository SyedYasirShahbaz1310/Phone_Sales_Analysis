import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("https://raw.githubusercontent.com/SachinkumarSakthivel/PROJECT-1/refs/heads/main/apple_products.csv")
print(data)

#cleaning the data:

print(data.isnull().sum())

print(data.describe())
#Iphone Sales Analysis in India:

highest_rated = data.sort_values(by = ["Star Rating"], ascending = False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])

#highest rated iphone on flipcard
# iphones = highest_rated["Product Name"].value_counts()
# labels = iphones.index
# counts = highest_rated["Number Of Ratings"]
# figure = px.bar(highest_rated, x = labels , y = counts , title = "Number of highest ratin iphone on flipcard")
# print(figure.show())
# print(iphones)

# highest reviews iphone on flipcard
# iphones = highest_rated["Product Name"].value_counts()
# labels = iphones.index
# counts = highest_rated["Number Of Reviews"]
# figure = px.bar(highest_rated, x = labels , y = counts , title = "Number of highest ratin iphone on flipcard")
# print(figure.show())
# print(iphones)

# figure = px.scatter(data_frame = data , x = "Number Of Ratings", y = "Sale Price", size = "Discount Percentage" ,title = "Relationship Between Sale Price and Number of ratings")
# print(figure.show())

figure = px.scatter(data_frame = data , x = "Number Of Ratings", y = "Discount Percentage" , size = "Sale Price" ,title = "Relationship Between Discount Percentage and Number of ratings")
print(figure.show())