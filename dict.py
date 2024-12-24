dict_car = {
    'model_car': 'Toyota C-HR Hybrid',
    'price': 1905290,
    'engine_volume_sm3': 1987,
    'mass_kg': 1780,
    'speed': 180,
    'features_interior': ['Contour illumination with the possibility of personalization',
                          'Trimming the front door cards with vegan suede'],
    'baggage_compartment': {
        'trunk_volume_l': 292,
        'trunk_volume_with_folded_seat_l': 1072,
    }
}

dict_car['The_maximum_permissible_weight_trailer_brakes_kg'] = 725

print(dict_car['model_car'])
print(dict_car['price'])
print(dict_car['features_interior'][0])
print(dict_car['baggage_compartment']['trunk_volume_with_folded_seat_l'])
