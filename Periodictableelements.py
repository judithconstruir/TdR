#This programme is created to be able to know some things about the elements of
#periodic table.
#I'm really thankful to Olga, my chemistry teacher, who with her pacience and 
#kindness, helped me love chemistry.
import string

class Element(): 
    def __init__(self, name, symbol, atomic_number, mass_number, energetic_levels, group, type, oxidation_number = None)-> None:
        self.name = name;
        self.X = symbol; 
        self.Z= atomic_number; 
        self.A = mass_number;
        self.energetic_levels = energetic_levels;
        self.group = group;
        self.type = type;
        self.ox_n = oxidation_number;
    
    def check_configuration(element, configuration):
        periodic_group =  element.group
        energetic_levels = element.energetic_levels
        Z = element.Z

        check_two_digits = False

        if configuration [-3].isnumeric():
            check_two_digits = True

        correct_configuration = ""
        configuration_is_correct = False

        if periodic_group <= 2:
            correct_configuration = f"s({periodic_group})" 
        elif element == He:
            correct_configuration = "s(2)"

        elif element == Ce or element == Lu or element == Gd: 
                correct_configuration = "d(1)"
        

        elif periodic_group <= 12 or element == Es or element == Fm or element == Md or element == No or element.type == "Lanthanide":

            if energetic_levels == 6 and Z > 57 and Z < 72:

                correct_configuration = f"f({Z-56})"


            elif energetic_levels == 7 and Z > 93 and Z < 103 and element != Cm:

                correct_configuration = f"f({Z-88})"


            elif energetic_levels == 7 and Z <= 93 and Z > 90 or element == Cm:
                #correct_configuration = f"f({Z-89})"
                correct_configuration = "d(1)"

            else: 

                correct_configuration = f"d({periodic_group-2})"

        elif element == Lr: 
                correct_configuration = "p(1)"

        elif periodic_group <= 18: 
            correct_configuration = f"p({periodic_group - 12})"
        else: 
            return "Something was wrong with the periodic group"


        if correct_configuration == configuration[-4:]:
            configuration_is_correct = True
        elif check_two_digits and correct_configuration == configuration[-5:]:
                configuration_is_correct = True

        else: 
            return "Something was wrong with the configuration. " + "Currently configuration is: " + configuration + ". Correct configuration is: " + correct_configuration

        return configuration_is_correct   

    def electronic_configuration(element):
        electrons_number = element.Z
        
        configuration = ""
        
        orbitals = ["s","p","d","f"]
        
        electronic_configuration_by_group = {1:"s(1)", 2:"s(2)"} #3:,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18}
        
        max_electrons_per_orbital = {"s":2, "p":6, "d": 10, "f":14}
        
        #For the moment, we print superindices between parenthesis()            
        while electrons_number >= 1:
            
            if "1s" not in configuration:
                if electrons_number >=2:
                    configuration = "1s(2)"
                    electrons_number -= 2
                else:
                    configuration = "1s(1)"
                    electrons_number -= 1
                
            elif "2s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "2s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "2s(1)"
                    electrons_number -= 1
            
            elif "2p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "2p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"2p({electrons_number})"
                    electrons_number = 0
                            
            elif "3s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "3s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "3s(1)"
                    electrons_number -= 1
            
            elif "3p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "3p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"3p({electrons_number})"
                    electrons_number = 0
            
            elif "4s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "4s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "4s(1)"
                    electrons_number -= 1
            
            elif "3d" not in configuration:
                if electrons_number >= 10:
                    configuration = configuration + "3d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"3d({electrons_number})"
                    electrons_number = 0
            
            elif "4p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "4p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"4p({electrons_number})"
                    electrons_number = 0
            
            elif "5s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "5s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "5s(1)"
                    electrons_number -= 1
            
            elif "4d" not in configuration:
                if electrons_number >= 10:
                    configuration = configuration + "4d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"4d({electrons_number})"
                    electrons_number = 0
            
            elif "5p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "5p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"5p({electrons_number})"
                    electrons_number = 0
                                   
            elif "6s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "6s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "6s(1)"
                    electrons_number -= 1
                
            elif "4f" not in configuration and element != La :
                if electrons_number >= 14:
                    configuration = configuration + "4f(14)"
                    electrons_number -= 14
                    
                elif element == Ce:
                    configuration = configuration + "4f(1)"
                    electrons_number -= 1
                    
                elif element == Eu or element == Gd:
                    configuration = configuration + "4f(7)"
                    electrons_number -= 7
                    
                else:
                    configuration = configuration + f"4f({electrons_number})"
                    electrons_number = 0        
                    
            elif "5d" not in configuration:     
                if electrons_number >= 10:
                    configuration = configuration + "5d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"5d({electrons_number})"
                    electrons_number = 0
            
            elif "6p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "6p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"6p({electrons_number})"
                    electrons_number = 0
                    
            elif "7s" not in configuration:
                if electrons_number >=2:
                    configuration = configuration + "7s(2)"
                    electrons_number -= 2
                else:
                    configuration = configuration + "7s(1)"
                    electrons_number -= 1
                       
            elif "5f" not in configuration and element != Ac and element != Th:
                if electrons_number >= 14:
                    configuration = configuration + "5f(14)"
                    electrons_number -= 14
                elif element == Pa:
                    configuration = configuration + "5f(2)"
                    electrons_number -= 2
                elif element == U:
                    configuration = configuration + "5f(3)"
                    electrons_number -= 3
                elif element == Np:
                    configuration = configuration + "5f(4)"
                    electrons_number -= 4
                elif element == Cm:
                    configuration = configuration + "5f(7)"
                    electrons_number -= 7
                else:
                    configuration = configuration + f"5f({electrons_number})"
                    electrons_number = 0
                    
            elif "7p" not in configuration and element == Lr:
                configuration = configuration + "7p(1)"
                electrons_number -= 1
            
            elif "6d" not in configuration:
                if electrons_number >= 10:
                    configuration = configuration + "6d(10)"
                    electrons_number -= 10
                else:
                    configuration = configuration + f"6d({electrons_number})"
                    electrons_number = 0
                    
            elif "7p" not in configuration:
                if electrons_number >= 6:
                    configuration = configuration + "7p(6)"
                    electrons_number -= 6
                else:
                    configuration = configuration + f"7p({electrons_number})"
                    electrons_number = 0
            
            else:
                return configuration + " Something happened with your electrons"

        if element.check_configuration(configuration):
            return configuration

def get_element_object(abbrev):
        for symbol in elements_list:
            if abbrev == symbol.X:
                element_object = symbol
                return element_object

def get_element_name(abbrev):
    for symbol in elements_list:
        if abbrev == symbol.X:
            element_name = symbol.name
            return element_name

def get_element_abbrev(name):
    for symbol in elements_list:
        if name == symbol.name:
            element_abbrev = symbol.X
            return element_abbrev

