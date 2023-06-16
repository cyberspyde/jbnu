library(tidyverse)

fastfood <- read_csv('fastfood_calories.csv')
glimpse(fastfood)

fastfood <- fastfood %>%
  select(-X1)

md <- fastfood %>%
  filter(restaurant %in% c("Dairy Queen", "Mcdonalds"))

glimpse(md)

ggplot(data=md, aes(x=restaurant, y=cal_fat)) + geom_boxplot()


dairy_queen <- fastfood %>%
  filter(restaurant == "Dairy Queen")

dqmean <- mean(dairy_queen$cal_fat)
dqsd <- sd(dairy_queen$cal_fat)

ggplot(data = dairy_queen, aes(x=cal_fat)) + geom_histogram(bins=15)

ggplot(data = dairy_queen, aes(x=cal_fat)) + geom_histogram(bins=15, aes(y=..density..)) + stat_function(fun=dnorm, args=c(mean = dqmean, sd=dqsd), col="tomato")

ggplot(data = dairy_queen, aes(sample = cal_fat)) + geom_qq(distribution = qnorm) + geom_qq_line(line.p = c(0.25, 0.75), col = "blue") + ylab("Calories from fat")

sim_norm <- rnorm(n=nrow(dairy_queen), mean=dqmean, sd=dqsd)
snorm <- data.frame(sim_norm)

ggplot(data=snorm, aes(sample=sim_norm)) +
  geom_qq(distribution = qnorm)+
  geom_qq_line(line.p = c(0.25, 0.75), col = "blue") +
  ylab("Simulated normal")

1 - pnorm(q=600, mean=dqmean, sd=dqsd)
pnorm(q=600, mean=dqmean, sd=dqsd, lower.tail=F)

#Problem 1

dairy_queen %>%
  filter(cal_fat > 600) %>%
  summarise(percent = n() / nrow(dairy_queen))

arbys <- fastfood %>%
  filter(restaurant == "Arbys")

arbys %>%
  filter(sodium > 600) %>%
  summarise(percent = n() / nrow(arbys))

#I couldn't solve the Problem 2

#Problem 3

#we got to find the mean and Standard deviation first
burgerkingsodmean <- mean(burger_king$total_carb)
burgerkingsodsd <- sd(burger_king$total_carb)

#here is a histogram to get the skewness or simmetric graph
hist(burger_king$total_carb, probability = TRUE, ylim= c(0,0.06))
x <- 150:190
y <- dnorm(x=x, mean=burgerkingsodmean, sd=burgerkingsodsd)
ggplot(data = burger_king, aes(x=total_carb)) + geom_histogram(bins=15)


#Here is my ggplot graph code where I use to show the arbys' sodium distribution.
ggplot(data = arbys, aes(sample = sodium)) + 
  geom_qq(distribution = qnorm)+
  geom_qq_line(line.p = c(0.10,0.60), col="red")+
  ylab("Sodium")