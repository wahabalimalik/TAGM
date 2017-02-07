# -*- coding: utf-8 -*-
from openerp import models, fields, api
from dateutil import relativedelta as rd
import datetime as dt

class hr_employee_pub_info_extension(models.Model):
	_inherit = 'hr.employee'

	home_address_inf = fields.Char(string="Home Address")
	xx_blood_group = fields.Char(string="Blood Group")
	bank_name = fields.Char(string="Bank Name")
	account_number = fields.Char(string="Account Number")
	branch_code = fields.Char(string="Branch Code")
	other_email = fields.Char(string="Other Email")
	other_email = fields.Char(string="Other Email")
	emergency_name_cnt = fields.Char(string="Emergency Contact Name")
	emergency_number = fields.Char(string="Emergency Contact Number")
	office_extension = fields.Char(string="Office Extention Number")
	mul_mbl_num = fields.Char(string="Mobile Number")
	post_quali_prac = fields.Date(string="Post Qualification Exp (Practice)")
	post_quali_other = fields.Date(string="Post Qualification Exp (Other)")
	student_entitlement = fields.Float(string="Student Entitlement")
	partner = fields.Boolean("Partner", default=False)
	other_firms = fields.Boolean("Other Training Firms", default=False)
	ca_firm = fields.Char(string="CA Firm")
	firm_status = fields.Selection([('partner','Partner'),('soleproprietor','SoleProprietor')], string="Status of Firm")
	entitlements = fields.Float(string="Entitlements Available")
	departmental_hierarchy = fields.Selection([
        ('Supervisor', 'Supervisor'),
        ('Assistant Manager', 'Assistant Manager'),
         ('Manager', 'Manager'),
        ('Senior Manager', 'Senior Manager'),
        ('Partner', 'Partner'),  
        ],default='Supervisor')
	xx_office_location = fields.Many2one('hr.officess', string="Office Location")
	father_name = fields.Char()
	working_addrss = fields.Char('Working Address')
	engineer = fields.Char('PEC #', size=64)
	ca = fields.Boolean('CA')
	icaew = fields.Boolean('ICAEW')
	acca = fields.Boolean('ACCA')
	other = fields.Boolean('OTHER')
	ca_reg_no = fields.Char('Batch No:')
	ca_date = fields.Date('Date of Membership:')
	ca_membership = fields.Char('Membership No:')
	icaew_reg_no = fields.Char('Registration No:')
	icaew_date = fields.Date('Date of Membership:')
	icaew_membership = fields.Char('Membership No:')
	acca_reg_no = fields.Char('Registration No:')
	acca_date = fields.Date('Date of Membership:')
	acca_membership = fields.Char('Membership No:')
	other_reg_no = fields.Char('Registration No:')
	other_date = fields.Date('Date of Membership:')
	other_membership = fields.Char('Membership No:')
	Date_Registration = fields.Date('Date of Registration')
	crn_no = fields.Char('CRN No')
	basis_artcle = fields.Selection([
        ('CA/CAF', 'CA/CAF'),
        ('Inter', 'Inter'),
         ('Bachelor', 'Bachelor'),
        ('Masters', 'Masters'),  
        ], string="Basis of Articles")
	post_qly_exp = fields.Integer('Post Qualification Experience')
	employee_qualify_id = fields.One2many('employee_qualification_8','employee_qual_id', string='Details')

	@api.onchange('date_membership') 
	def onchange_date_id(self):
		if self.date_membership:
			difference = rd.relativedelta(dt.date(int(str(dt.datetime.now())[0:4]),int(str(dt.datetime.now())[5:7]),int(str(dt.datetime.now())[8:10])),dt.date(int(str(self.date_membership)[0:4]),int(str(self.date_membership)[5:7]),int(str(self.date_membership)[8:])))
			self.post_qly_exp = "{0.years}".format(difference)


		# print "cxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		# s_experience = self.date_membership

		# print "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
		# if s_experience:
		# 	print "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
		# 	dt_s_obj = datetime.strptime(s_experience,"%Y-%m-%d")
		# 	print dt_s_obj
		# 	timedelta = dt_s_obj
		# 	days = timedelta.days
		# 	years = days/365
 	# 		self.post_qly_exp = years 


	@api.onchange('xx_office_location') 
	def onchange_partner_id(self):
		self.working_addrss = self.xx_office_location.Office_address



class employee_hr_qual(models.Model):
	_name = 'employee_qualification_8'
	_rec_name = 'employee_qual_id'

	qualification = fields.Many2one('qualifications.list','Qualification')
	passing_year = fields.Many2one('years.list','Passing Year')
	institue = fields.Many2one('institutes.list','Institue')

	employee_qual_id = fields.Many2one('hr.employee','Employee Qualification')

class qualification_list(models.Model):
    _name = 'qualifications.list'

    name = fields.Char(string='Name of Degree')
    list_code = fields.Integer(string='Qualification Code')

class institute_list(models.Model):
    _name = 'institutes.list'

    name = fields.Char(string='Name of Institute')
    list_code = fields.Integer(string='Institute Code')

class year_list(models.Model):
    _name = 'years.list'

    name = fields.Char(string='Create Year')
    list_code = fields.Integer(string='Year Code')




	# @api.onchange('post_quali_prac')
	# def onchange_post_prac(self):
	# 	if self.post_quali_prac:
	# 		# self.post_quali_prac = (datetime.strptime(self.date_start,'%Y-%m-%d')
