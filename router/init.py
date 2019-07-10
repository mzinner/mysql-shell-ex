# init.py
# -------

from ext.mysqlsh_plugins_common import register_plugin
from ext.router import status as router_status
from ext.router import connections as router_connections

register_plugin("status", router_status.status,
                {
                    "brief": "Get MySQL Router info",
                    "parameters": [
                        {
                            "name": "router_ip",
                            "brief": "IP of MySQL Router",
                            "type": "string",
                            "required": True
                        },
                        {
                            "name": "router_port",
                            "brief": "TCP port where MySQL Router REST API is listening.",
                            "type": "integer",
                            "required": True
                        },
                        {
                            "name": "user",
                            "brief": "MySQL Router user for REST API",
                            "type": "string",
                            "required": True
                        },
                        {
                            "name": "password",
                            "brief": "MySQL Router password for REST API",
                            "type": "string",
                            "required": True
                        }
                    ]
                },
                "router",
                {
                    "brief": "MySQL Router management and utilities.",
                    "details": [
                        "A collection of MySQL Router management tools"
                    ]
                })


register_plugin("connections", router_connections.connections,
                {
                    "brief": "Get Connections in MySQL Router",
                    "parameters": [
                        {
                            "name": "router_ip",
                            "brief": "IP of MySQL Router",
                            "type": "string",
                            "required": True
                        },
                        {
                            "name": "router_port",
                            "brief": "TCP port where MySQL Router REST API is listening.",
                            "type": "integer",
                            "required": True
                        },
                        {
                            "name": "user",
                            "brief": "MySQL Router user for REST API",
                            "type": "string",
                            "required": True
                        },
                        {
                            "name": "password",
                            "brief": "MySQL Router password for REST API",
                            "type": "string",
                            "required": True
                        }
                    ]
                },
                "router",
                {
                    "brief": "MySQL Router management and utilities.",
                    "details": [
                        "A collection of MySQL Router management tools"
                    ]
                })