# MSAI Probability Syllabus

For this course, we'll be closely following the excellent textbook **_"Introduction to Probability"_** (get it [**here**](https://ftp.xxcpeter.tech/Probability%20and%20Statistics/Books/Joseph%20K.%20Blitzstein%2C%20Jessica%20Hwang-Introduction%20to%20Probability.pdf)) by [Joseph K. Blitzstein](https://statistics.fas.harvard.edu/people/joseph-k-blitzstein) and Jessica Hwang , but we won't be limited by its contents.

If it feels that our syllabus and this textbook are a bit too advanced for you, or you're looking for more nice visualisations, see the excellent book **_"Introduction to Probability for Data Science"_** by [Stanley H. Chan](https://engineering.purdue.edu/ChanGroup/stanleychan.html) fully [**available online**](https://probability4datascience.com) for free. Big thank to Prof. Chan!

Below I tried to mark the key points (that is, obligatory to know) of the program **in bold**

## Syllabus:

1. **Definition of Probability:**
- **Sample spaces**
- Complements to events, mutually exclusive events, de Morgan's laws
- Counting rules: multiplication rule, sampling **with and without replacement**, permutations and factorials
- The Birthday problem/paradox
- Binomial coefficients, Binomial theorem, Vandermonde's identity
- Bose-Einstein statistic
- Rigorous definition of Probability: Probability spaces, properties of probability (additivity)
- Frequentist and Bayesian view
- Inclusion-exclusion formula

2. **Conditional probability:**
- Definition: prior, posterior
- Prosecutor's fallacy
- Frequentist interpretation
- Martin Gardner's "Two children" puzzle
- **Bayes' rule** and the **Law of Total Probability**
- Testing for diseases
- Conditional probabilities are probabilities (properties)
- **Independent events**
- Conditional independence
- Coherency of Bayes' rule
- Conditioning as a problem-solving tool: **Monty Hall**, Gambler's ruin, **Simpson's paradox**

3. **Random variables and distributions:** 
- Definition of r.v.-s. Indicator r.v.-s
- Discrete and continuous r.v.-s
- Distribution, **Probability mass function (pmf)**, its properties
- **Bernoulli and Binomial** distributions
- Hypergeometric distribution
- Discrete **uniform distribution**
- **Cumulative distribution function (cdf)**
- **Functions of random variables**
- **Independence** of r.v.-s
- Conditional independence of r.v.-s
- Connection between Binomial and Hypergeometric, Fisher's exact test

4. **Expectation:**
- Definition of **expected value** / mean, weighted mean
- **Linearity** of expectation
- Expectation of **Binomial** and Hypergeometric
- Monotonicity of expectation
- Geometric distribution, Negative Binomial distribution, their expectations
- Indicator functions again
- **Boole-Bonferroni's inequality**
- Law of the unconscious statistician (LOTUS)
- **Variance**, its non-linearity
- Variance of Binomial, Hypergeometric, Negative Binomial
- **Poisson** distribution, Poisson paradigm
- Connections between **Poisson and Binomial**
- Sum of Poissons, Poisson approximation of Binomial
- \* Noisy communication channels, coding, Hamming distance, entropy and Shannon's theorem

5. **Continuous random variables:**
- **Probability density function (pdf)**, its properties
- Logistic distribution, Rayleigh distribution
- Expectation of continuous r.v., LOTUS
- Uniform distribution
- **Location-scale transformation**
- Universality of the Uniform (and others) distribution
- Survival function
- The **Normal distribution**, its properties, standard normal, folded normal
- **Exponential distribution**, its properties (memoryless-ness)
- **Poisson processes**
- Symmetry of i.i.d. continuous r.v.-s

6. **Moments:**
- Measures of central tendency: **median, mode**
- **Moments,** central and standardized moments
- Mean = center of mass, Variance = moment of inertia
- **Skewness**, odd moments
- **Kurtosis** 
- **Sample moments,** bias
- **Moment generating functions (MGFs):** Bernoulli, Geometric, Uniform, Normal, Exponential
- MGF determines the distribution, MGF of sum (& loc-scale transform) of r.v.-s
- Finding moments with MGF
- **Log-normal distribution, Weibull distribution**
- MGF of sum of independent r.v.-s
- \* Probability generating functions

7. **Joint distributions:**
- **Joint, Marginal and Conditional** distributions (discrete)
- Independence
- **Joint, Marginal and Conditional** (continuous)
- Continuous Bayes and LOTP
- Uniform on a region of the plane
- **Cauchy distribution**
- Hybrid (continuous-discrete) distributions
- 2D LOTUS
- **Covariance and correlation**
- Multinomial distribution
- **Multivariate Normal distribution**

8. **Transformations of r.v.-s:**
- **Change of variable in 1D**
- Log-normal and Chi-square distributions from Normal
- Pdf of loc-scale transform
- **Change of variables, Jacobian** 
- Box-Muller method
- **Convolutions** 
- Convolutions with exponential, uniform
- The **Beta distribution**
- Beta-Binomial conjugacy
- The **Gamma distribution**
- Gamma-Poisson conjugacy
- Beta-Gamma connections
- **Order statistics**

9. **Conditional expectation:**
- **Conditional expectation, law of total expectation**
- Two envelopes paradox
- Time until HH vs HT
- **Properties of conditional expectation**
- Conditional expectation as projection
- **Linear regression**
- Conditional variance
- Adam's and Eves' laws
- Gamma-Poisson again

10. **Inequalities and Limit Theorems:**
-  **Cauchy-Schwarz inequality** and joint expectation
-  **Jensen inequality**
-  **Entropy**
-  **Kullback-Leibler divergence**
-  **Markov inequality**
-  **Chebyshev inequality**
-  Chernoff inequality
-  **Law of large numbers** (weak and strong)
-  Convergence of empirical CDF
-  **Central limit theorem**
-  Convergence of Binomial, Poisson, Gamma to Normal
-  Cauchy distribution again
-  **Chi-square**, sample variance 
-  **Student-t**, sample means, degrees of freedom

11. **Markov chains**
- Markov property
- **Transition matrix**
- Marginal disctibutions of MCs
- **Recurrent and transient** states
- Number of returns to transient is Geometric
- **Irreducible and reducible** chains
- Gambler's ruin as MC
- Period of state, periodic and aperiodic MCs
- **Stationary distribution**, its existence and uniqueness
- Convergence to stationary distribution
- Google's **PageRank**
- Reversibility of MCs
- Ehrenfest model

12. \* **Markov Chain Monte-Carlo (MCMC):**
- **Metropolis-Hastings**
- Simulating **Zipf's distribution**
- **MCMC samples are correlated**, 
- Knapsack problem
- Normal-Normal conjugacy
- **Gibbs sampling**, systematic and random scan
- Darwin's finches

12. \*\* **Poisson processes:**
-  Poisson processes in 1D again
-  Conditioning, superposition and thinning
-  Coloring
-  Poisson processes in multiple dimensions
-  Count-distance duality, Weibull
-  Cox and Yule processes
