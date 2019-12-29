#!/usr/bin/python
import re
import os

directory = "./dump"
os.chdir(directory)
cwd = os.getcwd()  

with open("result_temp_i.csv","w") as file_object:
    file_object.write("bitrate(kb/s) , psnr(Y) , psnr(U) , psnr(V) , Sequence\n")

files = os.listdir(os.getcwd())
for file in files:
    if "csv" in file.split("."):
        y_psnr = 0
        u_psnr = 0
        v_psnr = 0
        bitrate = 0
        cout = 0
        with open(file) as file_object:
            lines = file_object.readlines()
        for line in lines:
            if re.match('^I_SLICE.',line): 
                element  = line.split(",")
                y_psnr  += float(element[4])
                u_psnr  += float(element[5])
                v_psnr  += float(element[6])
                bitrate += float(element[8])
                cout += 1
        with open("result_temp_i.csv","a") as file_object:
            if cout != 0:
                file_object.write(str(bitrate/cout)+",")
                file_object.write(str(y_psnr /cout) +",")
                file_object.write(str(u_psnr /cout) +",")
                file_object.write(str(v_psnr /cout) +",")
                file_object.write(str(file)+"\n")

with open("result_temp_p.csv","w") as file_object:
    file_object.write("bitrate(kb/s) , psnr(Y) , psnr(U) , psnr(V) , Sequence\n")

files = os.listdir(os.getcwd())
for file in files:
    if "csv" in file.split("."):
        y_psnr = 0
        u_psnr = 0
        v_psnr = 0
        bitrate = 0
        cout = 0
        with open(file) as file_object:
            lines = file_object.readlines()
        for line in lines:
            if re.match('^P_SLICE.',line): 
                element  = line.split(",")
                y_psnr  += float(element[4])
                u_psnr  += float(element[5])
                v_psnr  += float(element[6])
                bitrate += float(element[8])
                cout += 1
        with open("result_temp_p.csv","a") as file_object:
            if cout != 0:
                file_object.write(str(bitrate/cout)+",")
                file_object.write(str(y_psnr /cout) +",")
                file_object.write(str(u_psnr /cout) +",")
                file_object.write(str(v_psnr /cout) +",")
                file_object.write(str(file)+"\n")

#sort
with open("../result.log","w") as file_object:

    file_object.write("%-47s %s\n"%("I frame","P frame"))
    file_object.write("%-13s \t %-7s \t %-7s \t %-7s    "%("bitrate(kb/s)","psnr(Y)","psnr(U)","psnr(V)"))
    file_object.write("%-13s \t %-7s \t %-7s \t %-7s    \n"%("bitrate(kb/s)","psnr(Y)","psnr(U)","psnr(V)"))
    
file_list = ["BasketballPass"  ,
             "BQSquare"        ,
             "BlowingBubbles"  ,
             "RaceHorses"      ,
             "BasketballDrill" ,
             "BQMall"          ,
             "PartyScene"      ,
             "RaceHorsesC"     ,
             "FourPeople"      ,
             "Johnny"          ,
             "KristenAndSara"  ,
             "Kimono"          ,
             "ParkScene"       ,
             "Cactus"          ,
             "BasketballDrive" ,
             "BQTerrace"       ,
             "Traffic"         ,
             "PeopleOnStreet"
            ]
qp_list = [22,27,32,37]

for file_name in file_list:
    for qp in qp_list:
        with open("result_temp_i.csv") as file_read:
            lines = file_read.readlines()
            for line in lines:
                if re.match(r'.*?%s\_%d'%(file_name,qp),line):
                    element = line.split(",")
                    with open("../result.log","a") as file_write:
                        file_write.write("%-13.2f \t "%(float(element[0])))
                        file_write.write("%-7.3f \t %-7.3f \t %-7.3f    "%(float(element[1]),float(element[2]),float(element[3])))
        with open("result_temp_p.csv") as file_read:
            lines = file_read.readlines()
            for line in lines:
                if re.match(r'.*?%s\_%d'%(file_name,qp),line):
                    element = line.split(",")
                    with open("../result.log","a") as file_write:
                        file_write.write("%-13.2f \t "%(float(element[0])))
                        file_write.write("%-7.3f \t %-7.3f \t %-7.3f    "%(float(element[1]),float(element[2]),float(element[3])))
                        str_temp = str(element[4])
        with open("../result.log","a") as file_write:
            str_temp = file_name + "_" + str(qp)
            file_write.write("%-94s\n"%(str_temp))

os.remove("result_temp_i.csv")  
os.remove("result_temp_p.csv")  
