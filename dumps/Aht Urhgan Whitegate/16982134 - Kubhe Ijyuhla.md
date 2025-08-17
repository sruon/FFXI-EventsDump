# 16982134 - Kubhe Ijyuhla

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 592 bytes                     |
| Total Events     | 26                            |
| References Count | 27                            |

## List of Events

| Event ID                    | Entrypoint   |   Size |   Instructions |
|-----------------------------|--------------|--------|----------------|
| [65535](#event-65535)       | 0x0000       |      1 |              1 |
| [662](#event-662)           | 0x0001       |     69 |             13 |
| [810](#event-810)           | 0x0046       |      1 |              1 |
| [65535.1](#event-65535-1)   | 0x0047       |     10 |              2 |
| [65535.2](#event-65535-2)   | 0x0051       |     14 |              4 |
| [65535.3](#event-65535-3)   | 0x005F       |     32 |              6 |
| [65535.4](#event-65535-4)   | 0x007F       |     26 |              4 |
| [65535.5](#event-65535-5)   | 0x0099       |     23 |              5 |
| [65535.6](#event-65535-6)   | 0x00B0       |     14 |              4 |
| [65535.7](#event-65535-7)   | 0x00BE       |      4 |              2 |
| [65535.8](#event-65535-8)   | 0x00C2       |      4 |              2 |
| [65535.9](#event-65535-9)   | 0x00C6       |      2 |              2 |
| [836](#event-836)           | 0x00C8       |      1 |              1 |
| [837](#event-837)           | 0x00C9       |     29 |              7 |
| [838](#event-838)           | 0x00E6       |      1 |              1 |
| [839](#event-839)           | 0x00E7       |     29 |              7 |
| [842](#event-842)           | 0x0104       |     46 |             10 |
| [845](#event-845)           | 0x0132       |      1 |              1 |
| [846](#event-846)           | 0x0133       |     33 |              7 |
| [5071](#event-5071)         | 0x0154       |      1 |              1 |
| [5073](#event-5073)         | 0x0155       |      1 |              1 |
| [5075](#event-5075)         | 0x0156       |      1 |              1 |
| [5076](#event-5076)         | 0x0157       |      1 |              1 |
| [5077](#event-5077)         | 0x0158       |      1 |              1 |
| [5078](#event-5078)         | 0x0159       |      1 |              1 |
| [65535.10](#event-65535-10) | 0x015A       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0037      |          55 |
|       2 | 0x18D1      |        6353 |
|       3 | 0x0036      |          54 |
|       4 | 0x18D2      |        6354 |
|       5 | 0x4764      |       18276 |
|       6 | 0x493E      |       18750 |
|       7 | 0x0000      |           0 |
|       8 | 0x0EE7      |        3815 |
|       9 | 0x0028      |          40 |
|      10 | 0x47C8      |       18376 |
|      11 | 0x4650      |       18000 |
|      12 | 0x000D      |          13 |
|      13 | 0x003B      |          59 |
|      14 | 0x4B33      |       19251 |
|      15 | 0x45E6      |       17894 |
|      16 | 0x0001      |           1 |
|      17 | 0x0032      |          50 |
|      18 | 0x1BE2      |        7138 |
|      19 | 0x1BF2      |        7154 |
|      20 | 0x0034      |          52 |
|      21 | 0x1C07      |        7175 |
|      22 | 0x1C08      |        7176 |
|      23 | 0x1C59      |        7257 |
|      24 | 0xFFF756B8  |  4294399672 |
|      25 | 0x7F81      |       32641 |
|      26 | 0x07CF      |        1999 |

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

### Event 662

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 69 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 66 01 80 F8  ....tlk0...#f...
0020: FF FF 7F F8 FF FF 7F 74  6C 6B 31 1C 00 80 66 03  .......tlk1...f.
0030: 80 F8 FF FF 7F F8 FF FF  7F 61 6E 67 30 1D 04 80  .........ang0...
0040: 23 1C 00 80 21 00                                 #...!.          
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=6353*)
    → "Grrr, that girl really makes the furrr on my tail stand on end! I can't believe I came all this way to be a mercenary in her rrridiculous company!\u007F1\u0000\u0007"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=55*
  6: 0x002B [0x1C] WAIT(30* ticks)
  7: 0x002E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=54*
  8: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=6354*)
    → "I'm gonna quit! I'm rrreally gonna quit!\u007F1\u0000\u0007"
  9: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0041 [0x1C] WAIT(30* ticks)
 11: 0x0044 [0x21] END_EVENT
 12: 0x0045 [0x00] END_REQSTACK()
```

### Event 810

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  05 80 06 80 07 80 08 80         7........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=18.276*, z=18.750*, y=0.000*, direction=335.3°*
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    32 09 80 1F 00 0A 80  0B 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0051 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.376*, Z=18.000*, Y=0.000*
  2: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 32 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               32                 2
0060: 0C 80 1F 00 05 80 06 80  07 80 1F 01 4A 76 20 03  ............Jv .
0070: 01 F0 FF FF 7F 4A 0B 21  03 01 F0 FF FF 7F 00     .....J.!....... 
```

#### Opcodes

```
  0: 0x005F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0062 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.276*, Z=18.750*, Y=0.000*
  2: 0x006A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006C [0x4A] Kubhe Ijyuhla (ID: 16982134/0x01032076) looks at LocalPlayer
  4: 0x0075 [0x4A] Galiwao (ID: 16982283/0x0103210B) looks at LocalPlayer
  5: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               66                 f
0080: 0D 80 76 20 03 01 76 20  03 01 73 68 61 30 1C 00  ..v ..v ..sha0..
0090: 80 29 32 77 20 03 01 06  00                       .)2w ....       
```

#### Opcodes

```
  0: 0x007F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [Kubhe Ijyuhla (ID: 16982134/0x01032076), Kubhe Ijyuhla (ID: 16982134/0x01032076)], work=59*
  1: 0x008E [0x1C] WAIT(30* ticks)
  2: 0x0091 [0x29] REQ_SET_WAIT(priority=0x32, entity_id=Tohka Telposkha (ID: 16982135/0x01032077), tag_num=0x06)
  3: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             32 0C 80 1F 00 0E 80           2......
00A0: 0F 80 07 80 1F 01 4A 76  20 03 01 0B 21 03 01 00  ......Jv ...!...
```

#### Opcodes

```
  0: 0x0099 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009C [0x1F] MOVE_ENTITY: EventEntity moves to X=19.251*, Z=17.894*, Y=0.000*
  2: 0x00A4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A6 [0x4A] Kubhe Ijyuhla (ID: 16982134/0x01032076) looks at Galiwao (ID: 16982283/0x0103210B)
  4: 0x00AF [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B0   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 32 0C 80 1F 00 0A 80 06  80 07 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x00B0 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.376*, Z=18.750*, Y=0.000*
  2: 0x00BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BE  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            95 10                ..
00C0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00BE [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 1*)
  1: 0x00C1 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C2  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       95 07 80 00                                   ....          
```

#### Opcodes

```
  0: 0x00C2 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C6  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   96 00                                 ..        
```

#### Opcodes

```
  0: 0x00C6 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x00C7 [0x00] END_REQSTACK()
```

### Event 836

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          00                               .       
```

#### Opcodes

```
  0: 0x00C8 [0x00] END_REQSTACK()
```

### Event 837

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1E F0 FF FF 7F 1C 00           .......
00D0: 80 66 11 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  .f..........tlk0
00E0: 1D 12 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x00C9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00CE [0x1C] WAIT(30* ticks)
  2: 0x00D1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  3: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7138*)
    → "Foudeel should be waiting rrright outside the secret passage to the Wajaom Woodlands. Do this for me and I promise I'll make it up to you.\u007F1\u0000\u0007"
  4: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00E4 [0x21] END_EVENT
  6: 0x00E5 [0x00] END_REQSTACK()
```

### Event 838

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00E6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00E6 [0x00] END_REQSTACK()
```

### Event 839

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E7   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                      1E  F0 FF FF 7F 1C 00 80 66         ........f
00F0: 11 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 13  ..........tlk0..
0100: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x00E7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00EC [0x1C] WAIT(30* ticks)
  2: 0x00EF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  3: 0x00FE [0x1D] PRINT_EVENT_MESSAGE(message_id=7154*)
    → "I'm positive that you'll find Foudeel wallowing away at the Shararat Teahouse. Ask arrround for him when you get there.\u007F1\u0000\u0007"
  4: 0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0102 [0x21] END_EVENT
  6: 0x0103 [0x00] END_REQSTACK()
```

### Event 842

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0104   |
| Data Size    | 46 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             1E F0 FF FF  7F 1C 00 80 66 14 80 F8      ........f...
0110: FF FF 7F F8 FF FF 7F 64  69 73 30 1D 15 80 23 53  .......dis0...#S
0120: F8 FF FF 7F F8 FF FF 7F  64 69 73 30 1D 16 80 23  ........dis0...#
0130: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0104 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0109 [0x1C] WAIT(30* ticks)
  2: 0x010C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "dis0" with entities [EventEntity, EventEntity], work=52*
  3: 0x011B [0x1D] PRINT_EVENT_MESSAGE(message_id=7175*)
    → "Foudeel is still at the Shararat Teahouse? Wow... Whateverrr has him down must be really serious.\u007F1\u0000\u0007"
  4: 0x011E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x011F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dis0" with entities [EventEntity, EventEntity]
  6: 0x012C [0x1D] PRINT_EVENT_MESSAGE(message_id=7176*)
    → "Hm? Have I been over therrre to check up on him? Hah! I haven't moved a muscle since we last talked. Just ask anybody.\u007F1\u0000\u0007"
  7: 0x012F [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0130 [0x21] END_EVENT
  9: 0x0131 [0x00] END_REQSTACK()
```

### Event 845

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0132  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:       00                                            .             
```

#### Opcodes

```
  0: 0x0132 [0x00] END_REQSTACK()
```

### Event 846

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0133   |
| Data Size    | 33 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          1E F0 FF FF 7F  1C 00 80 66 11 80 76 20     ........f..v 
0140: 03 01 76 20 03 01 74 6C  6B 30 2B 76 20 03 01 17  ..v ..tlk0+v ...
0150: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0133 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0138 [0x1C] WAIT(30* ticks)
  2: 0x013B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Kubhe Ijyuhla (ID: 16982134/0x01032076), Kubhe Ijyuhla (ID: 16982134/0x01032076)], work=50*
  3: 0x014A [0x2B] Kubhe Ijyuhla (ID: 16982134/0x01032076) [7257*]:
    → "Anyway, I'm sorry you had to get involved in all that.\u007F1\u0000\u0007"
  4: 0x0151 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0152 [0x21] END_EVENT
  6: 0x0153 [0x00] END_REQSTACK()
```

### Event 5071

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0154  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:             00                                        .           
```

#### Opcodes

```
  0: 0x0154 [0x00] END_REQSTACK()
```

### Event 5073

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0155  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                00                                      .          
```

#### Opcodes

```
  0: 0x0155 [0x00] END_REQSTACK()
```

### Event 5075

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0156  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                   00                                    .         
```

#### Opcodes

```
  0: 0x0156 [0x00] END_REQSTACK()
```

### Event 5076

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0157  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      00                                  .        
```

#### Opcodes

```
  0: 0x0157 [0x00] END_REQSTACK()
```

### Event 5077

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0158  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                          00                               .       
```

#### Opcodes

```
  0: 0x0158 [0x00] END_REQSTACK()
```

### Event 5078

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0159  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                             00                             .      
```

#### Opcodes

```
  0: 0x0159 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                32 0C 80 1F 00 18            2.....
0160: 80 19 80 1A 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x015A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x015D [0x1F] MOVE_ENTITY: EventEntity moves to X=-567.624*, Z=32.641*, Y=1.999*
  2: 0x0165 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0167 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0168 [0x00] END_REQSTACK()
```
