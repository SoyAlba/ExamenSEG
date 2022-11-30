from odoo import models, fields


class Base(models.Model):
    _name = 'coche.base'
    _description = 'Base class to be inherited'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    
    _sql_constraints = [
        ('name_unique',
         'UNIQUE(name)',
         'El nombre debe ser único'),
    ]

class Coche(models.Model):
    _name = 'coche.coche'
    _marca = fields.Char(string='Marca', required=True)
    _color = fields.Selection(string='Color', selection=[('blanco', 'Blanco'), ('gris', 'Gris'), ('negro','Negro'), ('rojo', 'Rojo'), ('azul', 'Azul'), ('verde', 'Verde'), ('amarillo', 'Amarillo'), ('naranja', 'Naranja'), ('rosa', 'Rosa'), ('morado', 'Morado'), ('marron', 'Marron'), ('otro', 'Otro')], required=True)
    _asientos = fields.Integer(string='Asientos', required=True)
    _conductores = fields.Many2one(comodel_name='coche.conductores', inverse_name='coche_id', string="Conductores")
    _viajes = fields.One2many(comodel_name='coche.viajes', inverse_name='coche_id', string="Viajes")
    _seguro = fields.Many2one(comodel_name='coche.seguro', inverse_name='coche_id', string="Seguro")

class Conductor(models.Model):
    _name = 'coche.conductores'
    _dni = fields.Char(string='DNI', required=True)
    _coche_id = fields.Many2one(comodel_name='coche.coche', inverse_name='conductores_id', string="Coche")

class Seguro(models.Model):
    _name = 'coche.seguro'
    _compania = fields.Char(string='Compañia', required=True)
    _fecha_vencimiento = fields.Date(string='Fecha de vencimiento', required=True)
    _coche_id = fields.one2one(comodel_name='coche.coche', inverse_name='seguro_id', string="Coche")

class Viaje(models.Model):
    _name = 'coche.viajes'
    _coche_id = fields.Many2one(comodel_name='coche.coche', inverse_name='viajes_id', string="Coche")
    _origen = fields.Many2one(comodel_name='coche.provincia', inverse_name='viajes_id', string="Origen")
    _destino = fields.Many2one(comodel_name='coche.provincia', inverse_name='viajes_id', string="Destino")
    _fecha = fields.Date(string='Fecha', required=True)
    _duracion = fields.Boolean(string='Duración', required=True)
    _seguro_caducado = fields.Boolean(string='Seguro caducado', required=True)

class Provincia(models.Model):
    _name = 'coche.provincia'
    _nombre = fields.Char(string='Nombre', required=True)