#The periodic table elements are created as instance of objects. 
Hydrogen = Element("Hydrogen", "H", 1, 1, 1, 1, "Non-Metal",[+1,-1])
H = Hydrogen
Helyum = Element("Helyum", "He", 2, 4, 1, 18, "Noble gas",[0] )
He = Helyum
Lithium = Element("Lithium", "Li", 3, 6.9, 2, 1, "Alkaline metal",[+1] )
Li = Lithium
Beryllium = Element("Beryllium", "Be", 4, 9.0, 2, 2, "Alkaline earth metal",[+2] )
Be = Beryllium
Boron = Element("Boron", "B", 5, 10.8, 2, 13, "Metalloid",[+3,-3] )
B = Boron
Carbon = Element("Carbon", "C", 6, 12, 2, 14, "Non-Metal",[+2,+4] )
C = Carbon
Nitrogen = Element("Nitrogen", "N", 7, 14, 2, 15, "Non-Metal",[+1,+2,+3,+4,+5,-3] )
N = Nitrogen
Oxygen = Element("Oxygen", "O", 8, 16, 2, 16, "Non-Metal",[-2, -1, +2] )
O = Oxygen
Fluor = Element("Fluor", "F", 9, 19, 2, 17, "Halogen",[-1] )
F = Fluor
Neon = Element("Neon", "Ne", 10, 20.2, 2, 18, "Noble gas",[0] )
Ne = Neon
Sodium = Element("Sodium", "Na", 11, 23, 3, 1, "Alkaline metal",[+1] )
Na = Sodium
Magnesium = Element("Magnesium", "Mg", 12, 24.3, 3, 2, "Alkaline earth metal",[+2] )
Mg = Magnesium 
Aluminum = Element("Aluminum", "Al", 13, 27, 3, 13, "Post-transition metal",[+3] )
Al = Aluminum
Silicon = Element("Silicon", "Si", 14, 28.1, 3, 14, "Metalloid",[+4,-4] )
Si = Silicon
Phosphorus = Element("Phosphorus", "P", 15, 31, 3, 15, "Non-Metal",[+1,+3,+5,+7,-3] ) #+1, +7 introduced later
P = Phosphorus
Sulfur = Element("Sulfur", "S", 16, 32.1, 3, 16, "Non-Metal",[+2,+4,+6,-2])
S = Sulfur
Chlorine = Element("Chlorine", "Cl", 17, 35.5, 3, 17, "Non-Metal",[+1,+3,+5,+7,-1])
Cl = Chlorine
Argon = Element("Argon", "Ar", 18, 39.9, 3, 18, "Noble gas",[0] )
Ar = Argon
Potassium = Element("Potassium", "K", 19, 39.1, 4, 1, "Alkaline metal",[+1] )
K = Potassium
Calcium = Element("Calcium", "Ca", 20, 40.1, 4, 2, "Alkaline earth metal",[+2] )
Ca = Calcium
Scandium = Element("Scandium", "Sc", 21, 45, 4, 3, "Transition metal" ) 
Sc = Scandium
Titanium = Element("Titanium", "Ti", 22, 47.9, 4, 4, "Transition metal" )
Ti = Titanium
Vanadium = Element("Vanadium", "V", 23, 50.9, 4, 5, "Transition metal" ) 
V = Vanadium
Chromium = Element("Chromium", "Cr", 24, 52, 4, 6, "Transition metal",[+2,+3,+6] ) 
Cr = Chromium
Manganese  = Element("Manganese", "Mn", 25, 54.9, 4, 7, "Transition metal",[+2, +3, +4, +6 , +7] )
Mn = Manganese
Iron = Element("Iron", "Fe", 26, 55.8, 4, 8, "Transition metal",[+2,+3] )
Fe = Iron
Cobalt = Element("Cobalt", "Co", 27, 58.9, 4, 9, "Transition metal" )
Co = Cobalt
Nickel = Element("Nickel", "Ni", 28, 58.7, 4, 10, "Transition metal",[+2,+3] )
Ni = Nickel
Copper= Element("Copper", "Cu", 29, 63.5, 4, 11, "Transition metal",[+1,+2] )
Cu = Copper
Zinc= Element("Zinc", "Zn", 30, 65.4, 5, 12, "Transition metal",[+2] )
Zn = Zinc
Gallium = Element("Gallium", "Ga", 31, 69.7, 4, 13, "Post-transition metal" )
Ga = Gallium
Germanium = Element("Germanium", "Ge", 32, 72.6, 4, 14, "Metalloid" )
Ge = Germanium
Arsenic = Element("Arsenic", "As", 33, 74.9, 4, 15, "Metalloid",[+3, +5, -3] )
As = Arsenic
Selenium = Element("Selenium", "Se", 34, 79, 4, 16, "Non-Metal",[+2,+4,+6,-2] )
Se = Selenium
Bromine = Element("Bromine", "Br", 35, 79.9, 4, 17, "Halogen",[+1,+3,+5,+7,-1] )
Br = Bromine
Kypton  = Element("Kypton", "Kr", 36, 83.8, 4, 18, "Noble gas",[0] )
Kr = Kypton 
Rubidium = Element("Rubidium", "Rb", 37, 85.5, 5, 1, "Alkaline metal",[+1] )
Rb = Rubidium
Strontium = Element("Strontium", "Sr", 38, 87.6, 5, 2, "Alkaline earth metal",[+2] )
Sr = Strontium
Yttrium = Element("Yttrium", "Y", 39, 88.9, 5, 3, "Transition metal" ) 
Y = Yttrium
Zirconium = Element("Zirconium", "Zr", 40, 91.2, 5, 4, "Transition metal" )
Zr = Zirconium
Niobium = Element("Niobium", "Nb", 41, 92.9, 5, 5, "Transition metal" ) 
Nb = Niobium
Molybdenum = Element("Molybdenum", "Mo", 42, 95.9, 5, 6, "Transition metal" ) 
Mo = Molybdenum
Technetium = Element("Technetium", "Tc", 43, 97.9, 5, 7, "Transition metal" )
Tc = Technetium
Ruthenium = Element("Ruthenium", "Ru", 44, 101.1, 5, 8, "Transition metal" )
Ru = Ruthenium
Rhodium = Element("Rhodium", "Rh", 45, 102.9, 5, 9, "Transition metal" )
Rh = Rhodium
Paladium = Element("Paladium", "Pd", 46, 106.4, 5, 10, "Transition metal",[+2,+4] ) 
Pd = Paladium
Silver = Element("Silver", "Ag", 47, 107.9, 5, 11, "Transition metal",[+1] )
Ag = Silver
Cadmium = Element("Cadmium", "Cd", 48, 112.4, 5, 12, "Transition metal",[+2] )
Cd = Cadmium
Indium = Element("Indium", "In", 49, 114.8, 5, 13, "Post-transition metal" )
In = Indium
Tin = Element("Tin", "Sn", 50, 118.7, 5, 14, "Post-transition metal",[+2,+4] )
Sn = Tin
Antimony = Element("Antimony", "Sb", 51, 121.8, 5, 15, "Metalloid",[+3,+5,-3] )
Sb = Antimony
Tellurium = Element("Tellurium", "Te", 52, 127.6, 5, 16, "Metalloid",[+2,+4,+6,-2] )
Te = Tellurium
Iodine = Element("Iodine", "I", 53, 126.9, 5, 17, "Halogen",[+1,+3,+5,+7,-1] )
I = Iodine
Xenon = Element("Xenon", "Xe", 54, 131.3, 5, 18, "Noble gas",[0] )
Xe = Xenon
Cesium = Element("Cesium", "Cs", 55, 132.9, 6, 1, "Transition metal",[+1] )
Cs = Cesium
Barium = Element("Barium", "Ba", 56, 137.3, 6, 2, "Transition metal",[+2] )
Ba = Barium
Lanthanum = Element("Lanthanum", "La", 57, 138.9, 6, 3, "Lanthanide" )
La = Lanthanum
Cerium = Element("Cerium", "Ce", 58, 140.1, 6, 4, "Lanthanide" )
Ce = Cerium
Praseodymium = Element("Praseodymium", "Pr", 59, 140.9, 6, 5, "Lanthanide" )
Pr = Praseodymium
Neodymium = Element("Neodymium", "Nd", 60, 144.2, 6, 6, "Lanthanide" )
Nd = Neodymium
Promethium = Element("Promethium", "Pm", 61, 145, 6, 7, "Lanthanide" )
Pm = Promethium
Samarium = Element("Samarium", "Sm", 62, 150.4, 6, 8, "Lanthanide" )
Sm = Samarium
Europium = Element("Europium", "Eu", 63, 152, 6, 9, "Lanthanide" )
Eu = Europium
Gadolinium = Element("Gadolinium", "Gd", 64, 157.2, 6, 10, "Lanthanide" )
Gd = Gadolinium
Terbium = Element("Terbium", "Tb", 65, 158.9, 6, 11, "Lanthanide" )
Tb = Terbium
Dysprosium = Element("Dysprosium", "Dy", 66, 162.5, 6, 12, "Lanthanide" )
Dy = Dysprosium
Holmium = Element("Holmium", "Ho", 67, 164.9, 6, 13, "Lanthanide" )
Ho = Holmium
Erbium = Element("Erbium", "Er", 68, 167.3, 6, 14, "Lanthanide" )
Er = Erbium
Thulium = Element("Thulium", "Tm", 69, 168.9, 6, 15, "Lanthanide" )
Tm = Thulium
Ytterbium = Element("Ytterbium", "Yb", 70, 173, 6, 16, "Lanthanide" )
Yb = Ytterbium
Lutetium = Element("Lutetium", "Lu", 71, 175, 6, 17, "Lanthanide" )
Lu = Lutetium
Hafnium = Element("Hafnium", "Hf", 72, 178.5, 6, 4, "Transition metal" )
Hf = Hafnium
Tantalum = Element("Tantalum", "Ta", 73, 180.9, 6, 5, "Transition metal" )
Ta = Tantalum
Tungsten = Element("Tungsten", "W", 74, 183.58, 6, 6, "Transition metal" )
W = Tungsten
Rhenium = Element("Rhenium", "Re", 75, 186.2, 6, 7, "Transition metal" ) 
Re = Rhenium
Osmium = Element("Osmium", "Os", 76, 190.2, 6, 8, "Transition metal" ) 
Os = Osmium
Iridium = Element("Iridium", "Ir", 77, 192.2, 6, 9, "Transition metal" )
Ir = Iridium
Platinum = Element("Platinum", "Pt", 78, 195.1, 6, 10, "Transition metal",[+2,+4] ) 
Pt = Platinum
Gold = Element("Gold", "Au", 79, 197, 6, 11, "Transition metal",[+1,+3] )
Au = Gold
Mercury = Element("Mercury", "Hg", 80, 200.6, 6, 12, "Transition metal",[+1,+2] )
Hg = Mercury
Thallium = Element("Thallium", "Tl", 81, 204.4, 6, 13, "Post-transition metal" ) 
Tl = Thallium
Lead = Element("Lead", "Pb", 82, 207.2, 6, 14, "Post-transition metal",[+2,+4] ) 
Pb = Lead
Bismuth = Element("Bismuth", "Bi", 83, 209, 6, 15, "Post-transition metal",[+3,+5] )  
Bi = Bismuth
Polonium = Element("Polonium", "Po", 84, 209, 6, 16, "Metalloid" )  
Po = Polonium
Astatine = Element("Astatine", "At", 85, 210, 6, 17, "Halogen" ) 
At = Astatine
Radon = Element("Radon", "Rn", 86, 222, 6, 18, "Noble gas",[0] )
Rn = Radon
Francium = Element("Francium", "Fr", 87, 223, 7, 1, "Alkaline metal" ) 
Fr = Francium
Radium = Element("Radium", "Ra", 88, 226, 7, 2, "Alkaline earth metal" ) 
Ra = Radium
Actinium = Element("Actinium", "Ac", 89, 227, 7, 3, "Actinide" )
Ac = Actinium
Thorium = Element("Thorium", "Th", 90, 232, 7, 4, "Actinide" )
Th = Thorium
Protactinium = Element("Protactinium", "Pa", 91, 231, 7, 5, "Actinide" )
Pa = Protactinium
Uranium = Element("Uranium", "U", 92, 238, 7, 6, "Actinide" )
U = Uranium
Neptuninum = Element("Neptuninum", "Np", 93, 237, 7, 7, "Actinide" )
Np = Neptuninum
Plutonium = Element("Plutonium", "Pu", 94, 244, 7, 8 , "Actinide" )
Pu = Plutonium
Americium = Element("Americium", "Am", 95, 243, 7, 9, "Actinide" )
Am = Americium
Curium = Element("Curium", "Cm", 96, 247, 7, 10, "Actinide" ) 
Cm = Curium
Berkelium = Element("Berkelium", "Bk", 97, 247, 7, 11, "Actinide" )
Bk = Berkelium
Californium = Element("Californium", "Cf", 98, 251, 7, 12, "Actinide" )
Cf = Californium
Einsteinium = Element("Einsteinium", "Es", 99, 252, 7, 13, "Actinide" ) 
Es = Einsteinium
Fermium = Element("Fermium", "Fm", 100, 257, 7, 14, "Actinide" )
Fm = Fermium
Mendelevium = Element("Mendelevium", "Md", 101, 258, 7, 15, "Actinide" )
Md = Mendelevium
Nobelium = Element("Nobelium", "No", 102, 259, 7, 16, "Actinide" )
No = Nobelium
Lawrencium = Element("Lawrencium", "Lr", 103, 262, 7, 17, "Actinide" )
Lr = Lawrencium
Rutherfordium = Element("Rutherfordium", "Rf", 104, 267, 7, 4, "Transition metal" )
Rf = Rutherfordium
Dubnium = Element("Dubnium", "Db", 105, 268, 7, 5, "Transition metal" )
Db = Dubnium
Seaborgium = Element("Seaborgium", "Sg", 106, 271, 7, 6, "Transition metal" )
Sg = Seaborgium
Bohrium = Element("Bohrium", "Bh", 107, 272, 7, 7, "Transition metal" )
Bh = Bohrium
Hassium = Element("Hassium", "Hs", 108, 270, 7, 8, "Transition metal" )
Hs = Hassium
Meitnerium = Element("Meitnerium", "Mt", 109, 276, 7, 9, "Transition metal") 
Mt = Meitnerium
Darmstadtium = Element("Darmstadtium", "Ds", 110, 281, 7, 10, "Transition metal" )
Ds = Darmstadtium
Roentgenium = Element("Roentgenium", "Rg", 111, 280, 7, 11, "Transition metal" )
Rg = Roentgenium
Copernicium = Element("Copernicium", "Cn", 112, 285, 7, 12, "Transition metal" )
Cn = Copernicium
Nihonium = Element("Nihonium", "Nh", 113, 284, 7, 13, "Post-transition metal" )
Nh = Nihonium
Flerovium = Element("Flerovium", "Fl", 114, 289, 7, 14, "Post-transition metal" )
Fl = Flerovium
Moscovium = Element("Moscovium", "Mc", 115, 288, 7, 15, "Post-transition metal" )
Mc = Moscovium
Livermorium = Element("Livermorium", "Lv", 116, 293, 7, 16, "Post-transition metal" )
Lv = Livermorium
Tennessine = Element("Tennessine", "Ts", 117, 294, 7, 17, "Halogen" )
Ts = Tennessine
Oganesson = Element("Oganesson", "Og", 118, 294, 7, 18, "Noble gas" )
Og = Oganesson

