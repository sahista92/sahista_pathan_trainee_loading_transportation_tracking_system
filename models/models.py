from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date 

class  transporter(models.Model):
    _name = 'transporter.transporter'
    _description = 'transporter.transporter'

    name = fields.Char(required=True)
    email = fields.Char(required=True)
    contactnumber = fields.Integer()
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
    address = fields.Text()
    city = fields.Char()
    pincode = fields.Integer()
    state= fields.Char()

    @api.constrains('contactnumber')
    def _check_number(self):
        number = self.contactnumber
        if number and len(str(abs(number))) > 10:
            raise ValidationError(_('Number of digits must on exceed 10'))
 

class inquirey(models.Model):
    _name = 'inquirey.inquirey.demo'
    _description = 'inquirey.inquirey'

    source_add = fields.Char(required=True)
    desti_add = fields.Char(required=True)
    distance = fields.Char()
    duration =fields.Char()
    weight = fields.Char()
    vehicle_type = fields.Many2one('vehicles.vehicles','vehicle_type')
    vehicle_capacity = fields.Char(related='vehicle_type.vehicle_capacity', store=True)
    vehicle_speed = fields.Char(related='vehicle_type.vehicle_speed',store=True)
    date_start=fields.Date()
    date_stop=fields.Date()


    @api.constrains('source_add', 'desti_add')
    def _check_add(self):
    	for record in self:
    		if record.source_add == record.desti_add:
    			raise ValidationError("source_add name and destination address must be different")


class drivers(models.Model):
    _name = 'drivers.drivers'
    _description = 'drivers.drivers'

    name = fields.Char()
    contactnumber = fields.Integer()
    email = fields.Char()
    address = fields.Text(required=True)
    Licence = fields.Selection(store=True,selection=[('yes','yes'),('no','no')], default="no")
    Licence_Number = fields.Char()
    city = fields.Char()
    pincode = fields.Char()
    state = fields.Char()
    photo = fields.Binary(attachment=True)


class vehicles(models.Model):
    _name = 'vehicles.vehicles'
    _description = 'vehicles.vehicles'
    _rec_name = 'vehicle_type'

    vehicle_type = fields.Char()
    vehicle_capacity = fields.Char()
    vehicle_speed = fields.Char()
    vehicle_weight = fields.Char()
    vehicle_length = fields.Char()
    vehicle_Engine = fields.Char()

# class order(models.Model):
#     _name = 'order.order'
#     _inherit = 'inquirey.inquirey.demo'
#     _description = 'order.order'

#     order_number = fields.Integer(required=True)



# class Wizard(models.TransientModel):
#     _name = 'inquirey.wizard'
#     _description = "Wizard: Quick inquirey of vehicles"

#     order_number = fields.Many2one('order.order',required=True)
# class customer(models.Model):
#     _name = 'customer.customer'
#     _description = 'customer.customer'

#     name = fields.Char(required=True)
#     email = fields.Char(required=True)
#     contactnumber = fields.Integer()
#     gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')])
#     address = fields.Text()
#     city = fields.Char()
#     state= fields.Char()