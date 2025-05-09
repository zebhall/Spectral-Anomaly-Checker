# XRF Spectral Anomaly Checker by ZH
import sys
import pandas as pd
import os

versionNum = 'v1.2.0'
versionDate = '2025/04/24'

pd.options.mode.chained_assignment = None  # default='warn'
# os.system('color')

# CHANGE THIS TO FALSE IF FORMATTING IN TERMINAL IS MESSED UP **********************************************
USE_COLOURS_IN_TERMINAL = False
# **********************************************************************************************************


def elementZtoSymbol(Z:int) -> str:        
	'''Takes Z (atomic number (int)) as arg, Returns 1-2 character Element symbol as a string. E.g.: elementZtoSymbol(14) -> "Si"'''
	if 0 < Z <= 118:
		elementSymbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
		return elementSymbols[Z-1]
	else:
		raise Exception(f'Error in elementZtoSymbol: {Z} is outside of range 1-118')

def elementSymboltoName(sym:str) -> str:
	'''Takes 1-2 char element symbol (str) as arg, returns Element name as string. E.g.: elementSymboltoName(Si) -> "Silicon"'''
	if len(sym) <= 3:
		elementSymbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
		elementNames = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
		try:
			i = elementSymbols.index(sym)
			return elementNames[i]
		except Exception as e:
			raise Exception(f'Error in elementSymboltoName: "{sym}" was not found in list of Element Symbols. Symbol is case-sensitive, first character should be capitalised.({e})')
	else:
		raise Exception(f'Error in elementSymboltoName: "{sym}" is too long. Element symbol should be MAX 3 Characters.')

def elementZtoSymbolZ(Z:int) -> str:       
	'''Takes Z (atomic number (int)) as arg, Returns 1-2 character Element symbol formatted WITH atomic number in brackets, as string. E.g.: elementZtoSymbolZ(14) -> "Si (14)"'''
	if 0 < Z <= 118:
		elementSymbols = ['H (1)', 'He (2)', 'Li (3)', 'Be (4)', 'B (5)', 'C (6)', 'N (7)', 'O (8)', 'F (9)', 'Ne (10)', 'Na (11)', 'Mg (12)', 'Al (13)', 'Si (14)', 'P (15)', 'S (16)', 'Cl (17)', 'Ar (18)', 'K (19)', 'Ca (20)', 'Sc (21)', 'Ti (22)', 'V (23)', 'Cr (24)', 'Mn (25)', 'Fe (26)', 'Co (27)', 'Ni (28)', 'Cu (29)', 'Zn (30)', 'Ga (31)', 'Ge (32)', 'As (33)', 'Se (34)', 'Br (35)', 'Kr (36)', 'Rb (37)', 'Sr (38)', 'Y (39)', 'Zr (40)', 'Nb (41)', 'Mo (42)', 'Tc (43)', 'Ru (44)', 'Rh (45)', 'Pd (46)', 'Ag (47)', 'Cd (48)', 'In (49)', 'Sn (50)', 'Sb (51)', 'Te (52)', 'I (53)', 'Xe (54)', 'Cs (55)', 'Ba (56)', 'La (57)', 'Ce (58)', 'Pr (59)', 'Nd (60)', 'Pm (61)', 'Sm (62)', 'Eu (63)', 'Gd (64)', 'Tb (65)', 'Dy (66)', 'Ho (67)', 'Er (68)', 'Tm (69)', 'Yb (70)', 'Lu (71)', 'Hf (72)', 'Ta (73)', 'W (74)', 'Re (75)', 'Os (76)', 'Ir (77)', 'Pt (78)', 'Au (79)', 'Hg (80)', 'Tl (81)', 'Pb (82)', 'Bi (83)', 'Po (84)', 'At (85)', 'Rn (86)', 'Fr (87)', 'Ra (88)', 'Ac (89)', 'Th (90)', 'Pa (91)', 'U (92)', 'Np (93)', 'Pu (94)', 'Am (95)', 'Cm (96)', 'Bk (97)', 'Cf (98)', 'Es (99)', 'Fm (100)', 'Md (101)', 'No (102)', 'Lr (103)', 'Rf (104)', 'Db (105)', 'Sg (106)', 'Bh (107)', 'Hs (108)', 'Mt (109)', 'Ds (110)', 'Rg (111)', 'Cn (112)', 'Nh (113)', 'Fl (114)', 'Mc (115)', 'Lv (116)', 'Ts (117)', 'Og (118)']
		return elementSymbols[Z-1]
	else:
		raise Exception(f'Error in elementZtoSymbolZ: {Z} is outside of range 1-118')

