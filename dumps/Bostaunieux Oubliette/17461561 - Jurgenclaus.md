# 17461561 - Jurgenclaus

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Bostaunieux Oubliette (ID: 167) |
| Block Size       | 1084 bytes                      |
| Total Events     | 4                               |
| References Count | 35                              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [6](#event-6)         | 0x0001       |    681 |             92 |
| [18](#event-18)       | 0x02AA       |     60 |              9 |
| [8](#event-8)         | 0x02E6       |    168 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x00A3      |         163 |
|       3 | 0x0013      |          19 |
|       4 | 0x11870     |       71792 |
|       5 | 0x3107      |       12551 |
|       6 | 0xFFFFA253  |  4294943315 |
|       7 | 0x0BB8      |        3000 |
|       8 | 0x0043      |          67 |
|       9 | 0x1CCA      |        7370 |
|      10 | 0x1CCB      |        7371 |
|      11 | 0x1CCC      |        7372 |
|      12 | 0x0028      |          40 |
|      13 | 0x000D      |          13 |
|      14 | 0x11846     |       71750 |
|      15 | 0x3980      |       14720 |
|      16 | 0xFFFFA240  |  4294943296 |
|      17 | 0x1CCD      |        7373 |
|      18 | 0x1CCE      |        7374 |
|      19 | 0x000A      |          10 |
|      20 | 0x1CCF      |        7375 |
|      21 | 0x1CD0      |        7376 |
|      22 | 0x1CD1      |        7377 |
|      23 | 0x1CD2      |        7378 |
|      24 | 0x005A      |          90 |
|      25 | 0x11A25     |       72229 |
|      26 | 0x1AFF      |        6911 |
|      27 | 0xFFFFA252  |  4294943314 |
|      28 | 0x00B4      |         180 |
|      29 | 0x1CD4      |        7380 |
|      30 | 0x003C      |          60 |
|      31 | 0x1CD5      |        7381 |
|      32 | 0x1CD6      |        7382 |
|      33 | 0x1CD7      |        7383 |
|      34 | 0x1CD8      |        7384 |

## String References

- **7382**: What do ya think you're lookin' at? You don't know nothing about what's really going on under this hellhole do ya? Compared to the sewers, my cell is a palace!
- **7383**: Oh yeah, I think I heard about some scientists who ran off into the sewers during the war. They say only one got out, but that he was messed up in the head for the rest of his life.
- **7384**: Rumor has it that there's a way out of there. Maybe the old guy got lucky.

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

### Event 6

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 681 bytes |
| Instructions | 92        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo1..U........
0020: FF 7F 66 64 6F 31 5C 00  02 80 5C 01 02 80 38 03  ..fdo1\...\...8.
0030: 80 37 04 80 05 80 06 80  07 80 27 03 F0 FF FF 7F  .7........'.....
0040: 08 27 03 07 71 0A 01 19  27 03 08 71 0A 01 02 4A  .'..q...'..q...J
0050: 07 71 0A 01 F0 FF FF 7F  4A F0 FF FF 7F 07 71 0A  .q......J.....q.
0060: 01 6F 76 F0 FF FF 7F 45  08 80 F0 FF FF 7F F0 FF  .ov....E........
0070: FF 7F 72 30 30 30 01 80  55 08 80 F0 FF FF 7F F0  ..r000..U.......
0080: FF FF 7F 72 30 30 30 45  00 80 F0 FF FF 7F F0 FF  ...r000E........
0090: FF 7F 66 64 69 31 01 80  55 00 80 F0 FF FF 7F F0  ..fdi1..U.......
00A0: FF FF 7F 66 64 69 31 27  03 08 71 0A 01 03 27 03  ...fdi1'..q...'.
00B0: 07 71 0A 01 11 2B 07 71  0A 01 09 80 23 2A 03 07  .q...+.q....#*..
00C0: 71 0A 01 27 04 07 71 0A  01 12 2A 03 08 71 0A 01  q..'..q...*..q..
00D0: 4A F0 FF FF 7F 08 71 0A  01 27 03 08 71 0A 01 06  J.....q..'..q...
00E0: 2B 08 71 0A 01 0A 80 23  2A 03 08 71 0A 01 29 04  +.q....#*..q..).
00F0: 08 71 0A 01 07 2B 39 71  0A 01 0B 80 23 4A 08 71  .q...+9q....#J.q
0100: 0A 01 39 71 0A 01 1C 0C  80 45 08 80 F0 FF FF 7F  ..9q.....E......
0110: F0 FF FF 7F 72 30 30 31  01 80 55 08 80 F0 FF FF  ....r001..U.....
0120: 7F F0 FF FF 7F 72 30 30  31 32 0D 80 1F 00 0E 80  .....r0012......
0130: 0F 80 10 80 1F 01 6F 45  08 80 F0 FF FF 7F F0 FF  ......oE........
0140: FF 7F 72 30 30 32 01 80  2B 39 71 0A 01 11 80 23  ..r002..+9q....#
0150: 55 08 80 F0 FF FF 7F F0  FF FF 7F 72 30 30 32 2B  U..........r002+
0160: 39 71 0A 01 12 80 23 27  03 08 71 0A 01 04 1C 13  9q....#'..q.....
0170: 80 45 08 80 F0 FF FF 7F  F0 FF FF 7F 72 30 30 33  .E..........r003
0180: 01 80 55 08 80 F0 FF FF  7F F0 FF FF 7F 72 30 30  ..U..........r00
0190: 33 2A 03 08 71 0A 01 2B  08 71 0A 01 14 80 23 45  3*..q..+.q....#E
01A0: 08 80 F0 FF FF 7F F0 FF  FF 7F 72 30 30 34 01 80  ..........r004..
01B0: 55 08 80 F0 FF FF 7F F0  FF FF 7F 72 30 30 34 2B  U..........r004+
01C0: 39 71 0A 01 15 80 23 2B  08 71 0A 01 16 80 23 45  9q....#+.q....#E
01D0: 08 80 F0 FF FF 7F F0 FF  FF 7F 72 30 30 35 01 80  ..........r005..
01E0: 55 08 80 F0 FF FF 7F F0  FF FF 7F 72 30 30 35 2B  U..........r005+
01F0: 39 71 0A 01 17 80 23 27  03 08 71 0A 01 05 1C 18  9q....#'..q.....
0200: 80 31 00 19 80 1A 80 1B  80 1C 80 31 01 2A 03 08  .1.........1.*..
0210: 71 0A 01 2B 08 71 0A 01  1D 80 23 45 08 80 F0 FF  q..+.q....#E....
0220: FF 7F F0 FF FF 7F 72 30  30 36 01 80 55 08 80 F0  ......r006..U...
0230: FF FF 7F F0 FF FF 7F 72  30 30 36 1C 1E 80 27 04  .......r006...'.
0240: 08 71 0A 01 0A 1C 1C 80  4A F0 FF FF 7F 07 71 0A  .q......J.....q.
0250: 01 27 03 07 71 0A 01 13  2B 07 71 0A 01 1F 80 23  .'..q...+.q....#
0260: 2A 03 07 71 0A 01 27 04  07 71 0A 01 14 45 00 80  *..q..'..q...E..
0270: F0 FF FF 7F F0 FF FF 7F  66 64 6F 32 01 80 55 00  ........fdo2..U.
0280: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 32 5C 00 01  .........fdo2\..
0290: 80 5C 01 01 80 46 00 45  00 80 F0 FF FF 7F F0 FF  .\...F.E........
02A0: FF 7F 66 64 69 32 01 80  21 00                    ..fdi2..!.      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0026 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 163*
  6: 0x002A [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 163*
  7: 0x002E [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  8: 0x0031 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=71.792*, z=12.551*, y=-23.981*, direction=263.7°*
  9: 0x003A [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x08)
 10: 0x0041 [0x27] REQ_SET(priority=0x03, entity_id=Novalmauge (ID: 17461511/0x010A7107), tag_num=0x19)
 11: 0x0048 [0x27] REQ_SET(priority=0x03, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x02)
 12: 0x004F [0x4A] Novalmauge (ID: 17461511/0x010A7107) looks at LocalPlayer
 13: 0x0058 [0x4A] LocalPlayer looks at Novalmauge (ID: 17461511/0x010A7107)
 14: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x0062 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 16: 0x0067 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r000" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 17: 0x0078 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r000" with entities [LocalPlayer, LocalPlayer], work=67*
 18: 0x0087 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0098 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 20: 0x00A7 [0x27] REQ_SET(priority=0x03, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x03)
 21: 0x00AE [0x27] REQ_SET(priority=0x03, entity_id=Novalmauge (ID: 17461511/0x010A7107), tag_num=0x11)
 22: 0x00B5 [0x2B] Novalmauge (ID: 17461511/0x010A7107) [7370*]:
    → "Cyranuce? No, you'll not find him here. He is dead. His cellmate was a beastmaster, who somehow called forth a terrible creature and fled."
 23: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00BD [0x2A] GET_REQ_LEVEL(level=3, entity_id=Novalmauge (ID: 17461511/0x010A7107))
 25: 0x00C3 [0x27] REQ_SET(priority=0x04, entity_id=Novalmauge (ID: 17461511/0x010A7107), tag_num=0x12)
 26: 0x00CA [0x2A] GET_REQ_LEVEL(level=3, entity_id=Chumia (ID: 17461512/0x010A7108))
 27: 0x00D0 [0x4A] LocalPlayer looks at Chumia (ID: 17461512/0x010A7108)
 28: 0x00D9 [0x27] REQ_SET(priority=0x03, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x06)
 29: 0x00E0 [0x2B] Chumia (ID: 17461512/0x010A7108) [7371*]:
    → "His beast knocked a gaping hole in the wall, so he was home free. But Cyranuce's body was found underneath the creature. It's too bad... We could've saved him if we got here sooner!"
 30: 0x00E7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00E8 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Chumia (ID: 17461512/0x010A7108))
 32: 0x00EE [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x07)
 33: 0x00F5 [0x2B] Jurgenclaus (ID: 17461561/0x010A7139) [7372*]:
    → "Yeah, I know."
 34: 0x00FC [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x00FD [0x4A] Chumia (ID: 17461512/0x010A7108) looks at Jurgenclaus (ID: 17461561/0x010A7139)
 36: 0x0106 [0x1C] WAIT(40* ticks)
 37: 0x0109 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r001" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 38: 0x011A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r001" with entities [LocalPlayer, LocalPlayer], work=67*
 39: 0x0129 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 40: 0x012C [0x1F] MOVE_ENTITY: EventEntity moves to X=71.750*, Z=14.720*, Y=-24.000*
 41: 0x0134 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 42: 0x0136 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 43: 0x0137 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r002" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 44: 0x0148 [0x2B] Jurgenclaus (ID: 17461561/0x010A7139) [7373*]:
    → "Rahal was jealous of his friend Cyranuce for becoming a dragoon. He set a trap for him, and saw him thrown into this very dungeon."
 45: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x0150 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r002" with entities [LocalPlayer, LocalPlayer], work=67*
 47: 0x015F [0x2B] Jurgenclaus (ID: 17461561/0x010A7139) [7374*]:
    → "That is how Rahal, the dragonslayer tainted with drakes' blood, seized the office of general. You knights were left in the dark."
 48: 0x0166 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x0167 [0x27] REQ_SET(priority=0x03, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x04)
 50: 0x016E [0x1C] WAIT(10* ticks)
 51: 0x0171 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r003" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 52: 0x0182 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r003" with entities [LocalPlayer, LocalPlayer], work=67*
 53: 0x0191 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Chumia (ID: 17461512/0x010A7108))
 54: 0x0197 [0x2B] Chumia (ID: 17461512/0x010A7108) [7375*]:
    → "What!? Lies, all of it!"
 55: 0x019E [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x019F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r004" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 57: 0x01B0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r004" with entities [LocalPlayer, LocalPlayer], work=67*
 58: 0x01BF [0x2B] Jurgenclaus (ID: 17461561/0x010A7139) [7376*]:
    → "Lies? Well then, why was Rahal always coming to check on him? He was waiting for Cyranuce to kick the bucket, wasn't he?"
 59: 0x01C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x01C7 [0x2B] Chumia (ID: 17461512/0x010A7108) [7377*]:
    → "No, it can't be!"
 61: 0x01CE [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x01CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r005" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 63: 0x01E0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r005" with entities [LocalPlayer, LocalPlayer], work=67*
 64: 0x01EF [0x2B] Jurgenclaus (ID: 17461561/0x010A7139) [7378*]:
    → "Hmph. The only people who can become dragonslayers are those who truly hate them. They're not after treasure or jewels; they just want to exterminate them!"
 65: 0x01F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x01F7 [0x27] REQ_SET(priority=0x03, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x05)
 67: 0x01FE [0x1C] WAIT(90* ticks)
 68: 0x0201 [0x31] UPDATE_ENTITY_POSITION: Set EventEntity goal position to X=72.229*, Z=6.911*, Y=-23.982*, Time=180*
 69: 0x020B [0x31] UPDATE_ENTITY_POSITION: Move EventEntity towards goal position
 70: 0x020D [0x2A] GET_REQ_LEVEL(level=3, entity_id=Chumia (ID: 17461512/0x010A7108))
 71: 0x0213 [0x2B] Chumia (ID: 17461512/0x010A7108) [7380*]:
    → "Why, you--!"
 72: 0x021A [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x021B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "r006" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 74: 0x022C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "r006" with entities [LocalPlayer, LocalPlayer], work=67*
 75: 0x023B [0x1C] WAIT(60* ticks)
 76: 0x023E [0x27] REQ_SET(priority=0x04, entity_id=Chumia (ID: 17461512/0x010A7108), tag_num=0x0A)
 77: 0x0245 [0x1C] WAIT(180* ticks)
 78: 0x0248 [0x4A] LocalPlayer looks at Novalmauge (ID: 17461511/0x010A7107)
 79: 0x0251 [0x27] REQ_SET(priority=0x03, entity_id=Novalmauge (ID: 17461511/0x010A7107), tag_num=0x13)
 80: 0x0258 [0x2B] Novalmauge (ID: 17461511/0x010A7107) [7381*]:
    → "If you wish to learn of dragons, ask the archeologist, Oiheaurese, in the cathedral. He should know well their lore."
 81: 0x025F [0x23] WAIT_FOR_DIALOG_INTERACTION
 82: 0x0260 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Novalmauge (ID: 17461511/0x010A7107))
 83: 0x0266 [0x27] REQ_SET(priority=0x04, entity_id=Novalmauge (ID: 17461511/0x010A7107), tag_num=0x14)
 84: 0x026D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 85: 0x027E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 86: 0x028D [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 87: 0x0291 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 88: 0x0295 [0x46] CAMERA_CONTROL: Restore default settings
 89: 0x0297 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 90: 0x02A8 [0x21] END_EVENT
 91: 0x02A9 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02AA   |
| Data Size    | 60 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                                1A 40 03 1D 20 80            .@.. .
02B0: 23 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 32  #E..........fdo2
02C0: 01 80 55 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
02D0: 32 46 00 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  2F.E..........fd
02E0: 69 32 01 80 21 00                                 i2..!.          
```

#### Opcodes

```
  0: 0x02AA [0x1A] CALL_SUBROUTINE(address=0x0340)
  1: 0x02AD [0x1D] PRINT_EVENT_MESSAGE(message_id=7382*)
    → "What do ya think you're lookin' at? You don't know nothing about what's really going on under this hellhole do ya? Compared to the sewers, my cell is a palace!"
  2: 0x02B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x02B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x02C2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x02D1 [0x46] CAMERA_CONTROL: Restore default settings
  6: 0x02D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x02E4 [0x21] END_EVENT
  8: 0x02E5 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02E6    |
| Data Size    | 168 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02E0:                   45 00  80 F0 FF FF 7F F0 FF FF        E.........
02F0: 7F 66 64 69 30 01 80 1A  40 03 1D 20 80 23 5E 69  .fdi0...@.. .#^i
0300: 64 31 30 1D 21 80 23 1D  22 80 23 45 00 80 F0 FF  d10.!.#.".#E....
0310: FF 7F F0 FF FF 7F 66 64  6F 32 01 80 55 00 80 F0  ......fdo2..U...
0320: FF FF 7F F0 FF FF 7F 66  64 6F 32 46 00 45 00 80  .......fdo2F.E..
0330: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 01 80 21 00  ........fdi2..!.
0340: 42 46 01 4A F0 FF FF 7F  F8 FF FF 7F 6F 76 F0 FF  BF.J........ov..
0350: FF 7F 1E F0 FF FF 7F 1C  13 80 45 00 80 F0 FF FF  ..........E.....
0360: 7F F0 FF FF 7F 6F 76 6C  31 01 80 45 08 80 F0 FF  .....ovl1..E....
0370: FF 7F F0 FF FF 7F 70 30  30 30 01 80 55 08 80 F0  ......p000..U...
0380: FF FF 7F F0 FF FF 7F 70  30 30 30 6F 70 1B        .......p000op.  
```

#### Opcodes

```
  0: 0x02E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x02F7 [0x1A] CALL_SUBROUTINE(address=0x0340)
  2: 0x02FA [0x1D] PRINT_EVENT_MESSAGE(message_id=7382*)
    → "What do ya think you're lookin' at? You don't know nothing about what's really going on under this hellhole do ya? Compared to the sewers, my cell is a palace!"
  3: 0x02FD [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x02FE [0x5E] EventEntity goes idle (kills current action) (animation: "id10")
  5: 0x0303 [0x1D] PRINT_EVENT_MESSAGE(message_id=7383*)
    → "Oh yeah, I think I heard about some scientists who ran off into the sewers during the war. They say only one got out, but that he was messed up in the head for the rest of his life."
  6: 0x0306 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0307 [0x1D] PRINT_EVENT_MESSAGE(message_id=7384*)
    → "Rumor has it that there's a way out of there. Maybe the old guy got lucky."
  8: 0x030A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x030B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x031C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 11: 0x032B [0x46] CAMERA_CONTROL: Restore default settings
 12: 0x032D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x033E [0x21] END_EVENT
 14: 0x033F [0x00] END_REQSTACK()

SUBROUTINE_0340:
 15: 0x0340 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 16: 0x0341 [0x46] CAMERA_CONTROL: Disable user control
 17: 0x0343 [0x4A] LocalPlayer looks at EventEntity
 18: 0x034C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 19: 0x034D [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 20: 0x0352 [0x1E] EventEntity looks at LocalPlayer and starts talking
 21: 0x0357 [0x1C] WAIT(10* ticks)
 22: 0x035A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x036B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "p000" with entities [LocalPlayer, LocalPlayer], work=[67*, 0*]
 24: 0x037C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "p000" with entities [LocalPlayer, LocalPlayer], work=67*
 25: 0x038B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 26: 0x038C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 27: 0x038D [0x1B] RETURN
```
