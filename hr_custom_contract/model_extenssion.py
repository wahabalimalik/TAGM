# -*- coding: utf-8 -*-
from openerp import models, fields, api
from dateutil import relativedelta as rd
import datetime as dt

class hr_oms(models.Model):
    _inherit = 'hr.employee'
    age = fields.Char()
    oms_experience  = fields.Integer(string ="OMS Experience :")
    @api.onchange('birthday','family_id','employee_expert_id')
    def _onchange_birthday(self):
    	if(self.birthday):
    		difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(self.birthday)[0:4]),int(str(self.birthday)[5:7]),int(str(self.birthday)[8:])))
    		self.age = "{0.years}".format(difference)

    	no_of_kids = 0
    	for x in self.family_id:
    		if (x.kid_name):
    			no_of_kids +=1
    			self.children = no_of_kids

    	self.total_experience = sum(int(x.total_experience_diff) for x in self.employee_expert_id if x.total_experience_diff)
    	self.oms_experience   = sum(int(x.total_experience_diff) for x in self.employee_expert_id if x.total_experience_diff and (x.company == "OMS" or x.company =="oms"))
    
    def auto_birthday(self, cr, uid, context=None):
        scheduler_line_obj = self.pool.get('hr.employee')
        #Contains all ids for the model hr.employee
        scheduler_line_ids = self.pool.get('hr.employee').search(cr, uid, [])   
        #Loops over every record in the model hr.employee
        for scheduler_line_id in scheduler_line_ids :
            
            #Contains all details from the record in the variable scheduler_line
            scheduler_line =scheduler_line_obj.browse(cr, uid,scheduler_line_id ,context=context)

            today = dt.date.today()
            
            if scheduler_line.birthday:

                if int(today.month)==int(scheduler_line.birthday[5:7]) and int(today.day) == int(scheduler_line.birthday[8:10]):
                    age = int(today.year) - int(scheduler_line.birthday[0:4])

                    scheduler_line_obj.write(cr, uid, scheduler_line_id, {'age': age, 'write_date': dt.date.today()}, context=context)

class family_info(models.Model):
	_name = 'family_info'
	kid_name = fields.Char('Kid Name')
	sex = fields.Char('Sex')
	dob = fields.Date('Date of Birth')
	age = fields.Integer('Age')
	family_info_id = fields.Many2one('hr.employee','Family Information')

	@api.onchange('dob')
	def _onchange_dob(self):
		if(self.dob):
			difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(self.dob)[0:4]),int(str(self.dob)[5:7]),int(str(self.dob)[8:])))
			self.age = "{0.years}".format(difference)

class cost_centre(models.Model):
	_name = 'cost_centre.cost_centre'

	name = fields.Char()
	code = fields.Char()
	working_address = fields.Char('Working Address')


class test_wizarddd(models.Model):
    
    _name = 'test.wizarddd'

        
    @api.multi
    def virtual_income(self):
        active_class = self.env['hr.employee'].browse(self._context.get('active_ids'))
        vv = self.env['family_info'].search([])
        for x in vv:
            if(x.dob):
                difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(x.dob)[0:4]),int(str(x.dob)[5:7]),int(str(x.dob)[8:])))
                x.age = "{0.years}".format(difference)

        for v in active_class:
            if(v.birthday):
                difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(v.birthday)[0:4]),int(str(v.birthday)[5:7]),int(str(v.birthday)[8:])))
                v.age = "{0.years}".format(difference)

            # for x in v.employee_expert_id:
            #     if x.total_experience_diff:
            #         vv = int(x.total_experience_diff)
            #     print vv

            v.total_experience = sum(int(x.total_experience_diff) for x in v.employee_expert_id if x.total_experience_diff)
            v.oms_experience   = sum(int(x.total_experience_diff) for x in v.employee_expert_id if x.total_experience_diff and (x.company == "OMS" or x.company =="oms"))
        