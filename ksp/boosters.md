---
layout: default
---
# How to create a Booster Library

## Context
Space exploration is costly business. therefore, its no surprise that one of the main goals in most modern space agencies is to develop standard (and potentially reusable) platforms for launching vehicles into well known locations.

The Saturn 5 was for many years the world's undisputed most powerful rocket, that is, until SpaceX Starship arrived on the scene. Both of these rockets main purpose is as heavy lifter booster stages.  

Typically, booster stages have enormous TWR (Trust to Weight Ratio) values; they're designed to overcome the high gravity pull and atmospheric drag of earth, and carry desired payloads to the lower orbit. They're also notoriously inefficient, the engines having low values for iSP (Specific Impulse). Boosters traditionally are discharged or separated in the first stages of flight after their fuel has been consumed, with some modern designs actually retrieving the booster stages back for refurbishing so most of the hardware can be reused in future launches. Available Delta-V on a craft is a function of mass, so discarding empty stages is essential to attain target Delta-V with efficiency. 

In KSP, booster profile engines can be found in two varieties: solid fuel (akin to a firework rocket) or liquid fuel. Usually, solid fuel boosters are used for smaller to medium sized payloads. Bi-Fuel liquid engines are preferred for heavier loads - using a strategy called "Asparagus Staging".

## Steps
The steps for creating a booster library in KSP are essentially:
1. Design a full craft for a given payload to a celestial body (Mun, Duna, Minmus, etc)
1. Identify the Booster stage(s): typically the sections of the vessel that provide roughly 3600m/s of Delta-V (Vac) fr the initial lift-off
1. Separate temporarily the booster on its last separator from the main payload, and use the engineer report to estimate the payload mass     
1. Re-root the craft, so the last separator for the booster stage becomes the new root part.
1. Replace the main payload with heavy parts that do not contribute to Delta-V (no engines or fuel cross feed) and stop when the craft is providing 3600 m/s (vac).
1. Use the engineer report again to find the effective mass of payload. Save the booster as a sub-assembly with a description including the payload mass.