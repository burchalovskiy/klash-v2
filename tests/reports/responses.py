car_info_vin_response = {
    'response': {
        'id': 'a9951a97-3ef3-4429-ad6b-5cab25906bf0',
        'cost': None,
        'method': 'car_info',
        'request': {'vin_number': 'Z94CB41AAFR256583'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'number_plate': 'Т733АЕ178',
                'vin_number': 'Z94CB41AAFR256583',
                'chassis_number': '0TCYTCTBYET',
                'car_body_number': 'Z94CB41AAFR256583',
                'manufacturing_year': 2014,
                'credential': {
                    'credential_type': 'VEHICLE_REGISTRATION',
                    'issue_date': '2016-12-08',
                    'number': '416417',
                    'series': '7848',
                },
                'engine_power': 107.0,
                'max_mass': 1565,
                'seats_count': 5,
                'car_type': '23',
                'car_model': 'Rio',
                'car_mark': 'Kia',
                'car_modification': '',
                'td_mark': 'kia',
                'td_model': 'rio',
                'td_modification': '1.4 comfort ac',
                'power_kwt': 79.0,
                'engine_model': '1.4 i',
                'engine_number': 'EW626008',
                'engine_volume': 1396.0,
                'car_category': 'B',
                'color': 'ГОЛУБОЙ',
                'doors_count': 4,
                'drive_type': 'Передний',
                'fuel_name': 'Бензин',
                'weight_netto': 1118.0,
                'steer_side': 'left',
            }
        ],
    }
}

car_info_np_response = {
    'response': {
        'id': '7cbc6bff-e475-4a33-86d0-cb2b93b6fef4',
        'cost': None,
        'method': 'car_info',
        'request': {'number_plate': 'Т733АЕ178'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'number_plate': 'Т733АЕ178',
                'vin_number': 'Z94CB41AAFR256583',
                'chassis_number': '0TCYTCTBYET',
                'car_body_number': 'Z94CB41AAFR256583',
                'manufacturing_year': 2014,
                'credential': {
                    'credential_type': 'VEHICLE_REGISTRATION',
                    'issue_date': '2016-12-08',
                    'number': '416417',
                    'series': '7848',
                },
                'engine_power': 107.0,
                'max_mass': 1565,
                'seats_count': 5,
                'car_type': '23',
                'car_model': 'Rio',
                'car_mark': 'Kia',
                'car_modification': '',
                'td_mark': 'kia',
                'td_model': 'rio',
                'td_modification': '1.4 comfort ac',
                'power_kwt': 79.0,
                'engine_model': '1.4 i',
                'engine_number': 'EW626008',
                'engine_volume': 1396.0,
                'car_category': 'B',
                'color': 'ГОЛУБОЙ',
                'doors_count': 4,
                'drive_type': 'Передний',
                'fuel_name': 'Бензин',
                'weight_netto': 1118.0,
                'steer_side': 'left',
            }
        ],
    }
}

policy_info_response = {
    'response': {
        'id': 'f559ea6e-0f6e-4f24-97d6-4f965e17df4a',
        'cost': None,
        'method': 'policy_info_full',
        'request': {'number_plate': 'T138AE178'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'series': 'ТТТ',
                'number': '7012317906',
                'company': 'АО \"СК ГАЙДЕ\"',
                'status': 'Действует',
                'start_date': '2022-02-08',
                'end_date': '2023-02-07',
                'date_created': '2022-02-05',
                'vin_number': 'WAUZZZ8K19A048439',
                'body_number': '',
                'chassis_number': '',
                'license_plate': 'Т138АЕ178',
                'KBM': 0.5,
                'region': 'г Санкт-Петербург',
                'price': 5505.17,
                'usage_period': 'Период использования ТС активен на запрашиваемую дату',
                'mark_model': 'Audi A4 -',
                'mark': '',
                'model': 'Audi A4, -',
                'engine_power': 160.0,
                'in_transit': False,
                'has_trailer': True,
                'usage_target': 'Личная',
                'category': 'B',
                'limitations': 'Ограничен список лиц, допущенных к управлению (допущено: 1 чел.)',
                'insurer': 'К***** АНДРЕЙ ИВАНОВИЧ 08.04.1975',
                'insurer_name': 'К***** АНДРЕЙ ИВАНОВИЧ',
                'insurer_birthday': '08.04.1975',
                'owner': 'К***** АНДРЕЙ ИВАНОВИЧ 08.04.1975',
                'owner_name': 'К***** АНДРЕЙ ИВАНОВИЧ',
                'owner_birthday': '08.04.1975',
                'period1_beg': '2022-02-08',
                'period1_end': '2023-02-07',
                'period2_beg': '',
                'period2_end': '',
                'period3_beg': '',
                'period3_end': '',
            }
        ],
    }
}