elements_list = [H,He,
                 Li,Be,B,C,N,O,F,Ne,Na,Mg,Al,Si,P,S,Cl,Ar,
                 K,Ca,Sc,Ti,V,Cr,Mn,Fe,Co,Ni,Cu,Zn,Ga,Ge,As,Se,Br,Kr,
                 Rb,Sr,Y,Zr,Nb,Mo,Tc,Ru,Rh,Pd,Ag,Cd,In,Sn,Sb,Te,I,Xe,
                 Cs,Ba,La,Ce,Pr,Nd,Pm,Sm,Eu,Gd,Tb,Dy,Ho,Er,Tm,Yb,Lu,
                 Hf,Ta,W,Re,Os,Ir,Pt,Au,Hg,Tl,Pb,Bi,Po,At,Rn,
                 Fr,Ra,Ac,Th,Pa,U,Np,Pu,Am,Cm,Bk,Cf,Es,Fm,Md,No,Lr,
                 Rf,Db,Sg,Bh,Hs,Mt,Ds,Rg,Cn,Nh,Fl,Mc,Lv,Ts,Og]

electronegativity_list = [F, Cl, Br, At,
                           O, S, Se, Te, Po,
                             H,
                               N, P, As, Sb, Bi,
                                 C, Si, Ge, Sn, Pb,
                                   B, Al, Ga, In, Tl,
                                     Zn, Cd, Hg,
                                       Cu, Ag, Au, Rg,
                                         Ni, Pd, Pt, Ds,
                                           Co, Rh, Ir, Mt,
                                             Fe, Ru, Os, Hs,
                                               Mn, Tc, Re, Bh,
                                                 Cr, Mo, W, Sg,
                                                   V, Nb, Ta, Db,
                                                    Ti, Zr, Hf, Rf, 
                                                     Sc, Y, La,
                                                      Lu,    Ac,     Lr,
                                                       Be, Mg, Ca, Sr, Ba, Ra,
                                                        Li, Na, K, Rb, Cs, Fr,
                                                        He, Ne, Ar, Kr, Xe, Rn]     

