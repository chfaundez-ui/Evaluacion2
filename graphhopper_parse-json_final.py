import requests
import urllib.parse


route_url = "https://graphhopper.com/api/1/route?"
key = "11b7dfcd-c1b5-4e64-8549-3dfda1ccb702"

def geocoding (location, key):
    while location == "":
        location = input("Por favor, ingresa nuevamente la ubicación: ")
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit": "1", "key":key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        json_data = requests.get(url).json()
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]
        value = json_data["hits"][0]["osm_value"]
        
        if "country" in json_data["hits"][0]:
            country = json_data["hits"][0]["country"]
        else:
            country=""
        if "state" in json_data["hits"][0]:
            state = json_data["hits"][0]["state"]
        else:
            state=""
        if len(state) !=0 and len(country) !=0:
            new_loc = name + ", " + state + ", " + country
        elif len(state) !=0:
            new_loc = name + ", " + country
        else:
            new_loc = name
        
        print("URL de la API de Geocodificación para " + new_loc + " (Location Type: " + value + ")\n" + url)
    else:
        lat="null"
        lng="null"
        new_loc=location
        if json_status != 200:
            print("Estado de la API de Geocodificación: " + str(json_status) + "\nMensaje de error: " + json_data["message"])
    return json_status,lat,lng,new_loc

while True:
    loc1 = input("Ubicación de inicio (o escribe 'salir' para terminar): ")
    if loc1 == "salir" or loc1 == "s":
        break
    orig = geocoding(loc1, key)
    loc2 = input("Ubicación de destino (o escribe 'salir' para terminar): ")
    if loc2 == "salir" or loc2 == "s":
        break
    dest = geocoding(loc2, key)
    print("=================================================")
    if orig[0] == 200 and dest[0] == 200:
        op="&point="+str(orig[1])+"%2C"+str(orig[2])
        dp="&point="+str(dest[1])+"%2C"+str(dest[2])

        route_params = {
            "key": key,
            "locale": "es",   
            "instructions": "true",
        }
        paths_url = route_url + urllib.parse.urlencode(route_params) + op + dp
        paths_status = requests.get(paths_url).status_code
        paths_data = requests.get(paths_url).json()
        print("Estado de la API de Rutas: " + str(paths_status) + "\nURL de la API de Rutas:\n" + paths_url)
    
    print("=================================================")
    print("Direcciones desde " + orig[3] + " hasta " + dest[3])
    print("=================================================")
    if paths_status == 200:
        miles = (paths_data["paths"][0]["distance"])/1000/1.61
        km = (paths_data["paths"][0]["distance"])/1000
        sec = int(paths_data["paths"][0]["time"]/1000%60)
        min = int(paths_data["paths"][0]["time"]/1000/60%60)
        hr = int(paths_data["paths"][0]["time"]/1000/60/60)
        print("Distancia total: {0:.2f} millas / {1:.1f} km".format(miles, km))
        print("Duración estimada: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
        print("=================================================")
        for each in range(len(paths_data["paths"][0]["instructions"])):
            path = paths_data["paths"][0]["instructions"][each]["text"]
            distance = paths_data["paths"][0]["instructions"][each]["distance"]
            print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000,distance/1000/1.61))
        print("=============================================")