registrations_response = {
    'response': {
        'id': '92c03395-b319-490d-9044-46c8e1b43866',
        'cost': None,
        'method': 'registrations',
        'request': {'vin_number': 'X4XKR094200K24720'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'vehicle': {
                    'vin': 'X4XKR094200K24720',
                    'model_car': 'BMW X5 XDRIVE 35I ',
                    'body_number': 'X4XKR094200K24720',
                    'chassis_number': '',
                    'year': 2014,
                    'category': 'В',
                    'engine_volume': 2979,
                    'color': 'БЕЛЫЙ МЕТАЛЛИК',
                    'engine_number': '00098981',
                    'power_kwt': 225.1,
                    'power_hp': 306,
                    'type': '21',
                    'type_name': 'Легковые автомобили универсал',
                    'vehicle_passport': {'issue': 'ООО \'БМВ РУСЛАНД ТРЕЙДИНГ\'', 'number': '39НУ943176'},
                },
                'ownership_periods': [
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
                        'period_end': '',
                        'period_start': '2020-02-28',
                        'person_type': 'Natural',
                        'extended_person_type': 'Физическое лицо',
                        'last_operation': '03',
                        'last_operation_name': 'изменение собственника (владельца) в результате совершения сделки, вступления в наследство, слияние и разделение капитала у юридического лица, переход права по договору лизинга, судебные решения и др.',
                    },
                ],
            }
        ],
    }
}

fines_response = {
    'response': {
        'id': 'fb8ef5fc-91d4-4b22-a121-a6cb0d127eff',
        'cost': None,
        'method': 'fines',
        'request': {'number_plate': 'Т733АЕ178'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'uin': '18810578220908026688',
                'vehicle_model': '',
                'is_discount_active': False,
                'is_revoked': False,
                'amount': 500,
                'amount_to_pay': 0,
                'decision_date': '2022-09-08 20:59:59',
                'details': '12.09.2 - Превышение скорости движения ТС от 20 до 40 км/ч',
                'discount_date': '',
                'discount_size': 50,
                'alt_payer_id': '',
                'article': '',
                'offense_point': '',
                'offense_place': '',
                'is_paid': False,
                'division_name': 'УФК по г. Санкт-Петербургу',
                'document': '7848416417',
                'certificate': '',
                'pay_status': 3,
                'violation_date': '2022-09-04 10:53:26',
                'article_description': '12.09.2 - Превышение скорости движения ТС от 20 до 40 км/ч',
                'division_id': '',
                'recipient_account': '03100643000000017200',
                'recipient_corr_account': '40102810945370000005',
                'recipient_name': 'УФК по г. Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)',
                'recipient_bank_name': 'СЕВЕРО-ЗАПАДНОЕ ГУ БАНКА РОССИИ',
                'recipient_bic': '014030106',
                'recipient_inn': '7830002600',
                'recipient_kpp': '781345001',
                'recipient_kbk': '18811601121010001140',
                'recipient_okato': '40394000',
                'providers': 0,
                'photo': False,
                'request_token': '',
                'payer_name': '-',
                'origin_uin': '',
                'dit_external_id': '',
                'offense_lon': '',
                'offense_lat': '',
                'legal_act': '12.09.2 - Превышение скорости движения ТС от 20 до 40 км/ч',
                'purpose': 'Оплата штрафа по постановлению 18810578220908026688 от 08.09.2022',
            },
            {
                'uin': '18810578211032027947',
                'vehicle_model': '',
                'is_discount_active': False,
                'is_revoked': False,
                'amount': 500,
                'amount_to_pay': 0,
                'decision_date': '2021-10-01 00:00:00',
                'details': '',
                'discount_date': '',
                'discount_size': 50,
                'alt_payer_id': '',
                'article': '',
                'offense_point': '',
                'offense_place': '',
                'is_paid': True,
                'division_name': 'УФК по г. Санкт-Петербургу',
                'document': '7848416417',
                'certificate': '',
                'pay_status': 3,
                'violation_date': '2021-09-26 13:24:44',
                'article_description': '12.09.2 - Превышение скорости движения ТС от 20 до 40 км/ч',
                'division_id': '',
                'recipient_account': '03100643000000017200',
                'recipient_corr_account': '40102810945370000005',
                'recipient_name': 'УФК по г. Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)',
                'recipient_bank_name': 'СЕВЕРО-ЗАПАДНОЕ ГУ БАНКА РОССИИ',
                'recipient_bic': '014030106',
                'recipient_inn': '7830002600',
                'recipient_kpp': '781345001',
                'recipient_kbk': '18811601121010001140',
                'recipient_okato': '40394000',
                'providers': 0,
                'photo': False,
                'request_token': '',
                'payer_name': '-',
                'origin_uin': '',
                'dit_external_id': '',
                'offense_lon': '',
                'offense_lat': '',
                'legal_act': 'Часть 2 статьи 12.9 КоАП',
                'purpose': 'Оплата штрафа по постановлению 18810578211032027947 от 01.10.2021',
            },
            {
                'uin': '18810578210910114907',
                'vehicle_model': '',
                'is_discount_active': False,
                'is_revoked': False,
                'amount': 500,
                'amount_to_pay': 0,
                'decision_date': '2021-09-10 00:00:00',
                'details': '',
                'discount_date': '',
                'discount_size': 50,
                'alt_payer_id': '',
                'article': '',
                'offense_point': '',
                'offense_place': '',
                'is_paid': True,
                'division_name': 'УФК по г. Санкт-Петербургу',
                'document': '7848416417',
                'certificate': '',
                'pay_status': 3,
                'violation_date': '2021-08-22 16:57:07',
                'article_description': '12.09.2 - Превышение скорости движения ТС от 20 до 40 км/ч',
                'division_id': '',
                'recipient_account': '03100643000000017200',
                'recipient_corr_account': '40102810945370000005',
                'recipient_name': 'УФК по г. Санкт-Петербургу (УГИБДД ГУ МВД России по г. Санкт-Петербургу и Ленинградской области)',
                'recipient_bank_name': 'СЕВЕРО-ЗАПАДНОЕ ГУ БАНКА РОССИИ',
                'recipient_bic': '014030106',
                'recipient_inn': '7830002600',
                'recipient_kpp': '781345001',
                'recipient_kbk': '18811601121010001140',
                'recipient_okato': '40394000',
                'providers': 0,
                'photo': False,
                'request_token': '',
                'payer_name': '-',
                'origin_uin': '',
                'dit_external_id': '',
                'offense_lon': '',
                'offense_lat': '',
                'legal_act': 'Часть 2 статьи 12.9 КоАП',
                'purpose': 'Оплата штрафа по постановлению 18810578210910114907 от 10.09.2021',
            },
        ],
    }
}

