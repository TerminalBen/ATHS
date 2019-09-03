import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets1 = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

period = [2010,2011,2012,2013,2014,2015,2016,2017,2018]

ms = [115314392,121952345,128825205,143571218,165483365,174549620,179758799,169142126,116612905]
av = [119149998,136923574,124404261,121116531,27713445,0,0,0,0]
camp = [680783718,660123184,620537103,676392002,742936141,821261459,841777083,713921039,453306000]
cid = [246884398,274010694,281539805,281800196,307644025,311277658,291193141,266089836,184324820]
rib = [191326755,193773816,189921523,206759918,234923911,215909686,221846569,216140176,158974237]
pn = [0,0,0,0,0,0,0,98036540,21778510]
rsj = [0,0,0,0,0,0,0,8973856,102093991]
total = [1399554265,1460930321,1409701602,1492033249,1528775690,1564836129,1561814500,1503063221,1251523953]


app = dash.Dash(__name__,external_stylesheets=external_stylesheets1)
app.layout = html.Div(children=[
    html.H1(children='Estatistica de Vendas Bento, SA'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='MS',
        figure={
            'data': [
                {'x': period, 'y': total,
                    'type': 'line', 'name': u'Somatório'},
                {'x': period, 'y': rsj,
                    'type': 'line', 'name': u'Rua de São João'},
                {'x': period, 'y': ms,
                    'type': 'line', 'name': u'Monte Sossego retalho'},
                {'x': period, 'y': av,
                    'type': 'line', 'name': u'Avenida da Holanda'},
                {'x': period, 'y': camp,
                    'type': 'line', 'name': u'Campinho'},
                {'x': period, 'y': cid,
                    'type': 'line', 'name': u'Rua do Coco'},
                {'x': period, 'y': rib,
                    'type': 'line', 'name': u'Ribeirinha'},
                {'x': period, 'y': pn,
                    'type': 'line', 'name': u'Porto Novo'},
            ],
            'layout': go.Layout( 
                title='Estatistica de Vendas',
                yaxis={'title': 'ECV(x1.000.000.000)'},
            )
        }
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)