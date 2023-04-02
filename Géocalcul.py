# AKAYAB Nadir

import tkinter as tk
from math import *
from tkinter import ttk


# un dictionnaire dans lequel on va ajouter les valeurs de a,b,f,e2
# ellipsoide = {'a': 6378249.2, 'b': 6356515, 'e2': 0.0068034876}
ellipsoide = {}

phicara = '\u03C6'
lamcara = '\u03BB'


"""fonctions pour le menu et les frames"""


root = tk.Tk()  # créer la fenetre principale

root.title('GéoCalcul')  # définir un titre

couleur1 = '#23906B'
couleur2 = '#3B7197'


# pour le style
style = ttk.Style()
style.configure('my.TButton', font=('Bold', 15),
                fg=couleur2)

# le frame globale
frame = tk.Frame(root, bg="#ececec", height=440, width=700)
frame.pack(expand=True, fill=tk.BOTH, side=tk.BOTTOM)
root.geometry('830x500')

# fonction pour la création des labels


def createLabel(color, font, size, text, row, column):
    label = tk.Label(
        frame,   fg=color, font=(font, size), text=text)
    label.grid(row=row, column=column)
    return label

# fonction pour la création des Text


def createText(height, width, font, size, fg, bg, row, column, columnspan):
    field = tk.Text(frame, height=height, width=width,
                    font=(font, size), fg=fg, bg=bg)
    field.grid(row=row, column=column, columnspan=columnspan)
    field.focus()
    return field


alabelaux = createLabel('#ececec', "Arial", 60, " ", 0, 0)

alabel0 = createLabel(couleur1, 'Open Sans Light', 130, "Géo", 3, 0)

label1 = createLabel(couleur2, 'Open Sans Light', 130, 'Calcul', 3, 1)

# créer un frame pour le menu
interface_menu = tk.Frame(root, bg=couleur2)
interface_menu.place(x=0, y=40, height=500, width=200)
interface_menu.place_forget()


def delete_pages():  # suprimer tous les widgets enfants dans un frame
    global frame
    for i in frame.winfo_children():
        i.destroy()

# fonction pour aller aux différentes pages de menu


def menu_selection():
    global interface_menu
    interface_menu.place(x=0, y=10, height=600, width=330)
    calellipse_btn = tk.Button(interface_menu, text="Paramètres de l'ellipse",
                               font=('Bold', 20), fg='#f2f2f2', bg=couleur2, bd=0, command=lambda: calul_ellipse_page())
    calellipse_btn.place(x=10, y=50)
    rayon_btn = tk.Button(interface_menu, text='Rayon de courbure',
                          font=('Bold', 20), fg='#f2f2f2', bg=couleur2, bd=0, command=lambda: calcul_rayon_page())
    rayon_btn.place(x=10, y=100)
    conversionphiU_btn = tk.Button(interface_menu, text=f'Conversion de {phicara} à U',
                                   font=('Bold', 20), fg='#f2f2f2', bg=couleur2, bd=0, command=lambda:  conversion_phi_U_page())
    conversionphiU_btn.place(x=10, y=150)
    conversionUphi_btn = tk.Button(interface_menu, text=f'Conversion de U à {phicara}',
                                   font=('Bold', 20), fg='#f2f2f2', bg=couleur2, bd=0, command=lambda:  conversion_U_phi_page())
    conversionUphi_btn.place(x=10, y=200)
    conversiongeorect = tk.Button(interface_menu, text='Coor. géo aux rect',
                                  font=('Bold', 20), fg='#f2f2f2', bg=couleur2, bd=0, command=lambda:  conversion_geo_rect_page())
    conversiongeorect.place(x=10, y=250)
    conversionrectgeo = tk.Button(interface_menu, text='Coor. rect aux géo',
                                  font=('Bold', 20), fg='#f2f2f2', bg=couleur2, bd=0, command=lambda:  conversion_rect_geo_page())
    conversionrectgeo.place(x=10, y=300)


head_frame = tk.Frame(root, bg='#2C2C2C', highlightbackground='white')

menu_btn = tk.Button(head_frame, text='☰', bg='#2C2C2C',
                     fg='white', command=menu_selection)
