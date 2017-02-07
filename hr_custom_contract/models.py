# -*- coding: utf-8 -*-
from openerp import models, fields, api
import datetime
from datetime import date, datetime, timedelta
from dateutil import relativedelta as rdelta
import time
import math
class qualification_list(models.Model):
    _name = 'qualification.list'

    name = fields.Char(string='Name of Degree')
    list_code = fields.Integer(string='Qualification Code')

class institute_list(models.Model):
    _name = 'institute.list'

    name = fields.Char(string='Name of Institute')
    list_code = fields.Integer(string='Institute Code')

class year_list(models.Model):
    _name = 'year.list'

    name = fields.Char(string='Create Year')
    list_code = fields.Integer(string='Year Code')

class hr_custom_contract(models.Model):
	_inherit = 'hr.contract'
	bonus = fields.Float('Bonus')
	ded_loan_and_advance = fields.Float('Loan & Advance')
	loan_and_advance = fields.Float('Loan & Advance')
	medical_opd = fields.Float('Medical OPD')
	fuel_other = fields.Float('Fuel/others')
	overtime = fields.Float('Overtime')
	#sr_other = fields.Float('SR/other')
	employee_number = fields.Char('Employee ID')
	sr = fields.Float('SR')
	other = fields.Float('Other')
	sr_fund_ded = fields.Float('S.R Fund')
	eobi = fields.Float('EOBI')
	food = fields.Float('Food Expenses')
	p_tax = fields.Float('Professional Tax')
	v_running = fields.Float('Vehicle Running')
	other_ded = fields.Float('Deduction Other')
	mobile_expenses = fields.Float('Mobile Expenses')
	days_worked = fields.Char('Days Worked')
	months = fields.Integer()
	test = fields.Boolean(default=True)
	alert = fields.Integer(compute="_compute_recoo")
	
	@api.one
	def _compute_recoo(self):
		if self.test == True:
			self.alert = 1
		else:
			self.alert = 0
        # if self.applied_resignation == True:
        #     self.alertl = 0
        # else:
        #     self.alertl = 1


	@api.onchange('trial_date_end')
	def onchange_partner_id(self):
		if self.trial_date_end:
			end_month = self.trial_date_end
			current_date = datetime.today()
			d2 = date(int(str(end_month)[0:4]),int(str(end_month)[5:7]),int(str(end_month)[8:10]))
			d1 = date(int(str(current_date)[0:4]),int(str(current_date)[5:7]),int(str(current_date)[8:10]))
			rd = rdelta.relativedelta(d2,d1)
			years = "{0.years}".format(rd)
			months = "{0.months}".format(rd)
			self.months = int(months)
			# rr = self.env['hr.employee'].search([('name','=',self.employee_id.name)])
			print self.months
			print "xxxxxxxxxxxxxxxxx"

			if years == '0':
				if self.months != 0:
					self.test = True
					# self.write({
					# 	'alert' : self.months,
					# 	})
				else :
					self.test = False
					self.write({
						'alert' : 1,
						})
			else:
				self.write({
					'alert' : 1,
					})
			print self.months



