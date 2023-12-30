---
layout: page
title: KSP Scrapbook
permalink: ksp/scrapbook
---
##### Thoughts and notes about Kerbal Space Program

More than just a simulation game, KSP is a learning platform for Rocket Science, Orbital Mechanics and other scientific and engineering disciplines associated to flight and space exploration. It works on a simplified scaled down model of around 80% of our own solar system. Concepts in KSP are also used in the real world, and more concrete definitions and explanations can be found on aeropsace agencies such as NASA or ESA.  
Please note that all this material applies only to the latest versions of KSP. I have not installed/played KSP2 up to this date, so even though I believe most information is applicable, I cannot vouch for it.

### Mods
I use exclusively the [CKAN][ckan-site] (Comprehensive Kerbal Archive Network) tool to download and install mods. It will ensure compatibility between mods and with the latest KSP versions. 

### Glossary
* **ASL** (At Sea Level): In contrast to Vacuum, or Atmospheric. An indication of altitude/pressure where a given engine operation is relevant.
  
* **Delta-V**: Change in speed (m/s) gained by a vessel through the conservation of momentum effect when it expels part of its mass - usually by burning fuel.
  The most important in-game currency, it is a function of current vessel's mass and gravity influences, amongst other parameters. More info [here][delta-v-guide].

* **TWR** (Trust To Weight Ratio): An indication of the power of a craft's engines in relation to its own weight. It changes in relation to altitude/pressure conditions.
  For Kerbin's launch stages, a targeted TWR of 1.33 to 1.5 is desirable to avoid excessive G-Forces.

* **ISP**(Specific Impulse):  A measure of the efficiency of an engine - amount of thrust per unit of fuel. The higher the number, the better. Changes with altitude/atmosphere.

* **Escape Velocity**: Space Travel is mostly dependent of speed. This is the velocity at which a vessel will be able to leave a celestial body's atmosphere. In Kerbin it is 3431.03 m/s.

*  **LKO**(Lower Kerbin Orbit): Any orbit in Kerbin within the 70km and 200km mark. Most operational maneuovres happen here.

* Keostationary Orbit (Kerbisynchronous Equatorial Orbit or KEO for short): The stationary orbit of Kerbin, very useful orbit for satellites.  
  A spacecraft on this orbit will appear stationary when viewed from the surface. Can be useful when establishing a wireless connection between the craft and a structure on the surface, but it also makes observation of a certain spot on the surface easy. To achieve this orbit, the craft must have:
```  
   Semi-Major Axis 3 463 333.52 m
   Orbital Altitude 2 863 333.52 m
   Orbital Speed 1 009.81 m/s
   Orbital Period 1 Kerbin Sidereal Day (5h 59m 9.425s)
```
* **SOI**(Sphere of Influence): indicates the spherical space around a celestial body in which it has sole gravitational influence on a craft or any other object.
  The dev team chose to simplify effects to a single body at a given point for feasible in-game path calculations instead of n-body influence experienced in the real world. Even despite the exact solvability of all path equations, calculating them in-game gives unexpectedly changing and struggling trajectories.

* **Aerobraking**: Usage of a celestial body's atmosphere to reduce vessel entry speed, either through the use of parachutes or surfaces, by creating drag resistance.

* **Rendezvous**: The design of a close encounter solution between two spearate celestial objects travelling at different orbits.

* **Docking**: The set of manoeuvres required after a rendezvous to enable the attachment of separate vessels through specialized _Docking ports_ as to become a single craft.   

### Vessel Design
Vessels can be classified according to function. Ship, Probe, Station, Booster, etc. Before designing a craft for a mission, refer to the [Delta-V map][delta-v-map] as to calculate how much Delta-V is required.
An interplanetary mission from Kerbin will typically use a three stage architecture: 

1. Booster (or launch) stage with high Thrust **ASL** engines. These engines usually have abysmal **ISP**, specially in Vacuum. Aim for providing the ~ 3000m/s required to reach space.
2. Circularization stage with enough Delta-V to circularize at **LKO**. Consider a strategy to dispose of used stages, either by remote guidance telemetry or retrograde burns to deorbit - as to avoid orbital debris.
3. Interplanetary travel stage, using a high Vacuum ISP that will allow to reach to and from desired celestial body orbits.
4. In case of landing on a remote celestial body, an additional lander stage _can_ be added in cooperation with the previous stage.

The lander stage can be designed to have the **Delta-V** requirements for takeoff and landing on the remote celestial body only - using e.g. aerobraking to conserve fuel, in addition to landing gear for stability and touchdown dampening. 
Many vessels use he style of e.g. Apollo separate Lander and Orbiter where upon reaching the body's orbit, they are separated. The Orbiter stage remains "parked" at an appropriate circular equatorial orbit and teh lander does the descent. Upon return, Rendezvous and Docking maneouvres are executed by the Lander as to reunite crew and any other objects/science/sample items. The reassembled craft makes its return to Kerbin.

