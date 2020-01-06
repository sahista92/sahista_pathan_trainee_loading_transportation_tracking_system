from odoo import models, fields, api
from odoo.exceptions import ValidationError


class agent_registration(models.Model):
    _name = 'agent_registration.agent_registration'
    _description = 'Agent_Registration.Agent_Registration'

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    c_number = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    address = fields.Text(required=True)
    city = fields.Char()
    state = fields.Char()
    password = fields.Char(required=True)


class inquirey(models.Model):
    _name = 'inquirey.inquirey.demo'
    _description = 'inquirey.inquirey'

    source_add = fields.Char(required=True)
    desti_add = fields.Char(required=True)
    KM = fields.Integer()
    duration = fields.Datetime()
    vehicle_type = fields.Selection(store='True',selection=[('2wheeler','2 wheeler'),('3wheeler','3 wheeler'),('4wheeler','4 wheeler')])
    vehicle_capacity = fields.Selection(store='True',selection=[('250kg','250 kg'),('550kg','550 kg'),('1000kg','1000 kg')])
    vehicle_speed = fields.Selection(store='True',selection=[('70kmph ','70 kmph'),('50kmph','50 kmph '),('60kmph','60 kmph')])


    @api.onchange('vehicle_type','vehicle_capacity')
    def _value_pc(self):
        	if self.vehicle_type == '2wheeler':
        		self.vehicle_capacity = '250kg'
        		self.vehicle_speed = '70kmph'

        	elif self.vehicle_type == '3wheeler':
        		self.vehicle_capacity = '550kg'
        		self.vehicle_speed = '50kmph'

        	elif self.vehicle_type == '4wheeler':
        		self.vehicle_capacity = '1000kg'
        		self.vehicle_speed = '60kmph'
	

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


class transporter_registration(models.Model):
    _name = 'transporter_registration.transporter_registration'
    _inherit = 'agent_registration.agent_registration'
    _description = 'transporter_registration.transporter_registration'    

