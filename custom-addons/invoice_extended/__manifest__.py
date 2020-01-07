
# -*- coding: utf-8 -*-
{
'name':'Invoice Extended',
'description':'Invoice extended for data flow between insurance',
'author':'sudishrestha',
'application': True,
   

    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
       
        'views/accountpdc.xml',
       
   
    ],
}
