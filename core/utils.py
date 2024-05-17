import pandas as pd
from django.db.models import QuerySet

from core.models import AccreditationStatus
from international_accreditation.models import InternationalAccreditation


def split_space(name: str) -> tuple[str, str]:
    try:
        first_name, last_name = name.split(' ', 1)

    except ValueError:
        first_name = name
        last_name = ''

    return first_name, last_name


def get_data_frame(queryset: QuerySet) -> pd.DataFrame:
    model = queryset.model

    fields = [
        'id',
        'passport_id',
        'first_name',
        'last_name',
        'birthday',
        'country__nationality',
        'type',
        'status',
    ]

    if model == InternationalAccreditation:
        fields.append('flight_arrival_datetime')
        fields.append('flight_departure_datetime')

    data = queryset.values(*fields)
    df = pd.DataFrame(data)

    df['second_name'] = df['first_name'].apply(lambda x: split_space(x)[1])
    df['first_name'] = df['first_name'].apply(lambda x: split_space(x)[0])

    df['second_last_name'] = df['last_name'].apply(lambda x: split_space(x)[1])
    df['last_name'] = df['last_name'].apply(lambda x: split_space(x)[0])

    df['birthday'] = df['birthday'].apply(lambda x: x.strftime('%d-%m-%Y'))

    df['type'] = df['type'].apply(lambda x: str(model.AccreditationType(x).label) if not pd.isnull(x) else 'N/A')
    df['status'] = df['status'].apply(lambda x: str(AccreditationStatus(x).label))

    if model == InternationalAccreditation:
        df['flight_arrival_datetime'] = df['flight_arrival_datetime'].apply(
            lambda x: x.strftime('%d-%m-%Y %H:%M') if not pd.isnull(x) else 'N/A')
        df['flight_departure_datetime'] = df['flight_departure_datetime'].apply(
            lambda x: x.strftime('%d-%m-%Y %H:%M') if not pd.isnull(x) else 'N/A')

    # Rename columns and change order
    df_fields = [
        'id',
        'first_name',
        'second_name',
        'last_name',
        'second_last_name',
        'passport_id',
        'birthday',
        'country__nationality',
        'type',
        'status',
    ]

    if model == InternationalAccreditation:
        df_fields.append('flight_arrival_datetime')
        df_fields.append('flight_departure_datetime')

    df = df[df_fields]

    rename_fields = {
        'id': 'ID',
        'first_name': 'Primer Nombre',
        'second_name': 'Segundo Nombre',
        'last_name': 'Primer Apellido',
        'second_last_name': 'Segundo Apellido',
        'passport_id': 'Cédula',
        'birthday': 'Fecha de Nacimiento',
        'country__nationality': 'Nacionalidad',
        'type': 'Tipo',
        'status': 'Estado',
    }

    if model == InternationalAccreditation:
        rename_fields['passport_id'] = 'Pasaporte'
        rename_fields['flight_arrival_datetime'] = 'Fecha y Hora de Llegada'
        rename_fields['flight_departure_datetime'] = 'Fecha y Hora de Salida'

    df = df.rename(columns=rename_fields)
    return df
