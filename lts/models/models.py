from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date 


class agent_registration(models.Model):
    _name = 'agent_registration.agent_registration'
    _description = 'Agent_Registration.Agent_Registration'

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    c_number = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    address = fields.Text(required=True)
    city = fields.Char()
    password = fields.Char(required=True)
    state= fields.Selection([('draft','draft'),('done','done'),('cancel','cancel')], default='draft')

    
    def button_done(self):
        self.write({'state': 'done'})
        return True
    
    def button_reset(self):
        self.write({'state': 'draft'})
        return True
    
    def button_cancel(self):
        self.write({'state': 'cancel'})
        return True
    

class inquirey(models.Model):
    _name = 'inquirey.inquirey.demo'
    _description = 'inquirey.inquirey'
    _rec_name = 'source_add'
    source_add = fields.Char(required=True)
    desti_add = fields.Char(required=True)
    KM = fields.Integer()
    duration =fields.Float()
    vehicle_type = fields.Selection(store='True',selection=[('2','2 wheeler'),('3','3 wheeler'),('4','4 wheeler')])
    vehicle_capacity = fields.Selection(store='True',selection=[('250','250 kg'),('550','550 kg'),('1000','1000 kg')])
    vehicle_speed = fields.Selection(store='True',selection=[('70 ','70 kmph'),('50','50 kmph '),('60','60 kmph')])
    date_start=fields.Date()
    date_stop=fields.Date()


    @api.onchange('vehicle_type','vehicle_capacity')
    def _value_pc(self):
        	if self.vehicle_type == '2':
        		self.vehicle_capacity = '250'
        		self.vehicle_speed = '70'

        	elif self.vehicle_type == '3':
        		self.vehicle_capacity = '550'
        		self.vehicle_speed = '50'

        	elif self.vehicle_type == '4':
        		self.vehicle_capacity = '1000'
        		self.vehicle_speed = '60'
	

    @api.constrains('source_add', 'desti_add')
    def _check_add(self):
    	for record in self:
    		if record.source_add == record.desti_add:
    			raise ValidationError("source_add name and destination address must be different")

class order(models.Model):
    _name = 'order.order'
    _inherit = 'inquirey.inquirey.demo'
    _description = 'order.order'

    order_number = fields.Integer(required=True)

class  transporter_regi(models.Model):
    _name = 'transporter_regi.transporter_regi'
    _inherit = 'agent_registration.agent_registration'
    _description = 'transporter_regi.transporter_regi'

    
