library(readxl)
library(ggplot2)
library(matrixStats)
library(effects)

# read data
pragm_data <- read_xlsx("pragm_zipped_all.xlsx", col_names = TRUE)
zipped <- read_xlsx("EDGe_Zipped_Sizes.xlsx", col_names = TRUE)

# merge data
pragm_total <- merge(zipped, pragm_data, by="...1")

# divide by full zipped size to get complexity ratio
pragm_total[,8:1007] <- pragm_total[,8:1007]/pragm_total[,5]
# get means for each row = get mean complexity ratio
pragm_means <- rowMeans(pragm_total[,8:1007])
# add mean complexity ratios to data frame
pragm_total$pragm_means <- pragm_means
# get standard deviations
pragm_std = rowSds(as.matrix(pragm_total[,8:1007]))

# linear model
pragm_model <- lm(pragm_means ~ year + language, data=pragm_total)
summary(pragm_model)
plot(allEffects(pragm_model))
pragm_model <- lm(pragm_means ~ year*language, data=pragm_total)
summary(pragm_model)
plot(allEffects(pragm_model))

# make plots

p1 <- ggplot(pragm_total, 
             aes(x = year, y = pragm_means, color = language, shape = text))+
  ggtitle("Pragmatic complexity ratio over time") +
  xlab("Year")+
  ylab("Mean pragmatic complexity ratio")+
  guides(color=guide_legend(title="Language"), 
         shape=guide_legend(title="Text"))+
  geom_point()
p1

p2 <- ggplot(pragm_total, 
             aes(x = year, y = pragm_means, color = language))+
  ggtitle("Pragmatic complexity ratio over time") +
  xlab("Year")+
  ylab("Mean pragmatic complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()+
  geom_smooth()
p2

p3 <- ggplot(pragm_total, 
              aes(x = language, y = pragm_means, fill = text))+
  ggtitle("Pragmatic complexity ratio aggregated by language") +
  xlab("Language")+
  ylab("Mean pragmatic complexity ratio")+
  guides(fill=guide_legend(title="Text"))+
  geom_boxplot()
p3
