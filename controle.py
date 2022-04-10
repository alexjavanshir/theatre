class pile:
    __liste =[]

    def __init__(self):
        self.__liste = []
    
    def ajouter(self, valeur):
        self.__liste.append(valeur)

    def enlever(self):
        return self.__liste.pop(-1)
    
    def est_vide(self):
        return len(self.__liste) == 0

    def hauteur(self):
        return len(self.__liste)
    
    def __repr__(self):
        s=""
        lmax = 1
        for x in self.__liste :
            if len(str(x)) > lmax :
                lmax = len(str(x))
        for i in range(len(self.__liste)-1, -1, -1) :
            x = str(self.__liste[i])
            l = (lmax-len(x))//2
            if (lmax-len(x)) % 2 == 0:
                s += "\u2503" + " "*l + x + " "*l + "\u2503\n"
            else : 
                s += "\u2503" + " "*l + x + " "*(l + 1) + "\u2503\n"
        s += "\u2517" + lmax*"\u2501" + "\u251B"
        return s

class file:
    __liste =[]

    def __init__(self):
        self.__liste = []
    
    def ajouter(self, valeur):
        self.__liste.append(valeur)

    def enlever(self):
        return self.__liste.pop(0)

    def __repr__(self):
        s = "\u2503"
        ssup = "\u250f"
        sinf = "\u2517"
        for x in self.__liste:
            ssup += len(str(x))*"\u2501" + "\u2533"
            sinf += len(str(x))*"\u2501" + "\u253B"
            s += str(x) + "\u2503"
        if self.__liste != []:
            ssup = ssup[:-1]
            sinf = sinf[:-1]
            s = s[:-1]
        ssup += "\u2513"
        sinf += "\u251B"
        s += "\u2503"
        return ssup + "\n" + s + "\n" + sinf

###---------------------------------------------------------------------------------------------###
###----------------------------devoir rattrapage - exo 1----------------------------------------###
###---------------------------------------------------------------------------------------------###

def fibo(n):
    p = pile()
    f = 0
    p.ajouter(n)
    while p.hauteur() !=0:
        x = p.enlever()
        if x == 0 or x ==1:
           f+=x  
        else:
            p.ajouter(x-1)
            p.ajouter(x-2)
    return f 

print(fibo(2))

###---------------------------------------------------------------------------------------------###
###----------------------------devoir rattrapage - exo 2----------------------------------------###
###---------------------------------------------------------------------------------------------###

groupe_1 = ['g1_a', 'g1_b','g1_c','g1_d','g1_e','g1_f','g1_g','g1_h','g1_i','g1_j','g1_k','g1_l','g1_m','g1_n','g1_o','g1_p','g1_q','g1_r','g1_s','g1_t']
groupe_2 = ['g2_a', 'g2_b','g2_c','g2_d','g2_e','g2_f','g2_g','g2_h','g2_i','g2_j']
groupe_3 = ['g3_a', 'g3_b','g3_c','g3_d','g3_e','g3_f','g3_g','g3_h','g3_i','g3_j','g3_k','g3_l','g3_m','g3_n','g3_o','g3_p','g3_q','g3_r','g3_s','g3_t','g3_u','g3_v','g3_w']
groupe_4 = ['g4_a', 'g4_b','g4_c','g4_d','g4_e','g4_f','g4_g','g4_h','g4_i','g4_j','g4_k']
groupe_5 = ['g5_a', 'g5_b','g5_c','g5_d','g5_e','g5_f','g5_g','g5_h','g5_i','g5_j','g5_k','g5_l','g5_m','g5_n','g5_o']
groupe_6 = ['g6_a', 'g6_b','g6_c','g6_d','g6_e','g6_f','g6_g','g6_h','g6_i','g6_j','g6_k','g6_l','g6_m','g6_n','g6_o','g6_p','g6_q','g6_r','g6_s','g6_t','g6_u','g6_v']
groupe_7 = ['g7_a', 'g7_b','g7_c','g7_d','g7_e','g7_f','g7_g','g7_h','g7_i','g7_j','g7_k','g7_l','g7_m','g7_n','g7_o','g7_p','g7_q','g7_r','g7_s','g7_t']
groupe_8 = ['g8_a', 'g8_b','g8_c','g8_d','g8_e','g8_f','g8_g','g8_h','g8_i','g8_j','g8_k','g8_l','g8_m','g8_n','g8_o','g8_p','g8_q','g8_r','g8_s','g8_t','g8_u','g8_v','g8_w','g8_x','g8_y','g8_z','g8_z1']
groupe_9 = ['g9_a', 'g9_b','g9_c','g9_d','g9_e','g9_f','g9_g','g9_h','g9_i','g9_j','g9_k','g9_l','g9_m','g9_n','g9_o','g9_p','g9_q','g9_r','g9_s','g9_t','g9_u','g9_v','g9_w','g9_x','g9_y','g9_z','g9_z1','g9_z2','g9_z3','g9_z4','g9_z5','g9_z6','g9_z7','g9_z8','g9_z9','g9_z10','g9_z11','g9_z12','g9_z13','g9_z14','g9_z15','g9_z16','g9_z17','g9_z18','g9_z19','g9_z20','g9_z21','g9_z22','g9_z23','g9_z24','g9_z25','g9_z26']
all_groups = [groupe_1, groupe_2, groupe_3, groupe_4, groupe_5, groupe_6, groupe_7, groupe_8, groupe_9]

all_persons = []
for group in all_groups:
    for person in group:
        all_persons.append(person)

#print(all_persons)

'''
def theatre_bis():
    ran_ver  =['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    f = file()
    sens = True
    for i in ran_ver:
        if sens:
            for ran_hori in range(1,21,1):
                if len(all_persons) > 0:
                    user = all_persons.pop(0)
                else:
                    user = "Erreur"
                f.ajouter(str(i)+ str(ran_hori) + "-" + user)
        else:
            for ran_hori in range(20, 0,-1):
                if len(all_persons) > 0:
                    user = all_persons.pop(0)
                else:
                    user = "Erreur"
                f.ajouter(str(i)+ str(ran_hori) + "-" + user)
        sens = not sens
    print(f)
'''

def theatre():
    ran_ver  =['A','B','C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    f = file()
    sens = True
    for i in ran_ver:
        if sens:
            start=1
            end=21
            step=1
        else:
            start=20
            end=0
            step=-1

        for ran_hori in range(start,end,step):
            if len(all_persons) > 0:
                user = all_persons.pop(0)
            else:
                user = "Erreur"
            f.ajouter(str(i)+ str(ran_hori) + "(" + user + ")")
        
        sens = not sens
    print(f)

theatre()
