# csv-data-pandas

Pandas is an open-source Python library that provides data structures and tools to manipulate and analyze data. 
The two key structures of Pandas are DataFrames (structured data arrays) and Series (one-dimensional arrays). Pandas facilitates the manipulation of complex data by allowing fast and efficient indexing and analysis, as well as data processing operations such as merging, aggregating and cleaning data.

## Documentation 
https://pandas.pydata.org/

## DataFrames and Series
```python
  data = pandas.read_csv("weather_data.csv")
  
  # DataFrame
  print(type(data))
  # Series
  print(type(data["temp"]))
```

## Dictionnary and List
```python
  data_dict = data.to_dict()
  print(data_dict)
  
  # List
  temp_list = data["temp"].tolist()
  print(temp_list)
```

## Average & Max
```python
print(data["temp"].mean())
print(data["temp"].max())
```

## Get Data in Columns
```python
print(data["condition"])
print(data.condition)
```

## Get Data in Rows
```python
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)

# Celsius to Fahrenheit 
monday_temp_F = (monday_temp * 9/5) + 32
print(monday_temp_F)
```

## Create a DataFrame from scratch
```python
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
```
![new_data](https://user-images.githubusercontent.com/87909401/216723527-788a24c6-6385-44e1-8ab3-d0eba5063ed8.png)

## Create a DataFrame from a csv file
```python
data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count")
```
![squirrels_count](https://user-images.githubusercontent.com/87909401/227153050-a4989dd5-fc75-4719-97cf-aa904a6839b8.png)




## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=appveyor&logoColor=white)](https://nicolas-cordeiro.webflow.io/)
[![github](https://img.shields.io/github/followers/nicodeiro?style=social)](https://github.com/nicodeiro)
