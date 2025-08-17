# 16883822 - Resauchamet

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 356 bytes                   |
| Total Events     | 2                           |
| References Count | 16                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [355](#event-355)     | 0x0001       |    266 |             42 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x01F1      |         497 |
|       1 | 0x2B47      |       11079 |
|       2 | 0x2B48      |       11080 |
|       3 | 0x2B49      |       11081 |
|       4 | 0x0000      |           0 |
|       5 | 0x001E      |          30 |
|       6 | 0x2B4A      |       11082 |
|       7 | 0x0001      |           1 |
|       8 | 0x01F0      |         496 |
|       9 | 0x2B4B      |       11083 |
|      10 | 0x0002      |           2 |
|      11 | 0x2B4C      |       11084 |
|      12 | 0x0003      |           3 |
|      13 | 0x2B4D      |       11085 |
|      14 | 0x003C      |          60 |
|      15 | 0x2B4E      |       11086 |

## String References

- **11079**: You are an adventurer... I can smell the dark blood of the undead as it drips slowly from your soiled garments.
- **11080**: Beware, my friend, for you are not alone in your journey. Lost spirits lurk in the shadows behind you, waiting for their chance to rob you of your soul.
- **11081**: Hmmm...
- **11082**: You still have a fairly good head start, but they will not let up until they have found you and filled your heart with poison and pain.
- **11083**: They are close... It is only a matter of time before you have fallen within their reach.
- **11084**: Can you not feel the hands that reach up from the bottomless depths of hell? Can you not feel the gaze of a thousand eyes, glowing red with anger and hate?
- **11085**: The grip of evil is tightening on the very essence of what makes you who you are. Be forewarned, as it will not be long before you are confronted with a battle for more than just your life.
- **11086**: Oh, poor child! May the light of the Dawn Goddess lead you from the pitch-black depths of darkness!

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 355

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 266 bytes |
| Instructions | 42        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  5B 00 80 F8 FF FF 7F F8   .....op[.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 5B  ...tlk0...#...#[
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 1D 03  ..........tlk1..
0030: 80 23 02 02 10 04 80 80  5F 00 5B 05 80 F8 FF FF  .#......_.[.....
0040: 7F F8 FF FF 7F 74 6C 6B  30 1D 06 80 23 5B 05 80  .....tlk0...#[..
0050: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 01 E6 00 02  ........tlk1....
0060: 02 10 07 80 80 8C 00 5B  08 80 F8 FF FF 7F F8 FF  .......[........
0070: FF 7F 74 6C 61 30 1D 09  80 23 5B 08 80 F8 FF FF  ..tla0...#[.....
0080: 7F F8 FF FF 7F 74 6C 61  31 01 E6 00 02 02 10 0A  .....tla1.......
0090: 80 80 B9 00 5B 08 80 F8  FF FF 7F F8 FF FF 7F 74  ....[..........t
00A0: 6C 61 30 1D 0B 80 23 5B  08 80 F8 FF FF 7F F8 FF  la0...#[........
00B0: FF 7F 74 6C 61 31 01 E6  00 02 02 10 0C 80 80 E6  ..tla1..........
00C0: 00 5B 08 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 61 30  .[..........tla0
00D0: 1D 0D 80 23 5B 08 80 F8  FF FF 7F F8 FF FF 7F 74  ...#[..........t
00E0: 6C 61 31 01 E6 00 1C 0E  80 5B 00 80 F8 FF FF 7F  la1......[......
00F0: F8 FF FF 7F 72 65 69 30  1D 0F 80 23 53 F8 FF FF  ....rei0...#S...
0100: 7F F8 FF FF 7F 72 65 69  30 21 00                 .....rei0!.     
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=497*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=11079*)
    → "You are an adventurer... I can smell the dark blood of the undead as it drips slowly from your soiled garments."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=11080*)
    → "Beware, my friend, for you are not alone in your journey. Lost spirits lurk in the shadows behind you, waiting for their chance to rob you of your soul."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=497*
  9: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=11081*)
    → "Hmmm..."
 10: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0032 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x005F
 12: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
 13: 0x0049 [0x1D] PRINT_EVENT_MESSAGE(message_id=11082*)
    → "You still have a fairly good head start, but they will not let up until they have found you and filled your heart with poison and pain."
 14: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x004D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 16: 0x005C [0x01] GOTO 0x00E6
 17: 0x005F [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x008C
 18: 0x0067 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=496*
 19: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=11083*)
    → "They are close... It is only a matter of time before you have fallen within their reach."
 20: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x007A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=496*
 22: 0x0089 [0x01] GOTO 0x00E6
 23: 0x008C [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x00B9
 24: 0x0094 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=496*
 25: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=11084*)
    → "Can you not feel the hands that reach up from the bottomless depths of hell? Can you not feel the gaze of a thousand eyes, glowing red with anger and hate?"
 26: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00A7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=496*
 28: 0x00B6 [0x01] GOTO 0x00E6
 29: 0x00B9 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x00E6
 30: 0x00C1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=496*
 31: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=11085*)
    → "The grip of evil is tightening on the very essence of what makes you who you are. Be forewarned, as it will not be long before you are confronted with a battle for more than just your life."
 32: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x00D4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=496*
 34: 0x00E3 [0x01] GOTO 0x00E6

SUBROUTINE_00E6:
 35: 0x00E6 [0x1C] WAIT(60* ticks)
 36: 0x00E9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rei0" with entities [EventEntity, EventEntity], work=497*
 37: 0x00F8 [0x1D] PRINT_EVENT_MESSAGE(message_id=11086*)
    → "Oh, poor child! May the light of the Dawn Goddess lead you from the pitch-black depths of darkness!"
 38: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x00FC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "rei0" with entities [EventEntity, EventEntity]
 40: 0x0109 [0x21] END_EVENT
 41: 0x010A [0x00] END_REQSTACK()
```