prefixes = ["", 
            "mono",
                "di",
                    "tri",
                        "tetra",
                            "penta",
                                "hexa",
                                    "hepta",
                                        "octa",
                                            "nona",
                                                "deca"]

#Elements are classified
metals = []
no_metals = []
noble_gases = []

for element in elements_list:
    if element.type == "Noble gas":
        noble_gases.append(element)

    elif element.type == "Halogen" or element.type == "Non-Metal" or element.type == "Post-transition metal" or element == B or element == Si or element == As or element == Te:
        no_metals.append(element)
    
    else: 
        metals.append(element)
    
    #If there is an element without number of oxidations is added an empty list 
    if element.ox_n == None:
        element.ox_n = []

#About oxidation numbers: They are invented numbers used by humans to work with the compounds. They are really useful to simplify 
# how atoms interacts and "fusionate" each other. As example, the difference between CO and CO2 is that oxygen almost always acts 
# with oxidation number -2, so then carbon acts with oxidation numbers +2 (CO) and with +4 (CO2).   

      
#This function return a dictionary with elements of formula or its charge. It is going to serve us to work. 
#Dictionary counts the quantity of atoms of each element abbreviation. 
def elements_in_formula(formula, atoms_or_charge=None): 

    elements_atoms = {} #Number of atoms of each element
    charge = 0 #Charge of elements in formula 
    
    abbrev_element = ""
    
    for i in range(len(formula)):
        num_of_atoms = 0

        #When there is a new element, uppercase is encountered. We check that.
        if formula[i] in string.ascii_uppercase:
            #This is checking if the next character is lower case e.g. "Fe" or "He" #0 is Uppercase, 1 is lowercase, 2 is number
            if i + 1  < len(formula) and formula[i+1] in string.ascii_lowercase: #01, Ul
                abbrev_element = formula[i] + formula[i+1]
                num_of_atoms = 1

                #This is checking if the next character is a number e.g. "Hg2"
                if i + 2 < len(formula) and formula[i+2].isnumeric(): #012 Uln
                    num_of_atoms = int(formula [i+2])
                    
            
            #This is checking if the next character is a number e.g. "N2"    
            elif i + 1 < len(formula) and formula[i+1].isnumeric(): #02 Un
                abbrev_element = formula[i]
                if i + 2 < len(formula) and formula[i+2].isnumeric(): #012 Unn
                    num_of_atoms = int(formula[i+1] + formula[i+2])  
                else:
                    num_of_atoms = int(formula[i+1]) #02 Un   
            
                   

            #This is checking if the next character is a new element e.g. "HF"
            elif i + 1 <= len(formula) or formula[i+1] in string.ascii_uppercase:#00 UU or 0 U
                abbrev_element = formula[i]
                num_of_atoms = 1


            else:
                return "Something happened. Check your code "

            #We add the element to the dictionary.
            elements_atoms[abbrev_element] = num_of_atoms

        #Here we check if there is a parenthesis. Then the formula has charge, is a molecule or is in aquous solution  .
        elif formula[i] == "(":
            

            #If charge is positive it indicates that is losing electrons, else is accepting ones.
            if formula[i+1].isnumeric(): #x(n+)
                #Positive with number
                if formula[i+2] == "+":
                    charge = int(formula[i+1])
                #Negative with number
                elif formula[i+2] == "-":
                    charge = -(int(formula[i+1]))

            #When there is not a number, the charge is 1 (positive or negative):    
            elif formula[i+1] == "+": #x(+)
                charge = 1
            #Negative without number
            elif formula[i+1] == "-": #x(-)
                charge = -1

            #If aquous solution we assign the charge -9:
            elif formula[i+1] + formula[i+2] == "aq":
                charge = -9
                #Rarely charge is going to be -9. At the moment, we use it to differentiate the aquous solution from charge. 

            #If is molecule, another dictionary is created:
            #A molecule indicates that a set of atoms are multiplied together inside the formula.
            elif formula[i+1] in string.ascii_uppercase and ")" in formula:#x(y)
                number_of_molecules = 0
                #Formula of inside the parenthesis, extracting the molecule.
                molecule = formula[i+1:formula.index(")")]
                
                #Number that multiplies molecule.
                if formula.index(")") >= len(formula) and formula[formula.index(")") + 1].isnumeric():
                    number_of_molecules = int(formula[formula.index(")") + 1])
                


                #New dictionary of molecule updates original one. You have all atoms in the same siege
                new_atoms_d = elements_in_formula(molecule, "atoms")

                for k in new_atoms_d:
                     new_atoms_d[k] = new_atoms_d[k]

                elements_atoms.update(new_atoms_d)
                #Estructure: {"Abbrev1": x, "Abbrev2": y}            
                if atoms_or_charge == "atoms":
                    return elements_atoms
    
                #Charge return an integer: N 
                #Charge return an integer: N 
                #Aquous solution return -9 as charge.
                elif atoms_or_charge == "charge":
                    return charge

                # {"Abbrev1": x, "Abbrev2": y} & N
                else:
                    return elements_atoms, charge
            
            else: 
                return "Wrong formula. Check the code"
    
    #This tree return the atoms or the charge according that asked
    
    #Estructure: {"Abbrev1": x, "Abbrev2": y}            
    if atoms_or_charge == "atoms":
        return elements_atoms
    
    #Charge return an integer: N 
    #Aquous solution return -9 as charge.
    elif atoms_or_charge == "charge":
        return charge
    
    # {"Abbrev1": x, "Abbrev2": y} & N
    else:
        return elements_atoms, charge

#This classifies the compound, according if they are simple, binary, tertiary, quaternary or more complex. 
#Depending on if compounds has one or more different elements it would be one type or another. 
#Simple type has atoms of the same element, binary of 2 different and so on. Since 5 elements differents the compounds are complexs. 
def classification_of_compounds(formula):
    compounds_are = ["simple", "binary", "tertiary", "quaternary", "complex"]
    elements_of_formula_to_classify = elements_in_formula(formula, "atoms")
    quantity_of_elements = len(elements_of_formula_to_classify) 
       
    #Here we check if there is a dictionary inside, then we have to count the elements there are in and sum them to the quantity of elements.
    #We do this because the estructure of dictionary with other inside is like the following:
    ## {"Abbrev1": v, "Abbrev2": x, {"Abbrev3": y, "Abbrev4": z}: w};
    #if dictionary_inside(elements_of_formula_to_classify) is not None:
        #quantity_of_elements += len(dictionary_inside(elements_of_formula_to_classify))

    #We assign the corresponding category.
    if quantity_of_elements >= 5:
        compound_is = "complex"
        
    else:
        compound_is = compounds_are[quantity_of_elements-1]

    return compound_is


