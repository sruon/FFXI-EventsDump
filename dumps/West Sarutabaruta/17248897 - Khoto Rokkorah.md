# 17248897 - Khoto Rokkorah

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 660 bytes                   |
| Total Events     | 13                          |
| References Count | 21                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     69 |             12 |
| [65535.2](#event-655352)   | 0x0046       |      1 |              1 |
| [65535.3](#event-655353)   | 0x0047       |      1 |              1 |
| [65535.4](#event-655354)   | 0x0048       |     31 |              3 |
| [65535.5](#event-655355)   | 0x0067       |     30 |              8 |
| [65535.6](#event-655356)   | 0x0085       |     36 |              4 |
| [65535.7](#event-655357)   | 0x00A9       |     61 |              5 |
| [65535.8](#event-655358)   | 0x00E6       |     81 |             10 |
| [65535.9](#event-655359)   | 0x0137       |     29 |              3 |
| [65535.10](#event-6553510) | 0x0154       |     95 |             16 |
| [65535.11](#event-6553511) | 0x01B3       |      1 |              1 |
| [65535.12](#event-6553512) | 0x01B4       |     69 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003B      |          59 |
|       1 | 0x2C80      |       11392 |
|       2 | 0x2C81      |       11393 |
|       3 | 0x0028      |          40 |
|       4 | 0x005A      |          90 |
|       5 | 0x05F9      |        1529 |
|       6 | 0x052B      |        1323 |
|       7 | 0x000D      |          13 |
|       8 | 0x2ACA      |       10954 |
|       9 | 0x4EC8      |       20168 |
|      10 | 0xFFFFFC18  |  4294966296 |
|      11 | 0x00C8      |         200 |
|      12 | 0x0000      |           0 |
|      13 | 0x000F      |          15 |
|      14 | 0x001E      |          30 |
|      15 | 0x2CAD      |       11437 |
|      16 | 0x2CAE      |       11438 |
|      17 | 0x2CAF      |       11439 |
|      18 | 0x0078      |         120 |
|      19 | 0x2CCF      |       11471 |
|      20 | 0x2CD0      |       11472 |

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
| Data Size    | 69 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 79 00  81 32 07 01 F0 FF FF 7F   .....y..2......
0010: 66 00 80 81 32 07 01 81  32 07 01 74 6C 6B 30 2B  f...2...2..tlk0+
0020: 81 32 07 01 01 80 23 2B  81 32 07 01 02 80 23 1C  .2....#+.2....#.
0030: 03 80 66 00 80 81 32 07  01 81 32 07 01 74 6C 6B  ..f...2...2..tlk
0040: 31 1C 04 80 21 00                                 1...!.          
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x79] Khoto Rokkorah (ID: 17248897/0x01073281) looks at LocalPlayer (Basic look)
  2: 0x0010 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
  3: 0x001F [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11392*]:
    → "Hello! Have you come to hear a tale?"
  4: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0027 [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11393*]:
    → "I'm a storyteller, and I often entertain the children here with fantastic yarns and magical myths."
  6: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002F [0x1C] WAIT(40* ticks)
  8: 0x0032 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
  9: 0x0041 [0x1C] WAIT(90* ticks)
 10: 0x0044 [0x21] END_EVENT
 11: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 31 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          5B 05 80 81 32 07 01 81          [...2...
0050: 32 07 01 68 6F 6E 31 5B  06 80 80 32 07 01 80 32  2..hon1[...2...2
0060: 07 01 68 6F 6E 31 00                              ..hon1.         
```

#### Opcodes

```
  0: 0x0048 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon1" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=1529*
  1: 0x0057 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon1" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  2: 0x0066 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0067   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                      32  07 80 1F 00 08 80 09 80         2........
0070: 0A 80 1F 01 6F 4A 81 32  07 01 82 32 07 01 6F 76  ....oJ.2...2..ov
0080: 81 32 07 01 00                                    .2...           
```

#### Opcodes

```
  0: 0x0067 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006A [0x1F] MOVE_ENTITY: EventEntity moves to X=10.954*, Z=20.168*, Y=-1.000*
  2: 0x0072 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0075 [0x4A] Khoto Rokkorah (ID: 17248897/0x01073281) looks at Tihk Rhumyie (ID: 17248898/0x01073282)
  5: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x007F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Khoto Rokkorah (ID: 17248897/0x01073281) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                3A 81 32  07 01 00 00 BA 80 32 07       :.2......2.
0090: 01 08 80 09 80 0A 80 00  00 5B 06 80 80 32 07 01  .........[...2..
00A0: 80 32 07 01 68 6F 6E 30  00                       .2..hon0.       
```

#### Opcodes

```
  0: 0x0085 [0x3A] CONVERT_YAW_TO_BYTE(entity=Khoto Rokkorah (ID: 17248897/0x01073281), result_destination=ExtData[1]->WorkLocal[0])
  1: 0x008C [0xBA] SET_ENTITY_POSITION(entity_id=Unnamed NPC (ID: 17248896/0x01073280), pos_x=10.954*, pos_z=20.168*, pos_y=-1.000*, direction=ExtData[1]->WorkLocal[0])
  2: 0x0099 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon0" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  3: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 61 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             5B 06 80 80 32 07 01           [...2..
00B0: 80 32 07 01 68 6F 6E 31  5B 05 80 81 32 07 01 81  .2..hon1[...2...
00C0: 32 07 01 68 6F 6E 31 5B  06 80 80 32 07 01 80 32  2..hon1[...2...2
00D0: 07 01 68 6F 6E 32 5B 05  80 81 32 07 01 81 32 07  ..hon2[...2...2.
00E0: 01 68 6F 6E 32 00                                 .hon2.          
```

#### Opcodes

```
  0: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon1" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  1: 0x00B8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon1" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=1529*
  2: 0x00C7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon2" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  3: 0x00D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon2" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=1529*
  4: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 81 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   45 0B  80 F0 FF FF 7F F0 FF FF        E.........
00F0: 7F 62 6C 6F 66 0C 80 1C  0D 80 80 80 32 07 01 80  .blof.......2...
0100: 81 32 07 01 5B 06 80 80  32 07 01 80 32 07 01 68  .2..[...2...2..h
0110: 6F 6E 30 5B 05 80 81 32  07 01 81 32 07 01 68 6F  on0[...2...2..ho
0120: 6C 32 5B 06 80 80 32 07  01 80 32 07 01 68 6F 6C  l2[...2...2..hol
0130: 32 1C 0D 80 AB 0A 00                              2......         
```

#### Opcodes

```
  0: 0x00E6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "blof" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  1: 0x00F7 [0x1C] WAIT(15* ticks)
  2: 0x00FA [0x80] LOAD_WAIT(entity=Unnamed NPC (ID: 17248896/0x01073280))
  3: 0x00FF [0x80] LOAD_WAIT(entity=Khoto Rokkorah (ID: 17248897/0x01073281))
  4: 0x0104 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon0" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  5: 0x0113 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hol2" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=1529*
  6: 0x0122 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hol2" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  7: 0x0131 [0x1C] WAIT(15* ticks)
  8: 0x0134 [0xAB] EventEntity->UnknownFlag = 0 // Disable unknown flag
  9: 0x0136 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0137   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                      5B  06 80 80 32 07 01 80 32         [...2...2
0140: 07 01 68 6F 6E 30 53 80  32 07 01 80 32 07 01 68  ..hon0S.2...2..h
0150: 6F 6E 30 00                                       on0.            
```

#### Opcodes

```
  0: 0x0137 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hon0" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)], work=1323*
  1: 0x0146 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hon0" with entities [Unnamed NPC (ID: 17248896/0x01073280), Unnamed NPC (ID: 17248896/0x01073280)]
  2: 0x0153 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0154   |
| Data Size    | 95 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             1E F0 FF FF  7F 1C 0E 80 66 00 80 81      ........f...
0160: 32 07 01 81 32 07 01 74  6C 6B 30 79 00 81 32 07  2...2..tlk0y..2.
0170: 01 F0 FF FF 7F 2B 81 32  07 01 0F 80 23 2B 81 32  .....+.2....#+.2
0180: 07 01 10 80 23 1C 03 80  66 00 80 81 32 07 01 81  ....#...f...2...
0190: 32 07 01 74 68 6B 31 2B  81 32 07 01 11 80 23 1C  2..thk1+.2....#.
01A0: 12 80 66 00 80 81 32 07  01 81 32 07 01 74 68 6B  ..f...2...2..thk
01B0: 32 21 00                                          2!.             
```

#### Opcodes

```
  0: 0x0154 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0159 [0x1C] WAIT(30* ticks)
  2: 0x015C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
  3: 0x016B [0x79] Khoto Rokkorah (ID: 17248897/0x01073281) looks at LocalPlayer (Basic look)
  4: 0x0175 [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11437*]:
    → "I still can't get "The Adventures of Babban Ny Mheillea" out of my mind."
  5: 0x017C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x017D [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11438*]:
    → "The realistic harshness makes me wonder..."
  7: 0x0184 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0185 [0x1C] WAIT(40* ticks)
  9: 0x0188 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
 10: 0x0197 [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11439*]:
    → "Could this fable be based on a true story...?"
 11: 0x019E [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x019F [0x1C] WAIT(120* ticks)
 13: 0x01A2 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
 14: 0x01B1 [0x21] END_EVENT
 15: 0x01B2 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:          00                                          .            
```

#### Opcodes

```
  0: 0x01B3 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B4   |
| Data Size    | 69 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             1E F0 FF FF  7F 79 00 81 32 07 01 F0      .....y..2...
01C0: FF FF 7F 66 00 80 81 32  07 01 81 32 07 01 74 6C  ...f...2...2..tl
01D0: 6B 30 2B 81 32 07 01 13  80 23 2B 81 32 07 01 14  k0+.2....#+.2...
01E0: 80 23 1C 03 80 66 00 80  81 32 07 01 81 32 07 01  .#...f...2...2..
01F0: 74 6C 6B 31 1C 04 80 21  00                       tlk1...!.       
```

#### Opcodes

```
  0: 0x01B4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01B9 [0x79] Khoto Rokkorah (ID: 17248897/0x01073281) looks at LocalPlayer (Basic look)
  2: 0x01C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
  3: 0x01D2 [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11471*]:
    → "Hello, <Player>!"
  4: 0x01D9 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x01DA [0x2B] Khoto Rokkorah (ID: 17248897/0x01073281) [11472*]:
    → "Just you wait! One day I'll be the best storyteller this town has ever seen!"
  6: 0x01E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x01E2 [0x1C] WAIT(40* ticks)
  8: 0x01E5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Khoto Rokkorah (ID: 17248897/0x01073281), Khoto Rokkorah (ID: 17248897/0x01073281)], work=59*
  9: 0x01F4 [0x1C] WAIT(90* ticks)
 10: 0x01F7 [0x21] END_EVENT
 11: 0x01F8 [0x00] END_REQSTACK()
```
