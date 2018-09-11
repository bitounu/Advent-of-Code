#!/usr/bin/python

x = ['draaabina', 'antylopa', 'fanatstyffaxy', 'jakasmamam', 'baaden baaden' , 'peace' , 'pees', 'goooldem', 'qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']

def doubler(line):
    f = 0
    for j in range(0, len(line)):
        c   = line[j:j+2]       # wycinam 2 znaki
        if c in line[j+3:]:     # sprawdzam czy znajde jeszcze takie
          #  print c
          #  print line[j+3:]
            f = 1
    return f

def cacy(plik):
    cacy = 0
    # otwieram plik z danymi
    with open(plik, 'r') as myfile:
        for line in myfile:
            if doubler(line):
                print line
    print "Linii, ktore sa cacy jest: %d" % cacy


def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print 'program -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'program -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
            doubler(inputfile)

if __name__ == "__main__":
    main(sys.argv[1:])

