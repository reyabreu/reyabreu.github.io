---
permalink: /vessel-design
layout: default
---
# Vessel Design Tips
Vessels can be classified according to function. Ship, Probe, Station, Booster, etc. Before designing a craft for a mission, refer to the [Delta-V map][delta-v-map] as to calculate how much Delta-V is required.
An interplanetary mission from Kerbin will typically use a three stage architecture: 

1. Booster (or launch) stage(s) with high Thrust **ASL** engines. These engines usually have abysmal **ISP**, specially in Vacuum. Aim for providing the initial ~ 3000m/s required to reach space vacuum.

2. Circularization stage with enough Delta-V to circularize at **LKO**. Consider a strategy to dispose adequately of used stages, either by remote guidance telemetry or retrograde burns to deorbit - as to avoid orbital debris.

3. Interplanetary travel stage, using a high Vacuum ISP that will allow to reach to and from desired celestial body orbits (in the vanilla game, Atomic engines offer the highest ISP with very low TWR, requiring several to be clustered and potentially multi-stage burns for longer trajectories).

4. In case of landing on a remote celestial body, an additional lander stage _can_ be added in cooperation with the previous stage, potentially with aerobraking features if the body has an atmosphere.

The lander stage can be designed to have the **Delta-V** requirements for takeoff and landing on the remote celestial body only - using e.g. aerobraking to conserve fuel, in addition to landing gear for stability and touchdown dampening. 
Many vessels use he style of e.g. Apollo separate Lander and Orbiter where upon reaching the body's orbit, they are separated. The Orbiter stage remains "parked" at an appropriate circular equatorial orbit and the lander does the descent. Upon return, Rendezvous and Docking manoeuver are executed by the Lander as to reunite crew and any other objects/science/sample items. The reassembled craft makes its return to Kerbin.

Some celestial bodies with very small **SOI** and low gravities don't even require a lander stage e.g. Minmus and Gilly. In the case of Gilly, not even landing gear is necessary, as the vessel can reorient itself for takeoff using strong enough reaction wheels.
