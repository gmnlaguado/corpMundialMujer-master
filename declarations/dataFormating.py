# coding=utf-8
import datetime
from declarations import querys
from codes import snippets


def GeneralInformationData(information):
    org = [
        information.project,  # 0
        information.id_name.text,  # 1
        information.id_lastName.text,  # 2
        information.id_documentType.text,  # 3
        information.payeeDocument,  # 4
        information.id_expeditionCity.text,  # 5
        information.id_birthdate.text,  # 6
        information.id_cities.text,  # 7
        information.id_departments.text,  # 8
        information.id_country.text,  # 9
        information.id_sign.text,  # 10
        information.id_address.text,  # 11
        information.id_neighborhoods.text,  # 12
        'information.Indicative.text',  # 13
        information.id_telephone.text,  # 14
        information.id_cellphone.text,  # 15
        information.id_email.text,  # 16
        information.operator,  # 17
        information.id_cellphone2.text,  # 18
        information.id_payeeType.text,  # 19
        'information.DateToday.text',  # 20
        information.id_ageRange.text,  # 21
        information.id_nationality.text,  # 22
        information.id_environment.text,  # 23
        information.id_tier.text,  # 24
        information.id_sex.text,  # 25
        information.id_gender.text,  # 26
        information.id_ethnicGroup.text,  # 27
        information.id_disability.text  # 28
    ]
    # Normalizing
    org[0] = querys.idProject(org[0].lower())
    org[3] = querys.idParametrics('tipo_de_documento', org[3])
    org[5] = querys.idParametrics('ciudades', org[5])
    org[6] = snippets.formattingDate(org[6])
    org[7] = querys.idParametrics('ciudades', org[7])
    org[8] = querys.idParametrics('departamentos', org[8])
    org[9] = querys.idParametrics('paises', org[9].lower())
    org[10] = querys.idParametrics('rotulos', org[10])
    if org[12] == 'Otro':
        org[12] = '9999'
    else:
        org[12] = querys.idParametrics('barrios', org[12].upper())
    org[13] = querys.indicator(org[8])
    org[14] = int(org[14])
    org[15] = int(org[15])
    org[18] = int(org[18])
    org[19] = querys.idParametrics('tipo_de_beneficiario', org[19])
    org[20] = str(datetime.date.today())
    org[21] = querys.idParametrics('rangos_de_edad', org[21])
    org[22] = querys.idParametrics('paises', org[22].lower())
    org[23] = querys.idParametrics('entornos', org[23])
    org[24] = int(org[24])
    org[25] = querys.idParametrics('sexo', org[25])
    org[26] = querys.idParametrics('genero', org[26])
    org[27] = querys.idParametrics('grupo_etnico', org[27])
    org[28] = querys.idParametrics('discapacidades', org[28])

    org = tuple(org)
    querys.cargar('informacion_general_beneficiario', 29, org)

    unique_id = org[0]+'__'+org[17]+'__'+org[4]
    pro = [
        unique_id,
        org[0],
        org[17],
        org[4],
        org[20],
        1
    ]
    payeeProjectsData(pro, True)


def payeeProjectsData(info, clean):
    if clean:
        for i in range(7):
            info.append(2)
        info.append(1)
        info = tuple(info)
        querys.cargar('beneficiario_proyectos', 14, info)


def productionProfileDiagData(info):
    info = tuple(info)
    querys.cargar('diagnostico_de_perfil_productivo', 71, info)


