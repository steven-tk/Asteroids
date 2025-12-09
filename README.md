# Asteroids Project

Project uses [pygame](https://www.pygame.org/) build with [UV](https://docs.astral.sh/uv/) and [Mise](https://mise.jdx.dev/mise-cookbook/python.html#mise-uv).

---

Controls:

- W/A/S/D to move
- SPACE to shoot
- P to pause/unpause

Main.py has a few things you can turn on/off via boolean (e.g asteroid bouncing, invulnerability, ..).

## Changelog

- Improvement: Colors tweaks
- Added: Pause key (p)
- Improved: Music queue with randomized playback (except the opening song)
- Added: Music loading and playback (proof of concept)
- Added: Audio-manager and changed how sound is handled
- Improved: Bounce physics now uses mass (toggle for planar vs volumetric)
- Added: Mass for physic calculations
- Improved: Scoring based on size (med/big = 2, small = 1)
- Added: Asteroid destruction sound (placeholder?)
- Improved: Randomized shot sound (less monotonous) with new sounds
- Fixed: Bullet spawn location (in front instead of inside player)
- Fixed: Asteroid splitting correctly with offset (instead of overlapping)
- Added: Asteroid-on-asteroid bounce (no mass/size physics yet)
- Added: Basic sound effect as a proof of concept
- Added: Basic score tracking (prints on death)
- Added: Asteroid explosions with randomized shrapnel in all direction
- Added: Rectangle class
- Initial prototype based off of a [boot.dev](boot.dev) project

## TODO

- [ ] Boolean for bounce calculation type (planar vs volumetric)
- [ ] High-score tracking (via file?)
- [ ] Implement cli flags to control settings (invulnerability, logging, bounce on/off, ...)
- [ ] Find better sounds..
- [ ] Implement non-circular hitboxes
- [ ] Fix collisions to use proper hitboxes for player

## Plans

Future feature ideas:

### Prio

- add screen wrap for player & shots
- add 2 player mode (arrow + right shift?)
  - use subclass and overwrite control function
  - Control via command flags (e.g. -2p) (or menu later on?)
  - add bounce for player-on-player (non damage-collision/ toggle?)
- add HUD to track score (+ upgrades later on)
- add progressive difficulty in some way (faster spawns...?)

### Menu/screens

- game over screen
- add score board (post game entry?)
  - load file/store in file?
  - top10? Separate 2p tracking?
- add an ingame menu

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

Sound Effect by

- [RescopicSound](https://pixabay.com/users/rescopicsound-45188866/) from [Pixabay](https://pixabay.com/)

Music by

- [5 Chiptunes (Action)](https://opengameart.org/content/5-chiptunes-action) by [Juhani Junkala](https://www.youtube.com/watch?v=dbACpSy9FWY) from [OpenGameArt](https://opengameart.org/) under [Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
