# -*- coding: utf-8 -*-
{
    "name": "Infinys Wilayah Indonesia API",
    "summary": "API for Indonesian regions (provinces, cities, etc.)",
    "description": """
        Provides a public API to access Indonesian regional data, including provinces, cities, sub-districts, and villages.
    """,
    "author": "Infinys System Indonesia",
    "website": "https://www.infinyscloud.com/platform/odoo/",
    "license": "LGPL-3",
    "category": "Technical Settings",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/wilayah_views.xml",
    ],
    "images": [
        "static/description/banner.png",
    ],
}
