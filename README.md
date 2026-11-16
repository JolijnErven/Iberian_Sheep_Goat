**SLiM 5 Modelling of Iberian Goat Demographic History**

This repository contains the SLiM 5 scripts used in the study Mediterranean dispersal imposed bottlenecks in Neolithic sheep and goats (DOI: 10.64898/2026.07.21.739115).

The simulations model the demographic history of domestic goats (Capra hircus), focusing on their dispersal into the Iberian Peninsula and the associated population bottleneck. They investigate how dispersal and subsequent demographic changes influenced genetic diversity and genomic variation.
**
Model**

The forward simulations are implemented in SLiM 5 and adapted from the SimHumanity framework (DOI: 10.1093/molbev/msaf313). The model includes:

-A model of ancestral goat population and dispersal into Iberia.
-A dispersal-associated population bottleneck.
-A nucleotide-based mutation model using Jukes–Cantor.
-The assumed mutation rate is (4.32 \times 10^{-9}) mutations per site per generation.

Model limitations: This is a deliberately simple demographic model intended as an initial exploration of the effects of dispersal-associated bottlenecks. More complex demographic scenarios, incorporating additional population structure, migration, and variation in demographic parameters, should be tested to assess the robustness of the results.

**Requirements**

SLiM 5
Python3.8 - tskit + pyslim


**References**

Mediterranean dispersal imposed bottlenecks in Neolithic sheep and goats. DOI: 10.64898/2026.07.21.739115

SimHumanity framework. Molecular Biology and Evolution (2025). DOI: 10.1093/molbev/msaf313
