# Probability Distributions
import scipy.stats as stats

# Bernoulli Distribution: A single trial with only two outcomes,
# which are success or failure.
dist = stats.bernoulli(0.7)
# Probability of success
print(dist.pmf(1))
# Probability of failure
print(dist.pmf(0))

# Binomial Distribution: Multiple Bernoulli trials.
dist = stats.binom(10, 0.5)
# Probability of exactly 6 heads
print(dist.pmf(6))

# Poisson Distribution: Used when counting events over time or space
dist = stats.poisson(mu=5)
# Probability of exactly 3 events
print(dist.pmf(3))

# Normal Distribution: The famous bell curve, continuous distribution
dist = stats.norm(loc=0, scale=1)
# Probability density at x = 1
print(dist.pdf(1))
