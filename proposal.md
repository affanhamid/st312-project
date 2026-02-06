ST312 Proposal
Candidate Numbers: 60276, 61881

Title: Understanding Performance Dynamics in Modern Formula 1

Topic: Analysing the relationship between qualifying performance and race outcomes, intra-team competitive dynamics, and strategic tyre management using data from 2018 to 2024 from the datasource FastF1. 

Research Question 1: Qualifying-Race Performance Correlation
“What is the relationship between qualifying session performance metrics and final race standings across different circuits, seasons, and regulatory eras?”
1a) Does the qualifying-race relationship change depending on the context of circuit type and overtaking difficulty?
1b) Do the regulations affecting overtaking introduced in 2022 affect the qualifying-race correlation?
Research Question 2: Intra-Team Performance Dynamics
“Does statistical evidence from lap times, pit stop timing, and tyre allocation indicate systematic performance differences between teammates within Formula 1 teams?”
Research Question 3*: Tyre Strategy Optimisation
“How do tyre compound choices, degradation patterns, and pit stop timing affect race performance across different circuit characteristics and driver profiles?”
* We may choose to remove research question 3 or alter it and add sub-questions to q1 and q2 based on the data and the results we find, if the topic is becoming too large and unmanageable

General Background & Context:

Data:
Formula 1 represents one of the most data-rich environments in modern sport, with cars generating 50-100 measurements per second during race weekends. FastF1 (https://docs.fastf1.dev/) is a very comprehensive dataset and easily accessible, which is why we chose it. It uses official FIA (Fédération Internationale de l'Automobile) data from FIA timing transponders on each car, which are broadcast in real-time and then archived in the FastF1 database, which lends credibility to the accuracy of the data. The data is also very granular, as it is collected for each completed lap for each driver in each practice, qualifying, and final race. For its sampling frame, it has info on all F1 races from 2018 to the current time, however for consistency purposes we only intend to use the data from 2018-2024. Each year has 24 final races, though due to COVID, 2020 only had 17, and each race has 20 drivers (2 drivers for each of the 10 teams), about 50-70 laps per race depending on the circuit length, which means for rough calculations, 7 years x 24 races x 20 drivers x 60 laps = 201,600 lap observations or data points. This doesn’t include the practice or qualifiers (for each final race, three qualifying races are conducted from which the five slowest drivers are knocked out in each qualifying round), even though data is collected for those as well. This means that there is a lot of data for analysis, even though we may have to discount some data due to crashes, disqualifications, or sensor failures, etc. 
Key data available:
Lap timing: LapTime, Sector1/2/3 times, TrackStatus flags, personal bests
Car telemetry: Speed, Throttle (0-100%), Brake (boolean), nGear, RPM, DRS
Tyre data: Compound (SOFT/MEDIUM/HARD/INTERMEDIATE/WET), TyreLife, FreshTyre flag
Position data: X/Y coordinates, can be used for spatial analysis
Weather: Temperature, humidity, wind conditions per session
	The specific data we intend to use for each question will be detailed out in the “our approach” section. 

Research Importance:
Our research addresses fundamental questions in F1 strategy and performance analysis such as:
Team Resource Allocation
To understand the qualifying-race correlation, which can inform how teams balance qualifying and final race development priorities.
Qualifying determines grid position which is widely believed to be the strongest predictor of race results. 
Understanding this relationship helps teams decide resource allocation between qualifying and final race setups. 
Strategically, if correlation is extremely strong, teams should prioritise qualifying pace however, if weaker, race strategies become more important.
Competitive Fairness: 
To examine within-team dynamics to provide evidence for whether systematic favouritism exists in resource allocation between teammates.
F1 teams field two drivers but have limited resources (wind tunnel time, simulation hours, upgrade parts). Public perception exists that teams favour championship contenders over supporting drivers.
To figure out if observed performance between teammates differs due to driver skill or systematic resource allocation?
Strategic Optimisation: 
To analyse the tyre strategy effects for which optimal decision-making frameworks for one of the few variables teams can control during races, unlike car performance or driver skill.
Different tyre compounds (C1-C5, soft/medium/hard) have trade-offs: softer compounds are faster but degrade quickly.
Given circuit characteristics and driver style, which tyre strategy minimises race time?
Target Audience:
F1 Teams: Our research can potentially provide strategic insights for resource allocation and race strategy optimisation by backing up claims quantifiably.
Academic Researchers: By using real telemetry data, we could create empirical validation of game-theoretic strategy models that other researchers can utilise.
Sports Analytics Community: Similar to researchers, we create methodological contributions in multilevel modelling for motorsports.
Regulatory Bodies: We showcase an evidence-based assessment of competitive balance and team dynamics, which could highlight some gaps in regulations that should be enforced.
Fans: As F1 fans ourselves, we’re curious on what the data will reveal. Particularly for the intra-team dynamics, there have been many rumours about teams focusing on one team member over the other and even purposely sabotaging the other member however, this is always denied by the leaders and no empirical evidence has come out. So by analysing it, we can satiate some of our own curiosities or even help other fans better understand different strategies within the system to make them well-informed viewers.

Literature Review

Research Question 1: Qualifying-Race Performance Correlation
The relationship between qualifying and race performance has been studied historically by Mühlbauer (2010), who analysed pre-2008 qualifying formats and established the foundational understanding of this correlation. More recently, Weissbock and Mills (2025) conducted a comprehensive analysis examining 7,800 driver-weekends from 2006-2023 and found a contingency coefficient of C = 0.741 and Spearman correlation of ρ = 0.763 between qualifying and race positions, demonstrating a strong positive association.
Their research revealed that the qualifying position accounts for 0.375 of total feature importance in predicting race outcomes and is approximately four times more predictive than practice session performance (Weissbock & Mills, 2025). When examining different technical eras, the turbo-hybrid era (2014-2022) showed the strongest correlation at C = 0.756, with pole position converting to victory in 42-60% of races (Weissbock & Mills, 2025). These findings reinforce the strategic emphasis teams place on qualifying performance as the primary determinant of race success.
However, no existing study examines the 2022-2024 ground effect regulations or provides circuit-specific correlation analysis, representing a significant gap that our research will potentially address.

Research Question 2: Intra-Team Performance Dynamics
Statistical analysis of Formula 1 performance has primarily focused on separating driver skill from car performance across teams rather than within teams. Van Kesteren and Bergkamp (2023) used rank-ordered logit regression and found that approximately 88% of performance variance comes from the constructor while only 12% is attributable to driver skill. This finding aligns closely with Bell et al. (2016), who applied cross-classified multilevel models to 64 years of historical data and obtained a similar 86%/14% car-driver split.
Beyond variance decomposition, Henderson and Kirrane (2018) developed Plackett-Luce ranking models for probabilistic forecasting of race outcomes, while Phillips (2014) used dummy variable regression to produce comprehensive driver rankings. Eichenberger and Stadelmann (2009) developed an econometric framework specifically designed to separate driver performance from equipment quality.
However, none of these studies examine within-team performance differences or investigate whether teams systematically allocate resources differently between teammates—for instance, through pit stop timing advantages or tyre allocation patterns. So to contribute some novelty to this concept, our analysis will use lap-by-lap telemetry data and a detailed pit stop timing analysis.

Research Question 3: Tyre Strategy Optimisation
Research on tyre strategy has primarily focused on optimisation through game theory and machine learning prediction rather than empirical causal analysis of actual race data. Aguad and Thraves (2024) used game-theoretic modelling to show that optimised pit stop timing can improve race times by approximately 2.3 seconds and reduce undercut probability by 17.8%, demonstrating the strategic value of optimal timing decisions.
Recent machine learning applications have increasingly leveraged the FastF1 dataset for prediction tasks. Sasikumar et al. (2025) trained Bi-LSTM networks on 99,928 laps from 2020-2024 to predict pit stop timing with an F1-score of 0.81, while a Tilburg University thesis (2024) used LSTM networks for lap time prediction on 136,122 laps. Thomas et al. (2025) collaborated with Mercedes-AMG Petronas to develop reinforcement learning algorithms for race strategy optimisation, achieving improved average finishing positions compared to baseline strategies.
However, most existing analyses rely on aggregate race results or focus on prediction accuracy rather than causal inference about strategy effects. The 2023-2024 ground effect era remains largely unstudied, and no research has systematically examined how different driving styles affect optimal tyre management strategies or estimated driver-specific degradation rates using empirical telemetry data, representing key gaps our project will address.

	So even though F1 is a subject that is commonly explored in statistical analyses, by using a different dataset and altering our approaches, there is no exact replication of any previous studies, though we add to some. This means that some of our results will be really novel, while others may be reinforced by existing literature. 
	
Our Planned Approach
	This is the approach we have planned so far, broken down for each question. However, it is entirely possible that once we start investigating the data further and on a deeper level, some other natural questions may emerge or we may realise some other model or stats analysis is better suited, so we’re allowing space for flexibility and adaptability in our approach. 

Research Question 1: Qualifying-Race Performance Correlation
We will use ordinal logistic regression with a multilevel structure to examine the relationship between qualifying position and race finishing position. This approach makes sense because race positions are ordered categories (1st, 2nd, 3rd, etc.) rather than continuous numbers. We will include random effects for drivers and teams to account for the fact that we have multiple observations from the same drivers and teams over the seasons.
We will also calculate Spearman rank correlations broken down by year, circuit type, and grid position. This will let us see if the qualifying-race relationship changes depending on context. For circuit types, we'll group tracks into street circuits (like Monaco and Singapore), high-speed circuits (like Monza and Spa), and technical circuits (like Barcelona and Suzuka) to test whether overtaking difficulty affects the correlation.
If our hypothesis is correct, we expect strong correlations of at least 0.70 overall, but with differences between circuits. For example, Monaco should show stronger correlations (around 0.85) because overtaking is nearly impossible there, while Monza might be weaker (around 0.65) because the long straights make it easier to pass. We'll also split the data into 2018-2021 and 2022-2024 periods to see if the 2022 regulation changes improved racing. If the new rules worked as intended, the qualifying-race correlation should be weaker in 2022-2024 because overtaking became easier.

Research Question 2: Intra-Team Performance Dynamics
We will use linear mixed effects models with nested and crossed random effects to look at systematic performance differences between teammates. This approach is necessary because lap times from the same driver are related to each other, teammates share the same car, and drivers race at multiple circuits throughout the season.
Our model will include random effects for drivers (to capture their baseline skill), teams (to account for car performance), and races (to control for circuit differences). The most important part is the teammate indicator coefficient, which tells us the average lap time difference between the two drivers after we account for tyre age, tyre type, track position, and which stint they're on. If this coefficient is significantly different from zero, it suggests one driver is systematically faster for reasons beyond just skill.
We'll also do paired t-tests comparing pit stop times between teammates in the same race to see if one driver consistently gets faster service. And we'll use chi-square tests to check if one driver gets fresh tyres more often in important moments. If there's favouritism, we'd expect to see lap time differences of at least 0.1 seconds between teammates even after controlling for everything else, plus one driver getting consistently faster pit stops (by 0.1-0.2 seconds) or better tyre strategies.

Research Question 3: Tyre Strategy Optimisation
We will use mixed effects models with interaction terms and random slopes to study how tyre choice and degradation relate to performance. The interaction terms between tyre life (laps on current tyres) and compound type will show us how quickly different tyres degrade—we expect soft tyres to get slower more quickly than mediums, with hards degrading slowest but being slower to start with.
The random slopes for tyre life at the driver level are important because they let us see that different drivers manage tyres differently. Some drivers are better at making tyres last through smoother driving, while others are harder on their tyres. Drivers with smaller slope coefficients would be the better tyre managers.
We'll also cluster drivers based on their driving style using telemetry data like how smoothly they use the throttle, how they brake, and their corner speeds. This will let us group drivers into categories like "aggressive" or "smooth." Then we can test if different driving styles work better with different tyre strategies—for example, maybe smooth drivers do better with longer stints on soft tyres while aggressive drivers benefit from stopping more often to always have fresh tyres.


References
Aguad, M., & Thraves, C. (2024). Game theory optimization for Formula 1 pit stop timing. European Journal of Operational Research.
Bell, A., et al. (2016). Within and between effects in Formula 1 racing. Journal of Quantitative Analysis in Sports.
Eichenberger, R., & Stadelmann, D. (2009). Who is the best Formula 1 driver? Economic Analysis and Policy.
Henderson, D., & Kirrane, R. (2018). Plackett-Luce ranking models for Formula 1. Bayesian Analysis.
Mühlbauer, T. (2010). Qualifying and race performance in Formula 1. International Journal of Performance Analysis in Sport.
Phillips, A. (2014). Uncovering Formula 1 driver performances from 1950 to 2013. Journal of Quantitative Analysis in Sports.
Sasikumar, A., et al. (2025). Deep learning for pit stop prediction using FastF1. Frontiers in Artificial Intelligence.
Thomas, S., et al. (2025). Reinforcement learning for Formula 1 race strategy. arXiv:2501.04068.
Van Kesteren, E., & Bergkamp, T. (2023). Bayesian multilevel models for Formula 1. Journal of Quantitative Analysis in Sports.
Weissbock, J., & Mills, S. (2025). Evaluating the Predictive Power of Qualifying Performance in Formula One Grand Prix. arXiv:2507.10966. https://arxiv.org/abs/2507.10966
