# Set your working directory to the folder containing this script
# Session > Set Working Directory > To Source File Location
# Pool Tracer Level Analysis= 23 pools, summer vs winter comparison

#Creating the dataframe

pool_ID= paste0("P", 1:23)
summer= c(820, 1700, 990, 800, 1600, 60, 50, 2110, 70, 350, 90, 210, 900, 470, 780, 250, 590,
490, 4300, 1400, 1000, 1300, 1200)
winter= c(400, 100, 90, 80, 160, 6, 50, 210, 7, 35, 90, 20, 100, 170, 280, 150, 90, 190, 300, 100,
104, 300, 20)
dfp=data.frame(pool_ID,summer,winter)
print(dfp)

#No. of rows and columns

dim(dfp)

#Displaying the first and last 5 rows

head(dfp)
tail(dfp)

#New column of the difference

Difference= summer-winter
dfp=cbind(dfp,Difference)
print(dfp)

#Higher activity levels are shown by pools: 2,5,8,19,20,22,23
dfp$pool_ID[dfp$summer>1000]

#Average column addition

Average_Activity= (summer+winter)/2
dfp=cbind(dfp,Average_Activity)
print(dfp)

#Renaming the column
colnames(dfp)[5]= "Mean_Tracer_Level"
#OR
names(dfp)[names(dfp) == "Average_Activity"]= "Mean_Tracer_Level"

#New entry for row

new_entry= data.frame(pool_ID="P24",summer=950,winter=120,Difference=950-120,Mean_Tracer_Level= (950 + 120)/2)
dfp=rbind(dfp,new_entry)
print(dfp)

#Busiest pool
dfp$pool_ID[which.max(dfp$summer)]

#Save the final data frame as a CSV file in your working directory.
write.csv(dfp, "pool.csv", row.names=FALSE)