def bussinesIdeaData(info):
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator,  # 2
        info.id_entrepreneurship.text,  # 3
        info.id_bussinesSector.text,  # 4
        info.id_ciiu.text,  # 5
        info.id_departments.text,  # 6
        info.id_cities.text,  # 7
        info.id_howArise.text,  # 8
        info.id_dedicationTime.text,  # 9
        info.id_studies.text,  # 10
        info.id_haveExperience.text,  # 11
        info.id_productServices.text,  # 12
        info.productServicesList,  # 13
        info.id_agricultural.text,  # 14
        info.id_briefcase.text,  # 15
        info.id_assetInvestment.text,  # 16
        info.id_initialInvestment.text,  # 17
        info.id_investmentPercent.text,  # 18
        info.id_capitalWorkInvestment.text,  # 19
        info.id_firstMonthSales.text,  # 20
        info.id_firstYearSales.text,  # 21
        info.id_needColabs.text,  # 22
        info.colaboratorsList,  # 23
        info.id_weeklyTime.text,  # 24
        info.id_whyNot.text,  # 25
        info.id_months.text,  # 26
        info.id_imagine.text,  # 27
        'date'  # 28
    ]
    if org[5][0] == '0':
        org[5] = org[5][1:]
    org[0] = querys.idProject(org[0].lower())
    org[4] = querys.idParametrics('sector_empresarial', org[4])
    org[5] = int(org[5])
    org[6] = querys.idParametrics('departamentos', org[6])
    org[7] = querys.idParametrics('ciudades', org[7])
    org[8] = querys.idParametrics('como_surge', org[8])
    org[9] = querys.idParametrics('tiempo_a_dedicar', org[9])
    org[10] = querys.idParametrics('estudios', org[10])
    org[11] = querys.idParametrics('si_no', org[11])
    org[12] = querys.idParametrics('producto_o_servicio', org[12])
    org[14] = querys.idParametrics('si_no', org[14])
    org[16] = float(org[16].replace('.',''))
    org[17] = float(org[17].replace('.',''))
    org[18] = querys.idParametrics('porcentaje_de_inversion', org[18])
    org[19] = float(org[19].replace('.',''))
    org[20] = float(org[20].replace('.',''))
    org[21] = float(org[21].replace('.',''))
    org[22] = querys.idParametrics('si_no', org[22])
    if org[23] is None:
        org[23] = ""
    org[24] = querys.idParametrics('tiempo_semanal', org[24])
    org[25] = querys.idParametrics('por_que_no', org[25])
    org[26] = int(org[26])
    org[28] = str(datetime.date.today())

    unique_id = org[0] + '__' + org[2] + '__' + org[1]
    org.insert(0, unique_id)
    org = tuple(org)
    querys.cargar('idea_de_negocio', 30, org)


def bussinesUnitData(info):
    org = [
        info.project,                                       # 0
        info.payeeDocument,                                 # 1
        info.operator,                                      # 2
        info.id_unit.text,                                  # 3
        info.id_departments.text,                           # 4
        info.id_cities.text,                                # 5
        info.id_howManyPartners.text,                       # 6
        info.id_sign.text,                                  # 7
        info.id_address.text,                               # 8
        info.id_ciiu.text,                                  # 9
        "info.id_indicator.text",                           # 10
        info.id_phone.text,                                 # 11
        info.id_email.text,                                 # 12
        info.id_webPage.text,                               # 13
        info.id_description.text,                           # 14
        info.id_briefcase.text,                             # 15
        info.id_creation.text,                              # 16
        info.id_nit.text,                                   # 17
        info.id_liabilitiesDescription.text,                # 18
        info.id_regCamara.text,                             # 19
        info.id_withContract.text,                          # 20
        info.id_withoutContract.text,                       # 21
        info.id_cellphone.text,                             # 22
        info.id_cellphone2.text,                            # 23
        info.id_tier.text,                                  # 24
        "date"                                              # 25
    ]

    if org[5][0] == '0':
        org[5] = org[5][1:]

    org[0] = querys.idProject(org[0].lower())
    org[4] = querys.idParametrics('departamentos', org[4])
    org[5] = querys.idParametrics('ciudades', org[5])
    org[6] = int(org[6])
    org[7] = querys.idParametrics('rotulos', org[7])
    org[9] = int(org[9])
    org[10] = querys.indicator(org[4])
    org[11] = int(org[11])
    org[16] = snippets.formattingDate(org[16])
    org[19] = querys.idParametrics('si_no', org[19])
    org[20] = int(org[20])
    org[21] = int(org[21])
    org[22] = int(org[22])
    org[23] = int(org[23])
    org[24] = int(org[24])
    org[25] = str(datetime.date.today())
    unique_id = org[0] + '__' + org[2] + '__' + org[1]
    org.insert(0, unique_id)

    org = tuple(org)
    querys.cargar('unidad_de_negocio', 27, org)