class hr_custom_employee(models.Model):

	_inherit = 'hr.employee'
	show_engineer = fields.Boolean('Is an Engineer?')
	engineer = fields.Char('PEC #', size=64)
	blood_group = fields.Selection([('o_positive', 'O+'), ('o_negative', 'O-'), ('a_positive', 'A+'), ('a_negative', 'A-'),('b_positive', 'B+'), ('b_negative', 'B-'), ('ab_positive', 'AB+'), ('ab_negative', 'AB-')], 'Blood Group',select=True)
	joining_date = fields.Date('Date of Joining')
	family_id = fields.One2many('family_info','family_info_id',string='Details')
	spouse_name = fields.Char('Spouse Name')
	s_dob = fields.Date('Date of Birth')
	s_contact = fields.Char('Spouse Contact')
	s_cnic = fields.Char('CNIC #')
	first_email = fields.Char('Primary Email')
	second_email = fields.Char('Secondary Email')
	email_password = fields.Char('Password')
	employee_qualify_id = fields.One2many('employee_qualification','employee_qualification_id',string='Details')
	employee_certify_id = fields.One2many('employee_certification','employee_certification_id',string='Details')
	total_experience = fields.Integer('Total Experience  :  Years:')
	employee_expert_id = fields.One2many('employee_experience','employee_experience_id',string='Details')
	service_period = fields.Char('Service Period')
	last_working_day = fields.Char('Last Working Day')
	accounts_and_finance = fields.Char('Accounts & Finance')
	administration_and_hrm = fields.Char('Administration & HRM')
	it_dept = fields.Char('IT Department')
	site_settlement = fields.Char('Site Settlement')
	hse_dept = fields.Char('HSE Department')
	security_settlement = fields.Char('Security Settlement')
	others_if_any = fields.Char('Others (if any)')
	validation_date = fields.Date('CNIC Validity')
	health_insurance = fields.Selection([
            ('a', 'A'),
            ('b', 'B'),
            ('c', 'C'),
            ('d', 'D'),
            ],)
	life_insurance = fields.Boolean("Life Insurance")
	provident_fund =fields.Boolean("Provident Fund")
	mobile_num = fields.Char("Mobile")
	xx_mobile_phone = fields.Boolean('Mobile Phone')
	xx_laptop = fields.Boolean('Laptop')
	xx_fuel = fields.Boolean('Fuel')
	xx_car = fields.Boolean('Comany Car')
	xx_salary = fields.Float()
	xx_opd = fields.Boolean('OPD')
	alerta = fields.Integer(default=1)
	
	laptop = fields.Char("Laptop")
	company_cell_number = fields.Char("Number")
	cost_centre = fields.Many2one('cost_centre.cost_centre')
	working_adress = fields.Char("Working Address")

	employee_status = fields.Selection([
            ('probation', 'Probation'),
            ('permanent', 'Permanent'),
            ('fixed', 'Fixed Term'),
            ('other', 'Other'),
            ], )
	emergency_name = fields.Char("Name")
	emergency_cell_number = fields.Char("Contact Number")
	emergency_relation = fields.Char("Relation")
	emergency_address = fields.Char("Address")
	_sql_constraints = [
	('mobile_num', 'unique(mobile_num)', 'This Mobile number already exists!')
	]

	@api.onchange('cost_centre')
	def onchange_partner_id(self):
		self.working_adress = self.cost_centre.working_address
	
class employee_qualification(models.Model):
	_name = 'employee_qualification'
	_rec_name = 'employee_qualification_id'
	qualification = fields.Many2one('qualification.list','Qualification')
	passing_year = fields.Many2one('year.list','Passing Year')
	institue = fields.Many2one('institute.list','Institue')
	employee_qualification_id = fields.Many2one('hr.employee','Employee Qualification')

class employee_certification(models.Model):
	_name = 'employee_certification'
	_rec_name = 'employee_certification_id'
	certification = fields.Char('Certification')
	year = fields.Many2one('year.list','Year')
	conducting_institute = fields.Many2one('institute.list','Conducting Institute')
	employee_certification_id = fields.Many2one('hr.employee','Employee Certification')

class employee_experience(models.Model):
	_name = 'employee_experience'
	@api.onchange('experience_from','experience_to')
	def experince_diff(self,):
		s_experience_from = self.experience_from
		s_experience_to = self.experience_to
		if s_experience_from and s_experience_to:
 			dt_s_obj = datetime.strptime(s_experience_from,"%Y-%m-%d")
 			dt_e_obj = datetime.strptime(s_experience_to,"%Y-%m-%d")
 			timedelta = dt_e_obj - dt_s_obj
 			days = timedelta.days
 			months = days/30.43
 			years = days/365
 			self.total_experience_diff = years 

	company = fields.Char('Company')
	designation = fields.Char('Designation')
	experience_from = fields.Date('Experience From')
	experience_to = fields.Date('Experience To')
	total_experience_diff = fields.Char('Total')
	employee_experience_id = fields.Many2one('hr.employee','Employee Experience')

class hr_custom_contract_payslip(models.Model):
	_inherit = 'hr.payslip'
	cost_centre = fields.Char("Cost Centre")
	@api.model
	def create(self, values):
		all_recs = self.env['hr.employee'].search([('id','=',values['employee_id'])])
		values['cost_centre'] = all_recs.cost_centre
		result = super(hr_custom_contract_payslip, self).create(values)
		return result