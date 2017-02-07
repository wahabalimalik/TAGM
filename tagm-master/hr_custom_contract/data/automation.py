# <openerp>
#     <data noupdate="1">
#         <record id="ir_cron_scheduler_birthday_action" model="ir.cron">
#             <field name="name">DoB Update</field>
#             # <field name="user_id" ref="base.user_root"/>
#             <field name="interval_number">1</field>
#             <field name="interval_type">minutes</field>
#             <field name="numbercall">-1</field>
#             <field eval="False" name="doall"/>
#             <field eval="'hr.employee'" name="model"/>
#             <field eval="'auto_birthday'" name="function"/>
#         </record>
#    </data>
# </openerp>