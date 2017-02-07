# -*- coding: utf-8 -*-

from openerp import models, fields, api

class hr_details_of_management_personnal_extenssion(models.Model):
	_name = 'hr.details.of.management.personnal.extenssion'

	date        = fields.Date(string="Date")	
	relation_id = fields.One2many('relation.fields', 'fields_conn_id')
	

class relational_fields(models.Model):
	_name = 'relation.fields'
	
	client_name       = fields.Many2one('hr.employee','Name of Partner (ACA/FCA)', required=True)
	membership_number = fields.Char(string="Membership Number")
	date_membership   = fields.Date(string="Membership Date")
	post_quali_prac   = fields.Float(string="Post Qualification Exp (Practice)")
	post_quali_other  = fields.Float(string="Post Qualification Exp (Other)")
	entitlements      = fields.Float(string="Individual Student's Entitlements")
	
	fields_conn_id    = fields.Many2one('hr.details.of.management.personnal.extenssion',
        ondelete='cascade',string="Wealth Statement", required=True)

	@api.onchange('client_name')
	def onchange_assesment_form_field(self):
		self.membership_number = self.client_name.membership_number
		self.date_membership   = self.client_name.date_membership
		self.post_quali_prac   = self.client_name.post_quali_prac
		self.post_quali_other  = self.client_name.post_quali_other
		self.entitlements      = self.client_name.student_entitlement
#-----------------------------------------------------------------------------------------------------------

class hr_details_training_offices_extenssion(models.Model):
	_name = 'hr.details.training.offices.extenssion'

	name_org 		  			  = fields.Char(string="Name of Training Organization")
	address 		  			  = fields.Char(string="Address")
	city_town 		  			  = fields.Char(string="City/Town")
	country 		  			  = fields.Char(string="Country")
	phone 			  			  = fields.Char(string="Phone")
	fax 			  			  = fields.Char(string="Fax")
	email 			  			  = fields.Char(string="E-mail")
	name_mrs 		  			  = fields.Char(string="Name of Nominated MRS")
	membership_number 			  = fields.Char(string="Membership Number")
	date_membership   			  = fields.Date(string="Membership Date")
	phone_mrs         			  = fields.Char(string="MRS Phone")
	fax_mrs           			  = fields.Char(string="MRS Fax")
	email_mrs         			  = fields.Char(string="MRS E_mail")
	num_partner       			  = fields.Integer(string="Number of Partner(s) in Training Office")
	num_employed      			  = fields.Char(string="Number of Qualified Employee(s) in Training Office")
	num_tech_supervisors_partnr   = fields.Char(string="Number of Technical Supervisors(partners) in Training Office")
	num_tech_supervisors_employee = fields.Char(string="Number of Technical Supervisors(employees) in Training Office")
#-----------------------------------------------------------------------------------------------------------

class hr_detail_of_audit(models.Model):
	_name = 'hr.details.of.audit'

	name               = fields.Char()
	relation_id_1 = fields.One2many('relation.fields.1', 'fields_conn_id_1')

class relational_fields_1(models.Model):
	_name = 'relation.fields.1'

	client_name        = fields.Char()
	client_address     = fields.Char()
	nature_of_business = fields.Char()
	public_solo_others = fields.Char(string="Public/Private Ltd /Solo Proprietor /Other")
	paid_up_capital    = fields.Float() 
	remarks            = fields.Char()
	
	fields_conn_id_1    = fields.Many2one('hr.details.of.audit',
        ondelete='cascade',string="Wealth Statement", required=True)
#-----------------------------------------------------------------------------------------------------------

class hr_declaration(models.Model):
	_name = 'hr.declaration'

	name_org 	 = fields.Char(string="Name of Training Organization")
	place 		 = fields.Char()
	date         = fields.Date()
	name 	     = fields.Char()
	designation  = fields.Char()
	on_behalf_of = fields.Char(string="On Behalf of : ")

#-----------------------------------------------------------------------------------------------------------

