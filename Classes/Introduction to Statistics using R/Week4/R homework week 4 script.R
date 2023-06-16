#These are to get the variables and I tried them all
getwd()
hotdog <- read.csv('hotdog.csv')
head(hotdog)
summary(hotdog)
str(hotdog)

#homework 1
hotdog[1,1]
hotdog[2,4]
hotdog[801,29]
hotdog[2, ]
hotdog[-1, ]
hotdog[1:4, 1]
hotdog[1:10, c("Type", "Calories")]
hotdog[, c("Type")]
head(hotdog)
tail(hotdog)
hotdog$Type
hotdog[hotdog$Type == "Beef",]

#homework 2
install.packages('tidyverse')

#homework 3
MeatData <- hotdog[hotdog$Type == "Meat", ]

#homework 4
summary(MeatData)

#homework 5
usedCars_data <- read.table('usedcars.txt', sep=',')

#homework 6
summary(usedCars_data)
