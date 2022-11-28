{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "<ipython-input-2-293e2ebfb012>:3: UserWarning: \n",
      "The dash_html_components package is deprecated. Please replace\n",
      "`import dash_html_components as html` with `from dash import html`\n",
      "  import dash_html_components as html\n",
      "<ipython-input-2-293e2ebfb012>:4: UserWarning: \n",
      "The dash_core_components package is deprecated. Please replace\n",
      "`import dash_core_components as dcc` with `from dash import dcc`\n",
      "  import dash_core_components as dcc\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash is running on http://127.0.0.1:8050/\n",
      "\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:8050/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/deps/polyfill@7.v2_7_0m1667835100.12.1.min.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/deps/react-dom@16.v2_7_0m1667835100.14.0.min.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/dash_table/bundle.v5_2_0m1667835100.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/dash-renderer/build/dash_renderer.v2_7_0m1667835099.min.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/html/dash_html_components.v2_0_6m1667835100.min.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/dcc/dash_core_components.v2_7_0m1667835100.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:39] \"\u001b[37mGET /_dash-component-suites/dash/dcc/dash_core_components-shared.v2_7_0m1667835100.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_dash-layout HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_dash-dependencies HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_favicon.ico?v=2.7.0 HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_dash-component-suites/dash/dcc/async-dropdown.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_dash-component-suites/dash/dcc/async-graph.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_dash-component-suites/dash/dcc/async-slider.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:40] \"\u001b[37mGET /_dash-component-suites/dash/dcc/async-plotlyjs.js HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:44] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:37:44] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:55:53] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:55:53] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:56:14] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:56:14] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:56:28] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 16:56:28] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:00:07] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:00:07] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:06:53] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:06:53] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:07:30] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:07:32] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:07:34] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:07:37] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:07:40] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [28/Nov/2022 17:09:37] \"\u001b[37mPOST /_dash-update-component HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import dash\n",
    "import dash_html_components as html\n",
    "import dash_core_components as dcc\n",
    "from dash.dependencies import Input, Output\n",
    "import plotly.express as px\n",
    "\n",
    "\n",
    "spacex_df = pd.read_csv(\"spacex_launch_dash.csv\")\n",
    "max_payload = spacex_df['Payload Mass (kg)'].max()\n",
    "min_payload = spacex_df['Payload Mass (kg)'].min()\n",
    "\n",
    "\n",
    "app = dash.Dash(__name__)\n",
    "server = app.server\n",
    "\n",
    "uniquelaunchsites = spacex_df['Launch Site'].unique().tolist()\n",
    "lsites = []\n",
    "lsites.append({'label': 'All Sites', 'value': 'All Sites'})\n",
    "for site in uniquelaunchsites:\n",
    " lsites.append({'label': site, 'value': site})\n",
    "\n",
    "\n",
    "\n",
    "app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',\n",
    "                                        style={'textAlign': 'center', 'color': '#503D36',\n",
    "                                               'font-size': 40}),\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "                                dcc.Dropdown(id='site_dropdown',options=lsites,placeholder='Select a Launch Site here', searchable = True , value = 'All Sites'),\n",
    "                                html.Br(),\n",
    "\n",
    "\n",
    "                                html.Div(dcc.Graph(id='success-pie-chart')),\n",
    "                                html.Br(),\n",
    "\n",
    "                                html.P(\"Payload range (Kg):\"),\n",
    "\n",
    "                                dcc.RangeSlider(\n",
    "                                    id='payload_slider',\n",
    "                                    min=0,\n",
    "                                    max=10000,\n",
    "                                    step=1000,\n",
    "                                    marks = {\n",
    "                                            0: '0 kg',\n",
    "                                            1000: '1000 kg',\n",
    "                                            2000: '2000 kg',\n",
    "                                            3000: '3000 kg',\n",
    "                                            4000: '4000 kg',\n",
    "                                            5000: '5000 kg',\n",
    "                                            6000: '6000 kg',\n",
    "                                            7000: '7000 kg',\n",
    "                                            8000: '8000 kg',\n",
    "                                            9000: '9000 kg',\n",
    "                                            10000: '10000 kg'\n",
    "                                    },\n",
    "\n",
    "                                    value=[min_payload,max_payload]\n",
    "                                ),\n",
    "\n",
    "                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),\n",
    "\n",
    "                                ])\n",
    "\n",
    "@app.callback(\n",
    "     Output(component_id='success-pie-chart',component_property='figure'),\n",
    "     [Input(component_id='site_dropdown',component_property='value')]\n",
    ")\n",
    "def update_graph(site_dropdown):\n",
    "    if (site_dropdown == 'All Sites'):\n",
    "        df  = spacex_df[spacex_df['class'] == 1]\n",
    "        fig = px.pie(df, names = 'Launch Site',hole=.3,title = 'Total Success Launches By all sites')\n",
    "    else:\n",
    "        df  = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]\n",
    "        fig = px.pie(df, names = 'class',hole=.3,title = 'Total Success Launches for site '+site_dropdown)\n",
    "    return fig\n",
    "\n",
    "@app.callback(\n",
    "     Output(component_id='success-payload-scatter-chart',component_property='figure'),\n",
    "     [Input(component_id='site_dropdown',component_property='value'),Input(component_id=\"payload_slider\", component_property=\"value\")]\n",
    ")\n",
    "def update_scattergraph(site_dropdown,payload_slider):\n",
    "    if site_dropdown == 'All Sites':\n",
    "        low, high = payload_slider\n",
    "        df  = spacex_df\n",
    "        mask = (df['Payload Mass (kg)'] > low) & (df['Payload Mass (kg)'] < high)\n",
    "        fig = px.scatter(\n",
    "            df[mask], x=\"Payload Mass (kg)\", y=\"class\",\n",
    "            color=\"Booster Version\",\n",
    "            size='Payload Mass (kg)',\n",
    "            hover_data=['Payload Mass (kg)'])\n",
    "    else:\n",
    "        low, high = payload_slider\n",
    "        df  = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]\n",
    "        mask = (df['Payload Mass (kg)'] > low) & (df['Payload Mass (kg)'] < high)\n",
    "        fig = px.scatter(\n",
    "            df[mask], x=\"Payload Mass (kg)\", y=\"class\",\n",
    "            color=\"Booster Version\",\n",
    "            size='Payload Mass (kg)',\n",
    "            hover_data=['Payload Mass (kg)'])\n",
    "    return fig\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run_server(debug=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