title_btn_menu = tk.Label(head_frame, text='Menu', bg='#2C2C2C', fg='white')
menu_btn.pack(side=tk.LEFT)
title_btn_menu.pack(side=tk.LEFT)
head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)


"""fin des fonctions de menu, frames, label et text"""


"""les sous fonctions de la page calcul ellipsoide"""


def calcul_a(fieldb, fieldf, fielde2):
    b = fieldb.get('1.0', 'end')
    f = fieldf.get('1.0', 'end')
    e2 = fielde2.get('1.0', 'end')
    try:
        b = float(b)
        f = float(f)
        ellipsoide['b'] = b
        ellipsoide['f'] = f
        a = b/(1-f)
    except:
        try:
            b = float(b)
            e2 = float(e2)
            ellipsoide['b'] = b
            ellipsoide['e2'] = e2
            a = b/sqrt(1-e2)
        except:
            a = 'ERROR'
    return a


def calcul_b(fielda, fieldf, fielde2):
    a = fielda.get('1.0', 'end')
    f = fieldf.get('1.0', 'end')
    e2 = fielde2.get('1.0', 'end')
    try:
        a = float(a)
        f = float(f)
        ellipsoide['a'] = a
        ellipsoide['f'] = f
        b = a*(1-f)
    except:
        try:
            a = float(a)
            e2 = float(e2)
            ellipsoide['a'] = a
            ellipsoide['e2'] = e2
            b = a*sqrt(1-e2)
        except:
            b = 'ERROR'
    return b


def calcul_f(fielda, fieldb, fielde2):
    a = fielda.get('1.0', 'end')
    b = fieldb.get('1.0', 'end')
    e2 = fielde2.get('1.0', 'end')
    try:
        e2 = float(e2)
        ellipsoide['e2'] = e2
        f = 1-sqrt(1-e2)
    except:
        try:
            a = float(a)
            b = float(b)
            ellipsoide['b'] = b
            ellipsoide['a'] = a
            f = 1-b/a
        except:
            f = 'ERROR'
    return f


def calcul_e2(fielda, fieldb, fieldf):
    a = fielda.get('1.0', 'end')
    b = fieldb.get('1.0', 'end')
    f = fieldf.get('1.0', 'end')
    try:
        f = float(f)
        ellipsoide['f'] = f
        e2 = 1-(1-f)**2
    except:
        try:
            a = float(a)
            b = float(b)
            ellipsoide['b'] = b
            ellipsoide['a'] = a
            e2 = 1-(b/a)**2
        except:
            e2 = 'ERROR'
    return e2


# pour ajouter les labels et les frames de a,b,f et e2
def labeletfield(frame, nomdevariable, row, column):
    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text=f"{nomdevariable} = ")
    alabel.grid(row=row, column=column)

    field = tk.Text(frame, height=1, width=35, font=(
        "Times New Roman", 15), fg="black", bg="#ececec")
    field.grid(row=row, column=column+1)
    field.focus()

    return field


# fonction qui fait appel au autres fonctions de calculs


def calcul_des_valeurs(fielda, fieldb, fieldf, fielde2):
    if fielda.compare('end-1c', '==', '1.0'):
        a = calcul_a(fieldb, fieldf, fielde2)
        ellipsoide['a'] = a
        fielda.insert(tk.INSERT, a)
    if fieldb.compare('end-1c', '==', '1.0'):
        b = calcul_b(fielda, fieldf, fielde2)
        ellipsoide['b'] = b
        fieldb.insert(tk.INSERT, b)
    if fieldf.compare('end-1c', '==', '1.0'):
        f = calcul_f(fielda, fieldb, fielde2)
        ellipsoide['f'] = f
        fieldf.insert(tk.INSERT, f)
    if fielde2.compare('end-1c', '==', '1.0'):
        e2 = calcul_e2(fielda, fieldb, fieldf)
        ellipsoide['e2'] = e2
        fielde2.insert(tk.INSERT, e2)


"""fin des sous fonctions de la page calcul ellipsoide"""


"""les sous fonctions de la page rayon"""


def calcul_N(phi):
    try:
        a = ellipsoide.get('a')
        e2 = ellipsoide.get('e2')
        N = a/sqrt(1-(e2)*(sin(phi)**2))
    except:
        N = 'ERROR'
    return N