def caracterizacion_ampliada(info):
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator,  # 2
        info.id_adittionalStudies.text,  # 3
        info.id_studies.text,  # 4
        info.id_workingRelationship.text,  # 5
        info.id_freelance.text,  # 6
        info.id_householdHead.text,  # 7
        info.id_householdMembers.text,  # 8
        info.id_healthRegime.text,  # 9
        info.id_maritalStatus.text,  # 10
        info.id_agreementType.text,  # 11
        info.id_rut.text,  # 12
        info.id_childrenNumber.text,  # 13
        info.id_dependants.text,  # 14
        info.id_coverTheFamily.text,  # 15
        info.id_agreementTime.text,  # 16
        info.id_averageIncomeContract.text,  # 17
        info.id_averageIncomeActivity.text,  # 18
        info.id_pension.text,  # 19
        info.id_arl.text,  # 20
        info.id_factorsThatPreventYou.text,  # 21
        info.id_observations.text  # 22
    ]

    org[0] = querys.idProject(org[0].lower())
    org[4] = querys.idParametrics('estudios', org[4])
    org[5] = querys.idParametrics('si_no', org[5])
    org[6] = querys.idParametrics('si_no', org[6])
    org[7] = querys.idParametrics('si_no', org[7])
    org[8] = int(org[8])
    org[9] = querys.idParametrics('regimen_de_salud', org[9])
    org[10] = querys.idParametrics('estado_civil', org[10])
    org[11] = querys.idParametrics('tipos_de_contrato', org[11])
    org[12] = querys.idParametrics('si_no', org[12])
    org[13] = int(org[13])
    org[14] = int(org[14])
    org[15] = querys.idParametrics('si_no', org[15])
    org[16] = int(org[16])
    org[17] = querys.idParametrics('promedio_de_ingresos', org[17])
    org[18] = querys.idParametrics('promedio_de_ingresos', org[18])
    org[19] = querys.idParametrics('si_no', org[19])
    org[20] = querys.idParametrics('si_no', org[20])
    unique_id = org[0] + '__' + org[2] + '__' + org[1]
    org.insert(0, unique_id)
    org = tuple(org)
    querys.cargar('caracterizacion_ampliada', 24, org)
    querys.registrar('beneficiario_proyectos', 'etapa_del_proceso', info.payeeDocument, org[1], 2)


def caracterizacion_ampliada_informacion_hijos(info, full_info):
    hijo = []
    counter = 0
    for inf in info:
        hijo.append(inf)
        if len(hijo) == 3:
            counter += 1
            hijo.insert(0, counter)
            hijo.insert(0, full_info.operator)
            hijo.insert(0, full_info.payeeDocument)
            hijo.insert(0, querys.idProject(full_info.project.lower()))
            hijo[4] = querys.idParametrics('discapacidades', hijo[4])
            hijo[5] = querys.idParametrics('si_no', hijo[5])
            hijo[6] = querys.idParametrics('genero', hijo[6])
            unique_id = hijo[0] + '__' + hijo[2] + '__' + hijo[1] + '__' + str(hijo[3])
            hijo.insert(0, unique_id)
            hijo = tuple(hijo)
            querys.cargar('caracterizacion_ampliada_informacion_hijos', 8, hijo)
            hijo = []


def caracterizacion_ampliada_informacion_personas_a_cargo(info, full_info):
    persona = []
    counter = 0
    for inf in info:
        persona.append(inf)
        if len(persona) == 3:
            counter += 1
            persona.insert(0, counter)
            persona.insert(0, full_info.operator)
            persona.insert(0, full_info.payeeDocument)
            persona.insert(0, querys.idProject(full_info.project.lower()))
            persona[4] = querys.idParametrics('discapacidades', persona[4])
            persona[5] = querys.idParametrics('si_no', persona[5])
            persona[6] = querys.idParametrics('genero', persona[6])
            unique_id = persona[0] + '__' + persona[2] + '__' + persona[1] + '__' + str(persona[3])
            persona.insert(0, unique_id)
            persona = tuple(persona)
            querys.cargar('caracterizacion_ampliada_informacion_personas_a_cargo', 8, persona)
            persona = []


