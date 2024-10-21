# Dictionaries

player_colors = (
                 '#0000ff',
                 '#fe0000',
                 '#00ff00',
                 '#ffff01',
                 '#00ffe1',
                 '#ff00ff',
                 '#434343',
                 '#ff8201'
                 )
tiles_colors = {
    0:   {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass 1'},
    1:   {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Water, Shallow'},
    2:   {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach'},
    3:   {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Dirt 3'},
    4:   {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Shallows'},
    5:   {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Underbrush'},
    6:   {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Dirt 1'},
    7:   {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Farm'},
    8:   {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Farm, Dead'},
    9:   {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass 3'},
    10:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Oak'},
    11:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Dirt 2'},
    12:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass 2'},
    13:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Palm Desert'},
    14:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Desert, Sand'},
    15:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Water 2D, Shoreless'},
    16:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass, Other'},
    17:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Jungle'},
    18:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Bamboo'},
    19:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Pine'},
    20:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Oak Bush'},
    21:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Pine Snow'},
    22:  {'normal': '#004aa1', 'shady': '#004aa1', 'sunny': '#004aa1', 'description': 'Water, Deep'},
    23:  {'normal': '#004abb', 'shady': '#004abb', 'sunny': '#004abb', 'description': 'Water, Medium'},
    24:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road'},
    25:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Broken'},
    26:  {'normal': '#98c0f0', 'shady': '#98c0f0', 'sunny': '#98c0f0', 'description': 'Ice, Navigable'},
    27:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Grass, Foundation'},
    28:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Water 2D, Bridge'},
    29:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Farm, 0%'},
    30:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Farm, 33%'},
    31:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Farm, 67%'},
    32:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Snow'},
    33:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Snow Dirt'},
    34:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Snow Grass'},
    35:  {'normal': '#98c0f0', 'shady': '#98c0f0', 'sunny': '#98c0f0', 'description': 'Ice'},
    36:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Snow, Foundation'},
    37:  {'normal': '#98c0f0', 'shady': '#98c0f0', 'sunny': '#98c0f0', 'description': 'Beach, Ice'},
    38:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Snow'},
    39:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Fungus'},
    40:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Rock 1'},
    41:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Dirt, Savannah'},
    42:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Dirt 4'},
    43:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Desert'},
    44:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Moorland'},
    45:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Desert, Cracked'},
    46:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Desert, Quicksand'},
    47:  {'normal': '#1c1c1c', 'shady': '#1c1c1c', 'sunny': '#1c1c1c', 'description': 'Black'},
    48:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Dragon Tree'},
    49:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Baobab'},
    50:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Acacia'},
    51:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach, White, Vegatation'},
    52:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach, Vegetation'},
    53:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach, White'},
    54:  {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Shallows, Mangrove'},
    55:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Mangrove'},
    56:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Rainforest'},
    57:  {'normal': '#004aa1', 'shady': '#004aa1', 'sunny': '#004aa1', 'description': 'Water, Deep Ocean'},
    58:  {'normal': '#0054b0', 'shady': '#0054b0', 'sunny': '#0054b0', 'description': 'Water, Azure'},
    59:  {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Shallows, Azure'},
    60:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass, Jungle'},
    61:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Jungle'},
    62:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'leaves, Jungle'},
    63:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Rice Farm'},
    64:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Rice Farm, Dead'},
    65:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Rice Farm, 0%'},
    66:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Rice Farm, 33%'},
    67:  {'normal': '#82884d', 'shady': '#768241', 'sunny': '#8a8b57', 'description': 'Rice Farm, 66%'},
    68:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Reserved'},
    69:  {'normal': '#1c1c1c', 'shady': '#1c1c1c', 'sunny': '#1c1c1c', 'description': 'Very Evil Fog'},
    70:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Gravel, Default'},
    71:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Underbrush, Leaves'},
    72:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Underbrush, Snow'},
    73:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Snow, Light'},
    74:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Snow, Strong'},
    75:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Fungus'},
    76:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Dirt, Mud'},
    77:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Underbrush, Jungle'},
    78:  {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Gravel'},
    79:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach (Non-Navigable)'},
    80:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach (Non-Navigable), Wet Sand'},
    81:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach (Non-Navigable), Wet Gravel'},
    82:  {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach (Non-Navigable), Wet Rock'},
    83:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass, Jungle'},
    84:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Moddable Grass'},
    85:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Moddable Grass'},
    86:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Moddable Grass'},
    87:  {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Moddable Grass'},
    88:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Mediteranean'},
    89:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Bush'},
    90:  {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Forest, Reeds (Shallows)'},
    91:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Reeds (Beach)'},
    92:  {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Reeds'},
    93:  {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Moddable Shallows'},
    94:  {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Moddable Shallows'},
    95:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Water, Green'},
    96:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Water, Brown'},
    97:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Moddable Normal Water'},
    98:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Moddable Normal Water'},
    99:  {'normal': '#305db6', 'shady': '#305db6', 'sunny': '#305db6', 'description': 'Moddable Deep Water'},
    100: {'normal': '#339727', 'shady': '#008d00', 'sunny': '#00a900', 'description': 'Grass, Dry'},
    101: {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Swamp, Bogland'},
    102: {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Gravel, Desert'},
    103: {'normal': '#e4a252', 'shady': '#da9c69', 'sunny': '#f3aa5c', 'description': 'Road, Gravel'},
    104: {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Autumn'},
    105: {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Autumn Snow'},
    106: {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Dead'},
    107: {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach, Wet'},
    108: {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach, Wet Gravel'},
    109: {'normal': '#e8b478', 'shady': '#bd966f', 'sunny': '#f8c98a', 'description': 'Beach, Wet Rock'},
    110: {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Birch'},
    111: {'normal': '#5492b0', 'shady': '#5492b0', 'sunny': '#5492b0', 'description': 'Swamp, Shallows'},
    112: {'normal': '#157615', 'shady': '#007200', 'sunny': '#257439', 'description': 'Forest, Palm Grass'}
}
wall_objects = {
    63: 'Fortified Gate (up.)',
    64: 'Gate', 
    72: 'Palisade Wall', 
    81: 'Fortified Gate', 
    88: 'Gate', 
    95: 'Fortified Gate', 
    117: 'Stone Wall', 
    119: 'Fortified Palisade Wall',
    155: 'Fortified Wall', 
    370: 'City Wall',
    662: 'Fortified Gate', 
    666: 'Fortified Gate', 
    670: 'Fortified Gate', 
    674: 'Fortified Gate',
    788: 'Sea Wall',
    789: 'Palisade Gate (up.)',
    790: 'Palisade Gate',
    791: 'Palisade Gate',
    792: 'Palisade Gate',
    793: 'Palisade Gate (down.)',
    794: 'Palisade Gate',
    795: 'Palisade Gate',
    796: 'Palisade Gate',
    797: 'Palisade Gate (hori.)',
    798: 'Palisade Gate',
    799: 'Palisade Gate',
    800: 'Palisade Gate',
    801: 'Palisade Gate (vert.)',
    802: 'Palisade Gate',
    803: 'Palisade Gate',
    804: 'Palisade Gate',
    1176: 'Trowulan Gate',
    1192: 'Gate',
    1379: 'Sea Gate',
    1380: 'Sea Gate',
    1381: 'Sea Gate',
    1382: 'Sea Gate',
    1383: 'Sea Gate',
    1384: 'Sea Gate',
    1385: 'Sea Gate',
    1386: 'Sea Gate',
    1387: 'Sea Gate',
    1388: 'Sea Gate',
    1389: 'Sea Gate',
    1390: 'Sea Gate',
    1391: 'Sea Gate',
    1392: 'Sea Gate',
    1393: 'Sea Gate',
    1394: 'Sea Gate',
    1406: 'Gate Foundation (Rubble)',
    1407: 'PalisadeWall DARK (Rubble)',
    1440: 'PalisadeGate DARK NE (Rubble)',
    1441: 'PalisadeGate DARK SE (Rubble)',
    1442: 'PalisadeGate DARK E (Rubble)',
    1443: 'PalisadeGate DARK N (Rubble)',
    1500: 'StoneGate NE (Rubble)',
    1501: 'StoneGate SE (Rubble)',
    1502: 'StoneGate E (Rubble)',
    1503: 'StoneGate N (Rubble)',
    1504: 'FortifiedGate NE (Rubble)',
    1505: 'FortifiedGate SE (Rubble)',
    1506: 'FortifiedGate E (Rubble)',
    1507: 'FortifiedGate N (Rubble)',
    1508: 'StoneWall (Rubble)',
    1509: 'FortifiedWall (Rubble)',
    1510: 'CityGate NE (Rubble)',
    1511: 'CityGate SE (Rubble)',
    1512: 'CityGate E (Rubble)',
    1513: 'CityGate N (Rubble)',
    1518: 'StoneGate Corner (Rubble)',
    1519: 'FortifiedGate Corner (Rubble)',
    1520: 'FortifiedGate Corner (Rubble)',
    1521: 'PalisadeGate Corner (Rubble)',
    1523: 'CityGate Corner (Rubble)',
    1562: 'Paifang Gate',
    1579: 'City Gate',
    1580: 'City Gate',
    1581: 'City Gate',
    1582: 'City Gate',
    1583: 'City Gate',
    1584: 'City Gate',
    1585: 'City Gate',
    1586: 'City Gate',
    1587: 'City Gate',
    1588: 'City Gate',
    1589: 'City Gate',
    1590: 'City Gate',
    1591: 'City Gate',
    1592: 'City Gate',
    1593: 'City Gate',
    1594: 'City Gate',
}

food_objects = {
    48: 'Wild Boar',
    53: 'Fish (Perch)',
    59: 'Forage Bush',
    65: 'Deer',
    69: 'Shore Fish',
    89: 'Dire Wolf',
    126: 'Wolf',
    202: 'Rabid Wold',
    305: 'Llama',
    333: 'Deer',
    450: 'Great Fish (Marlin1)',
    451: 'Great Fish (Marlin2)',
    452: 'Dolphin',
    455: 'Fish (Dorado)',
    456: 'Fish (Salmon)',
    457: 'Fish (Tuna)',
    458: 'Fish (Snapper)',
    486: 'Bear',
    594: 'Sheep',
    705: 'Cow A',
    810: 'Iron Boar',
    812: 'Jaguar',
    822: 'Javelina',
    833: 'Turkey',
    835: 'Wild Horse',
    884: 'Wild Camel',
    897: 'Camel',
    963: 'Elephant',
    1019: 'Zebra',
    1026: 'Ostrich',
    1031: 'Crocodile',
    1029: 'Lion',
    1059: 'Fruit Bush',
    1060: 'Goat',
    1135: 'Komodo Dragon',
    1137: 'Tiger',
    1139: 'Rhinoceros',
    1141: 'Box Turtles',
    1142: 'Water Buffalo',
    1239: 'Ibex',
    1241: 'Snow Leopard',
    1243: 'Goose',
    1245: 'Pig',
    1247: 'Wild Bactrian Camel',
    1301: 'Elephant',
    1596: 'Cow B',
    1598: 'Cow C',
    1600: 'Cow D',
    1796: 'Gazelle',
}

stone_objects = {
    102: 'Stone Mine'
}
gold_objects = {
    66: 'Gold Mine'
}
relic_objects = {
    285: 'Relic'
}
cliff_objects = {
    264: 'Cliff',
    265: 'Cliff',
    266: 'Cliff',
    267: 'Cliff',
    268: 'Cliff',
    269: 'Cliff',
    270: 'Cliff',
    271: 'Cliff',
    272: 'Cliff',
    1849: 'Cliff (Desert) 01',
    1850: 'Cliff (Desert) 02',
    1851: 'Cliff (Desert) 03',
    1852: 'Cliff (Desert) 04',
    1853: 'Cliff (Desert) 05',
    1854: 'Cliff (Desert) 06',
    1855: 'Cliff (Desert) 07',
    1856: 'Cliff (Desert) 08',
    1857: 'Cliff (Desert) 09',
    1858: 'Cliff (Snow) 01',
    1859: 'Cliff (Snow) 02',
    1860: 'Cliff (Snow) 03',
    1861: 'Cliff (Snow) 04',
    1862: 'Cliff (Snow) 05',
    1863: 'Cliff (Snow) 06',
    1864: 'Cliff (Snow) 07',
    1865: 'Cliff (Snow) 08',
    1866: 'Cliff (Snow) 09',
}