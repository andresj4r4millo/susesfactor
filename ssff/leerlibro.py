for index, row in enumerate(sheet.iter_rows(values_only=True), start=1):
    if index==1:
        continue
    cedula=str(row[0])
    fecha_ex=str(row[1])
    fecha_n=str(row[2])
    pais=str(row[3])
    nombre=str(row[4])
    apellido=str(row[5])
    campaña=str(row[6])
    semilla=str(row[7])
    celular=str(row[8])
    correo=str(row[9])
    correo_corporativo=str(row[10])
    direccion=str(row[11])
    barrio=str(row[12])
    preingreso=str(row[13])
    ingreso=str(row[14])
    rm=str(row[15])
    lider_virtual=str(row[16])
    estado=str(row[17])
    observaciones=str(row[18])

    #parte1(nombre,apellido,fecha_n,pais)
    driver.find_element(By.XPATH,'//*[@id="ui5wc_1-item-1"]//button').click()
    time.sleep(2)
    #driver.find_element(By.XPATH,'//*[@id="ui5wc_14-inner"]').click()
    #driver.find_element(By.XPATH,'//*[@id="ui5wc_14-inner"]').send_keys("Añadir trabajador temporal")

