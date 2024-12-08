from odoo import models, fields, api, _
from datetime import datetime


class Template(models.Model):
    _name = "docgen.template"
    _description = "Template"
    _rec_name = "name"
    _order = "name ASC"

    name = fields.Char(
        string="Name", required=True, default=lambda self: _("New"), copy=False
    )