def calcul_M(phi):
    try:
        a = ellipsoide.get('a')
        e2 = ellipsoide.get('e2')
        M = a*(1-e2)/sqrt(1-e2*(sin(phi)**2))**3
    except:
        M = 'ERROR'
    return M


def affiche_NM(fielddegre, fieldminute, fieldseconde):
    try:
        phi = float(fielddegre.get('1.0', 'end'))+float(fieldminute.get('1.0',
                                                                        'end'))/60+float(fieldseconde.get('1.0', 'end'))/3600

        phi *= pi/180
        N = calcul_N(phi)
        M = calcul_M(phi)
    except:
        N = M = 'ERROR'

    alabelN = createLabel(couleur2, 'Arial', 20, "N= ", 3, 0)
    fieldN = createText(1, 15, "Times New Roman", 15,
                        "black", "#f5f5f5", 3, 1, 1)
    fieldN.insert(tk.INSERT, N)

    alabelm = createLabel(couleur2, 'Arial', 20, "m ", 3, 3)
    alabelm1 = createLabel(couleur2, 'Arial', 20, "m ", 4, 3)

    alabelM = createLabel(couleur2, 'Arial', 20, "M= ", 4, 0)
    fieldM = createText(1, 15, "Times New Roman", 15,
                        "black", "#f5f5f5", 4, 1, 1)
    fieldM.insert(tk.INSERT, M)


"""fin des sous fonctions de la page calcul rayon"""

"""les sous fonctions de la page conversion phi u"""


def phi_U(fielddegre, fieldminute, fieldseconde, fieldU, selected_option):
    fieldU.delete("1.0", "end")
    try:
        phi = float(fielddegre.get('1.0', 'end'))+float(fieldminute.get('1.0',
                                                                        'end'))/60+float(fieldseconde.get('1.0', 'end'))/3600
    except:
        U = 'ERROR'

    phi *= pi/180

    if selected_option.get() == 'Nrod':
        phi = phi
    elif selected_option.get() == 'Sud':
        phi = -phi
    else:
        U = 'choisissez Nord ou Sud'

    try:
        e2 = ellipsoide.get('e2')
        e = sqrt(e2)
        U = log(tan(pi/4+phi/2))-(e2)/2*log((1+e*sin(phi))/(1-e*sin(phi)))
    except:
        U = 'ERROR'

    fieldU.insert(tk.INSERT, U)


"""fin des sous fonctions de la page conversion phi u"""

# la fonction de la page calcul des paramètres de l'ellipse


def calul_ellipse_page():
    delete_pages()
    global interface_menu
    interface_menu.place_forget()
    global frame

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text="Entrez les valeurs que vous voulez:")
    alabel.grid(row=0, column=0, columnspan=2)

    fielda = labeletfield(frame, 'a', 1, 0)
    fieldb = labeletfield(frame, 'b', 2, 0)
    fieldf = labeletfield(frame, 'f', 3, 0)
    fielde2 = labeletfield(frame, 'e²', 4, 0)

    labelm = createLabel(couleur2, 'Arial', 15, "m", 1, 2)
    labelm = createLabel(couleur2, 'Arial', 15, "m", 2, 2)

    calc = ttk.Button(frame, text="Calculer",
                      command=lambda: calcul_des_valeurs(fielda, fieldb, fieldf, fielde2), style='my.TButton')

    calc.grid(row=5, column=1)

    root.geometry('1000x500')

# fonction d'aide


def labelettextdegminsec(row, column0):
    labeldegre = createLabel(couleur2, 'Arial', 20, "°", row, column0+1)
    fielddegre = createText(1, 15, "Times New Roman",
                            15, "black", "#f5f5f5", row, column0, 1)
    fielddegre.insert(tk.INSERT, 0)

    labelminute = createLabel(couleur2, 'Arial', 20, "'", row, column0+3)
    fieldminute = createText(1, 15, "Times New Roman",
                             15, "black", "#f5f5f5", row, column0+2, 1)
    fieldminute.insert(tk.INSERT, 0)

    labelseconde = createLabel(couleur2, 'Arial', 20, "''", row, column0+5)
    fieldseconde = createText(1, 15, "Times New Roman",
                              15, "black", "#f5f5f5", row, column0+4, 1)
    fieldseconde.insert(tk.INSERT, 0)

    return labeldegre, fielddegre, labelminute, fieldminute, labelseconde, fieldseconde
