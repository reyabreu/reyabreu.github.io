---
permalink: /ksp-glossary
layout: default
---

# Glossary

Assume that most terms and definitions explained here are used in **real** space travel, not just in-game jargon. 

* **Ablator**: Non regenerative material used to cover heat shields. It is consumed when a craft uses atmospheric aerobraking to decelerate during landing, and allows for high heat dissipation so the craft doesn't burn. The amount adds to vessel mass, thus impacting Delta-V. Heat shields have a limited amount of it and maximum tolerances for the heat they are able to dissipate effectively. Typically necessary for command modules atmospheric re-entry at high Delta-V values.

* **Apoapsis (Ap)**: Farthest/Highest point in an orbit around a celestial body (lowest speed). If raised enough (and if travel direction is the same as rotation for the body), the speed will eventually match the rotational speed becoming stationary to an observer on the body. Higher values will eventually go beyond the body's SOI. 

![Orbital Apoapsis and Periapsis][orbit-ap-and-pe]

* **ASL** (At Sea Level): In contrast to Vacuum, or Atmospheric. An indication of altitude/pressure where a given engine operation is relevant.

* **Command Module** (cockpit, command pod, or probe core): is any part that allow a player to control a vessel, either a crewed capsule or an un-staffed telemetry part.

* **CommNet**: Relay and control communication system that can be enabled as a difficulty setting, and limits the operational range of antennae within the game. 

* **Delta-V**: Change in speed (m/s) gained by a vessel through the conservation of momentum effect when it expels part of its mass - usually by burning fuel.
  The most important in-game currency, it is a function of current vessel's mass and gravity influences, amongst other parameters. More info [here][delta-v-guide].

* **Escape Velocity**: Space Travel is mostly dependent of speed. This is the velocity at which a vessel will be able to leave a celestial body's atmosphere. In Kerbin it is 3431.03 m/s.

* **ISP** (Specific Impulse):  A measure of the efficiency of an engine - amount of thrust per unit of fuel. The higher the number, the better. Changes with altitude/atmosphere.

* **Keostationary Orbit** (Kerbisynchronous Equatorial Orbit or KEO for short): The stationary orbit of Kerbin, very useful orbit for satellites.  
  A spacecraft on this orbit will appear stationary when viewed from the surface. Can be useful when establishing a wireless connection between the craft and a structure on the surface, but it also makes observation of a certain spot on the surface easy. To achieve this orbit, the craft must have:
```  
   Semi-Major Axis 3 463 333.52 m
   Orbital Altitude 2 863 333.52 m
   Orbital Speed 1 009.81 m/s
   Orbital Period 1 Kerbin Sidereal Day (5h 59m 9.425s)
```

* **Kerbin**: The planet where the home base of the game is established, much smaller yet very similar to Earth, having similar gravity, temperature and atmospheric composition and pressure, with a lower atmospheric boundary. It is mostly uninhabited except for a few sparsely placed Space Centres and launch sites.

* **Kerbals**: the little green and comedic inhabitants of Kerbin, mostly there to provide immersion and motivation for the players, with very little backstory.

* **KSC (Kerbin Space Centre)**: The initial AeroSpace Centre for mission design and control with facilities for Craft building, crew management and tracking amongst others.   

* **Monopropellant**: Special kind of liquid fuel that does not require Oxidizer and is used for low power thrusters used in precision movements, such as the **RCS**. 

* **Oxidizer**: In Rocketry, is a substance that when combined with liquid fuel (a _Reducing_ agent) in a _bipropellant_ engine chamber, produces a violent **_Redox_** combustion, releasing hugh volumes of gases at high pressure and temperature. These gases, when guided trough the engine's nozzle, generate an opposing force that propel the Rocket. The reaction can happen in the absence of surrounding Oxygen, therefore making it useful for space travel.    

* **Periapsis (Pe)**: Closest/Lowest point in an orbit around a celestial body (highest speed). If the body has atmosphere, lower values may fall within it, provoking further deceleration through aerobraking. The Oberth manoeuver is optimal at the lowest Periapsis for a given body, as it will provide inordinate amounts of Delta-V.    

* **TWR** (Trust To Weight Ratio): An indication of the power of a craft's engines in relation to its own weight. It changes in relation to altitude/pressure conditions.
  For Kerbin's launch stages, a targeted TWR of 1.33 to 1.5 is desirable to avoid excessive G-Forces.

* **LKO** (Lower Kerbin Orbit): Any orbit in Kerbin within the 70km and 200km mark. Most operational manuevers happen here.

* **SAS**: Stability Augmentation System, a form pf automated flight control assistance that allows for easier piloting of a vessel. When enabled (and depending of the capabilities of the chosen command module) it can adjust vessel flight inputs automatically, so the craft maintain a chosen attitude. 

* **SOI** (Sphere of Influence): indicates the spherical space around a celestial body in which it has sole gravitational influence on a craft or any other object.
  The dev team chose to simplify effects to a single body at a given point for feasible in-game path calculations instead of n-body influence experienced in the real world. Even despite the exact solvability of all path equations, calculating them in-game gives unexpectedly changing and struggling trajectories.

* **Aerobraking**: Usage of a celestial body's atmosphere to reduce vessel entry speed, either through the use of parachutes or surfaces, by creating drag resistance.

* **Rendezvous**: The design of a close encounter solution between two separate celestial objects traveling at different orbits.

* **Docking**: The set of maneuvers required after a rendezvous to enable the attachment of separate vessels through specialized _Docking ports_ as to become a single craft.

[ckan-site]: https://forum.kerbalspaceprogram.com/topic/154922-ckan-the-comprehensive-kerbal-archive-network-v1280-dyson/
[delta-v-map]: images/ksp1-delta-v-map-dark.jpg
[kerbin-gravity-turn]: images/gravity-turn-graph.png
[delta-v-guide]: https://www.reddit.com/r/KerbalAcademy/comments/hagbmv/a_complete_guide_to_deltav/
[ker-mod]: https://github.com/jrbudda/KerbalEngineer
[transfer-tool]: https://ksp.olex.biz/
[launch-planner]: https://alexmoon.github.io/ksp/
[reyabreu-flag]: images/Flags/reyabreu-flag.png
[orbit-circularization]: images/orbit-circularization-lko.png
[orbit-ap-and-pe]: images/orbit-ap-and-pe.png
[comms-selector-file]: files/KSP%20CommNet%20Signal%20Strength%20Calculator%20%26%20Antenna%20Selector.xlsx