def elementZtoName(Z:int) -> str:          # Returns Element name 
	'''Takes Z (atomic number (int)) as arg, Returns full Element name as a string. E.g.: elementZtoName(14) returns "Silicon"'''
	if 0 < Z <= 118:
		elementNames = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']
		return elementNames[Z-1]
	else:
		raise Exception(f'Error in elementZtoName: {Z} is outside of range 1-118')


class bcol:
	if USE_COLOURS_IN_TERMINAL:
		HEADER = '\033[95m'
		OKBLUE = '\033[94m'
		OKCYAN = '\033[96m'
		OKGREEN = '\033[92m'
		WARNING = '\033[93m'
		FAIL = '\033[91m'
		ENDC = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'
	else: # hacky way of preventing errors if terminal doesn't support colour code useage
		HEADER = ''
		OKBLUE = ''
		OKCYAN = ''
		OKGREEN = ''
		WARNING = ''
		FAIL = ''
		ENDC = ''
		BOLD = ''
		UNDERLINE = ''
		

def getClosestByEnergy(energy, qty:int) -> str:
	closest = energies_df.iloc[(energies_df['Energy']-energy).abs().argsort()[:qty]]
	data = closest
	data['Element'] = data['Element'].apply(elementSymboltoName)
	data['Line'] = data['Line'].str.replace('a', '\u03B1')  # replace a with alpha
	data['Line'] = data['Line'].str.replace('b', '\u03B2')  # replace b with beta
	data.rename(columns={'Energy':'Energy (eV)'}, inplace = True)   
	return(data.to_string(index = False))