#It modifies the names.
def rename(element_name, suffix = "", prefix = ""):
    
    if suffix == "":
        pass
    elif element_name == "Hydrogen" or element_name == "Nitrogen":
        element_name = element_name.replace("ogen", suffix)

    elif element_name == "Phosphorus":
        element_name = element_name.replace("us", suffix)

    elif element_name == "Sulfur":
        element_name = element_name + suffix

    elif element_name == "Oxygen": 
        element_name = element_name.replace("ygen", suffix)

    elif element_name == "Antimony":
        element_name = element_name.replace("y", suffix)

    elif element_name == "Arsenic":
        element_name = element_name.replace("ic", suffix)

    elif element_name[-3:] == "ium": 
        element_name = element_name.replace("ium", suffix)

    elif element_name[-2:] == "on":
        element_name = element_name + suffix

    elif element_name [-3:] == "ine":
        element_name = element_name.replace("ine", suffix)
    
    else:
        element_name = element_name + suffix

    return prefix + element_name.lower()

#Inorganic nomenclature
#The following function return the names of a given formula. All the substances have name and formula, that identify them.
#There are 3 types of possible nomenclatures: substitution, addition and composition.
#We will focus on the nomenclature of composition or stoichiometric, that indicates the composition of substance. 
#We can name it at 3 different forms: with multipliers prefixes, expressing the oxidation number with romans numbers or using
#the charge with arabic numbers followed by sign. 
#For the moment, we focus on the nomenclature with multipliers prefixes. 

#Aclaration about the introduction of formulas: On paper we use superindices but here I'm going to use the parenthesis as indicator
#of a superindex to simplify. 

