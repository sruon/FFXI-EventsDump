# 17531161 - Cermet Door

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 696 bytes                        |
| Total Events     | 6                                |
| References Count | 16                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [0](#event-0)            | 0x0001       |    561 |             70 |
| [11](#event-11)          | 0x0232       |     17 |             10 |
| [65535.1](#event-655351) | 0x0243       |      5 |              3 |
| [65535.2](#event-655352) | 0x0248       |      5 |              3 |
| [65535.3](#event-655353) | 0x024D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x0013      |          19 |
|       3 | 0x0092      |         146 |
|       4 | 0x0078      |         120 |
|       5 | 0x001E      |          30 |
|       6 | 0x003C      |          60 |
|       7 | 0x005A      |          90 |
|       8 | 0x00A3      |         163 |
|       9 | 0x00A4      |         164 |
|      10 | 0x00A5      |         165 |
|      11 | 0x00A6      |         166 |
|      12 | 0x00A7      |         167 |
|      13 | 0x00A8      |         168 |
|      14 | 0x0096      |         150 |
|      15 | 0x00A1      |         161 |

## String References

- **161**: You see nothing of particular interest.

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

### Event 0

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 561 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo1..U........
0020: FF 7F 66 64 6F 31 38 02  80 29 03 F0 FF FF 7F 0F  ..fdo18..)......
0030: 45 03 80 F0 FF FF 7F F0  FF FF 7F 63 6D 34 30 01  E..........cm40.
0040: 80 55 03 80 F0 FF FF 7F  F0 FF FF 7F 63 6D 34 30  .U..........cm40
0050: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 01  E..........fdi1.
0060: 80 55 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .U..........fdi1
0070: 4C 4E 00 1A 81 0B 01 1C  04 80 2C 1A 81 0B 01 1A  LN........,.....
0080: 81 0B 01 63 6F 72 70 53  1A 81 0B 01 1A 81 0B 01  ...corpS........
0090: 63 6F 72 70 29 03 F0 FF  FF 7F 10 4A F0 FF FF 7F  corp)......J....
00A0: 1A 81 0B 01 1C 05 80 45  03 80 F0 FF FF 7F F0 FF  .......E........
00B0: FF 7F 63 6D 34 31 01 80  55 03 80 F0 FF FF 7F F0  ..cm41..U.......
00C0: FF FF 7F 63 6D 34 31 6F  76 F0 FF FF 7F 29 03 F0  ...cm41ov....)..
00D0: FF FF 7F 11 1C 06 80 2C  F0 FF FF 7F F0 FF FF 7F  .......,........
00E0: 72 65 73 30 1C 06 80 45  00 80 F0 FF FF 7F F0 FF  res0...E........
00F0: FF 7F 66 64 6F 31 01 80  55 00 80 F0 FF FF 7F F0  ..fdo1..U.......
0100: FF FF 7F 66 64 6F 31 45  03 80 F0 FF FF 7F F0 FF  ...fdo1E........
0110: FF 7F 63 6D 34 61 01 80  55 03 80 F0 FF FF 7F F0  ..cm4a..U.......
0120: FF FF 7F 63 6D 34 61 2C  F0 FF FF 7F F0 FF FF 7F  ...cm4a,........
0130: 72 65 73 32 4A 1A 81 0B  01 F0 FF FF 7F 6F 76 1A  res2J........ov.
0140: 81 0B 01 27 04 1A 81 0B  01 06 1C 07 80 45 00 80  ...'.........E..
0150: F0 FF FF 7F F0 FF FF 7F  66 64 69 32 01 80 55 00  ........fdi2..U.
0160: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 2B 1A 81  .........fdi2+..
0170: 0B 01 08 80 23 45 03 80  F0 FF FF 7F F0 FF FF 7F  ....#E..........
0180: 63 6D 34 36 01 80 29 05  1A 81 0B 01 07 2B 1A 81  cm46..)......+..
0190: 0B 01 09 80 23 27 03 1A  81 0B 01 04 2B 1A 81 0B  ....#'......+...
01A0: 01 0A 80 23 29 04 1A 81  0B 01 05 2B 1A 81 0B 01  ...#)......+....
01B0: 0B 80 23 27 03 1A 81 0B  01 03 2B 1A 81 0B 01 0C  ..#'......+.....
01C0: 80 23 2B 1A 81 0B 01 0D  80 23 29 04 1A 81 0B 01  .#+......#).....
01D0: 08 27 05 1A 81 0B 01 02  45 03 80 F0 FF FF 7F F0  .'......E.......
01E0: FF FF 7F 63 6D 34 64 01  80 1C 06 80 27 05 F0 FF  ...cm4d.....'...
01F0: FF 7F 12 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0200: 6F 32 01 80 55 00 80 F0  FF FF 7F F0 FF FF 7F 66  o2..U..........f
0210: 64 6F 32 4E 01 1A 81 0B  01 4D 1C 0E 80 46 00 45  do2N.....M...F.E
0220: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 32 01 80  ..........fdi2..
0230: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0026 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x0029 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x0F)
  7: 0x0030 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm40" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
  8: 0x0041 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm40" with entities [LocalPlayer, LocalPlayer], work=146*
  9: 0x0050 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0061 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 11: 0x0070 [0x4C] EventEntity->StatusEvent = 8 // Open door
 12: 0x0071 [0x4E] SET_ENTITY_HIDE_FLAG: Show Jima (ID: 17531162/0x010B811A)
 13: 0x0077 [0x1C] WAIT(120* ticks)
 14: 0x007A [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Jima (ID: 17531162/0x010B811A), Jima (ID: 17531162/0x010B811A)]
 15: 0x0087 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [Jima (ID: 17531162/0x010B811A), Jima (ID: 17531162/0x010B811A)]
 16: 0x0094 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x10)
 17: 0x009B [0x4A] LocalPlayer looks at Jima (ID: 17531162/0x010B811A)
 18: 0x00A4 [0x1C] WAIT(30* ticks)
 19: 0x00A7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm41" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 20: 0x00B8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm41" with entities [LocalPlayer, LocalPlayer], work=146*
 21: 0x00C7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 22: 0x00C8 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 23: 0x00CD [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x11)
 24: 0x00D4 [0x1C] WAIT(60* ticks)
 25: 0x00D7 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [LocalPlayer, LocalPlayer]
 26: 0x00E4 [0x1C] WAIT(60* ticks)
 27: 0x00E7 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x00F8 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 29: 0x0107 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm4a" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 30: 0x0118 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm4a" with entities [LocalPlayer, LocalPlayer], work=146*
 31: 0x0127 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [LocalPlayer, LocalPlayer]
 32: 0x0134 [0x4A] Jima (ID: 17531162/0x010B811A) looks at LocalPlayer
 33: 0x013D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 34: 0x013E [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Jima (ID: 17531162/0x010B811A) Render.Flags0 and Render.Flags3 conditions are met
 35: 0x0143 [0x27] REQ_SET(priority=0x04, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x06)
 36: 0x014A [0x1C] WAIT(90* ticks)
 37: 0x014D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x015E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=200*
 39: 0x016D [0x2B] Jima (ID: 17531162/0x010B811A) [163*]:
    → "Unh... Ungh..."
 40: 0x0174 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0175 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm46" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 42: 0x0186 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x07)
 43: 0x018D [0x2B] Jima (ID: 17531162/0x010B811A) [164*]:
    → "Who are you...? Not a foe, it seems... I am glad you've found me. I am Jima, Ambassador of San d'Oria."
 44: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0195 [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x04)
 46: 0x019C [0x2B] Jima (ID: 17531162/0x010B811A) [165*]:
    → "So you were sent on a mission to the embassy in Jeuno? I see. I am truly sorry you had to come to such a dangerous place as this."
 47: 0x01A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x01A4 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x05)
 49: 0x01AB [0x2B] Jima (ID: 17531162/0x010B811A) [166*]:
    → "Sorrier still am I that I was fool enough to let down my guard. I was struck from behind, and I woke to find myself here. To think, if you hadn't happened by..."
 50: 0x01B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x01B3 [0x27] REQ_SET(priority=0x03, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x03)
 52: 0x01BA [0x2B] Jima (ID: 17531162/0x010B811A) [167*]:
    → "This is a truly dangerous place, and not just because of the monsters. There is an ominous feel to the air..."
 53: 0x01C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x01C2 [0x2B] Jima (ID: 17531162/0x010B811A) [168*]:
    → "Going deeper would be folly. Take care, kind adventurer. I will leave this place while I still can, and we shall meet again at the embassy."
 55: 0x01C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x01CA [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x08)
 57: 0x01D1 [0x27] REQ_SET(priority=0x05, entity_id=Jima (ID: 17531162/0x010B811A), tag_num=0x02)
 58: 0x01D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm4d" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 59: 0x01E9 [0x1C] WAIT(60* ticks)
 60: 0x01EC [0x27] REQ_SET(priority=0x05, entity_id=LocalPlayer, tag_num=0x12)
 61: 0x01F3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 62: 0x0204 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 63: 0x0213 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Jima (ID: 17531162/0x010B811A)
 64: 0x0219 [0x4D] EventEntity->StatusEvent = 9 // Close door
 65: 0x021A [0x1C] WAIT(150* ticks)
 66: 0x021D [0x46] CAMERA_CONTROL: Restore default settings
 67: 0x021F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 68: 0x0230 [0x21] END_EVENT
 69: 0x0231 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0232   |
| Data Size    | 17 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:       20 01 42 4C 1C 0E  80 48 0F 80 23 4D 1C 0E     .BL...H..#M..
0240: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0232 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0234 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0235 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x0236 [0x1C] WAIT(150* ticks)
  4: 0x0239 [0x48] [System] [161*]:
    → "You see nothing of particular interest."
  5: 0x023C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x023D [0x4D] EventEntity->StatusEvent = 9 // Close door
  7: 0x023E [0x1C] WAIT(150* ticks)
  8: 0x0241 [0x21] END_EVENT
  9: 0x0242 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0243  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:          4C 1C 0E 80 00                              L....        
```

#### Opcodes

```
  0: 0x0243 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0244 [0x1C] WAIT(150* ticks)
  2: 0x0247 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0248  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                          4D 1C 0E 80 00                   M....   
```

#### Opcodes

```
  0: 0x0248 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0249 [0x1C] WAIT(150* ticks)
  2: 0x024C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x024D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                         00                     .  
```

#### Opcodes

```
  0: 0x024D [0x00] END_REQSTACK()
```
