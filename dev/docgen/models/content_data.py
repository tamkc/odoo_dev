from odoo import models, fields, api, _
from datetime import datetime


class ContentData(models.Model):
    _name = "docgen.content_data"
    _description = "Content"
    _rec_name = "name"
    _order = "sequence, name ASC"

    name = fields.Char(
        string="Name", required=True, default=lambda self: _("New"), copy=False
    )

    data_type = fields.Selection(
        selection=[
            ("fixed", "Fixed String"),
            ("variable", "Variable"),
            ("sequence", "Sequence"),
            ("date", "Date"),
        ],
        string="Data Type",
        required=True,
    )

    value = fields.Char(
        string="Value",
        help="For 'Fixed String', enter the static content. For 'Variable', use a variable placeholder.",
    )

    sequence = fields.Integer(
        string="Sequence", default=10, help="Order of the content in the report."
    )

    generator_id = fields.Many2one(
        "docgen.generator", string="Generator", required=True, ondelete="cascade"
    )

    computed_value = fields.Char(
        string="Computed Value",
        store=True,
        help="Holds the generated or final value based on the data type.",
    )


