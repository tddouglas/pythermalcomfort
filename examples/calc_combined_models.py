from clothing_calculator.get_current_temp import get_current_weather
from pythermalcomfort.models import utci, two_nodes
from pythermalcomfort.utilities import body_surface_area
from statistics import mean

# Docs -
# https://pythermalcomfort.readthedocs.io/en/latest/reference/pythermalcomfort.html#universal-thermal-climate-index-utci
from pythermalcomfort.utilities import met_typical_tasks, clo_dynamic, clo_individual_garments

current_weather = get_current_weather()
# wind_in_fps = current_weather['wind']['speed'] * 5280 / 3600  # convert miles/hour to feed/second

# input variables
tdb = current_weather['main']['temp']  # dry bulb air temperature, [$^{\circ}$C]
tr = current_weather['main']['temp']  # mean radiant temperature, [$^{\circ}$C]. Don't know how to calculate
v = current_weather['wind']['speed']  # average air speed, [m/s]
rh = current_weather['main']['humidity']  # relative humidity, [%]

activity = "Walking about"  # participant's activity description
garments = ["Thick trousers", "Long sleeve shirt (thick)", "Wooden stool", "Boots"]

met = met_typical_tasks[activity]  # (float or array-like) – metabolic rate, [met]
icl = sum(
    [clo_individual_garments[item] for item in garments]
)  # calculate total clothing insulation
clo = clo_dynamic(clo=icl, met=met)  # (float or array-like) – clothing insulation, [clo]
wme = 0  # (float or array-like) – external work, [met] default 0
body_surface_area = body_surface_area(weight=77, height=1.82)  # (float) – body surface area, default value 1.8258 [m2] in [ft2] if units = ‘IP’

# ATM_CONSTANT = 0.0009869233
# (float) – atmospheric pressure, default value 101325 [Pa] in [atm] if units = ‘IP’
p_atmospheric = current_weather['main']['pressure'] * 100  # convers from hPA to PA
body_position = "standing"  # (str default=”standing” or array-like) – select either “sitting” or “standing”
max_skin_blood_flow = 80  # (float) – maximum blood flow from the core to the skin, [kg/h/m2] default 80


utci_val = utci(tdb, tr, v, rh, units='SI')
two_nodes_val = two_nodes(tdb, tr, v, rh, met, clo, wme=wme, body_surface_area=body_surface_area, p_atmospheric=p_atmospheric,
                          body_position=body_position, max_skin_blood_flow=max_skin_blood_flow)
average = mean([utci_val, two_nodes_val["_set"]])
print(f'UTCI Value: {utci_val}\n'
      f'Two Nodes discomfort Level: {two_nodes_val["disc"]}\n'
      f'Averaged Value: {average}\n'
      f'Weather API feels like: {current_weather["main"]["feels_like"]}')
