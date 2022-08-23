from django.core.validators import RegexValidator

curp_validador = RegexValidator(
    regex='^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$',
    message='El CURP no tiene un formato válido',
    code='curp_invalido'
)

telefono_validador = RegexValidator(
    regex='^(\d{10})$',
    message='Numero de telefono invalido',
    code='telCelular_invalido'
)

codigoPos_validador = RegexValidator(
    regex='^(\d{5})$',
    message='El Codigo postal no tiene un formato válido',
    code='codigoPostal_invalido'
)