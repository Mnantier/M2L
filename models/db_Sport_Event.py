# -*- coding: utf-8 -*-
db.define_table('sportEvent',
             Field('ID_SPORT_EVT_ANNUEL','string',requires=IS_NOT_EMPTY()),
             Field('NOM_EVT','string'),
             Field('ADR_NUM','string'),
             Field('ADR_RUE','string'),
             Field('ADR_CP','string'),
             Field('ADR_BP','string'),
             Field('ADR_COMMUNE','string'),
             Field('MOIS_EVT','string'),
             Field('REMARQUES','string'),
             Field('SITE_INTERNET','string'),
             Field('DATE_MAJ','string'),
             Field('DATE_DEBUT','string'),
             Field('DATE_FIN','string')
             ,migrate=False)
