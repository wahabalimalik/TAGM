# -*- coding: utf-8 -*-

from openerp import models, fields, api

class atl_updation(models.Model):
    _inherit = 'res.partner'
    
    filer    = fields.Boolean('Filer')
    registration_no = fields.Char('Registration No')