def resource_path(relative_path) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def getCommonElementLineEnergies(symbol:str) -> list[float]:
	"""given an element symbol (e.g. Fe or Ca), returns a list of the line energies in eV of the common lines for that element. (Ka, Kb, La, Lb)"""
	all_standard_element_lines:list[str, str, float] = [['Be', 'Be Kα', 0.108], ['B', 'B Kα', 0.183], ['C', 'C Kα', 0.277], ['N', 'N Kα', 0.392], ['O', 'O Kα', 0.525], ['F', 'F Kα', 0.677], ['Ne', 'Ne Kα', 0.849], ['Na', 'Na Kα', 1.04], ['Mg', 'Mg Kα', 1.254], ['Mg', 'Mg Kβ', 1.302], ['Al', 'Al Kα', 1.486], ['Al', 'Al Kβ', 1.557], ['Si', 'Si Kα', 1.74], ['Si', 'Si Kβ', 1.837], ['P', 'P Kα', 2.01], ['P', 'P Kβ', 2.139], ['S', 'S Kα', 2.309], ['S', 'S Kβ', 2.465], ['Cl', 'Cl Kα', 2.622], ['Cl', 'Cl Kβ', 2.812], ['Ar', 'Ar Kα', 2.958], ['Ar', 'Ar Kβ', 3.19], ['K', 'K Kα', 3.314], ['K', 'K Kβ', 3.59], ['Ca', 'Ca Kα', 3.692], ['Ca', 'Ca Kβ', 4.013], ['Sc', 'Sc Kα', 4.093], ['Sc', 'Sc Kβ', 4.464], ['Ti', 'Ti Kα', 4.512], ['Ti', 'Ti Kβ', 4.933], ['Ti', 'Ti Lβ', 0.458], ['Ti', 'Ti Lα', 0.452], ['V', 'V Kα', 4.953], ['V', 'V Kβ', 5.428], ['V', 'V Lβ', 0.518], ['V', 'V Lα', 0.51], ['Cr', 'Cr Kα', 5.415], ['Cr', 'Cr Kβ', 5.947], ['Cr', 'Cr Lβ', 0.582], ['Cr', 'Cr Lα', 0.572], ['Mn', 'Mn Kα', 5.9], ['Mn', 'Mn Kβ', 6.492], ['Mn', 'Mn Lβ', 0.648], ['Mn', 'Mn Lα', 0.637], ['Fe', 'Fe Kα', 6.405], ['Fe', 'Fe Kβ', 7.059], ['Fe', 'Fe Lβ', 0.718], ['Fe', 'Fe Lα', 0.705], ['Co', 'Co Kα', 6.931], ['Co', 'Co Kβ', 7.649], ['Co', 'Co Lβ', 0.79], ['Co', 'Co Lα', 0.775], ['Ni', 'Ni Kα', 7.48], ['Ni', 'Ni Kβ', 8.267], ['Ni', 'Ni Lβ', 0.866], ['Ni', 'Ni Lα', 0.849], ['Cu', 'Cu Kα', 8.046], ['Cu', 'Cu Kβ', 8.904], ['Cu', 'Cu Lβ', 0.947], ['Cu', 'Cu Lα', 0.928], ['Zn', 'Zn Kα', 8.637], ['Zn', 'Zn Kβ', 9.57], ['Zn', 'Zn Lβ', 1.035], ['Zn', 'Zn Lα', 1.012], ['Ga', 'Ga Kα', 9.251], ['Ga', 'Ga Kβ', 10.267], ['Ga', 'Ga Lβ', 1.125], ['Ga', 'Ga Lα', 1.098], ['Ge', 'Ge Kα', 9.886], ['Ge', 'Ge Kβ', 10.982], ['Ge', 'Ge Lβ', 1.218], ['Ge', 'Ge Lα', 1.188], ['As', 'As Kα', 10.543], ['As', 'As Kβ', 11.726], ['As', 'As Lβ', 1.317], ['As', 'As Lα', 1.282], ['Se', 'Se Kα', 11.224], ['Se', 'Se Kβ', 12.497], ['Se', 'Se Lβ', 1.419], ['Se', 'Se Lα', 1.379], ['Br', 'Br Kα', 11.924], ['Br', 'Br Kβ', 13.292], ['Br', 'Br Lβ', 1.526], ['Br', 'Br Lα', 1.481], ['Kr', 'Kr Kα', 12.648], ['Kr', 'Kr Kβ', 14.112], ['Kr', 'Kr Lβ', 1.636], ['Kr', 'Kr Lα', 1.585], ['Rb', 'Rb Kα', 13.396], ['Rb', 'Rb Kβ', 14.961], ['Rb', 'Rb Lβ', 1.751], ['Rb', 'Rb Lα', 1.692], ['Sr', 'Sr Kα', 14.165], ['Sr', 'Sr Kβ', 15.835], ['Sr', 'Sr Lβ', 1.871], ['Sr', 'Sr Lα', 1.806], ['Y', 'Y Kα', 14.958], ['Y', 'Y Kβ', 16.739], ['Y', 'Y Lβ', 1.998], ['Y', 'Y Lα', 1.924], ['Zr', 'Zr Kα', 15.775], ['Zr', 'Zr Kβ', 17.668], ['Zr', 'Zr Lβ', 2.126], ['Zr', 'Zr Lα', 2.044], ['Nb', 'Nb Kα', 16.615], ['Nb', 'Nb Kβ', 18.625], ['Nb', 'Nb Lβ', 2.26], ['Nb', 'Nb Lα', 2.169], ['Mo', 'Mo Kα', 17.48], ['Mo', 'Mo Kβ', 19.606], ['Mo', 'Mo Lβ', 2.394], ['Mo', 'Mo Lα', 2.292], ['Tc', 'Tc Kα', 18.367], ['Tc', 'Tc Kβ', 20.626], ['Tc', 'Tc Lβ', 2.535], ['Tc', 'Tc Lα', 2.423], ['Ru', 'Ru Kα', 19.279], ['Ru', 'Ru Kβ', 21.655], ['Ru', 'Ru Lβ', 2.683], ['Ru', 'Ru Lα', 2.558], ['Rh', 'Rh Kα', 20.216], ['Rh', 'Rh Kβ', 22.724], ['Rh', 'Rh Lβ', 2.834], ['Rh', 'Rh Lα', 2.697], ['Pd', 'Pd Kα', 21.177], ['Pd', 'Pd Kβ', 23.818], ['Pd', 'Pd Lβ', 2.99], ['Pd', 'Pd Lα', 2.838], ['Ag', 'Ag Kα', 22.163], ['Ag', 'Ag Kβ', 24.941], ['Ag', 'Ag Lβ', 3.15], ['Ag', 'Ag Lα', 2.983], ['Cd', 'Cd Kα', 23.173], ['Cd', 'Cd Kβ', 26.093], ['Cd', 'Cd Lβ', 3.315], ['Cd', 'Cd Lα', 3.133], ['In', 'In Kα', 24.21], ['In', 'In Kβ', 27.275], ['In', 'In Lβ', 3.487], ['In', 'In Lα', 3.286], ['Sn', 'Sn Kα', 25.271], ['Sn', 'Sn Kβ', 28.485], ['Sn', 'Sn Lβ', 3.663], ['Sn', 'Sn Lα', 3.444], ['Sb', 'Sb Kα', 26.359], ['Sb', 'Sb Kβ', 29.725], ['Sb', 'Sb Lβ', 3.842], ['Sb', 'Sb Lα', 3.604], ['Te', 'Te Kα', 27.473], ['Te', 'Te Kβ', 30.993], ['Te', 'Te Lβ', 4.029], ['Te', 'Te Lα', 3.768], ['I', 'I Kα', 28.612], ['I', 'I Kβ', 32.294], ['I', 'I Lβ', 4.221], ['I', 'I Lα', 3.938], ['Xe', 'Xe Kα', 29.775], ['Xe', 'Xe Kβ', 33.62], ['Xe', 'Xe Lβ', 4.418], ['Xe', 'Xe Lα', 4.11], ['Cs', 'Cs Kα', 30.973], ['Cs', 'Cs Kβ', 34.982], ['Cs', 'Cs Lβ', 4.619], ['Cs', 'Cs Lα', 4.285], ['Ba', 'Ba Kα', 32.194], ['Ba', 'Ba Kβ', 36.378], ['Ba', 'Ba Lβ', 4.828], ['Ba', 'Ba Lα', 4.466], ['La', 'La Kα', 33.442], ['La', 'La Kβ', 37.797], ['La', 'La Lβ', 5.038], ['La', 'La Lα', 4.647], ['Ce', 'Ce Kα', 34.72], ['Ce', 'Ce Kβ', 39.256], ['Ce', 'Ce Lβ', 5.262], ['Ce', 'Ce Lα', 4.839], ['Pr', 'Pr Kα', 36.027], ['Pr', 'Pr Kβ', 40.749], ['Pr', 'Pr Lβ', 5.492], ['Pr', 'Pr Lα', 5.035], ['Nd', 'Nd Kα', 37.361], ['Nd', 'Nd Kβ', 42.272], ['Nd', 'Nd Lβ', 5.719], ['Nd', 'Nd Lα', 5.228], ['Pm', 'Pm Kα', 38.725], ['Pm', 'Pm Kβ', 43.827], ['Pm', 'Pm Lβ', 5.961], ['Pm', 'Pm Lα', 5.432], ['Sm', 'Sm Kα', 40.118], ['Sm', 'Sm Kβ', 45.414], ['Sm', 'Sm Lβ', 6.201], ['Sm', 'Sm Lα', 5.633], ['Eu', 'Eu Kα', 41.542], ['Eu', 'Eu Kβ', 47.038], ['Eu', 'Eu Lβ', 6.458], ['Eu', 'Eu Lα', 5.849], ['Gd', 'Gd Kα', 42.996], ['Gd', 'Gd Kβ', 48.695], ['Gd', 'Gd Lβ', 6.708], ['Gd', 'Gd Lα', 6.053], ['Tb', 'Tb Kα', 44.482], ['Tb', 'Tb Kβ', 50.385], ['Tb', 'Tb Lβ', 6.975], ['Tb', 'Tb Lα', 6.273], ['Dy', 'Dy Kα', 45.999], ['Dy', 'Dy Kβ', 52.113], ['Dy', 'Dy Lβ', 7.248], ['Dy', 'Dy Lα', 6.498], ['Ho', 'Ho Kα', 47.547], ['Ho', 'Ho Kβ', 53.877], ['Ho', 'Ho Lβ', 7.526], ['Ho', 'Ho Lα', 6.72], ['Er', 'Er Kα', 49.128], ['Er', 'Er Kβ', 55.674], ['Er', 'Er Lβ', 7.811], ['Er', 'Er Lα', 6.949], ['Tm', 'Tm Kα', 50.742], ['Tm', 'Tm Kβ', 57.505], ['Tm', 'Tm Lβ', 8.102], ['Tm', 'Tm Lα', 7.18], ['Yb', 'Yb Kα', 52.388], ['Yb', 'Yb Kβ', 59.382], ['Yb', 'Yb Lβ', 8.402], ['Yb', 'Yb Lα', 7.416], ['Lu', 'Lu Kα', 54.07], ['Lu', 'Lu Kβ', 61.29], ['Lu', 'Lu Lβ', 8.71], ['Lu', 'Lu Lα', 7.655], ['Hf', 'Hf Kα', 55.79], ['Hf', 'Hf Kβ', 63.244], ['Hf', 'Hf Lβ', 9.023], ['Hf', 'Hf Lα', 7.899], ['Ta', 'Ta Kα', 57.535], ['Ta', 'Ta Kβ', 65.222], ['Ta', 'Ta Lβ', 9.343], ['Ta', 'Ta Lα', 8.146], ['W', 'W Kα', 59.318], ['W', 'W Kβ', 67.244], ['W', 'W Lβ', 9.672], ['W', 'W Lα', 8.398], ['Re', 'Re Kα', 61.141], ['Re', 'Re Kβ', 69.309], ['Re', 'Re Lβ', 10.01], ['Re', 'Re Lα', 8.652], ['Os', 'Os Kα', 63.0], ['Os', 'Os Kβ', 71.414], ['Os', 'Os Lβ', 10.354], ['Os', 'Os Lα', 8.911], ['Ir', 'Ir Kα', 64.896], ['Ir', 'Ir Kβ', 73.56], ['Ir', 'Ir Lβ', 10.708], ['Ir', 'Ir Lα', 9.175], ['Pt', 'Pt Kα', 66.831], ['Pt', 'Pt Kβ', 75.75], ['Pt', 'Pt Lβ', 11.071], ['Pt', 'Pt Lα', 9.442], ['Au', 'Au Kα', 68.806], ['Au', 'Au Kβ', 77.982], ['Au', 'Au Lβ', 11.443], ['Au', 'Au Lα', 9.713], ['Hg', 'Hg Kα', 70.818], ['Hg', 'Hg Kβ', 80.255], ['Hg', 'Hg Lβ', 11.824], ['Hg', 'Hg Lα', 9.989], ['Tl', 'Tl Kα', 72.872], ['Tl', 'Tl Kβ', 82.573], ['Tl', 'Tl Lβ', 12.213], ['Tl', 'Tl Lα', 10.269], ['Pb', 'Pb Kα', 74.97], ['Pb', 'Pb Kβ', 84.939], ['Pb', 'Pb Lβ', 12.614], ['Pb', 'Pb Lα', 10.551], ['Bi', 'Bi Kα', 77.107], ['Bi', 'Bi Kβ', 87.349], ['Bi', 'Bi Lβ', 13.023], ['Bi', 'Bi Lα', 10.839], ['Po', 'Po Kα', 79.291], ['Po', 'Po Kβ', 89.803], ['Po', 'Po Lβ', 13.446], ['Po', 'Po Lα', 11.131], ['At', 'At Kα', 81.516], ['At', 'At Kβ', 92.304], ['At', 'At Lβ', 13.876], ['At', 'At Lα', 11.427], ['Rn', 'Rn Kα', 83.785], ['Rn', 'Rn Kβ', 94.866], ['Rn', 'Rn Lβ', 14.315], ['Rn', 'Rn Lα', 11.727], ['Fr', 'Fr Kα', 86.106], ['Fr', 'Fr Kβ', 97.474], ['Fr', 'Fr Lβ', 14.771], ['Fr', 'Fr Lα', 12.031], ['Ra', 'Ra Kα', 88.478], ['Ra', 'Ra Kβ', 100.13], ['Ra', 'Ra Lβ', 15.236], ['Ra', 'Ra Lα', 12.339], ['Ac', 'Ac Kα', 90.884], ['Ac', 'Ac Kβ', 102.846], ['Ac', 'Ac Lβ', 15.713], ['Ac', 'Ac Lα', 12.652], ['Th', 'Th Kα', 93.351], ['Th', 'Th Kβ', 105.605], ['Th', 'Th Lβ', 16.202], ['Th', 'Th Lα', 12.968], ['Pa', 'Pa Kα', 95.868], ['Pa', 'Pa Kβ', 108.427], ['Pa', 'Pa Lβ', 16.703], ['Pa', 'Pa Lα', 13.291], ['U', 'U Kα', 98.44], ['U', 'U Kβ', 111.303], ['U', 'U Lβ', 17.22], ['U', 'U Lα', 13.614], ['Np', 'Np Kα', 101.059], ['Np', 'Np Kβ', 114.234], ['Np', 'Np Lβ', 17.751], ['Np', 'Np Lα', 13.946], ['Pu', 'Pu Kα', 103.734], ['Pu', 'Pu Kβ', 117.228], ['Pu', 'Pu Lβ', 18.296], ['Pu', 'Pu Lα', 14.282], ['Am', 'Am Kα', 106.472], ['Am', 'Am Kβ', 120.284], ['Am', 'Am Lβ', 18.856], ['Am', 'Am Lα', 14.62], ['Cm', 'Cm Kα', 109.271], ['Cm', 'Cm Kβ', 123.403], ['Cm', 'Cm Lβ', 19.427], ['Cm', 'Cm Lα', 14.961], ['Bk', 'Bk Kα', 112.121], ['Bk', 'Bk Kβ', 126.58], ['Bk', 'Bk Lβ', 20.018], ['Bk', 'Bk Lα', 15.308], ['Cf', 'Cf Kα', 115.032], ['Cf', 'Cf Kβ', 129.823], ['Cf', 'Cf Lβ', 20.624], ['Cf', 'Cf Lα', 15.66]]
	request_lines:list[float] = []
	for line in all_standard_element_lines:
		if line[0] == symbol:
			request_lines.append(line[2]*1000)
	return request_lines

