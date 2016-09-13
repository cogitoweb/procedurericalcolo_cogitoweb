{
	'name' : 'Procedure di ricalcolo',
	'version' : '1.0',
	'author' : 'Cogito',
	'website' : 'http://www.cogitoweb.it/',
	'category' : 'Tools',
	'depends' : ['base'],
	'description' : 'Procedure per il ricalcolo del piano dei conti',
	'data': [
        'cogito_procedurericalcolo.xml',
        'menu_items.xml',        
    ],
    'qweb': ['static/src/xml/*.xml'],
	'installable': True
}