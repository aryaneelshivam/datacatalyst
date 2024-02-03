import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go
import csv
st.set_page_config(
    page_title="Sales dashboard | Atlas Global",
    page_icon="🍣",
    initial_sidebar_state="expanded",
)
st.title('Atlas Global | sales dashboard')
st.subheader('Interactive sales analysis and visualization dashboard.')
file = open('sample.csv', 'r')
data = pd.read_csv(file, encoding='latin-1')

col1, col2 = st.columns(2)
#Calculating total sales
total = 0
for i in data['SALES']:
	total += i
col1.metric("Total sales 💸", total)
total2 = 0
for i in data['MSRP']:
    total2 += 1
col2.metric("Total MSRP 💵", total2)
st.divider()

#histogram charts visualization
x_axis = data['ORDERDATE']
color = data['STATUS']
fig = px.histogram(data, x=x_axis, color=color, title='Order Status Distribution Over Time', width=1240)
st.plotly_chart(fig)

#stacked filled area chart
x_axis = data['ORDERDATE']
color = data['PRODUCTLINE']
y_axis = data['SALES']
line = data['PRODUCTLINE']
fig = px.area(data, x=x_axis, y=y_axis, color=color, line_group=line, width=1240, title="Stacked filled area chart comparing sales with product line against order dates.")
st.plotly_chart(fig)

#two different matrices with two different columns
col1, col2 = st.columns(2)
x_axis = data['COUNTRY']
y_axis = data['SALES']
fig = px.bar(data, x=x_axis, y=y_axis,
             hover_data=['SALES', 'QUANTITYORDERED'], color='PRODUCTLINE',
              height=500, title=f'Bar chart for Country, Sales, Quantity and Product Line', width=650)
col1.plotly_chart(fig)
expander = col1.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')
x_axis = data['COUNTRY']
y_axis = data['SALES']
fig = px.bar(data, x=x_axis, y=y_axis,
             hover_data=['SALES', 'QUANTITYORDERED'], color='COUNTRY',
              height=500, title=f'Bar chart for Country, Sales, and Quantity', width=600)
col2.plotly_chart(fig)
expander = col2.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')

#Two different matrices with two different columns
col1, col2= st.columns(2)
selected_column1 = data['STATUS']
fig = px.pie(data, names=selected_column1, title=f'Pie Chart for Order Status')
col1.plotly_chart(fig)
expander = col1.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')
selected_column = data['COUNTRY']
fig = px.pie(data, names=selected_column, title=f'Pie Chart for Country distribution', width=500)
col2.plotly_chart(fig)
expander = col2.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')

#columns for radar chart and donut chart
col1, col2= st.columns(2)

#radar chart
# Assuming 'data' is a DataFrame and contains the columns 'QUANTITYORDERED', 'PRICEEACH', and 'SALES'
theta = ['QUANTITYORDERED', 'PRICEEACH', 'SALES']
r = [1,2,3,4]
# Plotting the polar plot
fig = go.Figure(data=go.Scatterpolar(
  r=r,
  theta=theta,
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=True
)

col1.plotly_chart(fig)
expander = col1.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')

df_grouped = data.groupby(['ORDERDATE', 'STATUS']).size().reset_index(name='Count')
fig = px.pie(df_grouped, names='STATUS', values='Count', hole=0.3, color='ORDERDATE', title='Order Status Over Time', width=500)
# Show the plot
col2.plotly_chart(fig)
expander = col2.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')

#Treemap chart visualization
cilent_country = data['COUNTRY']
status = data['STATUS']
values = data['SALES']
fig = px.treemap(data, path=[cilent_country, status], values=values,title='Sales Distribution by Client Country and Status', width=1240)
st.plotly_chart(fig)


#Scatter chart 
x_axis = data['PRICEEACH']
y_axis = data['QUANTITYORDERED']
fig = px.scatter(data, x=x_axis, y=y_axis, title='Scatterplot between Price Each and Quantity Ordered',width=1240)
st.plotly_chart(fig)
expander = st.expander("See explanation of above chart")
expander.write('''
    The above chart shows relationship between individual prices of each item with the total number of quantity ordered
''')