def main():
	args:list[str] = sys.argv[1:]
	# print(f'{len(args)} args: {args}')

	# check args for input
	if len(args) == 0:
		print('Spectral Anomaly Checker usage: \n\tsac <energy-in-eV or element-symbol> <number-of-possibilities-to-show(default=5)> <`all` flag: uses more comprehensive line list>')
		raise SystemExit(2)
	
	# first arg: element symbol or energy in eV
	if len(args) >= 1:
		# make sure capitalisation is right for easier matching of symbol
		request_str:str = args[0].capitalize()

	# second arg: number of possibilities to output for each energy (optional)
	if len(args) >= 2:
		qty_str:str = args[1]
		try:
			qty:int = int(qty_str)
		except ValueError:
			qty:int = 5

			# the second value might be 'all/--all' if the second arg was skipped. if so, add it onto the arg stack as the third.
			args.append(qty_str)
	else: 
		qty:int = 5

	# third arg: flag to use 'all' list for all energies
	if len(args) >= 3:
		line_list_choice:str = args[2]
		if line_list_choice.lower() in ['all', '--all']:
			energies_csv_path:str = resource_path('energies_all.csv')	# ALL LINES, K L M, etc. for all elements up to 103.
		else:
			energies_csv_path:str = resource_path('energies_std.csv')   # BASIC LINES, K and L lines for all elements at energies below 50kV.
	else:
		energies_csv_path:str = resource_path('energies_std.csv')   # BASIC LINES, K and L lines for all elements at energies below 50kV.


	global energies_df
	energies_df = pd.read_csv(energies_csv_path)   

	try:
		request_ev:float = float(request_str)

		output:str = ''
		# eV value provided
		output += f'{qty} nearest possibilities to {request_ev} eV:\n'
		output += f'{getClosestByEnergy(request_ev, qty)}\n'
		
		print(output)
		return

	except ValueError: 
		request_lines:list[float] = getCommonElementLineEnergies(request_str)

		if len(request_lines) == 0:
			print('Input must be numerical energy (eV) or a recognised Element Symbol.')
			raise SystemExit(1)

		output:str = ''
		# str (symbol) value provided
		output += f'Nearby spectral phenomena for the {len(request_lines)} common spectral lines of {elementSymboltoName(request_str)}:\n'
		for lin in request_lines:
			
			output += f'\n{qty} nearest possibilities to {lin} eV:\n'
			output += f'{getClosestByEnergy(lin, qty)}\n'

		print(output)
		return

  

if __name__ == main():
	main()
