#!/usr/bin/env python
# coding: utf-8

# In[4]:


from flask import Flask, render_template
import plotly.graph_objs as go
import pandas as pd
import json
import plotly.utils


app = Flask(__name__)

# Load the dataset
df = pd.read_csv('SampleSuperstore.csv')

# Define the route for the dashboard
@app.route('/')
def dashboard():
    
    # Create plot 1: Sales by Category
    plot1 = go.Bar(x=df['Category'], y=df['Sales'])
    
    # Create plot 2: Profit by Category
    plot2 = go.Bar(x=df['Category'], y=df['Profit'])
    
    # Create plot 3: Sales by Region
    plot3 = go.Bar(x=df['Region'], y=df['Sales'])
    
    # Create plot 4: Profit by Region
    plot4 = go.Bar(x=df['Region'], y=df['Profit'])
    
    # Create the layout for the dashboard
    layout = go.Layout(title='Superstore Dashboard', 
                       barmode='group', 
                       xaxis=dict(title='Category/Region'),
                       yaxis=dict(title='Sales/Profit'))
    
    # Combine the plots into a single figure
    fig = go.Figure(data=[plot1, plot2, plot3, plot4], layout=layout)
    
    # Convert the figure to JSON format
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    # Render the dashboard template with the graph data
    return render_template('index.html', graphJSON=graphJSON)

# Define the main function to run the app
if __name__ == '__main__':
    app.run(debug=True)

