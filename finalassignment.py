
#fungsi
def dashboard(x,y):
    print("\n")
    print ("Dashboard Of Premiere Leageu B:","\n")
    for i in dict_goals1:
        total_goals = 0
        total_games = 0
        for j in dict_goals2:
            if i == j:
                for x in dict_goals1[i]:
                    for y in dict_goals2[j]:
                        total_goals = x+y
                        average_goals = total_goals/2
                total_games = 2
        print(i.capitalize())
        print("Total Goals      : ",total_goals)
        print("Total Games      : ",total_games)
        print("Average Goals    :",average_goals)
        print("------------------------------------")
    print("Thank You")

#read file
nama_file = "poiuy.txt"
file = open(nama_file,'r')

dict_goals1 = {}
dict_goals2 = {}
teks = file.readline().replace('\n',"")
while teks != "":
    indexx = teks.split()    #indeks 0 :club1,indeks1:club1_goals,indeks2:club2_goals,indeks3:club2

    if indexx [0] in dict_goals1:
        dict_goals1[indexx[0]].append[int(indexx[1])]
    else:
        dict_goals1[indexx[0]] = [int(indexx[1])]

    if indexx [3] in dict_goals2:
        dict_goals2[indexx[3]].append[int(indexx[2])]
    else:
        dict_goals2[indexx[3]] = [int(indexx[2])]

        teks=file.readline().replace('\n',"")
file.close()

#calling function
dashboard(dict_goals1,dict_goals2)
# print(dict_goals1)