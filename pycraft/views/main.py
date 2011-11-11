from pyramid.view import view_config
from pycraft.models import PyCraft

@view_config(context=PyCraft, renderer='pycraft:templates/mytemplate.pt')
def my_view(request):
    return {'project':'PyCraft'}