# fonction d'aide


def NordSudbutton(row, column):
    selected_option = tk.StringVar()

    option1 = tk.Radiobutton(frame, text="Nord",
                             variable=selected_option, value="Nord")
    option2 = tk.Radiobutton(frame, text="Sud ",
                             variable=selected_option, value="Sud")
    option1.grid(row=row, column=column)
    option2.grid(row=row, column=column+1)
    selected_option.set("Nord")
    return selected_option


# fonction d'aide
def ellipsevide(row, column, columnspan):
    if len(ellipsoide) == 0:
        Labelellipsevide = tk.Label(
            frame,   fg='red', font=('Arial', 20), text="Vous n'avez pas entré les paramètres de l'ellipse!")
        Labelellipsevide.grid(row=row, column=column, columnspan=columnspan)
        return Labelellipsevide


def fonctionzone(row, column):
    selected_option = tk.StringVar()

    option1 = tk.Radiobutton(frame, text="zone 1",
                             variable=selected_option, value="1")
    option2 = tk.Radiobutton(frame, text="zone 2",
                             variable=selected_option, value="2")
    option3 = tk.Radiobutton(frame, text="zone 3",
                             variable=selected_option, value="3")
    option4 = tk.Radiobutton(frame, text="zone 4",
                             variable=selected_option, value="4")
    option1.grid(row=row, column=column)
    option2.grid(row=row+1, column=column)
    option3.grid(row=row+2, column=column)
    option4.grid(row=row+3, column=column)
    selected_option.set("1")
    return selected_option


def calcul_rayon_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text="Entrez les valeurs que vous voulez:")
    alabel.grid(row=0, column=0, columnspan=5)

    philabel = createLabel(couleur2, 'Arial', 20, f'{phicara}=', 1, 0)

    labeldegre, fielddegre, labelminute, fieldminute, labelseconde, fieldseconde = labelettextdegminsec(
        1, 1)

    calc = ttk.Button(frame, text="Calculer",
                      command=lambda: affiche_NM(fielddegre, fieldminute, fieldseconde), style='my.TButton')

    Labelellipsevide = ellipsevide(5, 0, 6)

    calc.grid(row=2, column=3)

    root.geometry("650x500")


def conversion_phi_U_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text="Entrez les valeurs que vous voulez:")
    alabel.grid(row=0, column=0, columnspan=5)

    # fieldphi = labeletfield(frame, 'phi', 1, 0)

    labelphi = createLabel(couleur2, 'Arial', 20, f'{phicara}=', 1, 0)

    labeldegre, fielddegre, labelminute, fieldminute, labelseconde, fieldseconde = labelettextdegminsec(
        1, 1)

    labelU = createLabel(couleur2, 'Arial', 20, 'U=', 2, 0)
    fieldU = createText(1, 15, "Times New Roman",
                        15, "black", "#f5f5f5", 2, 1, 1)

    selected_option = NordSudbutton(1, 7)

    calc = ttk.Button(frame, text="Calculer",
                      command=lambda: phi_U(fielddegre, fieldminute, fieldseconde, fieldU, selected_option), style='my.TButton')

    calc.grid(row=3, column=3)
    Labelellipsevide = ellipsevide(4, 0, 6)

    root.geometry('1000x500')


