train=int(input())
station_dict={}
for i in range(train):
    name=input()
    station_dict[name]={}
    no_comp=int(input())
    for i in range(no_comp):
        detail=input()
        li=detail.split(",")
        station_dict[name][li[0]]=int(li[1])
print(station_dict)
