# Asteroids Project

Project uses [pygame](https://www.pygame.org/) build with [UV](https://docs.astral.sh/uv/) and [Mise](https://mise.jdx.dev/mise-cookbook/python.html#mise-uv).

---

## How to play

### Install

[Install](https://mise.jdx.dev) mise if you don't have it and optionally [activate](https://mise.jdx.dev/getting-started.html#activate-mise) it.

Use `mise run` & confirm with enter to start.

Should now automatically download the correct pygame, python & uv version on your first start.

### Controls

- W/A/S/D to move
- SPACE to shoot
- P to pause/unpause

### Other

Main.py has a few things you can turn on/off via boolean (e.g asteroid bouncing, invulnerability, ...).

If you want a custom Player name for your scores: change it in constants.py (for now).

---

## Changelog

- 14 Dec 2025
  - Added: Out-of bounds handling for player (only for the player!)
    - screen wrap freely (default behavior)
    - take -1 life penalty & respawn in center (invulnerability timer) (main.py boolean set to True)
  - Improved: Refactored handling of score, lives, teleport and game over condition
- 14 Dec 2025
  - Improved: New post game display of score & current high scores in console
  - Added: High-Score tracking via .json
  - Added: ScoreManager
  - Fixes: improper quitting on game over
- forgot to add dates earlier
  - Added: Boolean for planar vs volumetric mass (bounce physics)
  - Added: Savezone in center - cleared of asteroids if respawning
  - Added: 3 lives, upon hit: respawn in center (1sec invulnerability)
  - Improvement: Colors tweaks
  - Added: Pause key (p)
  - Improved: Music queue with randomized playback (except the opening song)
  - Added: Music loading and playback (proof of concept)
  - Added: Audio-manager and changed how sound is handled
  - Improved: Bounce physics now uses mass (pick between planar vs volumetric)
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

## Current TODOs

- [ ] rework file structure and add directories
- [ ] Try increasing spawn rate by current score (multiplier for every XX score?)
- [ ] Add HUD
- [ ] Display current score
- [ ] Display High Score during pause
- [ ] Implement cli flags to control settings (invulnerability, logging, bounce on/off, ...)
- [ ] Find better sounds..?

## Future feature ideas

### General

- add 2 player mode (arrow + right shift?)
  - use subclass and overwrite control function
  - Control via command flags (e.g. -2p) (or menu later on?)
  - add bounce for player-on-player (non damage-collision/ toggle?)
- add HUD to track score (+ upgrades later on)
- add progressive difficulty in some way (faster spawns...?)
- Player flashing during invulnerability timer

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
- add asteroid sprite graphics (source?/license? DIY?)
  - random rotation speed/direction
  - sprite atlas to draw randomly from? just scale one?
  - ALT: try programmatically created shapes.
    - how to add multiple shapes to one entity? (Like small craters on the asteroids)

### Content features

- add acceleration (player) (also missile if added as weapon)
  - try strafing controls (q/e)
  - add inertia to player ship for balance?
- triangular hitbox for player
- collectable upgrades
  - add drops (+life, fire rate, ..?)
- other power ups (e.g. laser weapon for x seconds, invulnerability-shield, …) sprites/on-screen effects for this?

## Attribution

Sound Effect:

- [Sci-Fi Weapon - Shoot - Firing - Plasma KU 01-05 by RescopicSound](https://pixabay.com/users/rescopicsound-45188866/) from [Pixabay](https://pixabay.com/) under [Pixabay License / CCO](https://pixabay.com/service/license-summary/)

Music:

- [5 Chiptunes (Action)](https://opengameart.org/content/5-chiptunes-action) by [Juhani Junkala](https://www.youtube.com/watch?v=dbACpSy9FWY) from [OpenGameArt](https://opengameart.org/) under [Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)
