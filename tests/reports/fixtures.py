basic_report_vin = {
    'id': '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4',
    'request_type': 'vin_number',
    'request_info': 'Z94CB41AAFR256583',
    'is_completed': True,
    'report': {
        'number_plate': 'Т733АЕ178',
        'vin_number': 'Z94CB41AAFR256583',
        'car_body_number': 'Z94CB41AAFR256583',
        'manufacturing_year': 2014,
        'car_model': 'Rio',
        'car_mark': 'Kia',
        'engine_power': 107.0,
        'engine_volume': 1396.0,
        'car_category': 'B',
        'color': 'ГОЛУБОЙ',
        'steer_side': 'left',
        'credential': {
            'credential_type': 'VEHICLE_REGISTRATION',
            'issue_date': '2016-12-08',
        },
    },
}

basic_report_np = {
    'id': '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4',
    'request_type': 'number_plate',
    'request_info': 'Т733АЕ178',
    'is_completed': True,
    'report': {
        'number_plate': 'Т733АЕ178',
        'vin_number': 'Z94CB41AAFR256583',
        'car_body_number': 'Z94CB41AAFR256583',
        'manufacturing_year': 2014,
        'car_model': 'Rio',
        'car_mark': 'Kia',
        'engine_power': 107.0,
        'engine_volume': 1396.0,
        'car_category': 'B',
        'color': 'ГОЛУБОЙ',
        'steer_side': 'left',
        'credential': {
            'credential_type': 'VEHICLE_REGISTRATION',
            'issue_date': '2016-12-08',
        },
    },
}

free_report_vin = {
    'id': '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4',
    'request_type': 'vin_number',
    'request_info': 'Z94CB41AAFR256583',
    'is_completed': True,
    'report': {
        'number_plate': 'Т733АЕ178',
        'vin_number': 'Z94CB41AAFR25**83',
        'car_body_number': 'Z94CB41AAFR25**83',
        'manufacturing_year': 2014,
        'car_model': 'Rio',
        'car_mark': 'Kia',
        'engine_power': 107.0,
        'engine_volume': 1396.0,
        'car_category': 'B',
        'color': 'ГОЛУБОЙ',
    },
}

free_report_np = {
    'id': '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4',
    'request_type': 'number_plate',
    'request_info': 'Т733АЕ178',
    'is_completed': True,
    'report': {
        'number_plate': 'Т733АЕ178',
        'vin_number': 'Z94CB41AAFR25**83',
        'car_body_number': 'Z94CB41AAFR25**83',
        'manufacturing_year': 2014,
        'car_model': 'Rio',
        'car_mark': 'Kia',
        'engine_power': 107.0,
        'engine_volume': 1396.0,
        'car_category': 'B',
        'color': 'ГОЛУБОЙ',
    },
}

registration = {
    'is_completed': True,
    'registration_report': {
        'owners_number': 3,
        'registration_periods': [
            {
                'period_end': '2019-01-09',
                'period_start': '2006-02-18',
                'person_type': 'Natural',
                'extended_person_type': 'Физическое лицо',
                'last_operation': '07',
                'last_operation_name': 'прекращение регистрации в том числе',
            },
            {
                'period_end': '2020-02-28',
                'period_start': '2019-03-05',
                'person_type': 'Natural',
                'extended_person_type': 'Физическое лицо',
                'last_operation': '02',
                'last_operation_name': 'регистрация ранее зарегистрированных в регистрирующих органах',
            },
            {
                'period_end': None,
                'period_start': '2020-02-28',
                'person_type': 'Natural',
                'extended_person_type': 'Физическое лицо',
                'last_operation': '03',
                'last_operation_name': 'изменение собственника (владельца) в результате совершения сделки, вступления в наследство, слияние и разделение капитала у юридического лица, переход права по договору лизинга, судебные решения и др.',
            },
        ],
    },
}

fines = {
    'is_completed': True,
    'fines_report': {
        'paid_quantity': 2,
        'paid_amount': 1000,
        'unpaid_quantity': 1,
        'unpaid_amount': 500,
        'total_quantity': 3,
        'total_amount': 1500,
        'fines_list': [
            {'amount': 500, 'decision_date': '2022-09-08 20:59:59', 'is_paid': False},
            {'amount': 500, 'decision_date': '2021-10-01 00:00:00', 'is_paid': True},
            {'amount': 500, 'decision_date': '2021-09-10 00:00:00', 'is_paid': True},
        ],
    },
}

policy = {
    'is_completed': True,
    'policy_report': [
        {
            'series': 'ТТТ',
            'number': '7012317906',
            'company': 'АО \"СК ГАЙДЕ\"',
            'status': 'Действует',
            'start_date': '2022-02-08',
            'end_date': '2023-02-07',
            'region': 'г Санкт-Петербург',
            'usage_period': 'Период использования ТС активен на запрашиваемую дату',
            'usage_target': 'Личная',
        }
    ],
}

restricted = {
    'is_completed': True,
    'restricted_report': [
        {
            'restriction': 'Запрет на снятие с учета',
            'dateogr': '06.06.2022',
            'regname': 'Орловская область',
            'dateadd': '06.06.2022',
            'restrict_creator': 'Судебные органы',
        },
        {
            'restriction': 'Запрет на регистрационные действия',
            'dateogr': '06.06.2022',
            'regname': 'Орловская область',
            'dateadd': '06.06.2022',
            'restrict_creator': 'Судебный пристав',
        },
    ],
}

wanted = {
    'is_completed': True,
    'wanted_report': {
        'w_rec': 1,
        'w_reg_inic': 'Ставропольский край',
        'w_data_pu': '27.04.2022',
        'w_god_vyp': '2017',
        'w_vid_uch': 'Т',
        'w_un_gic': '1667721',
    },
}


mileage_bad = {
    'is_completed': True,
    'mileage_report': {
        'is_rollback_found': True,
        'diagnostics': [
            {'car_mileage': 200000, 'date_of_diagnosis': '07.04.2020', 'is_valid': False},
            {'car_mileage': 300000, 'date_of_diagnosis': '07.04.2021', 'is_valid': False},
            {'car_mileage': 250000, 'date_of_diagnosis': '07.04.2022', 'is_valid': True},
        ],
    },
}

mileage_good = {
    'is_completed': True,
    'mileage_report': {
        'is_rollback_found': False,
        'diagnostics': [
            {'car_mileage': 200000, 'date_of_diagnosis': '07.04.2020', 'is_valid': False},
            {'car_mileage': 250000, 'date_of_diagnosis': '07.04.2021', 'is_valid': False},
            {'car_mileage': 300000, 'date_of_diagnosis': '07.04.2022', 'is_valid': True},
        ],
    },
}

taxi = {
    'is_completed': True,
    'taxi_report': {
        'update_date': '26.09.2022',
        'license_date': '04.02.2019',
        'blank_no': '004211',
        'validity_date': '04.02.2024',
        'region': 'Республика Марий Эл',
        'condition': 'Аннулировано',
    },
}

pts = {'is_completed': True, 'pts_report': {'pts': '164301007879448', 'is_epts': True}}