class hr_undertaking(models.Model):
	_name = 'hr.undertaking'

	member_name	        = fields.Char(string="Member Name")
	membership_number   = fields.Char(string="Membership Number")
	designation         = fields.Char()
	mrs                 = fields.Char(string="MRS")
	training_office_add = fields.Char(string="Train Office Address")
	place               = fields.Char()
	date                = fields.Date()

#-----------------------------------------------------------------------------------------------------------

class hr_undertaking(models.Model):
	_name = 'hr.registration'

	name = fields.Char(string="Name of Trainee Student")
	father_name = fields.Char(string="Father Name")
	date = fields.Date(string="Date if Birth")
	nic_no = fields.Integer(string="NIC NO")
	nationality = fields.Char()
	address = fields.Char()
	crn_issue = fields.Char(string="CRN Issuance")
	p_address = fields.Char(string="Permanent Address")
	mrs = fields.Char(string="Name of MRS")
	training_org = fields.Char(string="Name of Training Organization")
	org_address = fields.Char()
	crn_status = fields.Char(string="Present Status with CRN")
	crn = fields.Char()
	place = fields.Char()
	prev_mrs = fields.Char(string="Previous MRS")
	prev_training_org = fields.Char(string="Previous Training Organization")
	period_start_served = fields.Date()
	period_end_served = fields.Date()
	obj_certificate = fields.Boolean("No Objection Certificate Yes")
	obj_certificate_no = fields.Boolean("No Objection Certificate No")
	place = fields.Char()
	probation_period_start = fields.Date()
	probation_period_end = fields.Date()
	prob_place = fields.Char("Probation Place")
	

	relation_id_2 = fields.One2many('relation.fields.2', 'fields_conn_id_2')
	relation_id_3 = fields.One2many('relation.fields.3', 'fields_conn_id_3')
	relation_id_4 = fields.One2many('relation.fields.4', 'fields_conn_id_4')

class relational_fields_2(models.Model):
	_name = 'relation.fields.2'

	exe_pass        = fields.Char(string="Examinations Passed")
	month_year     = fields.Char(string="Month & Year of Exam")
	grade_div = fields.Char(string="Grade/Div")
	board_univ = fields.Char(string="Board/University/Institute")

	
	fields_conn_id_2    = fields.Many2one('hr.registration',
        ondelete='cascade',string="Education", required=True)
	
class relational_fields_3(models.Model):
	_name = 'relation.fields.3'

	exc_pass        = fields.Char(string="Examinations Passed")
	mnth_year     = fields.Char(string="Month & Year of Exam")
	grade = fields.Char(string="Grade/Div")
	board_uni = fields.Char(string="Board/University/Institute")

	
	fields_conn_id_3    = fields.Many2one('hr.registration',
        ondelete='cascade',string="Education", required=True)

class hr_office(models.Model):
	_name = 'hr.officess'
	name                 = fields.Char(string="Office Name")
	Office_address                 = fields.Char(string="Office Address")
	city                 = fields.Char(string="City")



class relational_fields_4(models.Model):
	_name = 'relation.fields.4'

	study        = fields.Char(string="Study Leave")
	sick     = fields.Char(string="Sick Leave")
	others = fields.Char(string="Others")
	total = fields.Char(string="Total")

	
	fields_conn_id_4    = fields.Many2one('hr.registration',
        ondelete='cascade',string="Education", required=True)

	# membership_number = fields.Char(string="Membership Number")
	# date_membership = fields.Date(string="Date of Membership")
	# post_quali_prac = fields.Float(string="Post Qualification Exp (Practice)")
	# post_quali_other = fields.Float(string="Post Qualification Exp (Other)")
	# # location = fields.Char(string="Office Location")
	# student_entitlement = fields.Float(string="Student Entitlement")
	# partner = fields.Boolean("Partner", default=False)
	# other_firms = fields.Boolean("Other Training Firms", default=False)
	# ca_firm = fields.Char(string="CA Firm")
	# firm_status = fields.Selection([('partner','Partner'),('soleproprietor','SoleProprietor')], string="Status of Firm")
	# entitlements = fields.Float(string="Entitlements Available")# 