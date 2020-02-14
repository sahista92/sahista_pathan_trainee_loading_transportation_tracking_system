from odoo import models, fields, api
from odoo.exceptions import ValidationError


class transporter(models.Model):
    _name = 'transporter.transporter'
    _description = 'transporter.transporter'
    _rec_name = "name"

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    name = fields.Char(required=True, string="Name", copy=False, help="Enter Your Name")
    email = fields.Char(required=True, string="Email")
    contactnumber = fields.Integer(string="Contact Number")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    address = fields.Text(string="Address")
    city = fields.Char(string="City")
    pincode = fields.Integer(string="Pincode")
    state = fields.Char(string="State")
    photo = fields.Binary(attachment=True, string="Image")
    active = fields.Boolean(default=True)

    def archive(self):
        self.write({'active': False})

    def unarchive(self):
        self.write({'active': True})

    # @api.returns('self', lambda value: value.id)
    # def copy(self, n=None):
    #     n = dict(n or {})
    #     n.update(name=("%s (copy)") % (self.name or ''))
    #     return super(transporter, self).copy(n)


class vehicles(models.Model):
    _name = 'vehicles.vehicles'
    _description = 'vehicles.vehicles'
    _rec_name = 'vehicle_type'

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    vehicle_type = fields.Integer(string="Vehicle Type(Wheeler)")
    vehicle_capacity = fields.Integer(string="Vehicle Capacity(KG)")
    vehicle_speed = fields.Integer(string="Vehicle Speed(kmph)")
    vehicle_weight = fields.Integer(string="Vehicle Weight(KG)")
    vehicle_length = fields.Integer(string="Vehicle Length(mtr)")
    vehicle_Engine = fields.Char(string="Vehicle Engine")
    vehicle_image = fields.Binary(string="Vehicle Image")
    available = fields.Selection([('available', 'Available'), ('not available', 'Not Available')], default='available')


class inquirey(models.Model):
    _name = 'inquirey.inquirey.demo'
    _description = 'inquirey.inquirey'

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    source_add = fields.Char(required=True, string="Source Address")
    desti_add = fields.Char(string="Destination Address", required=True)
    distance = fields.Integer(string="Distance(km)")
    duration = fields.Integer(string="Duration(hr)", store=True)
    weight = fields.Integer(string="Weight(KG)")
    driver_id = fields.Many2one('drivers.drivers', string="Driver Name", required=True, store=True)
    vehicle_type = fields.Many2one('vehicles.vehicles', string="Vehicle Type", required=True, store=True)
    vehicle_capacity = fields.Integer(related='vehicle_type.vehicle_capacity', store=True, string="Vehicle Capacity")
    vehicle_speed = fields.Integer(related='vehicle_type.vehicle_speed', string="Vehicle Speed(kmph)", store=True)
    vehicle_weight = fields.Integer(related='vehicle_type.vehicle_weight', string="Vehicle weight(KG)", store=True)
    date = fields.Date(string="Date")
    order_status = fields.Selection([('confirm', 'confirm'), ('pending', 'pending'), ('cancel', 'cancel')], default='pending')

    @api.constrains('source_add', 'desti_add')
    def _check_add(self):
        for record in self:
            if record.source_add == record.desti_add:
                raise ValidationError("source_add name and destination address must be different")

    def order(self):
        self.write({'order_status': 'confirm'})
        return{
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'order.order',
            'target': 'current',
            'res_id': False,
            'type': 'ir.actions.act_window',
            'context': {'current_id': self.id}
        }

    def ordercancel(self):
        self.write({'order_status': "cancel"})
        return True


class drivers(models.Model):
    _name = 'drivers.drivers'
    _description = 'drivers.drivers'
    _rec_name = "name"

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    name = fields.Char(string="Name")
    contactnumber = fields.Integer(string="Contact Number")
    email = fields.Char(string="Email")
    address = fields.Text(required=True, string="Address")
    Date_Of_Birth = fields.Date(string="Date Of Date")
    Licence = fields.Selection(store=True, selection=[('yes', 'yes'), ('no', 'no')], default="yes", string="Licence_Availability")
    Licence_Number = fields.Char(string="Licence Number")
    Valid_Date = fields.Date(string="Due Date")
    city = fields.Char(string="City")
    pincode = fields.Char(string="Pincode")
    state = fields.Char(string="State")
    photo = fields.Binary(attachment=True, string="Image")
    available = fields.Selection([('available', 'Available'), ('not available', 'Not Available')], default='available')


class order(models.Model):
    _name = "order.order"
    _description = "order table"

    @api.onchange('inquiryid', 'order_status')
    def getorder(self):
        orderid = self.env.context.get('current_id')
        self.inquiryid = orderid
        self.order_status = 'confirm'
        rec = self.env['inquirey.inquirey.demo'].search([])
        for i in rec:
            if i.id == orderid:
                self.source_add = i.source_add
                self.desti_add = i.desti_add
                self.distance = i.distance
                self.duration = i.duration
                self.weight = i.weight
                self.vehicle_type = i.vehicle_type
                self.date = i.date
                self.driver_id = i.driver_id
                self.vehicle_type = i.vehicle_type

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)
    inquiryid = fields.Many2one('inquirey.inquirey.demo', string="inquiryid", required=True)
    source_add = fields.Char(required=True, string="Source Address")
    desti_add = fields.Char(string="Destination Address", required=True)
    distance = fields.Integer(string="Distance(km)")
    duration = fields.Float(string="Duration(hr)", store=True)
    weight = fields.Integer(string="Weight(KG)")
    driver_id = fields.Many2one('drivers.drivers', string="Driver Name", required=True, store=True)
    vehicle_type = fields.Many2one('vehicles.vehicles', string="Vehicle Type", required=True, store=True)
    vehicle_capacity = fields.Integer(related='vehicle_type.vehicle_capacity', store=True, string="Vehicle Capacity")
    vehicle_speed = fields.Integer(related='vehicle_type.vehicle_speed', string="Vehicle Speed(kmph)", store=True)
    vehicle_weight = fields.Integer(related='vehicle_type.vehicle_weight', string="Vehicle weight(KG)", store=True)
    date = fields.Date(string="Date")
    state = fields.Selection([('onprogress', 'OnProgress'), ('done', 'Done')], required=True, default='onprogress')

    @api.model
    def create(self, vals):
        self.env['drivers.drivers'].sudo().browse([vals.get('driver_id')]).write({'available': 'not available'})
        self.env['vehicles.vehicles'].sudo().browse([vals.get('vehicle_type')]).write({'available': 'not available'})
        return super(order, self).create(vals)

    def button_onprogress(self):
        rec = self.env['drivers.drivers'].sudo().search([])
        res = self.env['vehicles.vehicles'].sudo().search([])
        for i in rec:
            if i.id == self.driver_id.id:
                i.available = "not available"
        for j in res:
            if j.id == self.vehicle_type.id:
                j.available = "not available"

        for re in self:
            re.write({'state': 'onprogress'})

    def button_done(self):
        rec = self.env['drivers.drivers'].sudo().search([])
        res = self.env['vehicles.vehicles'].sudo().search([])
        print("\n\n", res)
        for i in rec:
            if i.id == self.driver_id.id:
                i.available = "available"
        for j in res:
            if j.id == self.vehicle_type.id:
                j.available = "available"

        self.write({'state': 'done'})
