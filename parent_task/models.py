# -*- coding: utf-8 -*-

from openerp import models, fields, api

class parent_task(models.Model):
    _inherit = 'project.task'

    main_task_1    = fields.Boolean(string='Main Task')
    main_task_2    = fields.Many2one('project.task','Main Task',domain="[('main_task_1','=',True)]" )

    @api.onchange('main_task_1')
    def _onchange_main_task_1(self):
		self.main_task_1 = 1