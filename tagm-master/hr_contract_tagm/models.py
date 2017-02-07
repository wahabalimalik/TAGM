# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_custom_contract(models.Model):

	_inherit = 'hr.contract'
	xx_mobile = fields.Char('Mobile')
	replacement = fields.Char()
	special = fields.Char()
	xxx_other = fields.Char('Other')
	tax = fields.Char('Tax u/s 149')
	leave = fields.Char()
	provident_fund = fields.Char()
	xx_other = fields.Char('Other')
	
class button_refresh_wizard(models.Model):
    
    _name = 'test.refresh'

    @api.multi
    def contract_refresh(self):
    	active_class = self.env['hr.contract'].browse(self._context.get('active_ids'))
    	for v in active_class:
    		v.xx_mobile = 0
    		v.replacement = 0
    		v.special = 0
    		v.xxx_other = 0
    		v.tax = 0
    		v.leave = 0
    		v.provident_fund = 0
    		v.xx_other = 0
