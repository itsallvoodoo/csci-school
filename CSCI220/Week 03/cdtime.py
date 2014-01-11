# cdtime.py
#
# A program that totals the time on a CD
#
# <Chad Hobbs> - Date: 120125

## ---------------PART 1 ONLY--------------------
##print("Welcome to the CD Time Calculator!")
##
##total_minutes = 0
##total_seconds = 0
##tracks = eval(input("How many tracks are on the CD?: "))
##
##for i in range(tracks):
##    print("Track",i+1)
##    minutes, seconds = eval(input("Please enter the minutes and seconds on the track, seperated by a comma:"))
##    total_minutes = total_minutes + minutes
##    total_seconds = total_seconds + seconds
##
##total_minutes = total_minutes + (total_seconds // 60)
##total_seconds = total_seconds % 60
##
##print("Total track time:",total_minutes,"minutes and",total_seconds,"seconds.")
##-----------------------------------------------


print("Welcome to the CD Play-time Calculator!")

o_minutes = 0
o_seconds = 0

cds = eval(input("How many CD's are being input?: "))

for j in range(cds):
    print()
    print("For CD",j+1,sep="")
    tracks = eval(input("How many tracks are on the CD?: "))

    total_minutes = 0
    total_seconds = 0

    for i in range(tracks):
        print("Track",i+1)
        minutes, seconds = eval(input("Please enter the minutes and seconds on the track, seperated by a comma:"))
        total_minutes = total_minutes + minutes
        total_seconds = total_seconds + seconds

    total_minutes = total_minutes + (total_seconds // 60)
    total_seconds = total_seconds % 60
    
    print()
    print("CD",cds+1," total track time: ",total_minutes," minutes and ",total_seconds," seconds.",sep="")

    o_minutes = o_minutes + total_minutes
    o_seconds = o_seconds + total_seconds

print()
print("Total time for all CD's is",int(o_minutes/60),"hours,",(o_minutes % 60 + int(o_seconds/60)),"minutes, and",o_seconds % 60,"seconds.")


    





