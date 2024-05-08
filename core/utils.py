import pandas as pd

from core.models import AccreditationStatus


def split_space(name: str) -> tuple[str, str]:
    try:
        first_name, last_name = name.split(' ', 1)

    except ValueError:
        first_name = name
        last_name = ''

    return first_name, last_name


def get_data_frame(queryset) -> pd.DataFrame:
    model = queryset.model
    data = queryset.values(
        'id',
        'first_name',
        'last_name',
        'birthday',
        'country__nationality',
        'type',
        'status',
    )

    df = pd.DataFrame(data)

    df['second_name'] = df['first_name'].apply(lambda x: split_space(x)[1])
    df['first_name'] = df['first_name'].apply(lambda x: split_space(x)[0])

    df['second_last_name'] = df['last_name'].apply(lambda x: split_space(x)[1])
    df['last_name'] = df['last_name'].apply(lambda x: split_space(x)[0])

    df['birthday'] = df['birthday'].apply(lambda x: x.strftime('%d-%m-%Y'))

    df['type'] = df['type'].apply(lambda x: str(model.AccreditationType(x).label) if not pd.isnull(x) else 'N/A')
    df['status'] = df['status'].apply(lambda x: str(AccreditationStatus(x).label))

    # Rename columns and change order
    df = df[[
        'id',
        'first_name',
        'second_name',
        'last_name',
        'second_last_name',
        'birthday',
        'country__nationality',
        'type',
        'status',
    ]]

    df = df.rename(columns={
        'id': 'ID',
        'first_name': 'Primer Nombre',
        'second_name': 'Segundo Nombre',
        'last_name': 'Primer Apellido',
        'second_last_name': 'Segundo Apellido',
        'birthday': 'Fecha de Nacimiento',
        'country__nationality': 'Nacionalidad',
        'type': 'Tipo',
        'status': 'Estado',
    })

    return df
