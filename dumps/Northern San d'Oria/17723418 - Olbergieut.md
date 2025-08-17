# 17723418 - Olbergieut

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 644 bytes                     |
| Total Events     | 9                             |
| References Count | 27                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     28 |              8 |
| [65](#event-65)          | 0x002D       |      1 |              1 |
| [62](#event-62)          | 0x002E       |      1 |              1 |
| [612](#event-612)        | 0x002F       |     94 |             16 |
| [619](#event-619)        | 0x008D       |    210 |             36 |
| [620](#event-620)        | 0x015F       |    112 |             18 |
| [16](#event-16)          | 0x01CF       |     18 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x21EF1     |      138993 |
|       1 | 0x2115B     |      135515 |
|       2 | 0x0000      |           0 |
|       3 | 0x020F      |         527 |
|       4 | 0x000D      |          13 |
|       5 | 0x211A7     |      135591 |
|       6 | 0x2188F     |      137359 |
|       7 | 0x20D4C     |      134476 |
|       8 | 0x215FD     |      136701 |
|       9 | 0x012D      |         301 |
|      10 | 0x0014      |          20 |
|      11 | 0x2C26      |       11302 |
|      12 | 0x001E      |          30 |
|      13 | 0x2BBA      |       11194 |
|      14 | 0x2C27      |       11303 |
|      15 | 0x2C28      |       11304 |
|      16 | 0x2BE8      |       11240 |
|      17 | 0x0097      |         151 |
|      18 | 0x2C2A      |       11306 |
|      19 | 0x0001      |           1 |
|      20 | 0x2C29      |       11305 |
|      21 | 0x40000000  |  1073741824 |
|      22 | 0x2C2C      |       11308 |
|      23 | 0x00C9      |         201 |
|      24 | 0x1D3F9     |      119801 |
|      25 | 0x1C8B0     |      116912 |
|      26 | 0x0207      |         519 |

## String References

- **11194**: May Paradise open its gates to you.
- **11240**: Well? [I accept./I must decline.]
- **11302**: In this chamber we study the teachings of Altana. Through years of prayer and devotion have we earned this right.
- **11303**: By the way, I have heard of your deeds, and I would ask of you a trivial favor.
- **11304**: One of our order is on retreat at the Crag of Holla. Might you take him scrolls for his next circle?
- **11305**: How unfortunate! I fear your place in Paradise may be in jeopardy.
- **11306**: Great is the generosity in your heart! Take $6 and carry it to Friar Faurbellant at the Crag of Holla.
- **11308**: Gracious are we for your service. Receive this as acknowledgment of your devotion.

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

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=138.993*, z=135.515*, y=0.000*, direction=46.3°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 1F 00   2..............
0020: 07 80 08 80 02 80 1F 01  6F 39 09 80 00           ........o9...   
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=135.591*, Z=137.359*, Y=0.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=134.476*, Z=136.701*, Y=0.000*
  4: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0029 [0x39] SET_ENTITY_DIRECTION(direction=1.7°*)
  7: 0x002C [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         00                     .  
```

#### Opcodes

```
  0: 0x002D [0x00] END_REQSTACK()
```

### Event 62

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 612

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 94 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1E                 .
0030: F0 FF FF 7F 6F 70 5B 0A  80 F8 FF FF 7F F8 FF FF  ....op[.........
0040: 7F 74 6C 6B 30 1D 0B 80  23 5B 0A 80 F8 FF FF 7F  .tlk0...#[......
0050: F8 FF FF 7F 74 6C 6B 31  53 F8 FF FF 7F F8 FF FF  ....tlk1S.......
0060: 7F 74 6C 6B 31 1C 0C 80  5B 0A 80 F8 FF FF 7F F8  .tlk1...[.......
0070: FF FF 7F 69 6E 6F 30 1D  0D 80 23 53 F8 FF FF 7F  ...ino0...#S....
0080: F8 FF FF 7F 69 6E 6F 30  1C 0C 80 21 00           ....ino0...!.   
```

#### Opcodes

```
  0: 0x002F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0034 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0035 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0036 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=11302*)
    → "In this chamber we study the teachings of Altana. Through years of prayer and devotion have we earned this right."
  5: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0049 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  7: 0x0058 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x0065 [0x1C] WAIT(30* ticks)
  9: 0x0068 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 10: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=11194*)
    → "May Paradise open its gates to you."
 11: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 13: 0x0088 [0x1C] WAIT(30* ticks)
 14: 0x008B [0x21] END_EVENT
 15: 0x008C [0x00] END_REQSTACK()
```

### Event 619

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x008D    |
| Data Size    | 210 bytes |
| Instructions | 36        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         1E F0 FF               ...
0090: FF 7F 6F 70 5B 0A 80 F8  FF FF 7F F8 FF FF 7F 74  ..op[..........t
00A0: 6C 6B 30 1D 0B 80 23 1C  0C 80 1D 0E 80 23 1C 0C  lk0...#......#..
00B0: 80 1D 0F 80 23 5B 0A 80  F8 FF FF 7F F8 FF FF 7F  ....#[..........
00C0: 74 6C 6B 31 53 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  tlk1S........tlk
00D0: 31 24 10 80 02 80 02 80  25 02 00 10 02 80 00 1B  1$......%.......
00E0: 01 5B 0A 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .[..........tlk0
00F0: 03 02 10 11 80 1D 12 80  23 5B 0A 80 F8 FF FF 7F  ........#[......
0100: F8 FF FF 7F 74 6C 6B 31  53 F8 FF FF 7F F8 FF FF  ....tlk1S.......
0110: 7F 74 6C 6B 31 1C 0C 80  01 5D 01 02 00 10 13 80  .tlk1....]......
0120: 00 5D 01 5B 0A 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .].[..........tl
0130: 6B 30 1D 14 80 23 5B 0A  80 F8 FF FF 7F F8 FF FF  k0...#[.........
0140: 7F 74 6C 6B 31 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlk1S........tl
0150: 6B 31 1C 0C 80 03 01 10  15 80 01 5D 01 21 00     k1.........].!. 
```

#### Opcodes

```
  0: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0092 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0093 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0094 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=11302*)
    → "In this chamber we study the teachings of Altana. Through years of prayer and devotion have we earned this right."
  5: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A7 [0x1C] WAIT(30* ticks)
  7: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=11303*)
    → "By the way, I have heard of your deeds, and I would ask of you a trivial favor."
  8: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00AE [0x1C] WAIT(30* ticks)
 10: 0x00B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=11304*)
    → "One of our order is on retreat at the Crag of Holla. Might you take him scrolls for his next circle?"
 11: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00B5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 13: 0x00C4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 14: 0x00D1 [0x24] CREATE_DIALOG(message_id=11240*, default_option=0*, option_flags=0*)
    → "Well? [I accept./I must decline.]"
 15: 0x00D8 [0x25] WAIT_DIALOG_SELECT()
 16: 0x00D9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x011B
 17: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 18: 0x00F0 [0x03] Work_Zone[2] = 151*
 19: 0x00F5 [0x1D] PRINT_EVENT_MESSAGE(message_id=11306*)
    → "Great is the generosity in your heart! Take $6 and carry it to Friar Faurbellant at the Crag of Holla."
 20: 0x00F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x00F9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 22: 0x0108 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 23: 0x0115 [0x1C] WAIT(30* ticks)
 24: 0x0118 [0x01] GOTO 0x015D
 25: 0x011B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x015D
 26: 0x0123 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
 27: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=11305*)
    → "How unfortunate! I fear your place in Paradise may be in jeopardy."
 28: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x0136 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 30: 0x0145 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 31: 0x0152 [0x1C] WAIT(30* ticks)
 32: 0x0155 [0x03] Work_Zone[1] = 1073741824*
 33: 0x015A [0x01] GOTO 0x015D

SUBROUTINE_015D:
 34: 0x015D [0x21] END_EVENT
 35: 0x015E [0x00] END_REQSTACK()
```

### Event 620

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x015F    |
| Data Size    | 112 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                               42                 B
0160: 1E F0 FF FF 7F 6F 70 5B  0A 80 F8 FF FF 7F F8 FF  .....op[........
0170: FF 7F 74 6C 6B 30 1D 16  80 23 5B 0A 80 F8 FF FF  ..tlk0...#[.....
0180: 7F F8 FF FF 7F 74 6C 6B  31 53 F8 FF FF 7F F8 FF  .....tlk1S......
0190: FF 7F 74 6C 6B 31 1C 0C  80 5B 0A 80 F8 FF FF 7F  ..tlk1...[......
01A0: F8 FF FF 7F 69 6E 6F 30  1D 0D 80 23 53 F8 FF FF  ....ino0...#S...
01B0: 7F F8 FF FF 7F 69 6E 6F  30 45 17 80 F0 FF FF 7F  .....ino0E......
01C0: F0 FF FF 7F 71 73 74 63  02 80 1C 0C 80 21 00     ....qstc.....!. 
```

#### Opcodes

```
  0: 0x015F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0160 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0165 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0166 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0167 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0176 [0x1D] PRINT_EVENT_MESSAGE(message_id=11308*)
    → "Gracious are we for your service. Receive this as acknowledgment of your devotion."
  6: 0x0179 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x017A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  8: 0x0189 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  9: 0x0196 [0x1C] WAIT(30* ticks)
 10: 0x0199 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ino0" with entities [EventEntity, EventEntity], work=20*
 11: 0x01A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=11194*)
    → "May Paradise open its gates to you."
 12: 0x01AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x01AC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ino0" with entities [EventEntity, EventEntity]
 14: 0x01B9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 15: 0x01CA [0x1C] WAIT(30* ticks)
 16: 0x01CD [0x21] END_EVENT
 17: 0x01CE [0x00] END_REQSTACK()
```

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01CF   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                                               22                 "
01D0: 00 92 01 F8 FF FF 7F 37  18 80 19 80 02 80 1A 80  .......7........
01E0: 00                                                .               
```

#### Opcodes

```
  0: 0x01CF [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x01D1 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x01D7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=119.801*, z=116.912*, y=0.000*, direction=45.6°*
  3: 0x01E0 [0x00] END_REQSTACK()
```
