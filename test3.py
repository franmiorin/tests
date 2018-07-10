###  Se hace una query para guardar un numero de serie de dragonfish para que apunte a fr2008.
###  OLD_SERIE_NUMBER es un serie de dragon que esta en la base zNubeProvisioning tabla [Novedades].[SeriesModulos]
##   El nuevo serie que se va guardar en la tabla se tiene que asociar a un serie ya guardado de la company de QA,
###  por lo tanto se asocia a este serie viejo.""" 

# -- coding: utf-8 --
import pyodbc

OLD_SERIE_NUMBER = 203014

# Open the ServicioVyV.ini file
path_servicioVyV = "C:\CDI\ServicioVyV.ini"

# Get the dragon serie number
with open(path_servicioVyV) as f:
    content = f.readlines()

list_content = [x.strip() for x in content]
new_serie_number = list_content[66].split("=")[1]
environment = list_content[73].split("=")[1]

# Si el ambiente es http://fr2008.zoologicnet.com.ar registra el serie de dragon para fr
if environment == "http://fr2008.zoologicnet.com.ar":

    # Parameters
    server = 'Fr2008' 
    database = 'zNubeProvisioning' 
    username = 'sa' 
    password = 'Passw0rd' 

    # Create the connection 
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    # Create a cursor
    cur = cnxn.cursor()

    # Execute query
    cur.execute(u"INSERT INTO [Novedades].[SeriesModulos]\
    (\
        Id,\
        SerieCodigoZL,\
        SerieCodigoGuid,\
        Puesto,\
        ClienteCodigoZL,\
        ClienteCodigoGuid,\
        ModulosTipo,\
        Accion,\
        FechaRegistro\
    ) \
    SELECT \
        NEWID(),\
        {},\
        NEWID(),\
        Puesto,\
        ClienteCodigoZL,\
        ClienteCodigoGuid,\
        ModulosTipo,\
        Accion,\
        FechaRegistro \
    FROM [Novedades].[SeriesModulos] where SerieCodigoZL = {}".format(new_serie_number,OLD_SERIE_NUMBER))

    cnxn.commit()

    cur.execute(u"EXEC zNubeProvisioning.dbo.usp_zNubeProcesarNovedadesSeriesAltas")

    cur.close()
    cnxn.close()