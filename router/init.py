# init.py
# -------

from ext.mysqlsh_plugins_common import register_plugin
from ext.router import status as router_status
from ext.router import connections as router_connections
from ext.router.myrouter import MyRouter


router = shell.create_extension_object()

def create(ip, port, user, password):
    my_router = MyRouter(ip, port, user, password)
    return { 
         'connections': lambda route_to_find="": my_router.connections(route_to_find), 
         'status': lambda: my_router.status(), 
         'api': my_router.api
    }
                        
shell.add_extension_object_member(router, 'create', lambda ip, port, user, password=False:create(ip, port, user, password), 
            {
                'brief':'Create the MySQL Router Object', 'details':['It has MyRouter methods.'], 
                'parameters':[
                                {'name':'ip', 'type':'string', 'required':True, 'brief':'ip'},
                                {'name':'port', 'type':'integer', 'required':True, 'brief':'port'},
                                {'name':'user', 'type':'string', 'required':True, 'brief':'user'},
                                {'name':'password', 'type':'string', 'required':False, 'brief':'password'}
                        ]
                }
            )

shell.add_extension_object_member(ext, 'router', router, 
{
    'brief':'MySQL Router Object', 
    'details':['MySQL Router Object.']
})
