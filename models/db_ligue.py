# -*- coding: utf-8 -*-
db.define_table('ligue',
             Field('nom','string',requires=IS_NOT_EMPTY()),
             Field('adresseRue','string',requires=IS_NOT_EMPTY()),
             Field('ville','string',requires=IS_NOT_EMPTY()),
             Field('cp','string',requires=IS_NOT_EMPTY()),
             Field('tel','string',requires=IS_NOT_EMPTY()),
             Field('URLSiteWeb','string'),
             Field('emailContact','string')
             ,migrate=False)

db.define_table('personnel',
                Field('nom','string',requires=IS_NOT_EMPTY()),
                Field('prenom','string',requires=IS_NOT_EMPTY()),
                Field('mission','string',requires=IS_NOT_EMPTY()),
                Field('adresseRue','string',requires=IS_NOT_EMPTY()),
                Field('tel','string',requires=IS_NOT_EMPTY()),
                Field('emailContact','string'))