def name_formula (formula, name_or_type="name"):
    #Proclaming the name
    name = ""

    #Proclaming the type
    compound_type = ""
    

    #We will need this
    compound_is = classification_of_compounds(formula)
    atoms_per_formula = elements_in_formula(formula, "atoms")
    charge = elements_in_formula(formula, "charge")
    
    
    
    #As we said before, simple compound is made by the same element. Frecuently they present estructure of cristal nets or molecules. 
    if compound_is == "simple":
        element_name = ""
        number_of_atoms = 0
        
        atom_d = atoms_per_formula

        for unique_element in atom_d:
            element_name = get_element_name(unique_element)
            number_of_atoms = atom_d[unique_element]

        prefix = prefixes[number_of_atoms]
        #Rarely the prefix mono is used 
        if prefix == "mono":
            prefix = ""

        electrons_balance = charge

        #It's cation, then loses electrons
        if charge > 0: 
            charge_ = "(" + str(abs(electrons_balance)) + "+" + ")"
        
        #It's anion, then gains electrons. Anions changes the name with suffix. This is usual in all the substances, the most electronegative elements are encountered at the right on formulas.  
        elif charge < 0:
            charge_ ="(" + str(abs(electrons_balance)) + "-" + ")"

            element_name = rename(element_name, "ide")

        else:
            charge_ = ""
            if atoms_per_formula["O"] == 3:
                name = "Ozone"
                return name

        name = prefix + element_name.lower() + charge_

    #Binary compounds can be combined with oxygen, combined with hydrogen, binary salts, or two no metals combined.
    if compound_is == "binary":
        list_of_elements = []
        for element in atoms_per_formula:
            list_of_elements.append(element)
        ###
        #This exception is written to ions heteropolyatomics, when they have charge it means that they are ions.
        if 0 > charge and charge < 0:
            compound_is = "tertiary"
        ###
        #This function help us to otorgate some names:
        def adjust_prefixes_and_name(list_of_binary_elements):
                list_of_elements = list_of_binary_elements

                first_element = list_of_elements[0]
                second_element = list_of_elements[1]
                

                #We assign prefixes
                first_prefix = prefixes[atoms_per_formula[first_element]]
                second_prefix = prefixes[atoms_per_formula[second_element]]
                

                #Prefix mono is not necessary at least that confusion is generated and it is necessary to know if there is only one possibility. 
                if second_prefix == "mono":
                    #We are sure that there is only one possibility, knowing if the element has only one number of oxidation 
                    if len(get_element_object(first_element).ox_n) == 1:
                        second_prefix = ""

                if first_prefix == "mono":
                        first_prefix = ""

                name = rename(get_element_name(first_element), "", first_prefix) + " " + rename(get_element_name(second_element), "ide", second_prefix)
                return name.capitalize()
        ###
        
        #Compounds with oxygen can be oxides or peroxides:
        #  
        #Oxides are binary combinations between oxygen with oxidation number -2 and elements more electropositives than oxygen.
        maybe_is_oxide = False
                
        #Peroxides are binary combinations where oxygen acts with oxidation number -1. Peroxides are combined with alkaline and alkaline earth metal.
        maybe_is_peroxide = False

        #Compounds with hydrogen can be metal hydrides, hydracids, and parent hydrides.
        maybe_is_metal_hydride = False #Hydrogen with metal, oxidation number of hydrogen is -1.
        maybe_is_hydracid = False #Hydrogen with more electronegative elements(group 16 and 17), hydrogen acts with oxidation number 1.
        maybe_is_parent_hydride = False #Special case of hydrides, element is not hydrogen from group 13 to group 17. 

        #Binary salts are the combination of a metal with no metal. The no-metal will finish with -ur. 
        metal_with_no_metal = False #(Salt)
        maybe_is_binary_salt = True
        
        #The combination of two metals are formulated based on the oxidation numbers. This one more electronegative is written second. 
        combination_of_two_no_metals = False

        ###
        #Parent hydrides (hidrurs progenitors) are named with an specific name(usually known), although can be named with systematic nomenclature or traditionally if it is in aquous solution.
        parent_hydrides = {
            "H2O" : ["water"],
            "HF": ["fluorine", "hydrofluoric acid"],
            "HCl": ["chlorine", "hydrochloric acid"],
            "HBr": ["bromane",  "hydrobromic acid"],
            "HI":  ["iodane",   "hydroiodic acid"],
            "H2S": ["sulfane",  "hydrosulfuric acid"],
            "H2Se":[ "selenane","hydroselenic acid"],
            "H2Te":[ "tellane", "hydrotelluric acid"],
            "AtH": ["astatane", "hydroastatic acid"],
            "BH3": ["borane",   "Boron trihydride"],
            "CH4": ["methane",  "Methane"],
            "NH3": ["ammonia",  "Ammonia"],
            "AlH3":[ "alumane", "Aluminium hydride"],
            "SiH4":[ "silane",  "Silicon hydride"],
            "PH3": ["phosphane","Phosphine (Phosphane)"],
            "GaH3":["gallane", "Gallium trihydride" ],
            "GeH4":["germane","Germanium hydride"],
            "AsH3":["arsine" , "Arsenic hydride"],
            "SnH4":["stannane", "Tin hydride"],
            "SbH3":["stibine"  , "Antimony hydride (Stibine)"],
            "InH3":["indigane" , "Indium hydride"],
            "TlH3":["thalane"  , "Thallium hydride"],
            "PbH4":["plumbane" , "Lead hydride"],
            "BiH3":["bismuthane", "Bismuth hydride"],
            "PoH2":["polonane" ,"Polonium hydride"]
        }

        #Assign the name parent hydrides directly because they are special case. 
        if formula in parent_hydrides:
            #The name depends on the aquous solution: 
            if charge == -9:#-9 charge indicates aquous solution, as we said before.
                name = parent_hydrides[formula][1]
            #If is not in aquous solution, is called by the usual name.
            else:
                name = parent_hydrides[formula][0]
            
            return name.capitalize()

        #We start with prefixes
        element_name = ""

        #Here the elements of the formula are iterated to do some complexities
        for element in atoms_per_formula:
            element_object = get_element_object(element)
            element_name = get_element_name(element)

            
            #Here we check the possibility of having an oxide.
            # We search elements more electropositives than oxygen, then, with an oxidation number greater than -2, this one with which acts oxygen.   
            for oxidation_number in element_object.ox_n:
                if oxidation_number > -2:
                    maybe_is_oxide = True
                    
            #This is checking the possibility of a peroxide.
            if element_object.type == "Alkaline metal" or element_object.type == "Alkaline earth metal" and "O" in list_of_elements:
                if 2/atoms_per_formula[element] in element_object.ox_n and atoms_per_formula["O"] == 2:
                    maybe_is_peroxide = True #Oxidation number of oxigen in the case of peroxide is -1 ( peroxide group 02(-2)), then we need element that withstands this oxidation number.

            #We name the peroxide.
            elif element == "O" and maybe_is_peroxide:               
                name = get_element_name(list_of_elements[0]) + " peroxide" ##
                commpoud_type = "peroxide"
                break
                return name
                #Peroxide has not nomenclature with number of oxidation or charge because is known that the number of oxidation of peroxide is -1. Then, these nomenclatures will be the same.
                       
            #If it can be a oxide and it cointains oxygen, indeed it is oxide. 
            elif maybe_is_oxide and element == "O":
                name = adjust_prefixes_and_name(list_of_elements)
                compound_type == "oxide"
                break
                return name

            #Here we check the possibility of having metal hydride and binary salt. 
            elif element_object in metals:
                
                maybe_is_metal_hydride = True
                maybe_is_binary_salt = True
                
            #When metal hydride, hydrogen acts with oxidation number -1. We name it.
            elif maybe_is_metal_hydride and element == "H":
                name = adjust_prefixes_and_name(list_of_elements)
                compound_type = "metal hydride"
                break

            #Here we check the possibility of an hydracid
            elif element == "H" :
                maybe_is_hydracid = True

            #First, we checked if can be binary salt having a metal. Now, we check the combination (metal + no metal)
            #No metal finishes -ide  
            
            elif maybe_is_binary_salt and element_object in no_metals:
    
                name = adjust_prefixes_and_name(list_of_elements)
                return name
            
            #Hydrogen is joined with and halogen or amfigen, more electronegative elements. It acts with oxidation number +1.
            #Compounds emerged are soluble in water (aq) and forms acid solutions. Traditionally are named hydro+element+ic + acid 
            elif maybe_is_hydracid and (element_object.group == 16 or element_object.group == 17):
                #We see if it is aquous solution.
                if charge == -9:
                    name = rename(get_element_name(element), "ic", "hydro") +  " acid"
                else:
                    name = "hydrogen" + rename(get_element_name(element), "ide")  
            #
            elif element_object in no_metals and maybe_is_metal_hydride == False and maybe_is_binary_salt == False and maybe_is_hydracid == False:
                maybe_are_2_no_metal = True

            #iF is a combination of two no metals then, the most electronegative element acts with the oxidation nmber more negative.
            elif element_object in no_metals and maybe_are_2_no_metal:
                
                name = adjust_prefixes_and_name(list_of_elements)
                return name





    #Tertiary/Quaternary.           
    if compound_is == "tertiary" or compound_is == "quaternary":
        name = ""
        prefix = ""
        suffix = ""
        
        list_of_elements = []
        for element in atoms_per_formula:
            list_of_elements.append(element)
            
        #Tertiary and quaternary can be classified in 4 types: hydroxide, oxoacid, oxosalt, and ion heteropolyatomic.

        #Hydroxides are formed with metal and OH- group. This group always acts with valence -1. 
        #In the formulas the metal is always encountered before than the group hydroxide. 

        ###
        #XOH X(OH)n
        maybe_is_hydroxide = False 
         
        #HaXbOc
        #In general, it is added water to an oxide to create an oxoacid. 
        maybe_is_oxoacid = False
        
        ###
        name_molecule = ""
        #if dictionary_inside(atoms_per_formula) is not None:

        #     part_molecule = dictionary_inside(atoms_per_formula)
        #     prefix = prefix[atoms_per_formula[part_molecule]]
        #     if prefix == "mono":
        #         prefix = ""
        #     name_molecule = prefix + name_formula(part_molecule)
        # ###

        #OH Oxigen acts -2, hydrogen acts +1, the group hydroxide acts -1 as a whole
        #We iterate the elements of the formula to check some complexities of it. 
        for element in atoms_per_formula:
            element_object = get_element_object(element)
            
            #Here we check the possibility of having an hydroxide.
            if element == "O" and charge == 0:
                maybe_is_hydroxide = True

            #Here we check if it is a hydroxide and we name the hydroxide
            elif maybe_is_hydroxide and element == "H" and charge == 0:
                if ")" in formula:
                    if ( formula[formula.index(")") + 1]).isnumeric():
                        quantity_of_hydroxides = (formula[formula.index(")") + 1])
                        if prefixes[int(quantity_of_hydroxides)] == "mono":
                            prefix = ""
                        else:
                            prefix = prefixes[int(quantity_of_hydroxides)]

                name = get_element_name(list_of_elements[0]) + " " + prefix + "hydroxide"

            #Here we have the possibility of having an oxoacid. 
            elif element == "H"and charge == 0:
                maybe_is_oxoacid = True
                
            #Here we are naming if is oxoacid.
            elif maybe_is_oxoacid and element != "O" and "O" in atoms_per_formula and (element_object in no_metals or element_object.type == "Transition metal") and charge == 0: #It is oxoacid.
                #print(True)
                H_atoms = atoms_per_formula["H"]
                O_atoms = atoms_per_formula["O"]
                
                oxidations_number_H_acts = H_atoms * 1
                oxidations_number_O_acts = O_atoms * (-2)

                number_of_oxidation_numbers = len(element_object.ox_n)
                
                #Here we calculate the  number of oxidation of the element different to hydrogen and oxygen is acting. 
                supposed_oxidation_number = int(abs(oxidations_number_H_acts + oxidations_number_O_acts) / atoms_per_formula[element])
                

                #According to the quantity of oxygen atoms in the oxoacid
                #Odd numbers of oxidation that corresponds to the transition metal or no metal when the formula of oxoacid has only 1 atom of hydrogen
                odds = {1 : +1, 2: +3, 3 : +5, 4 : +7 }
                
                #Even numbers of oxidation that corresponds to the transition metal or no metal when the formula of oxoacid has 2 atom of hydrogen
                evens = {2 : +2, 3 : +4, 4 : +6}


                if H_atoms == 1 and 0 < O_atoms <= 4:
                    oxidation_number_element_acting = odds[O_atoms]

                elif H_atoms == 2 and 0 < O_atoms <= 4:
                    oxidation_number_element_acting = evens[O_atoms]

                else:
                    oxidation_number_element_acting = supposed_oxidation_number               
                #print(oxidation_number_element_acting)
                
                #Here we are check if the oxidation number acting is this one supposed. 
                if oxidation_number_element_acting == supposed_oxidation_number:
                    oxidation_numbers = element_object.ox_n
                    
                    #This is an exception of Phosphourous
                    if element=="P" and H_atoms == 2 and O_atoms == 4:
                        name = "fosfate"
                        return name.capitalize()
                    
                    #This is an exception of Sulfur
                    elif H_atoms == 1 and O_atoms == 4:
                        name = prefixes[O_atoms] + "oxide " + "sulfate"
                        return name.capitalize()
                    
                    #Here we verified if the supposed oxidation number belong to oxidation number of the concrete element
                    if supposed_oxidation_number in element_object.ox_n:
                        
                        #Depending on how many numbers of oxidation the element has it will be called one way or another.
                        #If the oxidation number that is acting is lower or higher, the traditional nomenclature changes.

                        ### Numbers of oxidation ->      4                           3                     2                    1
                        ### Lowest  number acting        hypo...ous acid        hypo...ous acid            -ous acid            -ic acid
                        ### 2nd lowest number            -ous acid              -ous acid                  -ic acid   
                        ### 3rd lowest number            -ic acid               -ic acid  
                        ### 4th lowest number            per...ic acid  


                        #Note that this nomenclature is with the catalan as base and it can cointain errors.
                        
                        #We write these prefixes and suffixes
                        order_oxidation_number = sorted(element_object.ox_n).index(supposed_oxidation_number)
                        prefix1 = "hypo"
                        prefix2 = "per"
                        suffix1 = "ous"
                        suffix2 = "ic"
                        
                        #There are some exception that we handle
                        if number_of_oxidation_numbers > 4:
                            
                            if element == "Cl" or element == "Br":
                                oxidation_numbers.remove(-1)

                            elif element == "N":
                                oxidation_numbers = [+3, +5]

                            elif element == "I":
                                oxidation_numbers = [0, 0, +5, +7]
                                if supposed_oxidation_number == 1:
                                    oxidation_numbers = [1, 3, +5, +7]

                            elif element == "Mn":
                                oxidation_numbers = [ 0, +4, +6, +7]

                            elif element == "P":
                                if H_atoms == 4 and O_atoms == 6 or H_atoms == 2 and O_atoms == 3:
                                    suffix = "ic"
                                    prefix = "hypo"

                                else:
                                    oxidation_numbers = [+1, +3 , +5, +7]


                            number_of_oxidation_numbers = len(oxidation_numbers)
                            
                            order_oxidation_number = sorted(oxidation_numbers).index(supposed_oxidation_number)
                        #Exception of Selenium
                        if element == "Se":
                                oxidation_numbers = [+4, +6]

                                number_of_oxidation_numbers = len(oxidation_numbers)
                                order_oxidation_number = sorted(oxidation_numbers).index(supposed_oxidation_number)    
                        #Exception of Sulfur
                        if element == "S":
                            oxidation_numbers = [+2, +4, +6]
                            number_of_oxidation_numbers = len(oxidation_numbers)
                            order_oxidation_number = sorted(oxidation_numbers).index(supposed_oxidation_number)

                            if oxidation_number_element_acting == 5:
                                prefix = "dithion"
                                element_name = ""
                                suffix = "ic"

                            elif oxidation_number_element_acting == 7:
                                prefix = "peroxydy"
                                suffix = "ic"
                        #There is not a real global consensus with the numbers of oxidation and all the nomenclature.
                        #This code could not be really accurate 

                        #Here we follow the instructions according the table. 
                        if number_of_oxidation_numbers == 4:

                            if order_oxidation_number == 0:
                                prefix = prefix1
                                suffix = suffix1

                            elif order_oxidation_number == 1:
                                prefix = ""
                                suffix = suffix1

                            elif order_oxidation_number == 2:
                                prefix = ""
                                suffix = suffix2
                                if element == "P":
                                    if H_atoms == 1 and O_atoms == 3 or H_atoms == 2 and O_atoms == 6:
                                        suffix = "ic"
                                        prefix = "meta"
                                    elif H_atoms == 4 and O_atoms == 7:
                                        suffix = "ic"
                                        prefix = "di"

                            elif order_oxidation_number == 3:
                                prefix = prefix2
                                suffix = suffix2
                                if element == "P":
                                    if H_atoms == 1 and O_atoms == 4 or H_atoms == 2 and O_atoms == 8:
                                        suffix = "ic"
                                        prefix = "meta"

                        elif number_of_oxidation_numbers == 3:
                            
                            if order_oxidation_number == 0:
                                prefix = prefix1
                                suffix = suffix1
                                
                            elif order_oxidation_number == 1:
                                prefix = ""
                                suffix = suffix1
                                if element == "As":
                                    suffix = "ious"

                                if element == "S" and O_atoms == 5 and H_atoms == 2:
                                    prefix = "di"
                                
                            elif order_oxidation_number == 2:
                               
                                prefix = ""
                                suffix = suffix2

                                if (element == "Cr" or element == "S") and O_atoms == 7 and H_atoms == 2:
                                    prefix = "di"
                                    
                        elif number_of_oxidation_numbers == 2:


                            if order_oxidation_number == 0:
                                prefix = ""
                                suffix = suffix1


                            elif order_oxidation_number == 1:
                                prefix = ""
                                suffix = suffix2

                                if element == "B": 
                                    if H_atoms == 3 and O_atoms == 3:
                                        prefix == "orto"

                                    elif H_atoms == 1  and O_atoms == 2:
                                        prefix == "meta"

                                if element == "Si": 
                                    if H_atoms == 4 and O_atoms == 4:
                                        prefix == "orto"

                                    elif H_atoms == 2 and O_atoms == 3:
                                        prefix == "meta"

                        elif number_of_oxidation_numbers == 1:
                            prefix = ""
                            suffix = suffix2 

                        else:
                            "Something is happening with number of oxidation numbers"

                        element_name = get_element_name(element)

                        name = rename(element_name, suffix, prefix) +" acid"  
                          

            #Oxosals are oxoacids losing hydrogens 
            #(although not necessarly they are losing all hydrogens)  #Some oxosals are with hydrogen but they not coincide neither hydroxids nor oxosals.
            elif ("H" not in atoms_per_formula and charge == 0) or ("H" != list_of_elements[0] and "H" != list_of_elements[-1] and "H" != formula[(formula.index(")") - 1)]) and charge == 0:
                
                #To name the oxosal:
                formula_oxoacid = formula

                #First element of the formula is named as it is, at the beggining.
                first_element_name = get_element_name(list_of_elements[0])
                                
                #First element is removed of the formula
                if len(list_of_elements[0]) == 1 :
                    if formula_oxoacid[1].isnumeric():
                        formula_oxoacid = formula_oxoacid[2:]
                    else:
                        formula_oxoacid = formula_oxoacid[1:]
                
                elif len(list_of_elements[0]) == 2 :
                    if formula_oxoacid[2].isnumeric():
                        formula_oxoacid = formula_oxoacid[3:]
                    else:
                        formula_oxoacid = formula_oxoacid[2:]

                #Then, the quantity of atoms of the first element indicates the hydrogen lost.
                # The quantity of atoms of the anion is removed of the formula. We recuperate these hydrogen to be able to name the oxoacid for what the oxosal is derivated. 
                number_of_cation = atoms_per_formula[list_of_elements[0]]
                
                #We count the number of current Hydrogen to add ones
                number_of_current_H = 0 
                
                #One exception of oxosals is the following:
                if formula == "Na(HCO3)2":
                    return "Sodium bicarbonate"
                    

                #The parenthesis and the formula is prepared. Hydrogen is added too.
                for i in range(len(formula_oxoacid)):
                    if i <= len(formula_oxoacid) :

                        ch = formula_oxoacid[i]

                        if ch == "(":
                           formula_oxoacid = formula_oxoacid[:formula_oxoacid.index(ch)] + formula_oxoacid[formula_oxoacid.index(ch)+1 :]

                        elif ch == ")":

                            formula_oxoacid = formula_oxoacid[:formula_oxoacid.index(ch)]

                        elif ch == "H":
                            number_of_current_H = 1

                            if formula_oxoacid[i+1].isnumeric():

                                number_of_current_H = int(formula_oxoacid[i+1])
                                formula_oxoacid = formula_oxoacid[:formula_oxoacid.index(ch)+1] + str(number_of_current_H + number_of_cation)+ formula_oxoacid[formula_oxoacid.index(ch)+2 :]

                if "H" not in formula_oxoacid:
                    if 1 == number_of_cation:
                        formula_oxoacid = "H" + formula_oxoacid
                    elif 2 <= number_of_cation:
                        formula_oxoacid = "H" + str(number_of_cation)+ formula_oxoacid
                
                #Oxoacid is named. The suffix of the oxoacid (usually -ic or -ous) are interchanged (with -ate or -ide, respectively).
                
                provisional_oxoacid = name_formula(formula_oxoacid)
                

                oxosal_name = provisional_oxoacid.replace("ic ", "ate ")
                
                oxosal_name = provisional_oxoacid.replace("ous", "ide")

                oxosal = oxosal_name.replace(" acid", "")
                
                oxosal = oxosal.lower()

                name = first_element_name + " " + oxosal.replace("ic ", "ate ")
                return name
            
            #If ions are heteropolyatomics they have charge. These are the unique tertiary or quaternary with charge, nevertheless we encounter some of them binaries(from hydracids).
            #There are cations and anions of this type.
            #The most common cations are oxoni (H3O(+)) and amoni (NH4(+))
            #Some anions are encountered when oxoacid loses H to become an oxosal. This are called oxoanions. The process to name them is similar to this one of oxosals. 
            #However some anions are derivated from hydracids. 
            elif charge != 0:
                if formula == "H3O(+)":
                    name = "oxonium"

                elif formula == "NH4(+)":
                    name = "ammonium" 
            
                #Oxoanions has lost hydrogens. We add this ones to know the nomenclature.
                #  
                #The charge say to us the quantity of hydrogen the oxoanions has lost.
                formula_oxoanion = formula
                for i in range(len(formula_oxoanion)):
                    if i <= len(formula_oxoanion) :
                        ch = formula_oxoanion[i]
                        if ch == "(":
                           formula_oxoanion = formula_oxoanion[:formula_oxoanion.index(ch)]

                #If there is not hydrogen in the formula, we add it to the original one.
                if "H" not in formula_oxoanion:
                        
                        
                        if charge == 1:
                            formula_oxoanion = "H" + formula_oxoanion

                        elif charge >= 2:
                            formula_oxoanion = "H" + str(abs(charge))+ formula_oxoanion
                    

                #If we encounter hydrogen in the formula, it is necessary to sum them.         
                else: 
                        i = formula_oxoanion.index("H")

                        if formula_oxoanion[i+1].isnumeric():
                            number_of_current_H = int(formula_oxoanion[i+1])
                            formula_oxoanion = formula_oxoanion[:i+1] + str(number_of_current_H + abs(charge))+ formula_oxoanion[i+2:]

                        else:
                            number_of_current_H = 1
                            formula_oxoanion = formula_oxoanion[:i+1] + str(number_of_current_H + abs(charge))+ formula_oxoanion[i+2:]
                            
                name_oxoanion = name_formula(formula_oxoanion).replace("acid", "ion")
                name = name_oxoanion.replace("ic ", "ate") + f"({abs(charge)}-)"

            elif get_element_object(element) in elements_list:
                name += prefixes[atoms_per_formula[element]] + element

            else:
                name = name + name_molecule
    
   
        
    if name_or_type == "type":
        return compound_type
    elif name_or_type == "name":
        return name.capitalize()
    else:
        return name.capitalize(), compound_type
        
