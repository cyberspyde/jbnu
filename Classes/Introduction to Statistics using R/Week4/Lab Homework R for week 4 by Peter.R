#I have tried all these commands, and they are perfectly working
getwd()
hotdog <- read.csv('hotdog.csv')
head(hotdog)
summary(hotdog)
str(hotdog)

# a to i, Completed all, they are working, I can explain their values, because I have studied programming concepts and they are all similar
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

#Package has been installed
install.packages('tidyverse')
library(tidyverse)

#I created data_meat variable and assigned the Meat data to it
data_meat <- hotdog[hotdog$Type == "Meat", ]

#got the summary
summary(data_meat)

#now, cars_data observation has been created to get the data from usedcars.txt
cars_data <- read.table('usedcars.txt', sep=',')

#got the summary of the new observation I have created
summary(cars_data)
