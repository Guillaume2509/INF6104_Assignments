# K constant
K <- 31.867

# Your vector of observations
n <- seq(from = 1, to = 23, by = 1)

# Your sum of all frequencies
TotalFrequencies <- 119

# The Shannon Entropy Calculator
output <- vector(mode = "numeric", length = length(n))
for (i in 1:length(n))
  output[i] <- -((K/n[i])/TotalFrequencies)*log2((K/n[i])/TotalFrequencies)

# The Shannon Entropy Awnser
sum(output)

#######
y <- c(0.160, 0.126, 0.118, 0.109, 0.101,  0.092, 0.025,  0.025,  0.025,  0.025,  0.025,  0.025,  0.017,  0.017,  0.017,  0.017,  0.017,  0.017,  0.008,  0.008,  0.008,  0.008,  0.008)

# The Shannon Entropy Calculator
output <- vector(mode = "numeric", length = length(y))
for (i in 1:length(y))
  output[i] <- -(y[i]*log2(y[i]))

# The Shannon Entropy Awnser
sum(output)

#######
y <- c(0.043)

# The Shannon Entropy Calculator
output <- vector(mode = "numeric", length = length(y))
for (i in 1:23)
  output[i] <- -(y*log2(y))

# The Shannon Entropy Awnser
sum(output)