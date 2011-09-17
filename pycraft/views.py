from pyramid.view import view_config
from pycraft.models import MyModel

@view_config(context=MyModel, renderer='pycraft:templates/mytemplate.pt')
def my_view(request):
    return {'project':'PyCraft'}
