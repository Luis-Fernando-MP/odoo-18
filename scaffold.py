import os
import sys

# ⚙️ Parámetros
nombre_modulo = sys.argv[1] if len(sys.argv) > 1 else "modulo_demo"
ruta_base = "./addons"
ruta_modulo = os.path.join(ruta_base, nombre_modulo)

# 📁 Estructura básica
estructura = [
    ruta_modulo,
    f"{ruta_modulo}/models",
    f"{ruta_modulo}/views",
    f"{ruta_modulo}/security",
    f"{ruta_modulo}/data",
    f"{ruta_modulo}/static/description"
]

# 📝 Archivos por defecto
archivos = {
    "__init__.py": "",
    "models/__init__.py": "",
    "models/model.py": '''from odoo import models, fields

class MiModelo(models.Model):
    _name = 'mi.modelo'
    _description = 'Mi Modelo'
    name = fields.Char(string='Nombre')
''',
    "views/view.xml": '''<odoo>
    <record id="view_form_mi_modelo" model="ir.ui.view">
        <field name="name">mi.modelo.form</field>
        <field name="model">mi.modelo</field>
        <field name="arch" type="xml">
            <form string="Mi Modelo">
                <field name="name"/>
            </form>
        </field>
    </record>
</odoo>''',
    "security/ir.model.access.csv": "id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n",
    "__manifest__.py": f'''{{
    'name': '{nombre_modulo}',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Resumen del módulo {nombre_modulo}',
    'description': 'Descripción larga del módulo',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/view.xml'
    ],
    'installable': True,
    'application': True,
}}'''
}

# 🛠️ Crear carpetas
for carpeta in estructura:
    os.makedirs(carpeta, exist_ok=True)

# 🛠️ Crear archivos
for ruta_relativa, contenido in archivos.items():
    ruta_archivo = os.path.join(ruta_modulo, ruta_relativa)
    with open(ruta_archivo, "w") as f:
        f.write(contenido)

print(f"✅ Módulo '{nombre_modulo}' creado en '{ruta_modulo}'")
