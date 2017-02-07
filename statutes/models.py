# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Income_Tax_Ordinance_2001(models.Model):
    _name = 'income_tax_ordinance_2001.income_tax_ordinance_2001'
    section_no = fields.Integer('Section No',required=True)
    section_name = fields.Char('Section Name',required=True)
    schedule_no = fields.Char('Schedule No')
    part_no = fields.Char('Part No')
    division_no = fields.Char('Division No')
    chapter_no = fields.Char('Chapter No')
    date_applicable = fields.Date('Date Applicable')
    date_inactive = fields.Date('Date Inactive')
    related_rules = fields.Char('Related Rules')
    related_sections = fields.Many2one('income_tax_ordinance_2001.income_tax_ordinance_2001', 'Related Sections')
    description = fields.Text()
    note = fields.Text()
    vv = fields.Char(compute="_compute_rec")
    @api.multi
    def _compute_rec(self):
        self.vv = 'Section No %s %s' %(self.section_no,self.section_name)

    _rec_name = 'vv'





class Sales_Tax_Act_1990(models.Model):
    _name = 'sales_tax_act_1990.sales_tax_act_1990'

    section_no = fields.Integer('Section No',required=True)
    section_name = fields.Char('Section Name',required=True)
    chapter_no = fields.Char('Chapter No')
    date_applicable = fields.Date('Date Applicable')
    date_inactive = fields.Date('Date Inactive')
    description = fields.Text()
    related_sections = fields.Many2one('sales_tax_act_1990.sales_tax_act_1990', 'Related Sections')
    related_rules = fields.Char('Related Rules')
    description = fields.Text()
    note = fields.Text()
    vv = fields.Char(compute="_compute_rec")
    @api.multi
    def _compute_rec(self):
        self.vv = 'Section No %s %s' %(self.section_no,self.section_name)

    _rec_name = 'vv'