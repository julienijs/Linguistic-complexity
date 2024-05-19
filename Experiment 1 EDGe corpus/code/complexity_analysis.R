# This is the r script for analyzing the morphological and syntactic complexity datasets

library(readxl)
library(ggplot2)
library(matrixStats)
library(effects)
library(ppcor)
library(dplyr)

#### morphology ####

# read data
morph_data <- read_xlsx("EDGe_Morph_Zipped.xlsx", col_names = TRUE)
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
morph_total$morph_means <- as.numeric(morph_means)
# get standard deviations
morph_std = rowSds(as.matrix(morph_total[,8:1007]))

morph_total <- morph_total %>%
  mutate(language_bin = ifelse(language == "English", "English", "Continental"))

# linear model
morph_model <- lm(morph_means ~ year + language, data=morph_total)
summary(morph_model)
morph_Dutch <- lm(morph_means ~ year, data = subset(morph_total, language == 'Dutch'))
summary(morph_Dutch)
morph_German <- lm(morph_means ~ year, data = subset(morph_total, language == 'German'))
summary(morph_German)
morph_English <- lm(morph_means ~ year, data = subset(morph_total, language == 'English'))
summary(morph_English)

ml <- ggplot(morph_total, 
             aes(x = year, y = morph_means, color = language))+
  ggtitle("Morphological complexity ratio over time") +
  xlab("Year")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()
ml

#### morphology suffix ####

# read data
morph_suffix_data <- read_xlsx("EDGe_Morph_Suffix_Zipped.xlsx", col_names = TRUE)

# merge data
morph_suffix_total <- merge(zipped, morph_suffix_data, by="...1")

# make all numbers negative
morph_suffix_total[,8:1007] <- morph_suffix_total[,8:1007]*(-1)
# divide by full zipped size to get complexity ratio
morph_suffix_total[,8:1007] <- morph_suffix_total[,8:1007]/morph_suffix_total[,5]
# get means for each row = get mean complexity ratio
morph_suffix_means <- rowMeans(morph_suffix_total[,8:1007])
# add mean complexity ratios to data frame
morph_suffix_total$morph_suffix_means <- as.numeric(morph_suffix_means)
# get standard deviations
morph_suffix_std = rowSds(as.matrix(morph_suffix_total[,8:1007]))

# linear model
morph_suffix_model <- lm(morph_suffix_means ~ year + language, data=morph_suffix_total)
summary(morph_suffix_model)
morph_suffix_Dutch <- lm(morph_suffix_means ~ year, data = subset(morph_suffix_total, language == 'Dutch'))
summary(morph_suffix_Dutch)
morph_suffix_German <- lm(morph_suffix_means ~ year, data = subset(morph_suffix_total, language == 'German'))
summary(morph_suffix_German)
morph_suffix_English <- lm(morph_suffix_means ~ year, data = subset(morph_suffix_total, language == 'English'))
summary(morph_suffix_English)

msl <- ggplot(morph_suffix_total, 
             aes(x = year, y = morph_suffix_means, color = language))+
  ggtitle("Morphological complexity ratio over time (suffix)") +
  xlab("Year")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()
msl

#### syntax ####

# read data
synt_data <- read_xlsx("EDGe_Synt_Zipped.xlsx", col_names = TRUE)

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
summary(synt_model)
synt_Dutch <- lm(synt_means ~ year, data = subset(synt_total, language == 'Dutch'))
summary(synt_Dutch)
synt_English <- lm(synt_means ~ year, data = subset(synt_total, language == 'English'))
summary(synt_English)
synt_German <- lm(synt_means ~ year, data = subset(synt_total, language == 'German'))
summary(synt_German)

sl <- ggplot(synt_total, 
             aes(x = year, y = synt_means, color = language))+
  ggtitle("Syntactic complexity over time") +
  xlab("Year")+
  ylab("Mean syntactic complexity")+
  guides(color=guide_legend(title="Language"))+
  geom_point()
sl

#### morphology vs syntax ####

morph_and_synt <- merge(synt_total, morph_total, by = "filename", all = TRUE)

# linear model
morph_and_synt_model <- lm(synt_means ~ morph_means, data=morph_and_synt)
summary(morph_and_synt_model)

scp <- ggplot(morph_and_synt,
              aes(x = synt_means, y = morph_means, color = language.x))+
  ggtitle("Trade-off between morphological complexity and syntactic complexity") +
  xlab("Mean syntactic complexity ratio")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()
scp

#### morphology suffix vs syntax ####

morph_and_synt <- merge(morph_and_synt, morph_suffix_total, by = "filename", all = TRUE)


# linear model
morph_suffix_and_synt_model <- lm(synt_means ~ morph_suffix_means, data=morph_and_synt)
summary(morph_suffix_and_synt_model)

scp <- ggplot(morph_and_synt,
              aes(x = synt_means, y = morph_suffix_means, 
                  color = language.x))+
  ggtitle("Morphological complexity ratio (more restrictive) vs syntactic complexity ratio") +
  xlab("Mean syntactic complexity ratio")+
  ylab("Mean morphological complexity ratio")+
  guides(color=guide_legend(title="Language"))+
  geom_point()
scp

