from pythermalcomfort.models import two_nodes

# Docs - https://pythermalcomfort.readthedocs.io/en/latest/reference/pythermalcomfort.html#gagge-et-al-two-node-model

# input variables
tdb = 27  # dry bulb air temperature, [$^{\circ}$C]
tr = 25  # mean radiant temperature, [$^{\circ}$C]
v = 0.3  # average air speed, [m/s]
rh = 50  # relative humidity, [%]

met = 1.2  # (float or array-like) – metabolic rate, [met]
clo = 0.5  # (float or array-like) – clothing insulation, [clo]
wme = 0  # (float or array-like) – external work, [met] default 0
body_surface_area = 0  # (float) – body surface area, default value 1.8258 [m2] in [ft2] if units = ‘IP’
# The body surface area can be calculated using the function pythermalcomfort.utilities.body_surface_area().
p_atmospheric = 0  # (float) – atmospheric pressure, default value 101325 [Pa] in [atm] if units = ‘IP’
body_position = 0  # (str default=”standing” or array-like) – select either “sitting” or “standing”
max_skin_blood_flow = 0  # (float) – maximum blood flow from the core to the skin, [kg/h/m2] default 80

two_nodes_val = two_nodes(tdb, tr, v, rh, met, clo, wme=0, body_surface_area=1.8258, p_atmospheric=101325,
                          body_position='standing', max_skin_blood_flow=90)
print(f'Two Nodes Value Run 1: {two_nodes_val}')
