setwd("C:/Users/u0149275/OneDrive - KU Leuven/Complexity/EDGe")

library(readxl)
library(ggplot2)
library(matrixStats)
library(effects)

#### morphology ####

# read data
morph_data <- read_xlsx("morph_zipped_all.xlsx", col_names = TRUE)
zipped <- read_xlsx("EDGe_Zipped_Sizes.xlsx", col_names = TRUE)

# merge data
morph_total <- merge(zipped, morph_data, by="...1")

# make all numbers negative
morph_total[,8:1007] <- morph_total[,8:1007]*(-1)
# divide by full zipped size to get complexity ratio
morph_total[,8:1007] <- morph_total[,8:1007]/morph_total[,5]
# get means for each row = get mean complexity ratio
morph_means <- rowMeans(morph_total[,8:1007])
# add mean complexity ratios to data frame
morph_total$morph_means <- morph_means
# get standard deviations
morph_std = rowSds(as.matrix(morph_total[,8:1007]))


# linear model
morph_model <- lm(morph_means ~ year + language, data=morph_total)
morph_model <- lm(morph_means ~ year*language, data=morph_total)
summary(morph_model)
plot(allEffects(morph_model))

# make plots

mp <- ggplot(morph_total, 
             aes(x = year, y = morph_means, color = language, shape = text))+
  ggtitle("Morphological complexity ratio over time") +
  xlab("Year")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"), 
         shape=guide_legend(title="Text"))+
  geom_point()
mp

ml <- ggplot(morph_total, 
             aes(x = year, y = morph_means, color = language))+
  ggtitle("Morphological complexity ratio over time") +
  xlab("Year")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()+
  geom_smooth()
ml

mbp <- ggplot(morph_total, 
             aes(x = language, y = morph_means, fill = text))+
  ggtitle("Morphological complexity ratio aggregated by language") +
  xlab("Language")+
  ylab("Mean morphological complexity ratio")+
  guides(fill=guide_legend(title="Text"))+
  geom_boxplot()
mbp

#### syntaxis ####

# read data
synt_data <- read_xlsx("synt_zipped_all.xlsx", col_names = TRUE)

# merge data
synt_total <- merge(zipped, synt_data, by="...1")

# divide by full zipped size to get complexity ratio
synt_total[,8:1007] <- synt_total[,8:1007]/synt_total[,5]
# get means for each row = get mean complexity ratio
synt_means <- rowMeans(synt_total[,8:1007])
# add mean complexity ratios to data frame
synt_total$synt_means <- synt_means
# get standard deviations
synt_std = rowSds(as.matrix(synt_total[,8:1007]))


# linear model
synt_model <- lm(synt_means ~ year+language, data=synt_total)
synt_model <- lm(synt_means ~ year*language, data=synt_total)
summary(synt_model)
plot(allEffects(synt_model))

# make plots

sp <- ggplot(synt_total, 
             aes(x = year, y = synt_means, color = language, shape = text))+
  ggtitle("Syntactic complexity ratio over time") +
  xlab("Year")+
  ylab("Mean syntactic complexity ratio")+
  guides(color=guide_legend(title="Language"), 
         shape=guide_legend(title="Text"))+
  geom_point()
sp

sl <- ggplot(synt_total, 
             aes(x = year, y = synt_means, color = language))+
  ggtitle("Syntactic complexity ratio over time") +
  xlab("Year")+
  ylab("Mean syntactic complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()+
  geom_smooth()
sl

sbp <- ggplot(synt_total, 
              aes(x = language, y = synt_means, fill = text))+
  ggtitle("Syntactic complexity ratio aggregated by language") +
  xlab("Language")+
  ylab("Mean syntactic complexity ratio")+
  guides(fill=guide_legend(title="Text"))+
  geom_boxplot()
sbp

#### morphology vs syntaxis ####

morph_and_synt <- data.frame(morph_total$morph_means, 
                             synt_total$synt_means, 
                             synt_total$language,
                             synt_total$text,
                             synt_total$year)

morph_and_synt_model <- lm(synt_means ~ morph_means, data=morph_and_synt)
summary(morph_and_synt_model)

scp <- ggplot(morph_and_synt,
              aes(x = synt_means, y = morph_means, color = synt_total.language))+
  ggtitle("Syntactic vs morphological complexity ratio") +
  xlab("Mean syntactic complexity ratio")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()
scp

