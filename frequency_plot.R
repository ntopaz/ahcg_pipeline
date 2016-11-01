


library(ggplot2)


cov <- read.delim("brca2_depth.txt", header=FALSE)
names(cov) <- c("Chr", "Position", "Coverage")

png(filename="coverage_3.png")
qplot(cov$Coverage,
      geom="histogram",
      binwidth=10,
      main="Distribution of Coverage",
      xlab="Coverage",
      fill=I("blue"),
      col=I("black"),
      alpha=I(.2),
      breaks=seq(0,350,5))

dev.off()


