set.seed(20200512)
library(tidyverse)
library(infer)
global_monitor <- tibble(scientist_work = c(rep("Benefits", 80000), rep("Doesn't benefit", 20000))
                         )
glimpse(global_monitor)

summary(global_monitor)

ggplot(data=global_monitor, aes(x = scientist_work)) +
  geom_bar() +
  labs( x = "", y = "",
        title = "Do you believe that the work scientists do benefit people like you?") +
  coord_flip()

global_monitor %>%
  count(scientist_work) %>%
  mutate(p = n /sum(n))

samp1 <- global_monitor %>%
  sample_n(50)

ggplot(samp1, aes(x = scientist_work)) +
  geom_bar() +
  labs( x = "", y = "",
        title = "Do you believe that the work scientists do benefit people like you?") +
  coord_flip()

samp1 %>%
  count(scientist_work) %>%
  mutate(p_hat = n/sum(n))

samp2 <- global_monitor %>%
  sample_n(50)

samp2 %>%
  count(scientist_work) %>%
  mutate(p_hat = n/sum(n))

sample_props50 <- global_monitor %>%
  rep_sample_n(size = 50, reps = 15000, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")

ggplot(data = sample_props50, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.02) +
  labs(
    x = "p_hat (Doesn't benefit)",
    title = "Sampling distribution of p_hat",
    subtitle = "Sample size = 50, Number of samples = 15000"
  )

glimpse(sample_props50)

mean(sample_props50$p_hat)

sample_props_small <- global_monitor %>%
  rep_sample_n(size = 10, reps = 25, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")
sample_props_small

glimpse(sample_props_small)

ggplot(data = sample_props50, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.02)

sample_props10 <- global_monitor %>%
  rep_sample_n(size = 10, reps = 5000, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")

sample_props50 <- global_monitor %>%
  rep_sample_n(size = 50, reps = 5000, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")

sample_props100 <- global_monitor %>%
  rep_sample_n(size = 100, reps = 5000, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")

mean(sample_props10$p_hat)
sd(sample_props10$p_hat)

mean(sample_props50$p_hat)
sd(sample_props50$p_hat)

mean(sample_props100$p_hat)
sd(sample_props100$p_hat)

ggplot(data = sample_props10, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.1)+
  labs(
    x = "p_hat (Doesn't benefit)",
    title = "Sampling distribution of p_hat",
    subtitle = "Sample size = 10, Number of samples = 5000"
  )

ggplot(data = sample_props50, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.02)+
  labs(
    x = "p_hat (Doesn't benefit)",
    title = "Sampling distribution of p_hat",
    subtitle = "Sample size = 50, Number of samples = 5000"
  )

ggplot(data = sample_props100, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.02)+
  labs(
    x = "p_hat (Doesn't benefit)",
    title = "Sampling distribution of p_hat",
    subtitle = "Sample size = 100, Number of samples = 5000"
  )


#Lab Problem 1
sample_props15 <- global_monitor %>%
  rep_sample_n(size = 15, reps = 2000, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")

ggplot(data = sample_props15, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.02)+
  labs(
    x = "p_hat (Do enhances)",
    title = "Sampling distribution of p_hat",
    subtitle = "Sample size = 15, Number of samples = 2000"
  )



#Lab Problem 2
sample_props15 <- global_monitor %>%
  rep_sample_n(size = 150, reps = 2000, replace = TRUE) %>%
  count(scientist_work) %>%
  mutate(p_hat = n /sum(n)) %>%
  filter(scientist_work == "Doesn't benefit")

ggplot(data = sample_props15, aes(x = p_hat)) +
  geom_histogram(binwidth = 0.02)+
  labs(
    x = "p_hat (Do enhances)",
    title = "Sampling distribution of p_hat",
    subtitle = "Sample size = 150, Number of samples = 2000"
  )

