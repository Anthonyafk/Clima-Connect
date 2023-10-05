"""
Importamos la biblioteca difflib, que nos ayudará a buscar nombres similares.
"""
import difflib

# Lista de nombres conocidos y sus códigos IATA en minúsculas
nombres_abreviados = {
    "ciudad de méxico": ["ciudad de méxico", "mex", "cdmx", "mxm", "mejico"],
    "guadalajara": ["guadalajara", "gdl", "miguel hidalgo y costilla"],
    "cancun": ["cancun", "cun"],
    "acapulco": ["acapulco", "aca", "pulc"],
    "aguascalientes": ["aguascalientes", "agu"],
    "guanajuato": ["guanajuato", "bjx"],
    "ciudad juárez": ["ciudad juárez", "cjs", "juá"],
    "ciudad del carmen": ["ciudad del carmen", "cme", "car"],
    "chetumal": ["chetumal", "ctm"],
    "chihuahua": ["chihuahua", "cuu"],
    "cozumel": ["cozumel", "czm", "ozu"],
    "hermosillo": ["hermosillo", "hmo", "rmo"],
    "santa maría huatulco": ["huatulco", "hux", "santa maría huatulco"],
    "mérida": ["mérida", "mid"],
    "oaxaca": ["oaxaca", "oax", "axa"],
    "puebla": ["puebla", "pbc", "ebla"],
    "amsterdam": ["amsterdam", "ams"],
    "atlanta": ["atlanta", "atl"],
    "bogotá": ["bogotá", "el dorado", "bog"],
    "belize": ["belize", "philip s.w. goldson", "bze"],
    "paris": ["paris", "cdg", "paris-charles de gaulle"],
    "ciudad obregón": ["ciudad obregón", "cen"],
    "north carolina": ["north carolina", "charlotte-douglas", "clt"],
    "texas": ["texas", "dallas/fort worth", "dfw"],
    "guatemala city": ["guatemala city", "gua"],
    "havana": ["havana", "hav"],
    "houston": ["houston", "iah"],
    "queens": ["queens", "jfk"],
    "los angeles": ["lax", "los angeles"],
    "lima": ["lima", "lim"],
    "madrid": ["madrid", "mad"],
    "miami": ["miami", "mia"],
    "mazatlán": ["mazatlán", "mzt"],
    "chicago": ["chicago", "ord"],
    "houston": ["houston", "phl"],
    "philadelphia": ["philadelphia", "phl"],
    "phoenix": ["phoenix", "phx"],
    "santiago": ["santiago", "scl"],
    "vancouver": ["vancouver", "yvr"],
    "toronto": ["toronto", "yyz"],
    "puerto vallarta": ["puerto vallarta", "pvr", "licenciado gustavo díaz ordaz"],
    "puerto escondido": ["puerto escondido", "pxm"],
    "querétaro": ["querétaro", "qro", "eré"],
    "san luis potosí": ["san luis potosí", "slp", "otosí"],
    "tampico": ["tampico", "tam"],
    "toluca": ["toluca", "tlc", "ait"],
    "torreón": ["francisco sarabia", "trc", "torreón"],
    "villahermosa": ["carlos rovirosa pérez", "vsa", "villahermosa"],
    "zacatecas": ["zacatecas", "zcl"],
    "ixtapa-zihuatanejo": ["zihuatanejo", "zih"],
    "zihuatanejo": ["zihuatanejo", "zih"],
    "tijuana": ["tijuana", "tij"],
    "veracruz": ["veracruz", "ver", "acruz"],
    "monterrey": ["monterrey", "mty", "mon"]
}

def encontrar_nombre_similar(entrada_usuario):
    """
    Función que busca un nombre similar en la lista de nombres conocidos
    basándose en la entrada proporcionada por el usuario.

    Args:
        entrada_usuario (str): La entrada del usuario.

    Returns:
        str: El nombre similar encontrado o None si no se encuentra ninguna coincidencia.
    """
    if entrada_usuario is not None:
        entrada_usuario = entrada_usuario.lower()
    
        for nombre, abreviaturas in nombres_abreviados.items():
            if entrada_usuario in abreviaturas:
                return nombre
    
    coincidencias = difflib.get_close_matches(entrada_usuario, nombres_abreviados.keys())
    
    if coincidencias:
        return coincidencias[0]
    else:
        return None


