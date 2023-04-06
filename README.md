# blubblub

An app for the [MCH2022 Badge](https://badge.team/docs/badges/mch2022/) to be used in a swimming pool to keep tracking of your training.

## Installation

1. Get the mch2022-tools repository:

```
git clone https://github.com/badgeteam/mch2022-tools
```

2. Get your python environment set up:

```
python3 -m venv venv
venv/bin/pip install pyusb
```

3. Connect the badge and turn it on

4. Perform OS update (configure wifi in settings, then update OS)

5. Create the app directory:

```
venv/bin/python mch2022-tools/fsoverbus/webusb_fat_mkdir.py /flash/apps/python/blub/ 
```

5. Upload the app:

```
venv/bin/python mch2022-tools/fsoverbus/webusb_fat_push.py __init__.py /flash/apps/python/blub/__init__.py
```

## Usage

1. Power on the badge

2. Go to "apps", then "blub"

3. Select mode by pressing home

### Up

Timer counts up

* B = start/pause
* A = reset

### Down

Timer counts down

* B = start/pause
* A = reset
* Menu = increase minutes
* Select = decrease minutes
* Start = decrease seconds

Leds:

* Red: now <= 0 seconds remaining
* Orange/Yellow: now < 20 seconds remaining
* Green: now < 40 seconds remaining
* Blue: now < 60 seconds remaining

### Target

Led colors depend on the target time per 100m

* B = start/pause
* A = reset
* Menu = increase seconds
* Select = decrease seconds

Leds change color based on the timing per 50m (so turning point at the badge):

Leds:

* Green = now > calculated turning time - 3 seconds
* Orange/Yellow: now > calculated turning time + 15 seconds
* Red: now > calculated turning time + 30 seconds


### Target 3

Led colors depend on the target time per 100m

* B = start/pause
* A = reset
* Menu = increase seconds
* Select = decrease seconds

Leds change color based on the timing per 50m (so turning point at the badge), for three different speeds:

* Green led = target time speed
* Orange/Yellow led = target time speed + 10 seconds (per 100m)
* Red led = target time speed + 20 seconds (per 100m)

Leds turn on:

* Green led: green target time - 3 seconds < now < green target_time + 7 seconds
* Orange/Yellow led: orange/yellow target time + 1 seconds < now < orange/yellow target_time + 11 seconds
* Red led: red target time + 5 seconds < now < red target_time + 15 seconds
