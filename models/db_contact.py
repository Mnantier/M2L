# -*- coding: utf-8 -*-
db.define_table('Contact',
                Field('nom','string',requires=IS_NOT_EMPTY()),
                Field('prenom','string',requires=IS_NOT_EMPTY()),
                Field('grade','string',requires=IS_NOT_EMPTY()),
                Field('tel','string',requires=IS_NOT_EMPTY()),
                Field('Fax','string'),
                Field('emailContact','string'))
