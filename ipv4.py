class Ipv4():
    def __init__(self,adress):
        self.adress = adress
        if self.adress[-1] == "." :
            raise Exception("Sorry, incorrectly entered adress")
        self.array = adress.split(".")
        self.splitadress = []
        for x in self.array:
            x = int(x)
            self.splitadress.append(x)



    def IsValid(self):
        # ověřuje jestli je adresa zapsaná správně
        for x in self.splitadress:
            if self.adress.count(".") != 3 or len(self.splitadress) != 4 :
                raise Exception("Sorry, incorrectly entered adress")
            if x <= 255 and x >=0:
                continue
            else:
                return False
        return True
    

    def GetAsString(self):
        # vypíše adresu jako string
        return self.adress
    
    def GetAsBinaryString(self):
        # vypíše adresu ve 2 soustavě
        b = []
        for x in self.splitadress:
            x = str(bin(x))[2:]
            b.append(x)
        c = ".".join(b)
        return (c)

    def GetAsInt(self):
        #  vypíše  adresu jako jeden int
        a =""
        for x in self.splitadress:
            x = str(bin(x))[2:]
            a  += x
        return int(a,2)
    def GetClass(self):
        # vypíše classu adresy
        if self.splitadress[0] <=  127 and self.splitadress[0] >= 0:
            return "A"
        elif self.splitadress[0] <=  191 and self.splitadress[0] >= 128:
            return "B"
        elif self.splitadress[0] <=  223 and self.splitadress[0] >= 192:
            return "C"
        elif self.splitadress[0] <=  239 and self.splitadress[0] >= 224:
            return "D"
        elif self.splitadress[0] <=  255 and self.splitadress[0] >= 240:
            return "E"
        else:
            raise Exception("Sorry, incorrectly entered adress")
    def GetOctet(self,x):
        #vypíše konkrétní octet adresy
        if x > 3 or x < 0:
            raise Exception("Please write number between 0 and 3")
        else:
            return self.splitadress[x]

adress1= Ipv4("198.162.10.36")
print(adress1.IsValid())
print(adress1.GetAsString())
print(adress1.GetAsBinaryString())
print(adress1.GetAsInt())
print(adress1.GetClass())
print(adress1.GetOctet(0))