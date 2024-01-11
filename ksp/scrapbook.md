---
permalink: /ksp-scrapbook
layout: default
---
# KSP Scrapbook
##### Thoughts and notes about Kerbal Space Program

More than just a simulation game, KSP is a learning platform for Rocket Science, Orbital Mechanics and other scientific and engineering disciplines associated to flight and space exploration. It works on a simplified scaled down model of around 80% of our own solar system. Concepts in KSP are also used in the real world, and more concrete definitions and explanations can be found on aerospace agencies such as NASA or ESA.

Please note that all this material applies only to the latest versions of KSP. I have not installed/played KSP2 up to this date, so even though I believe most information is applicable, I cannot vouch for it.

This is the mission [Flag][reyabreu-flag] I use.

## Mods
I use exclusively the [CKAN][ckan-site] (Comprehensive Kerbal Archive Network) tool to download and install mods. It will ensure compatibility between mods and with the latest KSP versions. 

[Glossary][glossary]

## General Tips
* The most important tool in KSP my appreciation is the maneuver node editor. Understand it correctly, and when and how to edit it for maximum manuever effectivity.

* Although kind of unintuitive, remember that changes in speed do not make your vessel or craft transit faster at a given orbit; instead it changes the _geometry_ of the orbit, so you may find yourself at higher or lower speeds because the orbit has a different shape.

* Burning at orbital special points is optimal. E.g. burning prograde at your Apoapsis is the most efficient way to raise Periapsis. Burning in Normal or Anti-Normal direction at either the orbit's Descending or Ascending Nodes is the most efficient way to change Orbital inclination.    

* Travel to other celestial bodies requires planning and execution at appropriate times. The amount of Delta-V a vessel can carry is finite, so there are limits to the maximum range of your craft based on the efficiency and size of the design and how well maneuvers are executed. There are planning tools that allow you to determine the amount of Delta-v required for a given encounter at a specific orbit, so you can design a craft accordingly.  
To find the best dates/time for planning your missions, please refer to the tools section linked below.

* If enabling **CommNet**, Choosing the right type of communication device and antennas for space travel is also important, and there are tools for that. A **Pilot** in KSP is a role that can create/edit maneuver nodes, so if you lose communication with KSC and your vessel is not crewed by a Pilot, you may not be able to design a navigation solution with maneuver nodes, until Comms are reestablished (as in the case of traveling in the shadow of another celestial body between the craft and Kerbin). 

* Besides a **Pilot**, the other roles are **Scientist**, which allows for certain experiment resets in Science Mode, and **Engineer** which is capable of fixing malfunctioning equipment with toolkits.

## Vessel Design
Vessels can be classified according to function. Ship, Probe, Station, Booster, etc. Before designing a craft for a mission, refer to the [Delta-V map][delta-v-map] as to calculate how much Delta-V is required.
An interplanetary mission from Kerbin will typically use a three stage architecture: 

1. Booster (or launch) stage with high Thrust **ASL** engines. These engines usually have abysmal **ISP**, specially in Vacuum. Aim for providing the ~ 3000m/s required to reach space.

2. Circularization stage with enough Delta-V to circularize at **LKO**. Consider a strategy to dispose of used stages, either by remote guidance telemetry or retrograde burns to deorbit - as to avoid orbital debris.

3. Interplanetary travel stage, using a high Vacuum ISP that will allow to reach to and from desired celestial body orbits.

4. In case of landing on a remote celestial body, an additional lander stage _can_ be added in cooperation with the previous stage.

The lander stage can be designed to have the **Delta-V** requirements for takeoff and landing on the remote celestial body only - using e.g. aerobraking to conserve fuel, in addition to landing gear for stability and touchdown dampening. 
Many vessels use he style of e.g. Apollo separate Lander and Orbiter where upon reaching the body's orbit, they are separated. The Orbiter stage remains "parked" at an appropriate circular equatorial orbit and the lander does the descent. Upon return, Rendezvous and Docking manoeuver are executed by the Lander as to reunite crew and any other objects/science/sample items. The reassembled craft makes its return to Kerbin.

Some celestial bodies with very small **SOI** and low gravities don't even require a lander stage e.g. Minmus and Gilly. In the case of Gilly, not even landing gear is necessary, as the vessel can reorient itself for takeoff using strong enough reaction wheels.

## Essential Vessel Checklist before launch
* Verify the craft has a _root part_ (a **Command Module**, either a crewed capsule or an unguided telemetry part) so it can be flyable.

* Does your **Command Module** have (and need) a Heat Shield? have you added the coupling parts for stage separation? have you added means for atmospheric stability (such as fins) in your lower stages?

* Reduce weight (mass) as much as possible.  
40 units of Ablator (on Heat Shield) is enough for a Kerbin Command Module reentry at 2500m/s. Maybe 3 times as much for higher speed re-entries at inclined orbit. 600 units is an overkill. Are you using single fuel engines, such as Nuclear? - then, no oxidizer is needed. Are you using **RCS**? if the answer is no, then no need to carry monopropellant.