def U_phi(fielddegre, fieldminute, fieldseconde, fieldU):
    fielddegre.delete("1.0", "end")
    fieldminute.delete("1.0", "end")
    fieldseconde.delete("1.0", "end")
    try:
        U = float(fieldU.get('1.0', 'end'))
        if U < 0:
            labelNS = createLabel(couleur2, 'Arial', 18, 'Sud', 2, 7)
        else:
            labelNS = createLabel(couleur2, 'Arial', 18, 'Nord', 2, 7)

        Lphi = []
        phi0 = 0
        Lphi.append(phi0)

        e2 = ellipsoide.get('e2')

        E = (e2/2)*(log((1+sqrt(e2)*sin(phi0))/(1-sqrt(e2)*sin(phi0))))
        LE = []
        LE.append(E)

        phi = 2*atan((exp(U+LE[-1])-1)/(exp(U+LE[-1])+1))
        Lphi.append(phi)

        while (abs(Lphi[-1]-Lphi[-2]) > 0.000000000000000000000001):
            LE.append(
                log((1+sqrt(e2)*sin(Lphi[-1]))/(1-sqrt(e2)*sin(Lphi[-1])))*e2/2)
            Lphi.append(2*atan((exp(U+LE[-1])-1)/(exp(U+LE[-1])+1)))
        phi = Lphi[-1]

        phi = Lphi[-1]*180/pi
        phidegre = int(phi)
        phi2 = (phi-phidegre)*60
        phiminute = int(phi2)
        phiseconde = (phi2-phiminute)*60

        fielddegre.insert(tk.INSERT, abs(phidegre))
        fieldminute.insert(tk.INSERT, abs(phiminute))
        fieldseconde.insert(tk.INSERT, round(abs(phiseconde), 5))
    except:
        fielddegre.insert(tk.INSERT, "ERROR")
        fieldminute.insert(tk.INSERT, "ERROR")
        fieldseconde.insert(tk.INSERT, "ERROR")


def conversion_U_phi_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text="Entrez les valeurs que vous voulez:")
    alabel.grid(row=0, column=0, columnspan=5)

    labelU = createLabel(couleur2, 'Arial', 20, 'U=', 1, 0)
    fieldU = createText(1, 15, "Times New Roman",
                        15, "black", "#f5f5f5", 1, 1, 1)
    fieldU.insert(tk.INSERT, 0)

    labelphi = createLabel(couleur2, 'Arial', 20, f'{phicara}=', 2, 0)

    labeldegre, fielddegre, labelminute, fieldminute, labelseconde, fieldseconde = labelettextdegminsec(
        2, 1)

    Labelellipsevide = ellipsevide(4, 0, 6)
    # selected_option = NordSudbutton(1, 7)

    calc = ttk.Button(frame, text="Calculer",
                      command=lambda: U_phi(fielddegre, fieldminute, fieldseconde, fieldU), style='my.TButton')

    calc.grid(row=3, column=3)

    root.geometry('1000x500')

# fonction qui contient les paramètres de chaque zone


def returnzoneparametres(zone):
    if zone == '1':
        phi0 = 37*pi/200
        X0 = 500000
        Y0 = 300000
        K0 = 0.999625769
    elif zone == '2':
        phi0 = 33*pi/200
        X0 = 500000
        Y0 = 300000
        K0 = 0.999615596
    elif zone == '3':
        phi0 = 29*pi/200
        X0 = 1200000
        Y0 = 400000
        K0 = 0.999616304
    elif zone == '4':
        phi0 = 25*pi/200
        X0 = 1500000
        Y0 = 400000
        K0 = 0.999616437
    return phi0, X0, Y0, K0

# fonction pour la conversion des coord géo vers rect


def geo_rect(fielddegrelam, fieldminutelam, fieldsecondelam, fielddegrephi, fieldminutephi, fieldsecondephi, fieldX, fieldY, zone):
    fieldX.delete("1.0", "end")
    fieldY.delete("1.0", "end")

    zone = zone.get()

    try:
        lam = -(float(fielddegrelam.get('1.0', 'end'))+float(fieldminutelam.get('1.0',
                'end'))/60+float(fieldsecondelam.get('1.0', 'end'))/3600)
        phi = float(fielddegrephi.get('1.0', 'end'))+float(fieldminutephi.get('1.0',
                                                                              'end'))/60+float(fieldsecondephi.get('1.0', 'end'))/3600

        a = ellipsoide.get('a')
        e2 = ellipsoide.get('e2')

        phi *= pi/180
        lam *= pi/180
        e = sqrt(e2)
        lam0 = -6*pi/200
        phi0, X0, Y0, K0 = returnzoneparametres(zone)
        U0 = log(tan(pi/4+phi0/2))-((e**2)/2) * \
            log((1+e*sin(phi0))/(1-e*sin(phi0)))
        U = log(tan(pi/4+phi/2))-((e**2)/2)*log((1+e*sin(phi))/(1-e*sin(phi)))

        # Ubar = abs(U-U0)
        # lambar = abs(lam-lam0)

        Ubar = U-U0
        lambar = lam-lam0

        N0 = a/sqrt(1-(e**2)*(sin(phi0)**2))

        gho0 = K0*N0/tan(phi0)

        Xproj = gho0*exp(-Ubar*sin(phi0))*sin(sin(phi0)*lambar)
        Yproj = -gho0*(exp(-Ubar*sin(phi0))*cos(sin(phi0)*lambar)-1)

        X = Xproj+X0
        Y = Yproj+Y0
    except:
        X = 'ERROR'
        Y = 'ERROR'

    fieldX.insert(tk.INSERT, X)
    fieldY.insert(tk.INSERT, Y)


