import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
year = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun','jul', 'ago', 'set', 'out', 'nov', 'dec']

#DataSets

ms2017 = [5527, 5557, 4544, 4900, 5815, 5934, 6437, 5438, 7481,7065,6886,5239]
s1 = sum(ms2017)
ms2018 = [4836,3262, 3669,3911,4734,4356,5397,6823,6328,6552,4679,5200]
s2=sum(ms2018)
ms2019 = [5366, 4136, 3915, 3683, 4667, 4476, 0, 0, 0, 0, 0, 0]
s3=sum(ms2019)

camp2017 = [8056,7946,6254,6441,10511,10514,10764,8521,8448,8100,7392,8442]
s4=sum(camp2017)
camp2018 = [11967, 11420, 7636, 10732, 13025, 15489,13807, 18913, 26454, 18470, 15099, 13355]
s5=sum(camp2018)
camp2019 = [12595, 9918, 13403, 17575, 13512, 9809,0,0,0,0,0,0]
s6=sum(camp2019)

#sj2017=[0,0,0,0,0,0,0,0,0,0,0,0]
#s7=sum(sj2017)
sj2018 = [7996, 8284, 6180, 6858, 7523, 6392, 8351, 8576, 7052, 6566, 4881, 4922]
s8 = sum(sj2018)
sj2019 = [5798, 6539, 4857, 5401, 4235, 4954,0,0,0,0,0,0]
s9= sum(sj2019)

escr2017 =[2087,1535,1582,1746,1853,2112,1258,2500,3017,2879,2270,1921]
s10= sum(escr2017)
escr2018 = [1763, 1306, 1522, 1613, 1779,1618, 1862, 1441, 696, 1697, 1243, 1438]
s11=sum(escr2018)
escr2019 = [1610, 1500, 1040, 1105, 1978, 1307,0,0,0,0,0,0]
s12=sum(escr2019)

cid2017=[1912,1665,1463,1331,179,88,1084,1258,1084,949,1137,1147]
s13=sum(cid2017)
cid2018 = [1317, 862, 807, 818, 906, 806, 961, 1440, 697, 1697, 1242, 1437]
s14 = sum(cid2018)
cid2019 = [1610, 1499, 1040, 1105, 1978, 1303,0,0,0,0,0,0]
s15 = sum(cid2019)

rib2017= [1428,1585,1081,1449,1371,1529,1519,1736,2231,1732,1693,2021]
s16=sum(rib2017)
rib2018 = [1151,1888,1793,1458,1508,1537,1506,1864,1837,2139,2186,1952]
s17=sum(rib2018)
rib2019 = [1688,1928,1789,2058,1091,962,0,0,0,0,0,0]
s18=sum(rib2019)


pn2017 = [0,0,0,0,0,0,0,0,0,3172,2819,2183]
s19 = sum(pn2017)
pn2018 = [3511,2733,2045,2377,2841,2630,2729,2909,3049,3130,2845,2511]
s20 = sum(pn2018)
pn2019 = [2713, 2117, 2309, 2364, 2322, 2629,0,0,0,0,0,0]
s21 = sum(pn2019)



external_stylesheets1 = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets1)
#go.Figure(data=[go.Pie(labels=[ms2017,ms2018,ms2019], values=[s1,s2,s3])])
app.layout = html.Div(children=[
    html.H1(children='Apuramento Faturas Eletricidade'),

    html.Div(children='''
        Valores em Kilowatts
    '''),

    dcc.Graph(
        id='MS',
        figure={
            'data': [
                {'x': year, 'y': ms2017,
                    'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': ms2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': ms2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Monte Sossego Rua 1'
            }
        }
    ),

    dcc.Graph(
        id='sum_ms',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019'], values=[s1, s2, s3], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}
        }
    ),

    dcc.Graph(
        id='Camp',
        figure={
            'data': [
                {'x': year, 'y': camp2017,
                    'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': camp2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': camp2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Campinho Zona Industrial'
            }
        }
    ),

    dcc.Graph(
        id='sum_camp',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019'], values=[s4, s5, s6], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}
        }
    ),

    dcc.Graph(
        id='sj',
        figure={
            'data': [
                #{'x': year, 'y': sj2017,
                 #   'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': sj2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': sj2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Minimercado Rua Sao João'
            }
        }
    ),

    dcc.Graph(
        id='sum_sj',
        figure={
            'data': [go.Pie(labels=['2018', '2019'], values=[s8, s9], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}
        }
    ),

    dcc.Graph(
        id='Escr',
        figure={
            'data': [
                {'x': year, 'y': escr2017,
                    'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': escr2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': escr2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Escritorio Rua do Coco'
            }
        }
    ),

    dcc.Graph(
        id='sum_escr',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019'], values=[s10, s11, s12], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}
        }
    ),

    dcc.Graph(
        id='cid',
        figure={
            'data': [
                {'x': year, 'y': cid2017,
                    'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': cid2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': cid2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Posto de venda Rua do Coco'
            }
        }
    ),

    dcc.Graph(
        id='sum_cid',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019'], values=[s13, s14, s15], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}
        }
    ),

    dcc.Graph(
        id='rib',
        figure={
            'data': [
                {'x': year, 'y': rib2017,
                    'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': rib2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': rib2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Posto de venda Grosso Ribeirinha'
            }
        }
    ),
    dcc.Graph(
        id='sum_rib',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019'], values=[s16, s17, s18], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}
            
        }
    ),
    dcc.Graph(
        id='pn',
        figure={
            'data': [
                {'x': year, 'y': pn2017,
                    'type': 'bar', 'name': u'2017'},
                {'x': year, 'y': pn2018,
                    'type': 'bar', 'name': u'2018'},
                {'x': year, 'y': pn2019,
                    'type': 'bar', 'name': u'2019'},
            ],
            'layout': {
                'title': 'Posto de venda Grosso Porto Novo'
            }
        }
    ),
    dcc.Graph(
        id='sum_pn',
        figure={
            'data': [go.Pie(labels=['2017', '2018', '2019'], values=[s19, s20, s21], hole=0.3)],
            'layout': {'title': 'Comparação anual Directa'}

        }
    )
]) 

if __name__ == '__main__':
    app.run_server(debug=True)