def monitoreo(info):
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator,  # 2
        info.numero_de_monitoreo,   # 3
        info.ingresos_familia,  # 4
        info.gastos_familia,  # 5
        info.id_belongToAssosiation.text,  # 6
        info.id_ciiu.text,  # 7
        info.id_pension.text,  # 8
        info.id_bussinesSector.text,  # 9
        info.id_totalDependants.text,  # 10
        info.id_whoDefineIncome.text,  # 11
        info.id_houseType.text,  # 12
        info.id_houseMaterial.text,  # 13
        info.id_bedroomsNumber.text,  # 14
        info.id_kitchenFuel.text,  # 15
        info.id_tier.text,  # 16
        info.id_houseAge.text,  # 17
        info.id_cual_asociacion.text,  # 18
        info.id_asociacion_mujeres.text  # 19
    ]

    for grid in info.id_container_grid_1.children[::-1]:
        if len(grid.children) > 0:
            indice = [box.active for box in grid.children].index(True)
            if indice == 0:
                indice = 2
            org.append(indice)
    org[0] = querys.idProject(info.project.lower())
    org[4] = float(org[4])
    org[5] = float(org[5])
    org[6] = querys.idParametrics('si_no', org[6])
    org[7] = int(org[7])
    org[8] = querys.idParametrics('si_no', org[8])
    org[9] = querys.idParametrics('sector_empresarial', org[9])
    org[10] = int(org[10])
    org[11] = querys.idParametrics('quien_define_el_ingreso', org[11])
    org[12] = querys.idParametrics('tipo_de_casa', org[12])
    org[13] = querys.idParametrics('material_de_la_casa', org[13])
    org[14] = int(org[14])
    org[15] = querys.idParametrics('combustible_de_cocina', org[15])
    org[16] = int(org[16])
    org[17] = querys.idParametrics('antiguedad_de_la_casa', org[17])
    org[19] = querys.idParametrics('si_no', org[19])

    unique_id = org[0] + '__' + org[2] + '__' + org[1] + '__' + str(org[3])
    org.insert(0, unique_id)

    lista_spinners = []
    lista_texts = []
    items_scroll = info.id_container_grid_2.children
    for item in items_scroll[::-1]:
        if len(item.children) > 0:
            lista_texts.append(item.children[0].text)
        try:
            if item.class_type == "spinner":
                lista_spinners.append(item.text)
        except AttributeError:
            pass
    lista_spinners[0] = querys.idParametrics('si_no', lista_spinners[0])
    lista_spinners[1] = querys.idParametrics('si_no', lista_spinners[1])
    lista_spinners[2] = querys.idParametrics('si_no', lista_spinners[2])
    lista_spinners[3] = querys.idParametrics('si_no', lista_spinners[3])
    lista_spinners[4] = querys.idParametrics('si_no', lista_spinners[4])
    lista_spinners[5] = int(lista_spinners[5])
    lista_spinners[6] = querys.idParametrics('si_no', lista_spinners[6])
    lista_spinners[7] = querys.idParametrics('bancamia', lista_spinners[7])
    lista_spinners[8] = querys.idParametrics('si_no', lista_spinners[8])
    lista_spinners[9] = querys.idParametrics('si_no', lista_spinners[9])
    lista_spinners[10] = querys.idParametrics('de_quien_depende', lista_spinners[10])
    lista_spinners[11] = int(lista_spinners[11])
    lista_spinners[12] = int(lista_spinners[12])
    lista_spinners[13] = querys.idParametrics('si_no', lista_spinners[13])
    lista_spinners[14] = querys.idParametrics('si_no', lista_spinners[14])
    lista_spinners[15] = querys.idParametrics('si_no', lista_spinners[15])
    lista_spinners[16] = querys.idParametrics('donde_opera', lista_spinners[16])
    lista_spinners[17] = int(lista_spinners[17])
    lista_spinners[18] = int(lista_spinners[18])
    lista_spinners[19] = int(lista_spinners[19])
    lista_spinners[20] = querys.idParametrics('tipo_de_casa', lista_spinners[20])
    for item in lista_spinners:
        org.append(item)

    lista_texts[0] = float(lista_texts[0].replace('.',''))
    lista_texts[3] = float(lista_texts[3].replace('.',''))
    lista_texts[4] = float(lista_texts[4].replace('.',''))
    lista_texts[5] = float(lista_texts[5].replace('.',''))
    lista_texts[6] = float(lista_texts[6].replace('.',''))
    lista_texts[7] = float(lista_texts[7].replace('.',''))
    lista_texts[8] = float(lista_texts[8].replace('.',''))
    lista_texts[9] = float(lista_texts[9].replace('.',''))
    lista_texts[10] = float(lista_texts[10].replace('.',''))
    lista_texts[11] = float(lista_texts[11].replace('.',''))
    lista_texts[12] = float(lista_texts[12].replace('.',''))
    lista_texts[13] = float(lista_texts[13].replace('.',''))
    lista_texts[14] = float(lista_texts[14].replace('.',''))

    for item in lista_texts:
        org.append(item)

    org.append(str(datetime.date.today()))
    org = tuple(org)
    querys.cargar('monitoreo', 72, org)

    if info.numero_de_monitoreo == 1:
        querys.registrar('beneficiario_proyectos', 'plan_de_formacion', info.payeeDocument, querys.idProject(info.project.lower()), 1)

    elif info.numero_de_monitoreo == 2:
        querys.registrar('beneficiario_proyectos', 'plan_de_implementacion', info.payeeDocument, querys.idProject(info.project.lower()), 1)

    elif info.numero_de_monitoreo == 3:
        querys.registrar('beneficiario_proyectos', 'plan_de_seguimiento', info.payeeDocument, querys.idProject(info.project.lower()), 1)

    querys.registrar('beneficiario_proyectos', 'monitoreo', info.payeeDocument, querys.idProject(info.project.lower()), 2)


