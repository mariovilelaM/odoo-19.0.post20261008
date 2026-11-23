from odoo import fields, models
class Libro(models.Model):
    _name = 'biblioteca.libro' # nombre técnico del modelo
    _description = 'Libro' # nombre que entiende una persona
    # Los campos: cada uno será una columna de la tabla
    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor')
    isbn = fields.Char(string='ISBN')
    fecha_publicacion = fields.Date(string='Fecha de publicación')
    disponible = fields.Boolean(string='Disponible', default=True)
    paginas = fields.Integer(string='Número de páginas')
    genero = fields.Selection([
        ('novela', 'Novela'),
        ('tecnico', 'Técnico'),
        ('ensayo', 'Ensayo'),
    ], string='Género')

