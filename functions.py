import socket
import sys
import os


class OpenOCD:
    def __init__ (self):
        pass

    def initOCD(self):
        HOST = '127.0.0.1'  #  hostname
        PORT = 3232         #  port

        f = open("message.txt", "r+")
        f.write("Some random data to be put here")
        f.close()

        try:
            #open ocd server socket object, global variable
            global ocd
            ocd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print ("Socket successfully created")
        except ocd.error as err:
            print ("socket creation failed with error %s" %(err))

        try:
            ocd.connect(("localhost", PORT))
            print("Initiating connection with the server")

            st = os.getcwd() 
            # st += "/message.txt"
            st_ba = st.encode()
            # print(st_ba)
            ocd.send(st_ba)

            while True:
                print (ocd.recv(1024) )
                



        except  Exception as inst :
            print("Connection to server coudn't be established")
            print(inst)

        return

    def enterOCD(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter openOCD</body></note>")
        return

    def exitOCD(self):
        ocd.close()
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text exit openOCD</body></note>")
        return

    #reset trstclk
    def resetTcl(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to reset trstclk</body></note>")
        return

    #read regsiter
    def readReg(self,addrs):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read something from register " + str(addrs) + "</body></note>")
        return

    def readReg(self,addrs,expV):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read something from register " + str(addrs) + "</body></note>")
        #will compare the recieved data form the tcp socket, then will compare with expV. will return a bool value after comparison
        return




    #write register
    def writeReg(self , addrs, content):
        f = open("message.xml" , "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to write some content to register</body></note>")
        return


    #reading memory
    def readMem(self, addrs):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read something from the register " +str(addrs)+" </body></note>")
        return

    def readMem(self, addrs, expV):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read something from the register " +str(addrs)+" </body></note>")
        #will compare the recieved data form the tcp socket, then will compare with expV. will return a bool value after comparison
        return

    #writing memory
    def writeMem(self, addrs):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read something from the register " +str(addrs)+" </body></note>")
        return

    def writeMem(self, addrs, expV):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read something from the register " +str(addrs)+" </body></note>")
        #will compare the recieved data form the tcp socket, then will compare with expV. will return a bool value after comparison
        return


    #irscan
    def scanIR(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to perform irscan</body></note>")
        return

    #drscan
    def scanDR(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to perform drscan</body></note>")
        return

    #adapter speed
    def adrSpeed(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to read adapter speed</body></note>")
        return



class piumaTAP:
    def __init__(self):
        pass
    #set test mode
    def setTestMode(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #set dft mode
    def setDFTMode(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #select tape end point
    def selectTEP(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #set power ok
    def setPowerOK(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #get tap state
    def getTapState(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #move tap state
    def moveTapState(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #freeze clock
    def freezeCLK(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #get exception status
    def getExceptionStatus(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #get cat error
    def getCatErr(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #get aib thermal status
    def getAIBStatus(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return

    #get MEM thermal status
    def getMEMStatus(self):
        f = open("message.xml", "w")
        f.write("<?xml version = \"1.0\" encoding = \"UTF-8\" standalone = \"no\" ?><note><body>text to enter </body></note>")
        return




#to call any function to test the functions
def main():
    obj = OpenOCD()
    obj.initOCD()


#intial
if __name__ == "__main__":
    main()