def diagnostico_empresarial(info, monitoreo):
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator,  # 2
        monitoreo,  # 3
        info.puntaje_categoria[0],  # 4
        info.puntaje_categoria[1],  # 5
        info.puntaje_categoria[2],  # 6
        info.puntaje_categoria[3],  # 7
        info.puntaje_categoria[4],  # 8
        info.puntaje_categoria[5],  # 9
        info.puntaje_categoria[6],  # 10
        info.puntaje_categoria[7],  # 11
        info.puntaje_categoria[8],  # 12
        info.puntaje_total  # 13
    ]
    org[0] = querys.idProject(info.project.lower())
    unique_id = org[0] + '__' + org[2] + '__' + org[1] + '__' + str(org[3])
    org.insert(0, unique_id)
    org = tuple(org)
    querys.cargar('diagnostico_empresarial', 15, org)


def plan_de_formacion(info):
    for idx, item in enumerate(info.all_activities):
        keys, values = list(item.keys())[0], list(item.values())[0]

        org = [
            info.project,  # 0
            info.payeeDocument,  # 1
            info.operator  # 2
        ]
        org[0] = querys.idProject(info.project.lower())
        org.append(idx)
        unique_id = org[0] + '__' + org[2] + '__' + org[1] + '__' + str(org[3])
        org.insert(0, unique_id)
        org.append(querys.traer_id_de_actividad_de_formacion(keys))
        org.append(values)
        org.append('')
        org.append(2)
        org = tuple(org)
        querys.cargar('plan_de_formacion', 9, org)
    querys.registrar('beneficiario_proyectos', 'plan_de_formacion', info.payeeDocument, querys.idProject(info.project.lower()), 2)


def plan_de_implementacion(info):
    resp = info.total_plan
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator,
        info.numero_de_vis,
        0
    ]
    org[0] = querys.idProject(info.project.lower())
    unique_id = org[0] + '__' + org[2] + '__' + org[1]
    org.insert(0, unique_id)
    for re in resp:
        for rr in re:
            org.append(rr)
    org = tuple(org)
    querys.cargar('plan_de_implementacion', 33, org)
    querys.registrar('beneficiario_proyectos', 'plan_de_implementacion', info.payeeDocument, querys.idProject(info.project.lower()), 2)


def actividad_implementacion(info):
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator
    ]
    org[0] = querys.idProject(info.project.lower())
    visitas = list(querys.ver_cuantas_visitas(info.payeeDocument, querys.idProject(info.project.lower())))
    org.append(visitas[1])

    for metas in info.estados_metas[::-1]:
         org.append(querys.idParametrics('estado_meta', metas))

    org.append(querys.idParametrics('tipo_visita', info.spinner_1.text))

    if info.input_1.text == "":
        info.input_1.text = "No aplica"
    org.append(info.input_1.text)

    org.append(querys.idParametrics('plan_de_inversiones', info.spinner_2.text))

    if info.input_2.text == "":
        info.input_2.text = "No aplica"
    org.append(info.input_2.text)

    seg = querys.idParametrics('seguimiento_desembolso', info.seguimiento_desembolso)
    aler = querys.idParametrics('alerta_seguimiento', info.alerta_cumplimiento)

    if seg is None:
        seg = 0
    if aler is None:
        aler = 0

    org.append(seg)
    org.append(aler)

    if info.otro_tipo_de_alerta == "":
        info.otro_tipo_de_alerta = "No aplica"

    org.append(info.otro_tipo_de_alerta)
    unique_id = org[0] + '__' + org[2] + '__' + org[1] + '__' + str(org[3])
    org.insert(0, unique_id)
    org = tuple(org)
    querys.cargar('actividad_implementacion', 21, org)


