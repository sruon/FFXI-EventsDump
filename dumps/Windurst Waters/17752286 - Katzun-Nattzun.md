# 17752286 - Katzun-Nattzun

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 704 bytes                 |
| Total Events     | 10                        |
| References Count | 16                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [65535.5](#event-655355) | 0x0045       |     16 |              2 |
| [65535.6](#event-655356) | 0x0055       |     14 |              2 |
| [65535.7](#event-655357) | 0x0063       |     16 |              2 |
| [65535.8](#event-655358) | 0x0073       |     14 |              2 |
| [814](#event-814)        | 0x0081       |    455 |             62 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x0013      |          19 |
|       6 | 0x00D3      |         211 |
|       7 | 0x2730      |       10032 |
|       8 | 0x2731      |       10033 |
|       9 | 0x0096      |         150 |
|      10 | 0x2732      |       10034 |
|      11 | 0x2733      |       10035 |
|      12 | 0x0001      |           1 |
|      13 | 0x2734      |       10036 |
|      14 | 0x2735      |       10037 |
|      15 | 0x0064      |         100 |

## String References

- **10032**: Whaddaya want, whimperin' whipper-shnapper?
- **10033**: What? You shay you're wookin' for $6? Well, I can hewp you out in that department.
- **10034**: Ah-ha! Here it is!
- **10035**: Yesh...I remember the shtudent that wrote thish. A probwematic bugger-wugger that boy was.
- **10036**: But that was a wong, wong time ago... Wait a minute. You anshered all the queshtions in QUIZ DE VANA'DIEW correctwy.
- **10037**: You weren't cheat-sheetin' now, were you? Well, no matter. Here's your prize. You earned it.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          66 00 80 F8 FF  FF 7F F8 FF FF 7F 70 61     f..........pa
0070: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x0063 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          53 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30     S........pas0
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0073 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  1: 0x0080 [0x00] END_REQSTACK()
```

### Event 814

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0081    |
| Data Size    | 455 bytes |
| Instructions | 62        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    03 01 10 02 80 42 46  01 45 03 80 F8 FF FF 7F   .....BF.E......
0090: F8 FF FF 7F 66 64 6F 31  02 80 1C 04 80 38 05 80  ....fdo1.....8..
00A0: 29 0B F0 FF FF 7F 52 4E  00 DE E0 0E 01 80 DE E0  ).....RN........
00B0: 0E 01 4A F0 FF FF 7F DE  E0 0E 01 6F 76 F0 FF FF  ..J........ov...
00C0: 7F 79 00 DE E0 0E 01 F0  FF FF 7F 45 06 80 F0 FF  .y.........E....
00D0: FF 7F F0 FF FF 7F 73 30  39 37 02 80 45 03 80 F8  ......s097..E...
00E0: FF FF 7F F8 FF FF 7F 66  64 69 31 02 80 1C 04 80  .......fdi1.....
00F0: 1D 07 80 23 52 06 80 F0  FF FF 7F F0 FF FF 7F 73  ...#R..........s
0100: 30 39 37 45 06 80 F0 FF  FF 7F F0 FF FF 7F 73 30  097E..........s0
0110: 39 38 02 80 1D 08 80 23  45 03 80 F8 FF FF 7F F8  98.....#E.......
0120: FF FF 7F 66 64 6F 31 02  80 1C 09 80 52 06 80 F0  ...fdo1.....R...
0130: FF FF 7F F0 FF FF 7F 73  30 39 38 45 06 80 F0 FF  .......s098E....
0140: FF 7F F0 FF FF 7F 73 30  39 39 02 80 45 03 80 F8  ......s099..E...
0150: FF FF 7F F8 FF FF 7F 66  64 69 31 02 80 29 08 DE  .......fdi1..)..
0160: E0 0E 01 07 1D 0A 80 23  29 08 DE E0 0E 01 08 29  .......#)......)
0170: 08 DE E0 0E 01 03 1D 0B  80 23 29 08 DE E0 0E 01  .........#).....
0180: 04 02 04 10 0C 80 00 E3  01 52 06 80 F0 FF FF 7F  .........R......
0190: F0 FF FF 7F 73 30 39 38  03 01 10 0C 80 45 03 80  ....s098.....E..
01A0: F0 FF FF 7F F0 FF FF 7F  6F 76 6C 31 02 80 45 06  ........ovl1..E.
01B0: 80 F0 FF FF 7F F0 FF FF  7F 73 30 39 37 02 80 29  .........s097..)
01C0: 08 DE E0 0E 01 05 1D 0D  80 23 29 08 DE E0 0E 01  .........#).....
01D0: 06 29 08 DE E0 0E 01 07  1D 0E 80 23 29 08 DE E0  .).........#)...
01E0: 0E 01 08 45 03 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
01F0: 6F 31 02 80 1C 04 80 02  04 10 0C 80 00 11 02 52  o1.............R
0200: 06 80 F0 FF FF 7F F0 FF  FF 7F 73 30 39 37 01 20  ..........s097. 
0210: 02 52 06 80 F0 FF FF 7F  F0 FF FF 7F 73 30 39 39  .R..........s099
0220: 29 08 DE E0 0E 01 05 46  00 1C 0F 80 29 08 DE E0  )......F....)...
0230: 0E 01 06 45 03 80 F8 FF  FF 7F F8 FF FF 7F 66 64  ...E..........fd
0240: 69 31 02 80 20 00 21 00                           i1.. .!.        
```

#### Opcodes

```
  0: 0x0081 [0x03] Work_Zone[1] = 0*
  1: 0x0086 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0087 [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0089 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
  4: 0x009A [0x1C] WAIT(60* ticks)
  5: 0x009D [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  6: 0x00A0 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=LocalPlayer, tag_num=0x52)
  7: 0x00A7 [0x4E] SET_ENTITY_HIDE_FLAG: Show Katzun-Nattzun (ID: 17752286/0x010EE0DE)
  8: 0x00AD [0x80] LOAD_WAIT(entity=Katzun-Nattzun (ID: 17752286/0x010EE0DE))
  9: 0x00B2 [0x4A] LocalPlayer looks at Katzun-Nattzun (ID: 17752286/0x010EE0DE)
 10: 0x00BB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x00BC [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 12: 0x00C1 [0x79] Katzun-Nattzun (ID: 17752286/0x010EE0DE) looks at LocalPlayer (Basic look)
 13: 0x00CB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s097" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 14: 0x00DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 15: 0x00ED [0x1C] WAIT(60* ticks)
 16: 0x00F0 [0x1D] PRINT_EVENT_MESSAGE(message_id=10032*)
    → "Whaddaya want, whimperin' whipper-shnapper?"
 17: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x00F4 [0x52] END_LOAD_SCHEDULER: End scheduler "s097" with entities [LocalPlayer, LocalPlayer], work=211*
 19: 0x0103 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s098" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 20: 0x0114 [0x1D] PRINT_EVENT_MESSAGE(message_id=10033*)
    → "What? You shay you're wookin' for $6? Well, I can hewp you out in that department."
 21: 0x0117 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0118 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 23: 0x0129 [0x1C] WAIT(150* ticks)
 24: 0x012C [0x52] END_LOAD_SCHEDULER: End scheduler "s098" with entities [LocalPlayer, LocalPlayer], work=211*
 25: 0x013B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s099" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 26: 0x014C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 27: 0x015D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x07)
 28: 0x0164 [0x1D] PRINT_EVENT_MESSAGE(message_id=10034*)
    → "Ah-ha! Here it is!"
 29: 0x0167 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0168 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x08)
 31: 0x016F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x03)
 32: 0x0176 [0x1D] PRINT_EVENT_MESSAGE(message_id=10035*)
    → "Yesh...I remember the shtudent that wrote thish. A probwematic bugger-wugger that boy was."
 33: 0x0179 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x017A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x04)
 35: 0x0181 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x01E3
 36: 0x0189 [0x52] END_LOAD_SCHEDULER: End scheduler "s098" with entities [LocalPlayer, LocalPlayer], work=211*
 37: 0x0198 [0x03] Work_Zone[1] = 1*
 38: 0x019D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x01AE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s097" with entities [LocalPlayer, LocalPlayer], work=[211*, 0*]
 40: 0x01BF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x05)
 41: 0x01C6 [0x1D] PRINT_EVENT_MESSAGE(message_id=10036*)
    → "But that was a wong, wong time ago... Wait a minute. You anshered all the queshtions in QUIZ DE VANA'DIEW correctwy."
 42: 0x01C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x01CA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x06)
 44: 0x01D1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x07)
 45: 0x01D8 [0x1D] PRINT_EVENT_MESSAGE(message_id=10037*)
    → "You weren't cheat-sheetin' now, were you? Well, no matter. Here's your prize. You earned it."
 46: 0x01DB [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x01DC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x08)
 48: 0x01E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 49: 0x01F4 [0x1C] WAIT(60* ticks)
 50: 0x01F7 [0x02] IF !(Work_Zone[4] == 1*) GOTO 0x0211
 51: 0x01FF [0x52] END_LOAD_SCHEDULER: End scheduler "s097" with entities [LocalPlayer, LocalPlayer], work=211*
 52: 0x020E [0x01] GOTO 0x0220
 53: 0x0211 [0x52] END_LOAD_SCHEDULER: End scheduler "s099" with entities [LocalPlayer, LocalPlayer], work=211*

SUBROUTINE_0220:
 54: 0x0220 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x05)
 55: 0x0227 [0x46] CAMERA_CONTROL: Restore default settings
 56: 0x0229 [0x1C] WAIT(100* ticks)
 57: 0x022C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Katzun-Nattzun (ID: 17752286/0x010EE0DE), tag_num=0x06)
 58: 0x0233 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 59: 0x0244 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 60: 0x0246 [0x21] END_EVENT
 61: 0x0247 [0x00] END_REQSTACK()
```
