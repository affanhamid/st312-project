
Question: Does statistical evidence from lap times, pit stop timing, and tire allocation indicate systematic performance differences between teammates?

- Statistical analysis has tried to separate driver skill from car performance
    - van Kersteren and Bergkamp (2023) found approximate 88% of performance varience comes from the constructor while only 12% is attributable to drive.
    - Bell et al. (2016) found 86%/14%
- Herdernson and Kirrane (2018) developed Plackett-Luce ranking models for probabilistic forecasting
- Phillips (2014) used dummy variable regression for driver rankings
- Ehicenberger and Stadelmann (2009) developed an econometric framework to separate driver performance from equipment quality

# Van Kersetern and Bergkamp
- Hybrid era in F1 (2014 - 2021)
- Bayesian multilevel rank-ordered logit regression method to model individual race finishing positions
- Hamilton and Verstappen are the best drivers in the hybrid era
- Top 3 teams are Mercedes, Ferrari, and Red Bull
- 88% of varience in race results is explained by the constructor

- Competitive motor racing is not purely skill-based. It's skill + material base
- In contrast to "spec" series, F1 teams build their own cars from ground up with different specifications. Because of these differences, Mercedes dominated the sport in the hybrid era

- 2016 World Champion Niko Rosberg posed that 80% of success in F1 can be attributed to the car and 20% to the driver

- Bayesian Multilevel Beta regression model to answer:
    1. What is the relative influence of the driver and constructor on race results
    2. How do drivers rank in terms of skill level
    3. How do constructors rank in terms of race car advantage

- References Eichenverger and Stadlemann
    - Shortcoming of study: Choice of outcome variable: Number of contestants per race changed over seasons (sometimes within season). The interpretation of "finishing position" changed as well
    - Addressed by Phillips (2014): Estimated using an adjusted "pionts scored" outcome variable
    - Pihillips said "These cars have the same performance, allowing for direct comparisons of a driver's skill level against their teammates. Drivers move to different constructor-teams throughout their career, allows for simultaenous estimation of driver and constructor effects"

    - They used many dummy variables instead of multilevel model. Multileve approach is beneficial because it makes the model tractable with fewer observations per driver and improves predictions for nested data (Gleman, 2006)

    - Bell et al. used a similar argument ad ued the same "points scored" outcome variable but used a multilevel linear model
    - Improvements to Bell et al.
        - "Points scored" leads to information loss: Any result below sixth place leads to zero points. Our approach creates a rank-ordered logit model
        Bayesian workflow: Gelman et al, 2013
        visualisations: Gabry et al, 2019
        comparison: Vehtari et al., 2017
        - Parameters for driver skill and constructor advantage are directly interpretable as log-odds ratios of beating competitors, similar to Elo ratings in chess


# Data processing
- Ergast API from 2014 to 2021
- Enriched from Wikipedia to get weather type (wet or dry) and circuit type (street or permanent). Manually completed for the rest from publicaly available race summaries

- Non-finishers were rmoved from the analysis (removed 590)
    - Implications: Section 3
    - Sensitivity analysis: Appendxi A
    - Disregard the starting position. It's the same whether the driver starts at the start or the end

# Bayesian multilevel rank-ordered logit model

- f(driver skill, yearly driver form, constructor advantage, yearly constructor form)

For each race $r$, assume a set of competitors $\mathcal{C}_r$. Outcome variable is a vector representing a ranking of these competitors $\mathbb{y}_r$.
- Assume ranking follows a Rank-Ordered Logit distriubtion, based on a vector of latent abilities of the competitors $\mathbb{\mathcal{V}}_r$
$$
\mathbb{y}_r  \sim \text{RankOrderedLogit}(\mathbb{\mathcal{V}}_r)
$$
- Explained in detail in Glickman and Henessy. Appendix B
- A competitor $c \in \mathcal{C}_r$ is (driver, team, season) triplet
- Skill of each competitor is skill of the driver-constructor pairing in a season: $\mathcal{V}_c = \theta_{dts}$
- $\theta_{dts} = \theta_d + \theta_{ds} + \theta_t + \theta_{ts}$: Average driver skill + Driver's seasonal form + constructor's average advantage + constructor's seasonal form

$$
\begin{align*}

\end{align*}
$$
