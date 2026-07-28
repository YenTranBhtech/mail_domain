# -*- encoding: utf-8 -*-
{
    'name': "Email Sender Control",
    'version': '19.0.1.0',
    'summary': 'BHS Mail',
    'category': 'Mail',
    'description': """Email Sender Control""",
    "depends": ['mail', 'base_setup'],
    'data': [
        'views/mail_res_config_settings.xml'
    ],
    # Author
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}