def main():
    running = True
    while running:
        answer = int(input("What action I have to perform?\n"
                    "1. Name a formula\n"
                    "2. Know about an element\n"
                    "3. Classify a compound\n"
                    "4. Element configuration\n"
                    "5. Exit\n"))

        if answer == 1: #It has to be able to name only the element 
            formula = input("""Introduce the formula you want to know the name. Please write it with the first 
                        letter of the abbreviation of the element in capital letter. If you want to write
                        a molecule, charge or aquous solution write them between parenthesis, as the 
                        following examples K2(Cr2O7) , Hg2(2+), HF(aq): 
                            """)
            try:
                print(name_formula(formula))

            except:
                print("Please try again:")
                main()

        elif answer == 2:
            answer2 = int(input (""""" Choose one of the following:\n
                            1. Element name\n
                            2. Element abbreviation\n
                            3. Atomic number (number of protons)\n
                            4. Mass number\n
                            5. Periodic group \n
                            6. Type of element\n
                            7. Possible oxidation numbers\n
                            8. Energetic levels of the element
                             """))

            answer3 = input("""What element you want to know about? (Please, introduce it without white spaces)""")
            answer3 = answer3.capitalize()

            element_obj = get_element_object(answer3)

            if 0 < answer2 < 9:
                options = ["", get_element_name(answer3), get_element_abbrev(answer3), element_obj.Z, element_obj.A, element_obj.group, element_obj.type, element_obj.ox_n]
                print(options[answer2])

            else:
                print("Please try again:")
                main()

        elif answer == 3:
            formula = input("""Introduce the formula you want to classify. Please write it with the first 
                        letter of the abbreviation of the element in capital letter. If you want to write
                        molecule, charge or aquous solution write them between parenthesis, as the 
                        following examples K2(Cr2O7), Hg2(2+), HF(aq)""")
            try:
                print("This compound is " + classification_of_compounds(formula))

            except:
                print("Please try again:")
                main()

        elif answer == 4:
            answer4 = input("Introduce the element you want to know the electronic configuration.")

            answer4 = answer4.capitalize()

            element_obj = get_element_object(answer4)

            try:
                print(element_obj.electronic_configuration())

            except:
                print("Please try again:")
                main()

        elif answer == 5:
            running = False


