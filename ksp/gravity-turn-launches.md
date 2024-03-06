---
permalink: /gravity-turns
layout: default
---
# Vessel Launch (Gravity Turns)
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
   Higher values make G-Forces so high, your Kerbals will pass out during launch - lower values will make the ship take too long to achieve escape velocity. Tune the lower stage engines Thrust Limiters to get within this range.

2. Launch prograde at full throttle, aiming straight upwards.

3. When craft has reached a considerable Vertical Speed (**vy**), at roughly 100m/s, start turning East, following the 90º line in the NavBall.
   Aim for a 2º inclination at around ~ 1000m of altitude.

4. Continue with gentle, but steady inclination input changes making the prograde indicator border chase the vessel direction marker.  
   Aim for a 45º orientation at 10km of altitude (half way through the blue part of the NavBall).

5. Hold the vessel direction marker at 45º and let the prograde indicator drift away until time to Apoapsis is within 35 ~ 55s. Diminish throttle as required, because Delta-V rises as the dry mass vs wet mass ratio goes higher (empty fuel tanks vs fully full tanks mass).  
Also, once in vacuum above the 70km mark, higher TWRs are no longer required. Therefore, a lower rate/speed of ascension will "flatten" the launch trajectory parabola, making it more efficient to attain a round orbit later.  
The aim at this point is to let the craft gain enough altitude to reach orbit. When Apoapsis is roughly a minute or so away, craft should be way above the 30km mark.

6. Once far enough from Apoapis, nudge the inclination controls and allow the vessel's direction marker to follow the prograde marker gently.  
It should eventually follow very closely or slightly underneath the 90º inclination.

7. As soon as Apoapsis has reached desired orbit parking altitude (e.g. 80, 100 or 120km) cutoff throttle immediately. Allow vessel to coast.

At this point, you have successfully launched using a gravity turn. There should be plenty of time to Apoapsis, and enough fuel in the circularization stage to perform a prograde burn at Apoapsis to raise the flight path Periapsis to the same altitude, thus obtaining a circular orbit. This usually depends on how well you have executed previous manoeuvres and you current flight trajectory (how "flattened" it is), but usually around 30s to Apoapsis is a good start. Control throttle as to try to keep Apoapsis in teh defined spot.    

The same steps in a visual form can be seen here:
![Kerbin Gravity Turn][kerbin-gravity-turn]

[kerbin-gravity-turn]: images/gravity-turn-graph.png
[ker-mod]: https://github.com/jrbudda/KerbalEngineer
[orbit-circularization]: images/orbit-circularization-lko.png
[ckan-site]: https://forum.kerbalspaceprogram.com/topic/154922-ckan-the-comprehensive-kerbal-archive-network-v1280-dyson/
[delta-v-map]: images/ksp1-delta-v-map-dark.jpg