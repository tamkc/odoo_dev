from odoo import models, fields

class BlankTemplateModel(models.Model):
    _name = 'blank.template.model'
    _description = 'Blank Template Model'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')