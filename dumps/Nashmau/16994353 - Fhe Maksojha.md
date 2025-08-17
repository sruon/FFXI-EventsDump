# 16994353 - Fhe Maksojha

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 576 bytes        |
| Total Events     | 14               |
| References Count | 29               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [12](#event-12)          | 0x0001       |     41 |              9 |
| [293](#event-293)        | 0x002A       |      1 |              1 |
| [65535.1](#event-655351) | 0x002B       |     39 |              9 |
| [65535.2](#event-655352) | 0x0052       |     10 |              2 |
| [65535.3](#event-655353) | 0x005C       |     14 |              4 |
| [294](#event-294)        | 0x006A       |      1 |              1 |
| [65535.4](#event-655354) | 0x006B       |     53 |              9 |
| [65535.5](#event-655355) | 0x00A0       |     14 |              4 |
| [65535.6](#event-655356) | 0x00AE       |     14 |              4 |
| [295](#event-295)        | 0x00BC       |     13 |              7 |
| [296](#event-296)        | 0x00C9       |     28 |              8 |
| [297](#event-297)        | 0x00E5       |    110 |             20 |
| [298](#event-298)        | 0x0153       |     47 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0008      |           8 |
|       1 | 0x2914      |       10516 |
|       2 | 0x0028      |          40 |
|       3 | 0x4085      |       16517 |
|       4 | 0x11DFB     |       73211 |
|       5 | 0xFFFFE891  |  4294961297 |
|       6 | 0x003C      |          60 |
|       7 | 0x3EEE      |       16110 |
|       8 | 0x13648     |       79432 |
|       9 | 0xFFFFE890  |  4294961296 |
|      10 | 0x3DBB      |       15803 |
|      11 | 0x116BD     |       71357 |
|      12 | 0x0932      |        2354 |
|      13 | 0x000D      |          13 |
|      14 | 0x3AE1      |       15073 |
|      15 | 0x11550     |       70992 |
|      16 | 0x4C29      |       19497 |
|      17 | 0x104C4     |       66756 |
|      18 | 0x4812      |       18450 |
|      19 | 0x10F3C     |       69436 |
|      20 | 0x2B99      |       11161 |
|      21 | 0x2BD7      |       11223 |
|      22 | 0x2BD8      |       11224 |
|      23 | 0x0032      |          50 |
|      24 | 0x2BD9      |       11225 |
|      25 | 0x2BDA      |       11226 |
|      26 | 0x2BDB      |       11227 |
|      27 | 0x00C9      |         201 |
|      28 | 0x0000      |           0 |

## String References

- **10516**: Ah! Y-you scared me! Sorry, I'm not with the Imperial Army. You need to talk to the guy in the shiny armor over there if you want Sanction.
- **11161**: Someone saw the old woman's son heading to the north of the Deadmist Marsh. The sooner you find him, the better...
- **11223**: You've got to go after that woman's son, or he'll be killed!
- **11224**: Ah, there you are! The old woman and her son made it back safely and rrreturned to Al Zahbi together.
- **11225**: Ahgdeen looked prrretty down, but he seemed somehow...stronger than before. Or maybe I'm just imagining things.
- **11226**: In any case, it's a wonder he made it back in one piece after being trrricked by a Lamia. That's certainly cause for celebration!
- **11227**: Speaking of which, his mother told me to give this to you. I hope you find some use for it.

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

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 41 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 61 77 77 30 1D  01 80 23 53 F8 FF FF 7F  ...aww0...#S....
0020: F8 FF FF 7F 61 77 77 30  21 00                    ....aww0!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "aww0" with entities [EventEntity, EventEntity], work=8*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=10516*)
    → "Ah! Y-you scared me! Sorry, I'm not with the Imperial Army. You need to talk to the guy in the shiny armor over there if you want Sanction."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aww0" with entities [EventEntity, EventEntity]
  7: 0x0028 [0x21] END_EVENT
  8: 0x0029 [0x00] END_REQSTACK()
```

### Event 293

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                00                           .     
```

#### Opcodes

```
  0: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 02 80 1F 00             2....
0030: 03 80 04 80 05 80 1F 01  4A 31 50 03 01 73 50 03  ........J1P..sP.
0040: 01 1C 06 80 32 02 80 1F  00 07 80 08 80 09 80 1F  ....2...........
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=16.517*, Z=73.211*, Y=-5.999*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x4A] Fhe Maksojha (ID: 16994353/0x01035031) looks at Wadayra (ID: 16994419/0x01035073)
  4: 0x0041 [0x1C] WAIT(60* ticks)
  5: 0x0044 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  6: 0x0047 [0x1F] MOVE_ENTITY: EventEntity moves to X=16.110*, Z=79.432*, Y=-6.000*
  7: 0x004F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0051 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0052   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:       37 0A 80 0B 80 05  80 0C 80 00                7.........    
```

#### Opcodes

```
  0: 0x0052 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=15.803*, z=71.357*, y=-5.999*, direction=206.9°*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 0D 80 1F              2...
0060: 00 0E 80 0F 80 09 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=15.073*, Z=70.992*, Y=-6.000*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x00] END_REQSTACK()
```

### Event 294

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 53 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   79 00 31 50 03             y.1P.
0070: 01 74 50 03 01 1C 06 80  79 00 31 50 03 01 73 50  .tP.....y.1P..sP
0080: 03 01 1C 06 80 79 00 31  50 03 01 74 50 03 01 1C  .....y.1P..tP...
0090: 06 80 79 00 31 50 03 01  73 50 03 01 1C 06 80 00  ..y.1P..sP......
```

#### Opcodes

```
  0: 0x006B [0x79] Fhe Maksojha (ID: 16994353/0x01035031) looks at Ahgdeen (ID: 16994420/0x01035074) (Basic look)
  1: 0x0075 [0x1C] WAIT(60* ticks)
  2: 0x0078 [0x79] Fhe Maksojha (ID: 16994353/0x01035031) looks at Wadayra (ID: 16994419/0x01035073) (Basic look)
  3: 0x0082 [0x1C] WAIT(60* ticks)
  4: 0x0085 [0x79] Fhe Maksojha (ID: 16994353/0x01035031) looks at Ahgdeen (ID: 16994420/0x01035074) (Basic look)
  5: 0x008F [0x1C] WAIT(60* ticks)
  6: 0x0092 [0x79] Fhe Maksojha (ID: 16994353/0x01035031) looks at Wadayra (ID: 16994419/0x01035073) (Basic look)
  7: 0x009C [0x1C] WAIT(60* ticks)
  8: 0x009F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0: 32 02 80 1F 00 10 80 11  80 09 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x00A0 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00A3 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.497*, Z=66.756*, Y=-6.000*
  2: 0x00AB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            32 02                2.
00B0: 80 1F 00 12 80 13 80 09  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x00AE [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00B1 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.450*, Z=69.436*, Y=-6.000*
  2: 0x00B9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BB [0x00] END_REQSTACK()
```

### Event 295

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      1E F0 FF FF              ....
00C0: 7F 6F 70 1D 14 80 23 21  00                       .op...#!.       
```

#### Opcodes

```
  0: 0x00BC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=11161*)
    → "Someone saw the old woman's son heading to the north of the Deadmist Marsh. The sooner you find him, the better..."
  4: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00C7 [0x21] END_EVENT
  6: 0x00C8 [0x00] END_REQSTACK()
```

### Event 296

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 6F 70           .....op
00D0: 66 00 80 F8 FF FF 7F F8  FF FF 7F 61 77 77 30 1D  f..........aww0.
00E0: 15 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00CF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "aww0" with entities [EventEntity, EventEntity], work=8*
  4: 0x00DF [0x1D] PRINT_EVENT_MESSAGE(message_id=11223*)
    → "You've got to go after that woman's son, or he'll be killed!"
  5: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E3 [0x21] END_EVENT
  7: 0x00E4 [0x00] END_REQSTACK()
```

### Event 297

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00E5    |
| Data Size    | 110 bytes |
| Instructions | 20        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                42 4A F0  FF FF 7F F8 FF FF 7F 1E       BJ.........
00F0: F0 FF FF 7F 6F 70 1D 16  80 23 66 17 80 F8 FF FF  ....op...#f.....
0100: 7F F8 FF FF 7F 74 68 6B  31 1D 18 80 23 66 17 80  .....thk1...#f..
0110: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 1D 19 80 23  ........thk2...#
0120: 1D 1A 80 23 66 17 80 F8  FF FF 7F F8 FF FF 7F 70  ...#f..........p
0130: 61 73 30 53 F8 FF FF 7F  F8 FF FF 7F 70 61 73 30  as0S........pas0
0140: 45 1B 80 F0 FF FF 7F F0  FF FF 7F 71 73 74 63 1C  E..........qstc.
0150: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x00E5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00E6 [0x4A] LocalPlayer looks at EventEntity
  2: 0x00EF [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00F4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x00F6 [0x1D] PRINT_EVENT_MESSAGE(message_id=11224*)
    → "Ah, there you are! The old woman and her son made it back safely and rrreturned to Al Zahbi together."
  6: 0x00F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00FA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  8: 0x0109 [0x1D] PRINT_EVENT_MESSAGE(message_id=11225*)
    → "Ahgdeen looked prrretty down, but he seemed somehow...stronger than before. Or maybe I'm just imagining things."
  9: 0x010C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x010D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
 11: 0x011C [0x1D] PRINT_EVENT_MESSAGE(message_id=11226*)
    → "In any case, it's a wonder he made it back in one piece after being trrricked by a Lamia. That's certainly cause for celebration!"
 12: 0x011F [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0120 [0x1D] PRINT_EVENT_MESSAGE(message_id=11227*)
    → "Speaking of which, his mother told me to give this to you. I hope you find some use for it."
 14: 0x0123 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x0124 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=50*
 16: 0x0133 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 17: 0x0140 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 18: 0x0151 [0x21] END_EVENT
 19: 0x0152 [0x00] END_REQSTACK()
```

### Event 298

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0153   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:          1E F0 FF FF 7F  6F 70 66 17 80 F8 FF FF     .....opf.....
0160: 7F F8 FF FF 7F 74 68 6B  31 1D 18 80 23 66 17 80  .....thk1...#f..
0170: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 1D 19 80 23  ........thk2...#
0180: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0153 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0158 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0159 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x015A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=50*
  4: 0x0169 [0x1D] PRINT_EVENT_MESSAGE(message_id=11225*)
    → "Ahgdeen looked prrretty down, but he seemed somehow...stronger than before. Or maybe I'm just imagining things."
  5: 0x016C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x016D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=50*
  7: 0x017C [0x1D] PRINT_EVENT_MESSAGE(message_id=11226*)
    → "In any case, it's a wonder he made it back in one piece after being trrricked by a Lamia. That's certainly cause for celebration!"
  8: 0x017F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0180 [0x21] END_EVENT
 10: 0x0181 [0x00] END_REQSTACK()
```
