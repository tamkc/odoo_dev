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
        compute="_compute_computed_value",
        store=True,
        help="Holds the generated or final value based on the data type.",
    )

    @api.depends("data_type", "value")
    def _compute_computed_value(self):
        for record in self:
            if record.data_type == "fixed":
                record.computed_value = record.value
            elif record.data_type == "variable":
                # Placeholder logic for variable value processing.
                # This can be customized to fetch dynamic content based on 'value'.
                record.computed_value = f"{{{record.value}}}"
            elif record.data_type == "sequence":
                # Assume you have an auto-generated sequence.
                record.computed_value = str(record.sequence)
            elif record.data_type == "date":
                record.computed_value = "test"
            else:
                record.computed_value = ""
