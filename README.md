# Asteroids Project

## Done

- Asteroid explosions with randomized shrapnel in all directions
- Basic score tracking (prints on death)
- Basic sound effect as a proof of concept
- Added asteroid-on-asteroid bounce (no mass/size physics)
- Fixed asteroid split offset


## TODO

- [ ] Find better sounds.. (spamable for shots) or edit current one
- [ ] Implement non-circular hitboxes
- [ ] Fix collisions to use proper hitboxes
- [ ] Spawn "shot" at front of ship rather than center
- [ ] Randomize asteroid base speed and add speed on bounce?
- [ ] Make Asteroid bounce radius dependent (faking mass)
- [ ] Test asteroid bounce with collision thrown in

## Plans

Future feature ideas:

### Prio 1

- add screen wrap for player & shots
- add 2 player mode (arrow + right shift?)
  - use subclass and overwrite control function
  - Control via command flags (e.g. -2p) (or menu later on?)
  - add bounce for player-on-player (non damage-collision/ toggle?)
- add HUD to track score (+ upgrades later on)
- sound/music?
  - free sources?

### Menu/screens

- game over screen
- add score board (post game entry?)
  - load file/store in file?
  - top10? Separate 2p tracking?
- add an ingame menu
- add pause/menu (esc?)

### Graphics

- add background
  - sprite or programmatically created?
  - parallax?
  - make color subtle  
- add asteroid sprite graphics (license? make myself?)
  - random rotation speed/direction
  - sprite atlas to draw randomly from? just scale one?
  - ALT: try programmatically created shapes.
    - how to add multiple shapes to one entity? (Like small craters on the asteroids)

### Player features

- add acceleration (player) (also missile if added as weapon)
  - try with strafing controls (q/e)
- add life (max 3?) / respawn mechanic or short invul?
- add invulnerable frames & dmg to asteroid on ship collision?
- triangular hitbox for player
- collectable upgrades?
  - add drops (+life, fire rate, ..?)
for ship on asteroid collision)
- other power ups (e.g. laser weapon for x seconds, invulnerability-shield, …) sprites/on-screen effects for this?

## Reminder

try using the debugger

## Attribution

Sound Effect by [Universfield](https://pixabay.com/users/universfield-28281460/) from [Pixabay](https://pixabay.com/)