simple_test_elements = ["O2"]
simple_test_cations = ["Na(+)", "Fe(3+)", "H(+)", "Hg2(2+)"]
simple_test_anions = ["F(-)", "S(2-)", "O(2-)", "N(3-)", "H(-)", "O2(2-)", "C2(2-)"]
binary_test = ["KCl", "Li2O", "MgO", "CO2", "NO", "PH3", "HBr", "RaH2", "B2O3", "Al2Se3", "NH3", "H2O"]
oxide_test = ["CO2", "NO", "Fe2O3", "CaO"]
peroxide_test = ["Li2O2", "CaO2", "H2O2"]
hydride_hydracid_test = ["CuH2", "AgH", "NiH3", "HCl", "HF", "H2S", "HCl(aq)", "HF(aq)", "H2S(aq)"] #
binary_salt_test = ["CaBr2", "NaCl", "Fe2S3"]
two_no_metals_combined = ["SBr2", "CCl4", "P2S3"]
hydroxid_test = ["Mg(OH)2", "Pb(OH)4", "KOH"] 
oxoacid_test = ["HClO", "HClO2", "HClO3", "HClO4", "H2SO2", "H2SO3", "H2SO4","H2CO2", "H2CO3"]
tertiary_test = ["H2SO4", "HClO "]
oxosal_test = ["Mg(BrO)2",  "Au(H2PO4)3", "Ca(ClO4)2", "Cu(IO)2", "K2(Cr2O7)"]
formules_P = ["H3PO5", "H3PO2", "H3PO3", "H3PO4"]
oxoanions = ["CrO4(2-)", "MnO4(2-)", "HSO3(-)","Cr2O7(2-)" ]







