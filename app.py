# %%
import dash
from dash import html
from dash import dcc
from dash import Input, Output, State, callback
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
import pandas as pd
import logging
from urllib.parse import unquote
# %%
card_icon = {
    "color": "green",
    "textAlign": "center",
    "fontSize": "4em",
    "margin": "auto",
}

class value_box:
    def __init__(self, width='14em', 
                 value_box_output_id='value_box_output_id',
                 value_box_output_value='value output',
                 value_box_desc_id='description of value',
                 value_box_desc_value='desc value',
                 value_background_color='yellow',
                 value_icon_background_color='lightgreen',
                 value_icon_color='green',
                 value_icon_align='center'
                 ):
        self.value_box_output_id = value_box_output_id
        self.width = width

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = html.Div(style={'width': '14em'},
                        children=[
                            dbc.CardGroup([
                                            dbc.Card([html.H4(children='Value output'),
                                                      html.P(children='desc value')
                                                        ]
                                                     ),
                                            dbc.Card(children=[html.Div(className='bi bi-bullseye',
                                                                        style=card_icon
                                                                )
                                                                ]
                                                     )
                                        ])
                        ]
                )

app.run_server(port=8080)
# %%
