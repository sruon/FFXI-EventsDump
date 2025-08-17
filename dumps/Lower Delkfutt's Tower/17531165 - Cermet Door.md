# 17531165 - Cermet Door

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 684 bytes                        |
| Total Events     | 5                                |
| References Count | 16                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [13](#event-13)          | 0x0001       |     17 |             10 |
| [2](#event-2)            | 0x0012       |    561 |             70 |
| [65535.1](#event-655351) | 0x0243       |      2 |              2 |
| [65535.2](#event-655352) | 0x0245       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0096      |         150 |
|       1 | 0x00A1      |         161 |
|       2 | 0x00C8      |         200 |
|       3 | 0x0000      |           0 |
|       4 | 0x0013      |          19 |
|       5 | 0x0092      |         146 |
|       6 | 0x0078      |         120 |
|       7 | 0x001E      |          30 |
|       8 | 0x003C      |          60 |
|       9 | 0x005A      |          90 |
|      10 | 0x00AF      |         175 |
|      11 | 0x00B0      |         176 |
|      12 | 0x00B1      |         177 |
|      13 | 0x00B2      |         178 |
|      14 | 0x00B3      |         179 |
|      15 | 0x00B4      |         180 |

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

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 17 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 4C 1C 00 80  48 01 80 23 4D 1C 00 80    .BL...H..#M...
0010: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x4C] EventEntity->StatusEvent = 8 // Open door
  3: 0x0005 [0x1C] WAIT(150* ticks)
  4: 0x0008 [0x48] [System] [161*]:
    → "You see nothing of particular interest."
  5: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000C [0x4D] EventEntity->StatusEvent = 9 // Close door
  7: 0x000D [0x1C] WAIT(150* ticks)
  8: 0x0010 [0x21] END_EVENT
  9: 0x0011 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0012    |
| Data Size    | 561 bytes |
| Instructions | 70        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       20 01 46 01 42 45  02 80 F0 FF FF 7F F0 FF     .F.BE........
0020: FF 7F 66 64 6F 31 03 80  55 02 80 F0 FF FF 7F F0  ..fdo1..U.......
0030: FF FF 7F 66 64 6F 31 38  04 80 29 03 F0 FF FF 7F  ...fdo18..).....
0040: 17 45 05 80 F0 FF FF 7F  F0 FF FF 7F 63 6D 34 34  .E..........cm44
0050: 03 80 55 05 80 F0 FF FF  7F F0 FF FF 7F 63 6D 34  ..U..........cm4
0060: 34 45 02 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  4E..........fdi1
0070: 03 80 55 02 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..U..........fdi
0080: 31 4C 4E 00 1E 81 0B 01  1C 06 80 2C 1E 81 0B 01  1LN........,....
0090: 1E 81 0B 01 63 6F 72 70  53 1E 81 0B 01 1E 81 0B  ....corpS.......
00A0: 01 63 6F 72 70 29 03 F0  FF FF 7F 18 4A F0 FF FF  .corp)......J...
00B0: 7F 1E 81 0B 01 1C 07 80  45 05 80 F0 FF FF 7F F0  ........E.......
00C0: FF FF 7F 63 6D 34 35 03  80 55 05 80 F0 FF FF 7F  ...cm45..U......
00D0: F0 FF FF 7F 63 6D 34 35  6F 76 F0 FF FF 7F 29 03  ....cm45ov....).
00E0: F0 FF FF 7F 19 1C 08 80  2C F0 FF FF 7F F0 FF FF  ........,.......
00F0: 7F 72 65 73 30 1C 08 80  45 02 80 F0 FF FF 7F F0  .res0...E.......
0100: FF FF 7F 66 64 6F 31 03  80 55 02 80 F0 FF FF 7F  ...fdo1..U......
0110: F0 FF FF 7F 66 64 6F 31  45 05 80 F0 FF FF 7F F0  ....fdo1E.......
0120: FF FF 7F 63 6D 34 63 03  80 55 05 80 F0 FF FF 7F  ...cm4c..U......
0130: F0 FF FF 7F 63 6D 34 63  2C F0 FF FF 7F F0 FF FF  ....cm4c,.......
0140: 7F 72 65 73 32 4A 1E 81  0B 01 F0 FF FF 7F 6F 76  .res2J........ov
0150: 1E 81 0B 01 27 04 1E 81  0B 01 06 1C 09 80 45 02  ....'.........E.
0160: 80 F0 FF FF 7F F0 FF FF  7F 66 64 69 32 03 80 55  .........fdi2..U
0170: 02 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 32 2B 1E  ..........fdi2+.
0180: 81 0B 01 0A 80 23 45 05  80 F0 FF FF 7F F0 FF FF  .....#E.........
0190: 7F 63 6D 34 38 03 80 29  05 1E 81 0B 01 07 2B 1E  .cm48..)......+.
01A0: 81 0B 01 0B 80 23 27 03  1E 81 0B 01 04 2B 1E 81  .....#'......+..
01B0: 0B 01 0C 80 23 29 04 1E  81 0B 01 05 2B 1E 81 0B  ....#)......+...
01C0: 01 0D 80 23 27 03 1E 81  0B 01 03 2B 1E 81 0B 01  ...#'......+....
01D0: 0E 80 23 2B 1E 81 0B 01  0F 80 23 29 04 1E 81 0B  ..#+......#)....
01E0: 01 08 27 05 1E 81 0B 01  02 45 05 80 F0 FF FF 7F  ..'......E......
01F0: F0 FF FF 7F 63 6D 34 66  03 80 1C 08 80 27 05 F0  ....cm4f.....'..
0200: FF FF 7F 1A 45 02 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0210: 64 6F 32 03 80 55 02 80  F0 FF FF 7F F0 FF FF 7F  do2..U..........
0220: 66 64 6F 32 4E 01 1E 81  0B 01 4D 1C 00 80 46 00  fdo2N.....M...F.
0230: 45 02 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 32 03  E..........fdi2.
0240: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0012 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0014 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0016 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0017 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0028 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0037 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x003A [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x17)
  7: 0x0041 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm44" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
  8: 0x0052 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm44" with entities [LocalPlayer, LocalPlayer], work=146*
  9: 0x0061 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 10: 0x0072 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 11: 0x0081 [0x4C] EventEntity->StatusEvent = 8 // Open door
 12: 0x0082 [0x4E] SET_ENTITY_HIDE_FLAG: Show Heimji-Keimji (ID: 17531166/0x010B811E)
 13: 0x0088 [0x1C] WAIT(120* ticks)
 14: 0x008B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Heimji-Keimji (ID: 17531166/0x010B811E), Heimji-Keimji (ID: 17531166/0x010B811E)]
 15: 0x0098 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "corp" with entities [Heimji-Keimji (ID: 17531166/0x010B811E), Heimji-Keimji (ID: 17531166/0x010B811E)]
 16: 0x00A5 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x18)
 17: 0x00AC [0x4A] LocalPlayer looks at Heimji-Keimji (ID: 17531166/0x010B811E)
 18: 0x00B5 [0x1C] WAIT(30* ticks)
 19: 0x00B8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm45" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 20: 0x00C9 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm45" with entities [LocalPlayer, LocalPlayer], work=146*
 21: 0x00D8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 22: 0x00D9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 23: 0x00DE [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x19)
 24: 0x00E5 [0x1C] WAIT(60* ticks)
 25: 0x00E8 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [LocalPlayer, LocalPlayer]
 26: 0x00F5 [0x1C] WAIT(60* ticks)
 27: 0x00F8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 28: 0x0109 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 29: 0x0118 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm4c" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 30: 0x0129 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm4c" with entities [LocalPlayer, LocalPlayer], work=146*
 31: 0x0138 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res2" with entities [LocalPlayer, LocalPlayer]
 32: 0x0145 [0x4A] Heimji-Keimji (ID: 17531166/0x010B811E) looks at LocalPlayer
 33: 0x014E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 34: 0x014F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Heimji-Keimji (ID: 17531166/0x010B811E) Render.Flags0 and Render.Flags3 conditions are met
 35: 0x0154 [0x27] REQ_SET(priority=0x04, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x06)
 36: 0x015B [0x1C] WAIT(90* ticks)
 37: 0x015E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x016F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=200*
 39: 0x017E [0x2B] Heimji-Keimji (ID: 17531166/0x010B811E) [175*]:
    → "Oooh..."
 40: 0x0185 [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x0186 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm48" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 42: 0x0197 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x07)
 43: 0x019E [0x2B] Heimji-Keimji (ID: 17531166/0x010B811E) [176*]:
    → "Who...? Oh, I'm so glad you're not one of the baddies. Thank you for saving me! I'm the Windurstian ambassador to Jeuno, Heimji-Keimji."
 44: 0x01A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x01A6 [0x27] REQ_SET(priority=0x03, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x04)
 46: 0x01AD [0x2B] Heimji-Keimji (ID: 17531166/0x010B811E) [177*]:
    → "They sent you on a mission to the embassy? Oh... I'm sorry-worry you had to come to such a dangerous place because of me."
 47: 0x01B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x01B5 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x05)
 49: 0x01BC [0x2B] Heimji-Keimji (ID: 17531166/0x010B811E) [178*]:
    → "I should have been more careful... Someone bonky-wonked me on the head from behind, and I woke up in this hairy-scary place. If you hadn't come... It makes me shudder-budder to think what would've happened to me!"
 50: 0x01C3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x01C4 [0x27] REQ_SET(priority=0x03, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x03)
 52: 0x01CB [0x2B] Heimji-Keimji (ID: 17531166/0x010B811E) [179*]:
    → "This place is dangerous! Aside from all the monsters, I feel something nasty-wasty in the air."
 53: 0x01D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x01D3 [0x2B] Heimji-Keimji (ID: 17531166/0x010B811E) [180*]:
    → "We should go back as soon as possible! Don't worry about me, as I can run super-duper fast! I'll meet you back at the embassy!"
 55: 0x01DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x01DB [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x08)
 57: 0x01E2 [0x27] REQ_SET(priority=0x05, entity_id=Heimji-Keimji (ID: 17531166/0x010B811E), tag_num=0x02)
 58: 0x01E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm4f" with entities [LocalPlayer, LocalPlayer], work=[146*, 0*]
 59: 0x01FA [0x1C] WAIT(60* ticks)
 60: 0x01FD [0x27] REQ_SET(priority=0x05, entity_id=LocalPlayer, tag_num=0x1A)
 61: 0x0204 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 62: 0x0215 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 63: 0x0224 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Heimji-Keimji (ID: 17531166/0x010B811E)
 64: 0x022A [0x4D] EventEntity->StatusEvent = 9 // Close door
 65: 0x022B [0x1C] WAIT(150* ticks)
 66: 0x022E [0x46] CAMERA_CONTROL: Restore default settings
 67: 0x0230 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 68: 0x0241 [0x21] END_EVENT
 69: 0x0242 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0243  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:          4C 00                                       L.           
```

#### Opcodes

```
  0: 0x0243 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0244 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0245  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                4D 00                                   M.         
```

#### Opcodes

```
  0: 0x0245 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0246 [0x00] END_REQSTACK()
```