* Revise the Delta-V budget for different stages _ASL_ and in the _Vacuum_ of space.  
Your lower booster stages should be able to provide at least 3400m/s **ASL** to get the craft into orbit. The remaining Delta-V should be estimated with the aid of a [map][delta-v-map], including the return trip. Add some 20% to the overall budget if you're inexperienced.

* Unless you're an experienced Pilot, you may wish to add stability assisted control in the form of **SAS** to your craft for a more controlled flight.  
Please note that SAS usually is provided by the addition of **Reaction Wheels** to your vessel's stages - higher torques for heavier parts. Most **Command Modules** provide an embedded reaction wheel that is capable of handling most last stages/landers mass, but won't be useful for heavy boosters or clustered engines.

* Check your Communication capabilities. Select and add the correct antennae for your voyage, if having **CommNet** enabled.  
This [Antennae Selector][comms-selector-file] is helpful.

* If you have reaction wheels (included or not) and Antennae, its advisable to add a couple extra batteries to handle the excess electrical power drawn from these devices. Consider craft mass when adding batteries, and don't forget to add means to recharge them, e.g. Solar Panels.

* If your craft or parts of it will perform Docking maneuvers in Vacuum, its advisable to add **RCS** thrusters. They come in different sizes with low to high power respectively, from 0.1kN up to 12kN. Choose the smallest possible for the vessel, remembering to balance thrusters around the craft's centre of mass. You may consider carrying extra monopropellant in additional tanks, besides the amount included in some **Command Modules**.  
In addition, allow RCS to be used only for craft translation, by disabling the **Roll**, **Pitch** and **Yaw** control in the RCS thrusters setup (must have _Adjustable Tweakables_ enabled in the game settings), so these movements are provided by Reaction Wheels instead - no monopropellant required. 

* I suggest always rotating so the Root Part's front face is directly opposite to the launch pad.  
In other words, the whole assembly's back is facing towards the VAB door and towards the launch pad. By selecting the _Root Part_ and pressing **Q** or **E** on the keyboard, you can rotate the whole vessel assembly. This allows the 90º line on the Navball (East) to be facing down, allowing for key **W** to be used on _Gravity Turn_ launch corrections.
  
* Check your staging! verify that parts are deployed correctly in expected sequence.

* Check you have limited the thrusters **ASL** so the **TWR** for lower stages is between 1.33~1.35, to avoid excessive G-Forces.  

* Are you launching in the right Transfer Window for the celestial body you plan to encounter? Use tools such as the [Launch Window Planner][launch-planner] and warp time to reach the appropriate date and time in KSC's Tracking Station before your launch.

* Finally, verify your crew. Missions with separate docking parts may require more than one occupant, and ensure the role(s) is(are) appropriate for the chosen game style.

## Vessel Launch (Gravity Turns)
As shown by [Delta-V maps][delta-v-map], the estimated amount of Delta-V required by a vessel to reach a stable circular orbit around Kerbin at an altitude of 80km, stands at around 3400m/s (3431.03 m/s is the Escape Velocity).  
Please note that Kerbin's upper atmosphere ends at 70km, after which it is considered "space" by KSP in this celestial body. Other celestial bodies with atmospheres (such as Duna) have different limits. Most interplanetary maneuvers are made 
at orbits around 80, 100 or 120km at the most. As lower orbits are faster, to take advantage of the Oberth effect, it is advised to launch from the lowest orbit possible for a given vessel's **TWR**(Trust To Weight Ratio).  

To be able to efficiently use the vessel's fuel in reaching orbit, a vessel manoeuver called **Gravity Turn** is performed that takes uses the celestial body's rotation to assist additional Delta-V to the launched craft.  

In summary, if a craft is launched following the celestial body rotation (East in the case of Kerbin, following the 90º line in the NavBall), the body provides additional momentum, a slingshot effect that supplies Delta-V to the vessel, thus reducing total fuel consumption. Most booster designs and launch architectures are thought considering a properly executed Gravity Turn in mind - if ignored, there's a risk the vessel may not even reach orbit as most fuel will be consumed reaching the upper atmosphere. 

![Orbit circularization][orbit-circularization]

Obviously, we assume a craft with reasonable pitch/yaw/roll control on its lower stages is used and an acceptable degree of navigational stability. [Kerbal Engineer Redux][ker-mod] mod is recommended (use [CKAN][ckan-site]), so Orbital Periapsis and
Periapsis can be quickly consulted at a glance.

### Steps
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

6. Allow the vessel's direction marker to follow the prograde marker.
   It should eventually follow very closely to the 90º inclination.

7. As soon as Apoapsis has reached desired orbit parking altitude (e.g. 80, 100 or 120km) cutoff throttle immediately. Allow vessel to coast.

At this point, you have successfully launched using a gravity turn. There should be plenty of time to Apoapsis, and enough fuel in the circularization stage to perform a prograde burn at Apoapsis to raise the flight path Periapsis to the same altitude, thus obtaining a circular orbit.

The sames steps in a visual form can be seen here:
![Kerbin Gravity Turn][kerbin-gravity-turn]

## Tools
* [Launch Window Planner][launch-planner]
* [Interactive illustrated interplanetary guide and calculator for KSP][transfer-tool] 

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
[glossary]: /ksp-glossary