wanted_info_response = {
    'response': {
        'id': '4cbde06e-d3f6-46e0-a0f6-3a187b767ca5',
        'cost': None,
        'method': 'wanted',
        'request': {'vin_number': 'X4XKS694200W54223'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'w_rec': 1,
                'w_reg_inic': 'Ставропольский край',
                'w_kuzov': 'X4XKS694200W54223',
                'w_model': 'БМВХ5',
                'w_data_pu': '27.04.2022',
                'w_vin': 'X4XKS694200W54223',
                'w_god_vyp': '2017',
                'w_vid_uch': 'Т',
                'w_un_gic': '1667721',
            }
        ],
    }
}

restricted_info_response = {
    'response': {
        'id': 'b30870c4-8666-4c5f-99dc-33b77e3e18f3',
        'cost': None,
        'method': 'restricted',
        'request': {'vin_number': 'XWB3L32CD8A010799'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'tsVIN': 'XWB3L32CD8A010799',
                'ogrkod': '1',
                'divid': '3021',
                'codeTo': 47,
                'dateogr': '06.06.2022',
                'regname': 'Орловская область',
                'osnOgr': 'Документ: 295425163/5702 от 06.06.2022, Палютина Анастасия Валерьевна, СПИ: 54021039377338, ИП: 66151/21/57002-ИП от 04.08.2021',
                'tsmodel': 'Нет данных',
                'dateadd': '06.06.2022',
                'gid': '57#SP505379524',
                'divtype': '2',
                'tsKuzov': 'XWB3L32CD8A010799',
                'regid': '1154',
                'codDL': 0,
                'tsyear': '2008',
                'phone': '+7(4862)59-63-76',
            },
            {
                'tsVIN': 'XWB3L32CD8A010799',
                'ogrkod': '2',
                'divid': '3021',
                'codeTo': 47,
                'dateogr': '06.06.2022',
                'regname': 'Орловская область',
                'osnOgr': 'Документ: 295425164/5702 от 06.06.2022, Палютина Анастасия Валерьевна, СПИ: 54021039377338, ИП: 66150/21/57002-ИП от 04.08.2021',
                'tsmodel': 'Нет данных',
                'dateadd': '06.06.2022',
                'gid': '57#SP505379516',
                'divtype': '1',
                'tsKuzov': 'XWB3L32CD8A010799',
                'regid': '1154',
                'codDL': 0,
                'tsyear': '2008',
                'phone': '+7(4862)59-63-76',
            },
        ],
    }
}

