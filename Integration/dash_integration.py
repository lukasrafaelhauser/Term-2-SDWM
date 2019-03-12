#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 22:40:36 2019

@author: l-r-h
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_auth
import dash_html_components as html
import pandas_datareader.data as web
import plotly.graph_objs as go
import datetime
from Data_munge_1 import all_mir4, all_mir5, all_mir7, Act_Data


app = dash.Dash()
auth = dash_auth.BasicAuth(
    app,
    Act_Data
)
    
#
#@app.callback(
#        Output(component_id = 'output-graph', component_property='children'),
#        [Input(component_id='input', component_property='value')]
#        )
#def update_graph(input_data):
#    
#    return input_data
#



#app.layout = html.Div(children= [
#        html.Div(children='STOCK PLOTTER'),
#        dcc.Input(id='input', value='',type='text'),
#        html.Div(id='output-graph')])




 
app.layout = html.Div(children= [
        html.Div(children='DASHBOARD'),
        dcc.Graph(id='input', 
          figure= {
                  'data': [{'x': all_mir4.index, 'y': all_mir4.inc_id, 'type': 'line', 'name': 'Incidents per Day'},
                                          ],
                  'layout': {
                          'title': 'Incidents per weekday'
                          }}),
        dcc.Graph(id='input_2',
          figure= {
                  "data": [
                    {
                      "values": all_mir5.inc_id,
                      "labels": list(all_mir5.index),
                      "name": "Inc/Service",
                      "hoverinfo":"label+value",
                      "hole": .4,
                      "fill": "tozeroy",
                      "text": "Inc/Service",
                      "type": "pie"
                    }],
                  "layout": {
                        "title":"Incidents per Service",
                    }}), 
        dcc.Graph(id='input_3',
          figure= {
                  "data": [
                    {
                      "values": all_mir7.inc_id,
                      "labels": list(all_mir7.index),
                      "name": "Inc/Service",
                      "hoverinfo":"label+value",
                      "hole": .3,
                      "text": "CInc/Service",
                      "type": "pie"
                    }],
                  "layout": {
                        "title":"Critical Incidents per Service",
                    }}),
    

        html.Div(id='output-graph')])



#@app.callback(
#        Output(component_id = 'output-graph', component_property='children'),
#        [Input(component_id='input', component_property='value')]
#        )
#def update_graph(input_data):
#    start = 0
#    end = 6
##    df = web.DataReader(input_data, 'iex', start, end)
#    
#    return dcc.Graph(
#            id='example-graph',
#            figure= {
#                     'data': [{'x': all_mir4.index, 'y': all_mir4.inc_id, 'type': 'line', 'name': input_data},
#                              ],
#                     'layout': {
#                             'title': input_data
#                             }})
#

#app.layout = html.Div(children= [
#        html.Div(children=''),
#        dcc.Graph(id='input', 
#                  figure= {
#                          "data": [
#                            {
#                              "values": all_mir5.inc_id,
#                              "labels": list(all_mir5.index),
#                              "name": "Inc/Service",
#                              "hoverinfo":"label+percent",
#                              "hole": .4,
#                              "type": "pie"
#                            }],
#                          "layout": {
#                                "title":"Incidents per Service",
#                            }
#                        }),
#        html.Div(id='output-graph')])






if __name__ == '__main__':
    app.run_server(debug=True)

#%%
#app.layout = html.Div(children= [
#        html.Div(children='STOCK PLOTTER'),
#        html.H1('Stock'),
#                       dcc.Graph(id='example',
#                                 figure= {
#                                         'data': [{'x': df.index, 'y': df.close, 'type': 'line', 'name': stock},
#                                                  ],
#                                         'layout': {
#                                                 'title': stock
#                                                 }
#                                         })
#                      ])
#

#app.layout = html.Div(children=[
#        dcc.Input(id='input', value='Enter something', type='text'),
#        html.Div(id='output')
#        ])
#
#@app.callback(
#        Output(component_id='output', component_property='children'),
#        [Input(component_id='input', component_property='value')])
#
#def update_value(input_data):
#    try:
#        return str(float(input_data)**2)
#    except:
#        return 'Error'

