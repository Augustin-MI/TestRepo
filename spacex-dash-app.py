# Import required libraries
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a list of unique launch sites
launch_sites = spacex_df['Launch Site'].unique()

# Create Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # TASK 1: Add a dropdown list to select Launch Site
    dcc.Dropdown(id='site-dropdown',
                 options=[{'label': 'All Sites', 'value': 'ALL'}] + 
                         [{'label': site, 'value': site} for site in launch_sites],
                 value='ALL',
                 placeholder="Select a Launch Site here",
                 searchable=True),
    
    html.Br(),
    
    # TASK 2: Add a pie chart to show success count
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    html.P("Payload range (Kg):"),
    
    # TASK 3: Add a slider to select payload range
    dcc.RangeSlider(id='payload-slider',
                    min=0,
                    max=10000,
                    step=1000,
                    marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                    value=[min_payload, max_payload]),
    
    html.Br(),
    
    # TASK 4: Add a scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# TASK 2: Callback function for success-pie-chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Pie chart for all sites: total success launches
        success_count = spacex_df[spacex_df['class'] == 1].shape[0]
        failure_count = spacex_df[spacex_df['class'] == 0].shape[0]
        fig = px.pie(values=[success_count, failure_count],
                     names=['Success', 'Failure'],
                     title='Total Launch Success vs Failure (All Sites)',
                     color_discrete_sequence=['green', 'red'])
        return fig
    else:
        # Pie chart for selected site
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        success_count = filtered_df[filtered_df['class'] == 1].shape[0]
        failure_count = filtered_df[filtered_df['class'] == 0].shape[0]
        fig = px.pie(values=[success_count, failure_count],
                     names=['Success', 'Failure'],
                     title=f'Launch Success vs Failure for {entered_site}',
                     color_discrete_sequence=['green', 'red'])
        return fig

# TASK 4: Callback function for success-payload-scatter-chart
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    
    if entered_site == 'ALL':
        # Scatter plot for all sites
        filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & 
                                 (spacex_df['Payload Mass (kg)'] <= high)]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title='Launch Outcome vs Payload Mass (All Sites)',
                         labels={'class': 'Launch Outcome (1=Success, 0=Failure)',
                                 'Payload Mass (kg)': 'Payload Mass (kg)'})
        return fig
    else:
        # Scatter plot for selected site
        filtered_df = spacex_df[(spacex_df['Launch Site'] == entered_site) &
                                 (spacex_df['Payload Mass (kg)'] >= low) & 
                                 (spacex_df['Payload Mass (kg)'] <= high)]
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title=f'Launch Outcome vs Payload Mass for {entered_site}',
                         labels={'class': 'Launch Outcome (1=Success, 0=Failure)',
                                 'Payload Mass (kg)': 'Payload Mass (kg)'})
        return fig

# Run the app
if __name__ == '__main__':
    app.run(port=8050, debug=True)