pts_response = {
    'response': {
        'id': '081d47f3-9c11-4a27-99f2-2635744f345a',
        'cost': None,
        'method': 'pts',
        'request': {'vin_number': 'XW7BZYHK40S112140'},
        'is_error': False,
        'is_completed': True,
        'result': [{'pts': '164301007879448'}],
    }
}

taxi_response = {
    'response': {
        'id': 'd976b657-70f8-4f09-9ab4-ef36e21cccf1',
        'cost': None,
        'method': 'taxi',
        'request': {'vin_number': 'XTA21101050803637'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'update_date': '26.09.2022',
                'license_date': '04.02.2019',
                'name': 'Решетов Сергей Валентинович',
                'ogrn_num': '',
                'inn': '',
                'brand_model': 'ВАЗ, 2110 1',
                'reg_num': 'А518СЕ12',
                'blank_no': '004211',
                'full_name': '',
                'validity_date': '04.02.2024',
                'region': 'Республика Марий Эл',
                'region_num': '12',
                'condition': 'Аннулировано',
                'yellow_color': 0,
                'yellow_reg_num': 0,
                'used_in_taxi': True,
                'color': '',
                'manufacturing_year': 0,
                'norm_mark': '',
                'norm_model': '',
            }
        ],
    }
}

mileage_info_response_bad = {
    'response': {
        'id': '73ebf90d-44e5-4146-abe1-f67f65603290',
        'cost': None,
        'method': 'mileage',
        'request': {'vin_number': 'WVGZZZ7LZ8D059209'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'car_body': 'WVGZZZ7LZ8D059209',
                'car_chassis': '',
                'car_mileage': 200000,
                'car_number': 'Е707РА35',
                'car_vin': 'WVGZZZ7LZ8D059209',
                'date_of_diagnosis': '07.04.2020',
                'date_of_validity': '08.04.2021',
                'eaisto_number': '097280012001531',
                'is_valid': False,
                'operator_number': '09727',
                'region': '',
            },
            {
                'car_body': 'WVGZZZ7LZ8D059209',
                'car_chassis': '',
                'car_mileage': 250000,
                'car_number': 'Е707РА35',
                'car_vin': 'WVGZZZ7LZ8D059209',
                'date_of_diagnosis': '07.04.2022',
                'date_of_validity': '08.04.2023',
                'eaisto_number': '097280012001531',
                'is_valid': True,
                'operator_number': '09729',
                'region': '',
            },
            {
                'car_body': 'WVGZZZ7LZ8D059209',
                'car_chassis': '',
                'car_mileage': 300000,
                'car_number': 'Е707РА35',
                'car_vin': 'WVGZZZ7LZ8D059209',
                'date_of_diagnosis': '07.04.2021',
                'date_of_validity': '08.04.2022',
                'eaisto_number': '097280012001531',
                'is_valid': False,
                'operator_number': '09728',
                'region': '',
            },
        ],
    }
}

mileage_info_response_good = {
    'response': {
        'id': '73ebf90d-44e5-4146-abe1-f67f65603290',
        'cost': None,
        'method': 'mileage',
        'request': {'vin_number': 'WVGZZZ7LZ8D059209'},
        'is_error': False,
        'is_completed': True,
        'result': [
            {
                'car_body': 'WVGZZZ7LZ8D059209',
                'car_chassis': '',
                'car_mileage': 200000,
                'car_number': 'Е707РА35',
                'car_vin': 'WVGZZZ7LZ8D059209',
                'date_of_diagnosis': '07.04.2020',
                'date_of_validity': '08.04.2021',
                'eaisto_number': '097280012001531',
                'is_valid': False,
                'operator_number': '09727',
                'region': '',
            },
            {
                'car_body': 'WVGZZZ7LZ8D059209',
                'car_chassis': '',
                'car_mileage': 300000,
                'car_number': 'Е707РА35',
                'car_vin': 'WVGZZZ7LZ8D059209',
                'date_of_diagnosis': '07.04.2022',
                'date_of_validity': '08.04.2023',
                'eaisto_number': '097280012001531',
                'is_valid': True,
                'operator_number': '09729',
                'region': '',
            },
            {
                'car_body': 'WVGZZZ7LZ8D059209',
                'car_chassis': '',
                'car_mileage': 250000,
                'car_number': 'Е707РА35',
                'car_vin': 'WVGZZZ7LZ8D059209',
                'date_of_diagnosis': '07.04.2021',
                'date_of_validity': '08.04.2022',
                'eaisto_number': '097280012001531',
                'is_valid': False,
                'operator_number': '09728',
                'region': '',
            },
        ],
    }
}
