# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import api, fields, models


class Recepcion(models.Model):
    _name = "recepcion.recepcion"

    _description = "Registros de Recepcion_Antidoping"
    # hhh
    fecha = fields.Date(string="Fecha", required=True)

    # Realizar  el numero secuencial
    folio = fields.Char(string="Folio", readonly=True, required=True, copy=False, default='Nuevo')
    @api.model
    def create(self, val):
        x = self.env['ir.sequence'].next_by_code('library.card') or '/'
        val['folio'] = x
        return super(Recepcion, self).create(val)


    #busqueda

            #fin de numero de secuencia

   # SSP-COMI
    #123456789


    nombre_completo = fields.Many2one('hr.employee',string='Nombre_completo',required=True )

    #prueba
    responsable_nombre = fields.Char("Nombre_completo",
                                     related="nombre_completo.fullname")
    responsable_nombre1 = fields.Char("Numero_Empleado",
                                      related="nombre_completo.employee_number")
    responsable_nombre2 = fields.Selection(string="Sexo",
                                           related="nombre_completo.gender")
    responsable_nombre3 = fields.Date("Fecha",
                                      related="nombre_completo.birthday")
    responsable_nombre4 = fields.Integer("Edad",
                                         related="nombre_completo.age")
    departamento = fields.Many2one('hr.department', string='Departamento',related='nombre_completo.department_id',required=True)

    examen_a_realizar = fields.Selection(string='Examen_a_Realizar',
                                         selection=[("Orina", "Orina"), ("Sangre", "Sangre")])
    lugar_de_muestra = fields.Selection(string='Lugar de Muestra',
                                        selection=[("Cuartel General", "Cuartel General"), ("Zona 2", "Zona 2")])
    identificacion_que_presenta = fields.Selection(string='Motivo del Examen',
                                                   selection=[("Inclusión a la LOC 109", "Inclusión a la LOC 109"),
                                                              ("Revalidación a la LOC 109",
                                                               "Revalidación a la LOC 109")])
    motivo_de_examen = fields.Selection(string='Identificacion', selection=[("INE", "INE"), ("ISSSTELEON", "ISSSTELEON")])
    consume_medicamentos = fields.Selection(string='¿Consumo de medicamentos?', selection=[("Si", "Si"), ("No", "No")])
    nombre_del_medicamento = fields.Char(string="En caso de afirmación, escriba el nombre del medicamento ",
                                         required=True)
    motivo_de_consumo = fields.Char(string="Motivo de consumo", required=True)
    nombre_del_medico = fields.Char(string="Nombre del médico o Institución que lo indicó", required=True)
    observaciones = fields.Char(string="Observaciones", required=True)

   # el siguiente proceso de antidoping
    ###
    clv = fields.Boolean('Proceso De Antidoping', default=False)
    hora = fields.Datetime(string="Hora")
    quien_tomo_muestra = fields.Selection(string='Quien Tomo la Muestra',
                                      selection=[
                                          ("CRISTOPHER DAVID LOPEZ GONZALEZ", "CRISTOPHER DAVID LOPEZ GONZALEZ"),
                                          ("CESAR OMAR LOPEZ RAMIREZ", "CESAR OMAR LOPEZ RAMIREZ"),
                                          ("JESUS FERNANDO MEDINA LOPEZ", "JESUS FERNANDO MEDINA LOPEZ"),
                                          ("YAHAIRA MONTSERRAT BRIONES LOERA", "YAHAIRA MONTSERRAT BRIONES LOERA"),
                                          ("ROBERTO ANTONIO ORTIZ TREVIÑO", "ROBERTO ANTONIO ORTIZ TREVIÑO")])
    quien_analizo = fields.Selection(string='Quien Tomo la Muestra',
                                 selection=[("CRISTOPHER DAVID LOPEZ GONZALEZ", "CRISTOPHER DAVID LOPEZ GONZALEZ"),
                                            ("CESAR OMAR LOPEZ RAMIREZ", "CESAR OMAR LOPEZ RAMIREZ"),
                                            ("JESUS FERNANDO MEDINA LOPEZ", "JESUS FERNANDO MEDINA LOPEZ"),
                                            ("YAHAIRA MONTSERRAT BRIONES LOERA", "YAHAIRA MONTSERRAT BRIONES LOERA"),
                                            ("ROBERTO ANTONIO ORTIZ TREVIÑO", "ROBERTO ANTONIO ORTIZ TREVIÑO")])
    canabis = fields.Selection(string='Canabis', selection=[("Positivo", "Positivo"), ("Negativo", "Negativo")])
    comentario = fields.Char(string="Comentario")
    cocaina = fields.Selection(string='Cocaina', selection=[("Positivo", "Positivo"), ("Negativo", "Negativo")])
    comentario1 = fields.Char(string="Comentario")
    anfetaminas = fields.Selection(string='Anfetaminas', selection=[("Positivo", "Positivo"), ("Negativo", "Negativo")])
    comentario2 = fields.Char(string="Comentario")
    barbituricos = fields.Selection(string='Barbituricos',
                                selection=[("Positivo", "Positivo"), ("Negativo", "Negativo")])
    comentario3 = fields.Char(string="Comentario")
    benzodiacepinas = fields.Selection(string='Benzodiacepinas',
                                  selection=[("Positivo", "Positivo"), ("Negativo", "Nagativo")])
    comentario4 = fields.Char(string="Comentario")


    foto = fields.Binary(string="Foto")