def conversion_geo_rect_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text="Entrez les valeurs que vous voulez:")
    alabel.grid(row=0, column=0, columnspan=5)

    labellam = createLabel(couleur2, 'Arial', 20, f'{lamcara}=', 1, 0)
    labelphi = createLabel(couleur2, 'Arial', 20, f'{phicara}=', 2, 0)

    labelNord = createLabel(couleur2, 'Arial', 20, 'N', 2, 7)
    labelWest = createLabel(couleur2, 'Arial', 20, 'W', 1, 7)

    labeldegrelam, fielddegrelam, labelminutelam, fieldminutelam, labelsecondelam, fieldsecondelam = labelettextdegminsec(
        1, 1)

    labeldegrephi, fielddegrephi, labelminutephi, fieldminutephi, labelsecondephi, fieldsecondephi = labelettextdegminsec(
        2, 1)

    Labelellipsevide = ellipsevide(11, 0, 6)

    # selected_optionlam = NordSudbutton(1, 7)
    # selected_optionphi = NordSudbutton(2, 7)

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, padx=0, font=('Bold', 20), text="Entrez le numéro de la zone:        ")
    alabel.grid(row=3, column=0, columnspan=4)

    zone = fonctionzone(4, 1)

    calc = ttk.Button(frame, text="Calculer",
                      command=lambda: geo_rect(fielddegrelam, fieldminutelam, fieldsecondelam, fielddegrephi, fieldminutephi, fieldsecondephi, fieldX, fieldY, zone), style='my.TButton')

    calc.grid(row=8, column=3)

    labelX = createLabel(couleur2, 'Arial', 20, 'x=', 9, 0)
    fieldX = createText(1, 15, "Times New Roman",
                        15, "black", "#f5f5f5", 9, 1, 1)
    labelY = createLabel(couleur2, 'Arial', 20, 'y=', 10, 0)
    fieldY = createText(1, 15, "Times New Roman",
                        15, "black", "#f5f5f5", 10, 1, 1)

    labelm = createLabel(couleur2, 'Arial', 15, "m", 9, 2)
    labelm = createLabel(couleur2, 'Arial', 15, "m", 10, 2)

    root.geometry('1000x500')

# fonction pour la conversion des coord rect vers géo


