#-*- coding:utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011 OpenERP SA (<http://openerp.com>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import time
import datetime
from openerp.report import report_sxw
from openerp.osv import osv

class employees_yearly_salary_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(employees_yearly_salary_report, self).__init__(cr, uid, name, context)

        self.localcontext.update({
            'time': time,
            'get_employee': self.get_employee,
            'get_employee_detail': self.get_employee_detail,
            'cal_monthly_amt': self.cal_monthly_amt,
            'get_periods': self.get_periods,
            'get_value': self.get_value,
        })

        self.context = context

    def get_periods(self, form):
        #self.mnths = []
#       Get start year-month-date and end year-month-date
        print form['date_from']
        print form['date_to']
        first_year = int(form['date_from'][0:4])
        #last_year = int(form['date_to'][0:4])

        first_month = int(form['date_from'][5:7])
        monthDict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
            7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

        month = monthDict[first_month] 
        return month+' '+str(first_year)
   

    def get_employee(self, form):
        employes_test = self.pool.get('hr.payslip').browse(self.cr,self.uid, form.get('employee_ids', []), context=self.context)
        employes_idsss = []
        employes_idssss = []
        info = []
        for emp in employes_test:
            employes_idssss.append(emp.id)
            employes_idsss.append(emp.employee_id.id)

        check_ids = ",".join(str(x) for x in employes_idssss)
        cost_centres = []
        self.cr.execute("SELECT DISTINCT name FROM hr_payslip WHERE id in  ("+check_ids+");")
        res_ids = self.cr.fetchall()
        for i in res_ids:
            cost_centres.append(i[0])        
        for cost in cost_centres:
            contract_objss = self.pool.get('hr.payslip').search(self.cr,self.uid, [('name','=',cost),('id','in',employes_idssss)], context=self.context)
            resss = self.pool.get('hr.payslip').browse(self.cr, self.uid, contract_objss)
            empp_test_ids = []
            for ree in resss:
                empp_test_ids.append(ree.id)
            emp_id_data =  list(set(empp_test_ids))   
            data = {
            # 'cost_centre' :cost,
            'employee_idss' : list(set(empp_test_ids))
            }
            info.append(data)
        return info   

    def get_employee_detail(self, obj):
        #payslip_lines = self.cal_monthly_amt(obj)
        #return payslip_lines
        contract_obj = self.pool.get('hr.payslip').search(self.cr,self.uid, [('id','=',obj)], context=self.context)
        res = self.pool.get('hr.payslip').browse(self.cr, self.uid, contract_obj)
        #for r in res:
        #    print r.line_ids
        return res

    def get_value(self, total):
        print 'umair'
        print total

    def cal_monthly_amt(self, employee_id):
        contract_obj = self.pool.get('hr.payslip').search(self.cr,self.uid, [('employee_id','=',employee_id)], context=self.context)
        res = self.pool.get('hr.payslip').browse(self.cr, self.uid, contract_obj)
        return res

class wrapped_report_payslip(osv.AbstractModel):
    _name = 'report.salary_sheet.report_hryearlysalary'
    _inherit = 'report.abstract_report'
    _template = 'salary_sheet.report_hryearlysalary'
    _wrapped_report_class = employees_yearly_salary_report
