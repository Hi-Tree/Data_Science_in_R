library(dslabs)
data(heights)
male <- heights$height[heights$sex=="Male"]
female <- heights$height[heights$sex=="Female"]
p <- seq(0.10, 0.90, 0.20)
female_percentiles<-quantile(female, p)
male_percentiles<-quantile(male, p)
df<-data.frame(female = c( female_percentiles), male = c( male_percentiles))
print(df)