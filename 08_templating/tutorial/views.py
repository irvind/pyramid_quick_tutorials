from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='home.pt')
def home(request):
    return {'name': 'Home view'}
    return Response('<body>Visit <a href="/howdy">hello</a></body>')


@view_config(route_name='hello', renderer='home.pt')
def hello(request):
    return {'name': 'Hello view'}
    return Response('<body>Go back <a href="/">home</a></body>')
