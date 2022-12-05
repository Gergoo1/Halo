# python lista

#  A listák több elem tárolására szolgálnak egyetlen változóban.
# A listákat szögletes zárójelekkel hozzuk létre:
# Példa:
lista = ["alma", "banán", "cseresznye"]
print(lista)

lista = ["alma", "banán", "cseresznye", "alma", "banán"]
print(lista)
print(len(lista)lista = ["alma", "banán", "cseresznye"]
print(len(lista))
hossza = len(lista)
print(hossza)

# A lista elemek bármilyen típusúak lehetnek

lista1 = ["alma", "banán", "cseresznye"] # string
lista2 = 1, 5, 7, 9, 3] # int
lista3 = [True, False, False] # bool

lista = list(("alma", "banán", "cseresznye")) # vegye figyelembe a dupla kerek zárójeleket
print(lista) #['alma', 'banán', 'cseresznye']


# irassuk ki a lisrta utolsó elemét:
lista = ["alma", "banán", "cseresznye"]
print(lista[-1])
#cseresznye
print (lista[2])

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[2:5])
 ujlisa=lista[2:1]

 # ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 lista_10D_1csop = []
 lista: [FB, GM, HK, KG, MM, OA, PJ, PP, SP, SR,SM,TB TS, TT]

csop1=[]
csop2=[]
csop3=[]
csop1=lista_10D_1csop[0:5]
print(csop1)
csop2=lista_10D_1csop[5:10]
print(csop2)
csop3=lista_10D_1csop[10:]
print(csop3)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

lista = ["alma-0", "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print(lista[-4:-1]) #index = 3, 4, 5 !

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

lista_10D_1csop = []
 lista: ["FB", "GM" "HK", "KG", "MM", "OA", "PJ", "PP", "SP", "SR","SM","TB", "TS", "TT"]
 megbukott=lista_10D_1csop[10:14]
 nemmegbukott=lista_10D_1csop[0:9]