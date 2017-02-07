# -*- coding: utf-8 -*-

from openerp import models, fields, api

class project_ext_tagm(models.Model):
	_inherit = 'project.project'

	department = fields.Many2one('hr.department', 'Department')

	@api.onchange('department')
	def _onchange_department_id(self):
		user_ids = []
		dept_id = self.department.id
		result = self.env['hr.employee'].search([('department_id','=',dept_id)])
		for x in result:
			if(x.user_id):
				user_ids.append(x.user_id.id)
		
		return {'domain':{'members': [('id', 'in', user_ids)],}}

class project_ext_tagm_1(models.Model):
	_inherit = 'project.task'
	project_id = fields.Many2one('project.project',"Project")
	#listy = fields.Char()
	@api.onchange('project_id')
	def _onchange_project_id(self):
		my_list = []
		for x in self.project_id.members:
			my_list.append(x.name)
		my_list  = [item.encode('utf-8') for item in my_list]
		#self.listy = my_list
		return {'domain':{'user_id': [('name', 'in', my_list)],}}
	user_id = fields.Many2one('res.users',"Assigned to")
	_defaults = {
	'user_id': None ,
	}	

class project_task_work_1(models.Model):
	_inherit = 'project.task.work'
	
	user_id = fields.Many2one('res.users',"Done by")
	@api.onchange('name')
	def _onchange_project_id(self):
		my_list = []
		new_value = self._context.get('default_project_id',False)
		if new_value :
			data = self.env['project.project'].search([('id', '=', new_value)])
			print data.members
			for d in data.members:
				my_list.append(d.name)
			my_list  = [item.encode('utf-8') for item in my_list]
			return {'domain':{'user_id': [('name', 'in', my_list)]}}
		else :
			return {'domain':{'user_id': [('name', 'in',my_list)]}}

	_defaults = {
	'user_id': None ,
	}


	