Some celestial bodies with very small **SOI** and low gravities don't even require a lander stage e.g. Minmus and Gilly. In the case of Gilly, not even landing gear is ncessary, as the vessel can reorint itself for takeoff using strong enough reaction wheels. 
  
### Vessel Launch (Gravity Turns)
As shown by [Delta-V maps][delta-v-map], the estimated amount of Delta-V required by a vessel to reach a stable circular orbit around Kerbin at an altitude of 80km, stands at around 3400m/s (3431.03 m/s is the Escape Velocity).  
Please note that Kerbin's upper atmosphere ends at 70km, after which it is considered "space" by KSP in this celestial body. Other celestial bodies with atmospheres (such as Duna) have different limits. Most interplanetary maneuvres are made 
at orbits around 80, 100 or 120km at the most. As lower orbits are faster, to take advantage of the Oberth effect, it is advised to launch from the lowest orbit possible for a given vessel's **TWR**(Trust To Weight Ratio).  

To be able to efficently use the vessel's fuel in reaching orbit, a vessel maneouvre called **Gravity Turn** is performed that takes uses the celestial body's rotation to assist additional Delta-V to the launched craft.  

In summary, if a craft is launched following the celestial body rotation (East in the case of Kerbin, following the 90º line in the NavBall), the body provides additional mommentum, a slingshot effect that supplies Delta-V
to the vessel, thus reducing total fuel consumption. Most booster designs and launch architectures are thought considering a properly executed Gravity Turn in mind - if ignored, there's a risk the vessel may not even reach orbit as most fuel will be consumed reaching the upper atmosphere. 

Obviously, we assume a craft with reasonable pitch/yaw/roll control on its lower stages is used and an acceptable degree of navigational stability. [Kerbal Engineer Redux][ker-mod] mod is recommended (use [CKAN][ckan-site]), so Orbital Periapsis and
Periapsis can be quickly consulted at a glance.

#### Steps
The general steps for a Gravity Turn from an equatorial launch site (assuming from Kerbin's KSC) are as follows:
1. Verify the **TWR** for the lower stages **ASL**(At Sea Level) is between 1.33 ~ 1.35  
   Higher values make G-Forces so high, your Kerbals will pass out during launch - lower values will make the ship take too long to achieve escape velocity. Tune the lower stage engines Thrust Limiters to get within this range 
2. Launch prograde at full throttle, aiming straight up
3. When craft has reached a considerable Vertical Speed (**vy**), at roughly 100m/s, start turning East, following the 90º line in the NavBall.
   Aim for a 2º inclination at around ~ 1000m of altitude
4. Continue with gentle, but steady inclination input changes making the prograde indicator border chase the vessel direction marker.  
   Aim for a 45º orientation at 10km of altitude (half way through the blue part of the NavBall)
5. Hold the vessel direction marker at 45º and let the prograde indicator drift away until time to Apoapsis is within 35 ~ 55s.  
   The aim at this point is to let the craft gain enough altitude to reach orbit. when Apoapsis is roughly a minute or so away, craft should be above the 30km mark
6. Allow the vessel's diection marker to follow the prograde marker.
   It should eventually follow very closely to the 90º inclination.
7. As soon as Apoapsis has reached desired orbit parking altitude (e.g. 80, 100 or 120km) cutoff throttle immediately. Allow vessel to coast.

At this point, you have succesfully launched using a gravity turn. There should be plenty of time to Apoapsis, and enough fuel in the circularization stage to perform a prograde burn at Apoapsis to raise the flight path Periapsis to the same altitude, thus obtaining a circular orbit.

The sames steps in a visual form can be seen here:
![Kerbin Gravity Turn][kerbin-gravity-turn]

### Tools
* [Launch Window Planner][launch-planner]
* [Interactive illustrated interplanetary guide and calculator for KSP][transfer-tool] 

[ckan-site]: https://forum.kerbalspaceprogram.com/topic/154922-ckan-the-comprehensive-kerbal-archive-network-v1280-dyson/
[delta-v-map]: images/ksp1%20delta-v%20map.jpg
[kerbin-gravity-turn]: images/Untitled%2D2023%2D12%2D27%2D1334.png
[delta-v-guide]: https://www.reddit.com/r/KerbalAcademy/comments/hagbmv/a_complete_guide_to_deltav/
[ker-mod]: https://github.com/jrbudda/KerbalEngineer
[transfer-tool]: https://ksp.olex.biz/
[launch-planner]: https://alexmoon.github.io/ksp/
