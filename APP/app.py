from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
db_config = {
    "host": "bpdkfibkxq1nklilgl4v-mysql.services.clever-cloud.com",
    "user": "uqry7enycdyebwle",
    "password": "VdUzXeG00uKHGAL3tuXq",
    "database": "bpdkfibkxq1nklilgl4v",
    "port": 3306
}

@app.route('/agregar_grupo', methods=['POST'])
def agregar_grupo():
    try:
        data = request.get_json()
        nombre_grupo = data.get("nombre")
        default = "NO"

        if not nombre_grupo:
            return jsonify({"error": "El nombre es obligatorio"}), 400

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta_grupo = """
        INSERT INTO grupo1 (
            nombre, MSalon, MChacon, MLaBotella, MFCarvajal, MFMaldonado, 
            MFrenteSalon, MFPolanco, MFVargas, MTiendaLaPoderosa, MFCriales, 
            MFEcheverria, MHIslanda, MFCastro, MFSantiagoChacon, MIslita, 
            MBicicletasBikebar, MTiendaSureña, MCasaCarnaval
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = [nombre_grupo] + [default] * 18

        cursor.execute(consulta_grupo, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return jsonify({
            "mensaje": "Grupo agregado correctamente",
            "nombre": nombre_grupo,
            "MSalon": default
        }), 201

    except mysql.connector.IntegrityError:
        return jsonify({"error": "El nombre del grupo ya existe"}), 400  

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500

@app.route('/agregar_grupo2', methods=['POST'])
def agregar_grupo2():
    try:
        data = request.get_json()
        nombre_grupo = data.get("nombre")
        default = "NO"

        if not nombre_grupo:
            return jsonify({"error": "El nombre es obligatorio"}), 400

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta_grupo = """
        INSERT INTO grupo2 (
            nombre, MSede, MColegioCorazonSantuario, MFCantillo, MFCera, MMiselaneaEdgar, 
            MFNuma, MFCastañeda, MHJulia, MParquecito, MTiendaDiosConNosotros, 
            MTiendaMiAngelDeAmor, MLos6Hermanos, MHKelly, MFMartinez, MAlFrenteFMartinez, 
            MTiendaMerkanubar, MAlLadoParqueAbandonado, MAlLadoTiendaPrecioEsCorrecto,MParqueGoldaMeir,
            MAlLadoFCoronado,MFCoronado,MParqueAbandonado,MFrenteFSuarez,MFarmaciaJyH,MTiendaPrecioEsCorrecto
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = [nombre_grupo] + [default] * 25

        cursor.execute(consulta_grupo, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return jsonify({
            "mensaje": "Grupo agregado correctamente",
            "nombre": nombre_grupo,
            "MSalon": default
        }), 201

    except mysql.connector.IntegrityError:
        return jsonify({"error": "El nombre del grupo ya existe"}), 400  

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500        

@app.route('/agregar_grupo3', methods=['POST'])
def agregar_grupo3():
    try:
        data = request.get_json()
        nombre_grupo = data.get("nombre")
        default = "NO"

        if not nombre_grupo:
            return jsonify({"error": "El nombre es obligatorio"}), 400

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta_grupo = """
        INSERT INTO grupo3 (
            nombre, MFPerezSegura, MFPerezCarvajal, MTiendaLaRenovacion, MPanaderiaElLider, MLosGallos, 
            MMuebleriaLuxuryHouse, MTiendaLaFeEnDios, MVariedadesFenicia, MTiendaElBacan, MEstaderoLaRetoba, 
            MTallerCarlos, MSeñoraLevix, MHFrancelina, MTiendaElEden, MTiendaDondeTotto, 
            MTiendaNuevoRenacer, MAlLadoDondeTotto, MFSuarez,MLasPiedras,
            MLaIslita3,MFrenteFTapia,MFTapia,MTiendaRivero,MLaBombonera
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = [nombre_grupo] + [default] * 24

        cursor.execute(consulta_grupo, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return jsonify({
            "mensaje": "Grupo agregado correctamente",
            "nombre": nombre_grupo,
            "MSalon": default
        }), 201

    except mysql.connector.IntegrityError:
        return jsonify({"error": "El nombre del grupo ya existe"}), 400  

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500  


@app.route('/agregar_grupo4', methods=['POST'])
def agregar_grupo4():
    try:
        data = request.get_json()
        nombre_grupo = data.get("nombre")
        default = "NO"

        if not nombre_grupo:
            return jsonify({"error": "El nombre es obligatorio"}), 400

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta_grupo = """
        INSERT INTO grupo4 (
            nombre, MVariedadesSofy, MBillaresLasPernicias, MFrenteColegioLasAmericas, MFCeren, MColegioJesusDeNazareth, 
            MColegioAtanacioGirardot, MPanaderiaEsquinaDelSabor, MHEloina, MHGloria2, MHGloria, 
            MTiendaJJ, MFrenteLaPanaderiaLaEsquinaDelSabor, MFTorregrosa, MRestauranteChino, MFerreteriaElAmigo, 
            MHBelen, MAlLadoFundacionChildrenInternational, MFundacionChildrenInternational,MIslitaDelBrazil
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        valores = [nombre_grupo] + [default] * 19

        cursor.execute(consulta_grupo, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        return jsonify({
            "mensaje": "Grupo agregado correctamente",
            "nombre": nombre_grupo,
            "MSalon": default
        }), 201

    except mysql.connector.IntegrityError:
        return jsonify({"error": "El nombre del grupo ya existe"}), 400  

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500


        


@app.route('/agregar_mapa', methods=['POST'])
def agregar_mapa():
    try:
        data = request.get_json()
        nombre_mapa = data.get("nombre")

        if not nombre_mapa:
            return jsonify({"error": "El nombre es obligatorio"}), 400
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        consulta = "INSERT INTO mapas (nombre) VALUES (%s)"
        cursor.execute(consulta, (nombre_mapa,))
        
        conexion.commit()

        cursor.close()
        conexion.close()

        return jsonify({"mensaje": "Mapa agregado correctamente", "nombre": nombre_mapa}), 201

    except mysql.connector.IntegrityError:
        return jsonify({"error": "El nombre del mapa ya existe"}), 400 

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500


@app.route('/mapas', methods=['GET'])
def obtener_mapas():
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre FROM mapas")
        mapas = cursor.fetchall()

        cursor.close()
        conexion.close()

        if not mapas:
            return jsonify({"mensaje": "No hay mapas registrados"}), 200

        resultado = [{"nombre": mapa[0]} for mapa in mapas]

        return jsonify(resultado)

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500
        
@app.route('/eliminar_mapa', methods=['POST'])
def eliminar_mapa():
    try:
        datos = request.get_json()
        nombre_mapa = datos.get("Mapa")
        
        if not nombre_mapa:
            return jsonify({"error": "No se proporcionó un nombre de mapa"}), 400
        
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        tablas = ["grupo1", "grupo2", "grupo3", "grupo4", "mapas"]
        
        for tabla in tablas:
            columna = "Nombre" if tabla == "mapas" else "nombre"  
            query = f"DELETE FROM {tabla} WHERE {columna} = %s"
            cursor.execute(query, (nombre_mapa,))
        
        conexion.commit()
        cursor.close()
        conexion.close()
        
        return jsonify({"mensaje": "Mapa eliminado correctamente"})
    
    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500
 


@app.route('/actualizar_estado', methods=['POST'])
def actualizar_estado():
    try:
        datos = request.json
        grupo = datos.get("grupo")  
        mapa = datos.get("mapa")  
        columna = datos.get("columna") 
        nuevo_valor = datos.get("nuevo_valor") 

        if not grupo or not mapa or not columna or not nuevo_valor:
            return jsonify({"error": "Faltan datos en la solicitud"}), 400

        if grupo not in ["1", "2", "3", "4"]:
            return jsonify({"error": "Grupo inválido"}), 400

        tabla = f"grupo{grupo}"

        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()

        query = f"UPDATE {tabla} SET {columna} = %s WHERE nombre = %s"
        cursor.execute(query, (nuevo_valor, mapa))
        conexion.commit()

        cursor.close()
        conexion.close()

        return jsonify({"mensaje": f"Estado actualizado correctamente en {tabla}"})

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500
        



@app.route('/checkmanzanas/<int:grupo>', methods=['GET'])
def checkmanzanas(grupo):
    nombre = request.args.get('nombre')

    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor(dictionary=True)

        columnas_por_grupo = {
            1: [
                "MSalon", "MChacon", "MLaBotella", "MFCarvajal", "MFMaldonado",
                "MFrenteSalon", "MFPolanco", "MFVargas", "MTiendaLaPoderosa",
                "MFCriales", "MFEcheverria", "MHIslanda", "MFCastro",
                "MFSantiagoChacon", "MIslita", "MBicicletasBikebar",
                "MTiendaSureña", "MCasaCarnaval"
            ],
            2: [
                "MSede", "MColegioCorazonSantuario", "MFCantillo", "MFCera", "MMiselaneaEdgar",
                "MFNuma", "MFCastañeda", "MHJulia", "MParquecito",
                "MTiendaDiosConNosotros", "MTiendaMiAngelDeAmor", "MLos6Hermanos", "MHKelly",
                "MFMartinez", "MAlFrenteFMartinez", "MTiendaMerkanubar",
                "MAlLadoParqueAbandonado", "MAlLadoTiendaPrecioEsCorrecto","MParqueGoldaMeir",
                "MAlLadoFCoronado","MFCoronado","MParqueAbandonado","MFrenteFSuarez","MFarmaciaJyH",
                "MTiendaPrecioEsCorrecto"
            ],
            3: [
                "MFPerezSegura", "MFPerezCarvajal", "MTiendaLaRenovacion", "MPanaderiaElLider", "MLosGallos",
                                "MMuebleriaLuxuryHouse", "MTiendaLaFeEnDios", "MVariedadesFenicia", "MTiendaElBacan",
                                "MEstaderoLaRetoba", "MTallerCarlos", "MSeñoraLevix", "MHFrancelina",
                                "MTiendaElEden", "MTiendaDondeTotto", "MTiendaNuevoRenacer",
                                "MAlLadoDondeTotto", "MFSuarez", "MLasPiedras",
                                "MLaIslita3", "MFrenteFTapia", "MFTapia", "MTiendaRivero", "MLaBombonera"
            ],
            4: [
                "MVariedadesSofy", "MBillaresLasPernicias", "MFrenteColegioLasAmericas", "MFCeren", "MColegioJesusDeNazareth",
                                "MColegioAtanacioGirardot", "MPanaderiaEsquinaDelSabor", "MHEloina", "MHGloria2",
                                "MHGloria", "MTiendaJJ", "MFrenteLaPanaderiaLaEsquinaDelSabor", "MFTorregrosa",
                                "MRestauranteChino", "MFerreteriaElAmigo", "MHBelen",
                                "MAlLadoFundacionChildrenInternational", "MFundacionChildrenInternational", "MIslitaDelBrazil"
            ]
        }

        if grupo not in columnas_por_grupo:
            return jsonify({"error": f"Grupo {grupo} no encontrado"}), 404

        columnas = columnas_por_grupo[grupo]
        query = f"SELECT {', '.join(columnas)} FROM grupo{grupo} WHERE nombre = %s"
        cursor.execute(query, (nombre,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        if resultado:
            return jsonify(resultado)
        else:
            return jsonify({"error": f"Mapa no encontrado en grupo {grupo}"}), 404

    except mysql.connector.Error as error:
        return jsonify({"error": f"Error en la base de datos: {error}"}), 500



if __name__ == '__main__':
    app.run(debug=True)
