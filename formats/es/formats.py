# mi_proyecto/formats/es/formats.py

# Números
DECIMAL_SEPARATOR = '.'
THOUSAND_SEPARATOR = ','
NUMBER_GROUPING = 3

# Fechas
# Django usa estas variables para formatear las fechas, p.ej. en plantillas y validaciones
DATE_FORMAT = 'm/d/Y'
SHORT_DATE_FORMAT = 'm/d/Y'
DATETIME_FORMAT = 'm/d/Y H:i'
SHORT_DATETIME_FORMAT = 'm/d/Y H:i'

# Cuando Django parsea fechas, mira DATE_INPUT_FORMATS (entre otros). 
# Esto permite que los formularios acepten mm/dd/yyyy.
DATE_INPUT_FORMATS = [
    '%m/%d/%Y',     # 12/31/2025
    '%m/%d/%y',     # 12/31/25
    # ... otras variantes si deseas
]
