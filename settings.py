# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'user')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'evedemo')


#DEBUG = True

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# Public Read
PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']

# All Read Roles
ALLOWED_READ_ROLES = ["User", "Super", "Master"]
ALLOWED_ITEM_READ_ROLES = ["User", "Super", "Master"]
# Elevated Write Roles
ALLOWED_WRITE_ROLES = ["Super", "Master"]
ALLOWED_ITEM_WRITE_ROLES = ["Super", "Master"]

CACHE_CONTROL = "private, max-age=0, no-cache"
CACHE_EXPIRES = 0

X_DOMAINS = "*"
X_HEADERS = ["Authorization", "X-Requested-With", "Content-Type", "If-Match"]

PAGINATION = False

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
torneos = {
    "schema": {
        "Nombre": {"type": "string"}
    }
}

ediciones = {
    'item_title': 'edicion',
    "schema": {
        "Nombre": {"type": "string"},
        'Torneo': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'torneos',
                'field': '_id',
                'embeddable': True
            },
        },
        "fecha": {"type": "number"}
    }
}

eventotipos = {
    "schema":{
        "Nombre":{"type":"string"}
    }
}

eventos = {
    "schema": {
        "Nombre": {"type": "string"},
        "Genero": {"type": "string", 'allowed': ['Masculino', 'Femenino', 'Mixto']},
        'Tipo': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'eventotipos',
                'field': '_id',
                'embeddable': True
            },
        },
    }
}

atletas = {
    "schema": {
        'Nombre': {
            "type": "dict",
            "schema": {
                "Nombre": {"type": "string"},
                "Apellido1": {"type": "string"},
                "Apellido2": {"type": "string"},
            }
        },
        "Imagen": {"type": "string"},
        "Carrera": {"type": "string"},
        "Cedula": {"type": "string"},
        "Carne": {"type": "string"},
        "Correo": {"type": "string"},
        "Telefonos": {"type": "string"},
        "FechaNacimiento": {"type": "number"},
        "Genero": {"type": "string", "allowed": ["Masculino", "Femenino"]},
        "Lateralidad": {"type": "string", "allowed": ["Izquierda", "Derecha"]},
        "TipoSangre": {"type": "string", "allowed": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]},
        "Peso": {"type": "number"},
        "Estatura": {"type": "number"},
        "Beneficiario": {
            "type": "dict",
            "schema": {
                "Nombre": {"type": "string"},
                "Cedula": {"type": "string"}
            }
        }
    }
}

resultados = {
    "schema": {
        'Atleta': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'atletas',
                'field': '_id',
                'embeddable': True
            },
        },
        'Evento': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'eventos',
                'field': '_id',
                'embeddable': True
            },
        },
        'Edicion': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'ediciones',
                'field': '_id',
                'embeddable': True
            },
        },
        "Carril": {"type": "number"},
        "Hit": {"type": "number"},
        "TiempoRegistro": {"type": "string"},
        "TiempoRealizado": {"type": "string"},
        "Puntos": {"type": "number"}
    }
}

anvandaren = {
    "schema": {
        "anvandarnamn": {"type": "string", 'unique': True, 'minlength': 5},
        "losenord": {"type": "string"},
        "roll": {"type": "string", "allowed": ["User", "Super", "Master"]}
    },
    "allowed_roles": ["Master"],
    "allowed_write_roles": ["Master"],
    "public_methods": [],
    "public_item_methods": []
}

log = {
    "schema":{
        "user":{"type":"string"}},
    "public_methods": [],
    "public_item_methods": [],
    "resource_methods":["POST"],
    "item_methods":[]
}


# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    # 'people': people,
    # 'works': works,
    'torneos': torneos,
    "ediciones": ediciones,
    "torneos": torneos,
    "atletas": atletas,
    "eventos": eventos,
    "resultados": resultados,
    "anvandaren": anvandaren,
    "log":log
}
