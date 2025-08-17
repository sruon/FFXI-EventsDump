# 16982135 - Tohka Telposkha

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 528 bytes                     |
| Total Events     | 22                            |
| References Count | 29                            |

## List of Events

| Event ID                    | Entrypoint   |   Size |   Instructions |
|-----------------------------|--------------|--------|----------------|
| [65535](#event-65535)       | 0x0000       |      1 |              1 |
| [663](#event-663)           | 0x0001       |    153 |             27 |
| [810](#event-810)           | 0x009A       |      1 |              1 |
| [65535.1](#event-65535-1)   | 0x009B       |     10 |              2 |
| [65535.2](#event-65535-2)   | 0x00A5       |     23 |              5 |
| [65535.3](#event-65535-3)   | 0x00BC       |     23 |              5 |
| [65535.4](#event-65535-4)   | 0x00D3       |     23 |              5 |
| [65535.5](#event-65535-5)   | 0x00EA       |     23 |              5 |
| [65535.6](#event-65535-6)   | 0x0101       |      4 |              2 |
| [65535.7](#event-65535-7)   | 0x0105       |      4 |              2 |
| [65535.8](#event-65535-8)   | 0x0109       |      2 |              2 |
| [836](#event-836)           | 0x010B       |      1 |              1 |
| [838](#event-838)           | 0x010C       |      1 |              1 |
| [845](#event-845)           | 0x010D       |      1 |              1 |
| [5071](#event-5071)         | 0x010E       |      1 |              1 |
| [5073](#event-5073)         | 0x010F       |      1 |              1 |
| [5075](#event-5075)         | 0x0110       |      1 |              1 |
| [5076](#event-5076)         | 0x0111       |      1 |              1 |
| [5077](#event-5077)         | 0x0112       |      1 |              1 |
| [5078](#event-5078)         | 0x0113       |      1 |              1 |
| [65535.9](#event-65535-9)   | 0x0114       |     14 |              4 |
| [65535.10](#event-65535-10) | 0x0122       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0035      |          53 |
|       2 | 0x18D3      |        6355 |
|       3 | 0x18D4      |        6356 |
|       4 | 0x0000      |           0 |
|       5 | 0x0034      |          52 |
|       6 | 0x18D5      |        6357 |
|       7 | 0x18D6      |        6358 |
|       8 | 0x18D7      |        6359 |
|       9 | 0x0001      |           1 |
|      10 | 0x0044      |          68 |
|      11 | 0x18D8      |        6360 |
|      12 | 0x4650      |       18000 |
|      13 | 0x4574      |       17780 |
|      14 | 0x0EE7      |        3815 |
|      15 | 0x000D      |          13 |
|      16 | 0x4397      |       17303 |
|      17 | 0x438D      |       17293 |
|      18 | 0x42E0      |       17120 |
|      19 | 0x4699      |       18073 |
|      20 | 0x4561      |       17761 |
|      21 | 0x484B      |       18507 |
|      22 | 0x4B33      |       19251 |
|      23 | 0x45E6      |       17894 |
|      24 | 0xFFF74707  |  4294395655 |
|      25 | 0x9194      |       37268 |
|      26 | 0x07CF      |        1999 |
|      27 | 0xFFF754EB  |  4294399211 |
|      28 | 0x7E28      |       32296 |

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

### Event 663

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 153 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 62 31  1D 02 80 23 66 01 80 F8  ....tlb1...#f...
0020: FF FF 7F F8 FF FF 7F 74  6C 62 32 24 03 80 04 80  .......tlb2$....
0030: 04 80 25 02 00 10 04 80  00 68 00 66 05 80 F8 FF  ..%......h.f....
0040: FF 7F F8 FF FF 7F 74 6C  63 30 1D 06 80 23 1D 07  ......tlc0...#..
0050: 80 23 1D 08 80 23 66 05  80 F8 FF FF 7F F8 FF FF  .#...#f.........
0060: 7F 74 6C 63 31 01 95 00  02 00 10 09 80 00 95 00  .tlc1...........
0070: 66 0A 80 F8 FF FF 7F F8  FF FF 7F 74 6C 62 30 1D  f..........tlb0.
0080: 0B 80 23 66 0A 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  ..#f..........tl
0090: 62 31 01 95 00 1C 00 80  21 00                    b1......!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=53*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=6355*)
    → "You wouldn't happen to want to hear a juicy secrrret about Naja Salaheem, would you? Well?\u007F1\u0000\u0007"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb2" with entities [EventEntity, EventEntity], work=53*
  6: 0x002B [0x24] CREATE_DIALOG(message_id=6356*, default_option=0*, option_flags=0*)
    → "Ask her about Naja's secret?\u0007\u000BFill me in!\u0007How childish...\u007F1\u0000\u0007"
  7: 0x0032 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0033 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0068
  9: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=52*
 10: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=6357*)
    → "Naja's famous for her money-grrrubbing tendencies. They say she refused to go in debt, even a single bronze piece, when founding Salaheem's Sentinels.\u007F1\u0000\u0007"
 11: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x004E [0x1D] PRINT_EVENT_MESSAGE(message_id=6358*)
    → "Everrryone's whispering about how she managed to raise so much capital at such a young age...\u007F1\u0000\u0007"
 13: 0x0051 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=6359*)
    → "Personally, I think there's something to that giant club she carries arrround with her, but there's got to be more to it than that...\u007F1\u0000\u0007"
 15: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=52*
 17: 0x0065 [0x01] GOTO 0x0095
 18: 0x0068 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0095
 19: 0x0070 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=68*
 20: 0x007F [0x1D] PRINT_EVENT_MESSAGE(message_id=6360*)
    → "Are you surrre? Fine. Your loss.\u007F1\u0000\u0007"
 21: 0x0082 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0083 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=68*
 23: 0x0092 [0x01] GOTO 0x0095

SUBROUTINE_0095:
 24: 0x0095 [0x1C] WAIT(30* ticks)
 25: 0x0098 [0x21] END_EVENT
 26: 0x0099 [0x00] END_REQSTACK()
```

### Event 810

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                00                           .     
```

#### Opcodes

```
  0: 0x009A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   37 0C 80 0D 80             7....
00A0: 04 80 0E 80 00                                    .....           
```

#### Opcodes

```
  0: 0x009B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.000*, z=17.780*, y=0.000*, direction=335.3°*
  1: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A5   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                32 0F 80  1F 00 10 80 11 80 04 80       2..........
00B0: 1F 01 4A 77 20 03 01 F0  FF FF 7F 00              ..Jw .......    
```

#### Opcodes

```
  0: 0x00A5 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00A8 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.303*, Z=17.293*, Y=0.000*
  2: 0x00B0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B2 [0x4A] Tohka Telposkha (ID: 16982135/0x01032077) looks at LocalPlayer
  4: 0x00BB [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BC   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      32 0F 80 1F              2...
00C0: 00 12 80 13 80 04 80 1F  01 4A 77 20 03 01 F0 FF  .........Jw ....
00D0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x00BC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BF [0x1F] MOVE_ENTITY: EventEntity moves to X=17.120*, Z=18.073*, Y=0.000*
  2: 0x00C7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C9 [0x4A] Tohka Telposkha (ID: 16982135/0x01032077) looks at LocalPlayer
  4: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          32 0F 80 1F 00  14 80 15 80 04 80 1F 01     2............
00E0: 4A 77 20 03 01 76 20 03  01 00                    Jw ..v ...      
```

#### Opcodes

```
  0: 0x00D3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D6 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.761*, Z=18.507*, Y=0.000*
  2: 0x00DE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E0 [0x4A] Tohka Telposkha (ID: 16982135/0x01032077) looks at Kubhe Ijyuhla (ID: 16982134/0x01032076)
  4: 0x00E9 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EA   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                32 0F 80 1F 00 16            2.....
00F0: 80 17 80 04 80 1F 01 4A  77 20 03 01 0B 21 03 01  .......Jw ...!..
0100: 00                                                .               
```

#### Opcodes

```
  0: 0x00EA [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00ED [0x1F] MOVE_ENTITY: EventEntity moves to X=19.251*, Z=17.894*, Y=0.000*
  2: 0x00F5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F7 [0x4A] Tohka Telposkha (ID: 16982135/0x01032077) looks at Galiwao (ID: 16982283/0x0103210B)
  4: 0x0100 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0101  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:    95 09 80 00                                     ....           
```

#### Opcodes

```
  0: 0x0101 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 1*)
  1: 0x0104 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0105  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                95 04 80  00                            ....       
```

#### Opcodes

```
  0: 0x0105 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x0108 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0109  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                             96 00                          ..     
```

#### Opcodes

```
  0: 0x0109 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x010A [0x00] END_REQSTACK()
```

### Event 836

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   00                         .    
```

#### Opcodes

```
  0: 0x010B [0x00] END_REQSTACK()
```

### Event 838

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      00                       .   
```

#### Opcodes

```
  0: 0x010C [0x00] END_REQSTACK()
```

### Event 845

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                         00                     .  
```

#### Opcodes

```
  0: 0x010D [0x00] END_REQSTACK()
```

### Event 5071

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                            00                   . 
```

#### Opcodes

```
  0: 0x010E [0x00] END_REQSTACK()
```

### Event 5073

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               00                 .
```

#### Opcodes

```
  0: 0x010F [0x00] END_REQSTACK()
```

### Event 5075

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0110  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110: 00                                                .               
```

#### Opcodes

```
  0: 0x0110 [0x00] END_REQSTACK()
```

### Event 5076

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0111  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:    00                                              .              
```

#### Opcodes

```
  0: 0x0111 [0x00] END_REQSTACK()
```

### Event 5077

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0112  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:       00                                            .             
```

#### Opcodes

```
  0: 0x0112 [0x00] END_REQSTACK()
```

### Event 5078

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0113  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          00                                          .            
```

#### Opcodes

```
  0: 0x0113 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0114   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:             32 0F 80 1F  00 18 80 19 80 1A 80 1F      2...........
0120: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0114 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0117 [0x1F] MOVE_ENTITY: EventEntity moves to X=-571.641*, Z=37.268*, Y=1.999*
  2: 0x011F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0121 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0122   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:       32 0F 80 1F 00 1B  80 1C 80 1A 80 1F 01 6F    2............o
0130: 00                                                .               
```

#### Opcodes

```
  0: 0x0122 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0125 [0x1F] MOVE_ENTITY: EventEntity moves to X=-568.085*, Z=32.296*, Y=1.999*
  2: 0x012D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x012F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0130 [0x00] END_REQSTACK()
```
