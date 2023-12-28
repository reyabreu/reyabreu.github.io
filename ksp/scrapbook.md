# KSP Scrapbook
##### Thoughts and notes about Kerbal Space Program

### Vessel Launch (Gravity Turns)
As shown by [Delta-V maps][delta-v-map], the estimated amount of Delta-V required by a vessel to reach a stable circular orbit around Kerbin at an altitude of 100km, stands at around 3400m/s (3431.03 m/s is the Escape Velocity).  
Please note that Kerbin's upper atmosphere ends at 70km, after which it is considered "space" by KSP in this celestial body. Other celestial bodies with atmospheres (such as Duna) have different limits. Most interplanetary maneuvres are made 
at orbits around 80, 100 or 120km at the most. As lower orbits are faster, to take advantage of the Oberth effect, it is advised to launch from the lowest orbit possible for a given vessel's **TWR**(Trust To Weight Ratio).  

To be able to efficently use the vessel's fuel in reaching orbit, a vessel maneouvre called **Gravity Turn** is performed that takes uses the celestial body's rotation to assist additional Delta-V to the launched craft.  

In summary, if a craft is launched following the celestial body rotation (East in the case of Kerbin, following the 90º line in the NavBall), the body provides additional mommentum, a slingshot effect that supplies Delta-V
to the vessel, thus reducing total fuel consumption. Most booster designs and launch architectures are thought considering a properly executed Gravity Turn in mind - if ignored, there's a risk the vessel may not even reach orbit as most fuel will be consumed reaching the upper atmosphere. 

Obviously, we assume a craft with reasonable pitch/yaw/roll control on its lower stages is used and an acceptable degree of navigational stability. Kerbal Engineer Redux mod is recommended, so Orbital Periapsis and
Periapsis can be quickly consulted at a glance.

#### Steps
The general steps for a Gravity Turn from an equatorial launch site (assuming from Kerbin's KSC) are as follows:
1. Verify the **TWR** for the lower stages **ASL**(At Sea Level) is between 1.33~1.35  
   Higher values make G-Forces so high, your Kerbals will pass out during launch - lower values will make the ship take too long to achieve escape velocity. Tune the lower stage engines Thrust Limiters to get within this range 
2. Launch prograde at full throttle, aiming straight up
3. When craft has reached a considerable Vertical Speed (**vy**), at roughly 100m/s, start turning East, following the 90º line in the NavBall.
   Aim for a 2º inclination at around ~1200m of altitude
4. Continue with gentle, but steady inclination input changes making the prograde indicator border chase the vessel direction marker.  
   Aim for a 45º orientation at 10km of altitude (half way through the blue part of the NavBall)
5. Hold the vessel direction marker at 45º and let the prograde indicator drift away until time to Apoapsis is within 35~55s.  
   The aim at this point is to let the craft gain enough altitude to reach orbit. when Apoapsis is roughly a minute or so away, craft should be above the 30km mark
6. Allow the vessel's diection marker to follow the prograde marker.
   It should eventually follow very closely to the 90º inclination.
7. As soon as Apoapsis has reached desired orbit parking altitude (e.g. 80, 100 or 120km) cutoff throttle immediately. Allow vessel to coast.

At this point, you have succesfully launched using a gravity turn. There should be plenty of time to Apoapsis, and enough fuel in the circularization stage to perform a prograde burn at Apoapsis to raise the flight path Periapsis to the same altitude, thus obtaining a circular orbit.

The sames steps in a visual form can be seen here:
![Kerbin Gravity Turn][kerbin-gravity-turn]

[delta-v-map]: images/ksp1%20delta-v%20map.jpg
[kerbin-gravity-turn] : images/Untitled%2D2023%2D12%2D27%2D1334.png
