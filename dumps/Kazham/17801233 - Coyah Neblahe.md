# 17801233 - Coyah Neblahe

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Kazham (ID: 250) |
| Block Size       | 552 bytes        |
| Total Events     | 16               |
| References Count | 14               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     22 |              3 |
| [65535.6](#event-655356)   | 0x005B       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0069       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0079       |     20 |              3 |
| [65535.9](#event-655359)   | 0x008D       |     16 |              2 |
| [65535.10](#event-6553510) | 0x009D       |     14 |              2 |
| [65535.11](#event-6553511) | 0x00AB       |      9 |              3 |
| [156](#event-156)          | 0x00B4       |     47 |             14 |
| [157](#event-157)          | 0x00E3       |     47 |             14 |
| [158](#event-158)          | 0x0112       |     80 |             22 |
| [159](#event-159)          | 0x0162       |     62 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x0034      |          52 |
|       3 | 0x0008      |           8 |
|       4 | 0x2732      |       10034 |
|       5 | 0x2733      |       10035 |
|       6 | 0x284E      |       10318 |
|       7 | 0x284F      |       10319 |
|       8 | 0x2856      |       10326 |
|       9 | 0x2857      |       10327 |
|      10 | 0x0000      |           0 |
|      11 | 0x2858      |       10328 |
|      12 | 0x2859      |       10329 |
|      13 | 0x285A      |       10330 |

## String References

- **10034**: Hey, you're an adventurer, arrren't you? I wouldn't want you to get lost. Let me give you a little help.
- **10035**: The jungle rrright outside the village gates is the Yuhtunga Jungle. To the south of the Yuhtunga Jungle is the Yhoator Jungle. Did you get all that?
- **10318**: Hey, did you find a piece of paper lying around anywherrre?
- **10319**: I put up a warning posterrr for adventurerrrs, but I think it's fallen off...
- **10326**: That piece of paperrr you're holding. I've seen that beforrre.
- **10327**: I wrote that to warn adventurerrrs to stay away from Rafflesia flowerrrs that are full of pollen.
- **10328**: If you get enough of that foul-smelling stuff on you, you'll have a whole lot less friends. Trust me.
- **10329**: I'd stay away from Rafflesia flowerrrs if I were you. If you get enough of that foul-smelling pollen on you, you'll have a whole lot less friends. Trust me.
- **10330**: I'm thinking about writing a warning to tell adventurers that they should stay away from Rafflesia flowerrrs that are full of pollen.

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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
0020:                      66  02 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 64 69 73 30 00                              ..dis0.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
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
0040: 64 69 73 30 00                                    dis0.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                81 00 F8  FF FF 7F 66 00 80 F8 FF       ......f....
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x0045 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x004B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   53 F8 FF FF 7F             S....
0060: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             66 00 80 F8 FF FF 7F           f......
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 74 68 6B 32 81 01  F8 FF FF 7F 00           ..thk2.......   
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         66 03 80               f..
0090: F8 FF FF 7F F8 FF FF 7F  75 72 65 30 00           ........ure0.   
```

#### Opcodes

```
  0: 0x008D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ure0" with entities [EventEntity, EventEntity], work=8*
  1: 0x009C [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         53 F8 FF               S..
00A0: FF 7F F8 FF FF 7F 75 72  65 30 00                 ......ure0.     
```

#### Opcodes

```
  0: 0x009D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ure0" with entities [EventEntity, EventEntity]
  1: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AB  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   5E 69 64 6C 30             ^idl0
00B0: 1C 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x00AB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00B0 [0x1C] WAIT(30* ticks)
  2: 0x00B3 [0x00] END_REQSTACK()
```

### Event 156

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             1E F0 FF FF  7F 6F 70 29 08 11 A0 0F      .....op)....
00C0: 01 05 1D 04 80 23 29 08  11 A0 0F 01 06 29 08 11  .....#)......)..
00D0: A0 0F 01 07 1D 05 80 23  29 08 11 A0 0F 01 08 20  .......#)...... 
00E0: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x00B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00BA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00BB [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x05)
  4: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10034*)
    → "Hey, you're an adventurer, arrren't you? I wouldn't want you to get lost. Let me give you a little help."
  5: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00C6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x06)
  7: 0x00CD [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x07)
  8: 0x00D4 [0x1D] PRINT_EVENT_MESSAGE(message_id=10035*)
    → "The jungle rrright outside the village gates is the Yuhtunga Jungle. To the south of the Yuhtunga Jungle is the Yhoator Jungle. Did you get all that?"
  9: 0x00D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00D8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x08)
 11: 0x00DF [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x00E1 [0x21] END_EVENT
 13: 0x00E2 [0x00] END_REQSTACK()
```

### Event 157

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E3   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:          1E F0 FF FF 7F  6F 70 29 08 11 A0 0F 01     .....op).....
00F0: 05 1D 06 80 23 29 08 11  A0 0F 01 06 29 08 11 A0  ....#)......)...
0100: 0F 01 07 1D 07 80 23 29  08 11 A0 0F 01 08 20 00  ......#)...... .
0110: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00E3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00E8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00E9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00EA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x05)
  4: 0x00F1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10318*)
    → "Hey, did you find a piece of paper lying around anywherrre?"
  5: 0x00F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00F5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x06)
  7: 0x00FC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x07)
  8: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=10319*)
    → "I put up a warning posterrr for adventurerrrs, but I think it's fallen off..."
  9: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0107 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x08)
 11: 0x010E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0110 [0x21] END_EVENT
 13: 0x0111 [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0112   |
| Data Size    | 80 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       1E F0 FF FF 7F 6F  70 29 08 11 A0 0F 01 05    .....op)......
0120: 1D 08 80 23 29 08 11 A0  0F 01 06 29 08 11 A0 0F  ...#)......)....
0130: 01 07 1D 09 80 23 29 08  11 A0 0F 01 08 29 08 11  .....#)......)..
0140: A0 0F 01 01 02 05 10 0A  80 00 53 01 1D 0B 80 23  ..........S....#
0150: 01 57 01 1D 0C 80 23 29  08 11 A0 0F 01 02 20 00  .W....#)...... .
0160: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0112 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0117 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0118 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0119 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x05)
  4: 0x0120 [0x1D] PRINT_EVENT_MESSAGE(message_id=10326*)
    → "That piece of paperrr you're holding. I've seen that beforrre."
  5: 0x0123 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0124 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x06)
  7: 0x012B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x07)
  8: 0x0132 [0x1D] PRINT_EVENT_MESSAGE(message_id=10327*)
    → "I wrote that to warn adventurerrrs to stay away from Rafflesia flowerrrs that are full of pollen."
  9: 0x0135 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0136 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x08)
 11: 0x013D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x01)
 12: 0x0144 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x0153
 13: 0x014C [0x1D] PRINT_EVENT_MESSAGE(message_id=10328*)
    → "If you get enough of that foul-smelling stuff on you, you'll have a whole lot less friends. Trust me."
 14: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0150 [0x01] GOTO 0x0157
 16: 0x0153 [0x1D] PRINT_EVENT_MESSAGE(message_id=10329*)
    → "I'd stay away from Rafflesia flowerrrs if I were you. If you get enough of that foul-smelling pollen on you, you'll have a whole lot less friends. Trust me."
 17: 0x0156 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0157:
 18: 0x0157 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x02)
 19: 0x015E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x0160 [0x21] END_EVENT
 21: 0x0161 [0x00] END_REQSTACK()