def rect_geo(fieldX, fieldY, zone, fielddegrephi, fieldminutephi, fieldsecondephi, fielddegrelam, fieldminutelam, fieldsecondelam):
    fielddegrephi.delete("1.0", "end")
    fieldminutephi.delete("1.0", "end")
    fieldsecondephi.delete("1.0", "end")

    fielddegrelam.delete("1.0", "end")
    fieldminutelam.delete("1.0", "end")
    fieldsecondelam.delete("1.0", "end")
    zone = zone.get()
    try:
        a = ellipsoide.get('a')
        e2 = ellipsoide.get('e2')
        e = sqrt(e2)
        lam0 = -6*pi/200
        phi0, X0, Y0, K0 = returnzoneparametres(zone)

        X = float(fieldX.get('1.0', 'end'))
        Y = float(fieldY.get('1.0', 'end'))

        X -= X0
        Y -= Y0
        N0 = a/sqrt(1-e2*(sin(phi0))**2)
        gho0 = K0*N0/tan(phi0)

        lambar = atan(X/(gho0-Y))/sin(phi0)

        lam = lambar+lam0

        U0 = log(tan((pi/4)+(phi0/2))) - \
            ((e2/2)*log((1+(sqrt(e2))*sin(phi0))/(1-(sqrt(e2))*sin(phi0))))
        U_bar = (1/(2*sin(phi0)))*log((gho0 ** 2)/(X ** 2+(gho0-Y) ** 2))
        U = abs(U_bar+U0)

        Lphi = []
        Lphi.append(phi0)

        E = (e2/2)*(log((1+sqrt(e2)*sin(phi0))/(1-sqrt(e2)*sin(phi0))))
        LE = []
        LE.append(E)

        phi = 2*atan((exp(U+LE[-1])-1)/(exp(U+LE[-1])+1))
        Lphi.append(phi)

        while (abs(Lphi[-1]-Lphi[-2]) > 0.000001):
            LE.append(
                (log((1+e*sin(Lphi[-1]))/(1-e*sin(Lphi[-1]))))*e2/2)
            Lphi.append(2*atan((exp(U+LE[-1])-1)/(exp(U+LE[-1])+1)))

        phi = Lphi[-1]*180/pi
        phidegre = int(phi)
        phi2 = (phi-phidegre)*60
        phiminute = int(phi2)
        phiseconde = (phi2-phiminute)*60

        lam = lam*180/pi
        lam = abs(lam)
        lamdegre = int(lam)
        lam2 = (lam-lamdegre)*60
        lamminute = int(lam2)
        lamseconde = (lam2-lamminute)*60

        fieldsecondephi.insert(tk.INSERT, round(phiseconde, 9))
        fieldsecondelam.insert(tk.INSERT, round(lamseconde, 9))

    except:
        phidegre = phiminute = phiseconde = lamdegre = lamminute = lamseconde = 'ERROR'
        fieldsecondephi.insert(tk.INSERT, phiseconde)
        fieldsecondelam.insert(tk.INSERT, lamseconde)

    fielddegrephi.insert(tk.INSERT, phidegre)
    fieldminutephi.insert(tk.INSERT, phiminute)

    fielddegrelam.insert(tk.INSERT, lamdegre)
    fieldminutelam.insert(tk.INSERT, lamminute)


def conversion_rect_geo_page():
    delete_pages()
    global frame
    global interface_menu
    interface_menu.place_forget()

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, font=('Bold', 20), text="Entrez les valeurs que vous voulez:")
    alabel.grid(row=0, column=0, columnspan=5)

    labelX = createLabel(couleur2, 'Arial', 20, 'x=', 1, 0)
    fieldX = createText(1, 15, "Times New Roman",
                        15, "black", "#f5f5f5", 1, 1, 1)
    labelY = createLabel(couleur2, 'Arial', 20, 'y=', 2, 0)
    fieldY = createText(1, 15, "Times New Roman",
                        15, "black", "#f5f5f5", 2, 1, 1)

    labelm = createLabel(couleur2, 'Arial', 15, "m", 2, 2)
    labelm = createLabel(couleur2, 'Arial', 15, "m", 1, 2)

    labellam = createLabel(couleur2, 'Arial', 20, f'{lamcara}=', 9, 0)
    labelphi = createLabel(couleur2, 'Arial', 20, f'{phicara}=', 10, 0)

    labeldegrelam, fielddegrelam, labelminutelam, fieldminutelam, labelsecondelam, fieldsecondelam = labelettextdegminsec(
        9, 1)

    labeldegrephi, fielddegrephi, labelminutephi, fieldminutephi, labelsecondephi, fieldsecondephi = labelettextdegminsec(
        10, 1)

    alabel = tk.Label(
        frame, bg='#ececec', fg=couleur2, padx=0, font=('Bold', 20), text="Entrez le numéro de la zone:        ")
    alabel.grid(row=3, column=0, columnspan=4)

    zone = fonctionzone(4, 1)
    labelWest = createLabel(couleur2, 'Arial', 20, 'W', 9, 7)
    labelNord = createLabel(couleur2, 'Arial', 20, 'N', 10, 7)

    Labelellipsevide = ellipsevide(11, 0, 6)

    calc = ttk.Button(frame, text="Calculer",
                      command=lambda: rect_geo(fieldX, fieldY, zone, fielddegrephi, fieldminutephi, fieldsecondephi, fielddegrelam, fieldminutelam, fieldsecondelam), style='my.TButton')

    calc.grid(row=8, column=3)

    root.geometry('1000x500')


root.mainloop()