```

### Event 159

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0162   |
| Data Size    | 62 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:       1E F0 FF FF 7F 6F  70 29 08 11 A0 0F 01 05    .....op)......
0170: 1D 0D 80 23 29 08 11 A0  0F 01 06 29 08 11 A0 0F  ...#)......)....
0180: 01 07 02 05 10 0A 80 00  91 01 1D 0B 80 23 01 95  .............#..
0190: 01 1D 0C 80 23 29 08 11  A0 0F 01 08 20 00 21 00  ....#)...... .!.
```

#### Opcodes

```
  0: 0x0162 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0167 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0168 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0169 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x05)
  4: 0x0170 [0x1D] PRINT_EVENT_MESSAGE(message_id=10330*)
    → "I'm thinking about writing a warning to tell adventurers that they should stay away from Rafflesia flowerrrs that are full of pollen."
  5: 0x0173 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0174 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x06)
  7: 0x017B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x07)
  8: 0x0182 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x0191
  9: 0x018A [0x1D] PRINT_EVENT_MESSAGE(message_id=10328*)
    → "If you get enough of that foul-smelling stuff on you, you'll have a whole lot less friends. Trust me."
 10: 0x018D [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x018E [0x01] GOTO 0x0195
 12: 0x0191 [0x1D] PRINT_EVENT_MESSAGE(message_id=10329*)
    → "I'd stay away from Rafflesia flowerrrs if I were you. If you get enough of that foul-smelling pollen on you, you'll have a whole lot less friends. Trust me."
 13: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0195:
 14: 0x0195 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Coyah Neblahe (ID: 17801233/0x010FA011), tag_num=0x08)
 15: 0x019C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x019E [0x21] END_EVENT
 17: 0x019F [0x00] END_REQSTACK()
```
