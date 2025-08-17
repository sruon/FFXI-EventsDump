# 17723641 - Chasalvige

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 672 bytes                     |
| Total Events     | 30                            |
| References Count | 18                            |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     14 |              2 |
| [65535.3](#event-655353)   | 0x001F       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002F       |     14 |              2 |
| [65535.5](#event-655355)   | 0x003D       |     57 |              5 |
| [65535.6](#event-655356)   | 0x0076       |     16 |              2 |
| [65535.7](#event-655357)   | 0x0086       |     14 |              2 |
| [65535.8](#event-655358)   | 0x0094       |     16 |              2 |
| [65535.9](#event-655359)   | 0x00A4       |     14 |              2 |
| [65535.10](#event-6553510) | 0x00B2       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00C2       |     14 |              2 |
| [65535.12](#event-6553512) | 0x00D0       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00E0       |     14 |              2 |
| [65535.14](#event-6553514) | 0x00EE       |     16 |              2 |
| [65535.15](#event-6553515) | 0x00FE       |     14 |              2 |
| [65535.16](#event-6553516) | 0x010C       |     16 |              2 |
| [65535.17](#event-6553517) | 0x011C       |     14 |              2 |
| [65535.18](#event-6553518) | 0x012A       |     16 |              2 |
| [65535.19](#event-6553519) | 0x013A       |     14 |              2 |
| [762](#event-762)          | 0x0148       |     15 |              4 |
| [65535.20](#event-6553520) | 0x0157       |     10 |              2 |
| [65535.21](#event-6553521) | 0x0161       |     10 |              2 |
| [65535.22](#event-6553522) | 0x016B       |     15 |              5 |
| [65535.23](#event-6553523) | 0x017A       |     15 |              5 |
| [65535.24](#event-6553524) | 0x0189       |     15 |              5 |
| [65535.25](#event-6553525) | 0x0198       |     10 |              2 |
| [65535.26](#event-6553526) | 0x01A2       |     15 |              5 |
| [65535.27](#event-6553527) | 0x01B1       |     15 |              5 |
| [761](#event-761)          | 0x01C0       |     15 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x0019      |          25 |
|       2 | 0x178B0     |       96432 |
|       3 | 0x20B9E     |      134046 |
|       4 | 0xFFFFFDF8  |  4294966776 |
|       5 | 0x023D      |         573 |
|       6 | 0x20788     |      133000 |
|       7 | 0x1E848     |      125000 |
|       8 | 0x1963      |        6499 |
|       9 | 0x0EB7      |        3767 |
|      10 | 0x000D      |          13 |
|      11 | 0x2114C     |      135500 |
|      12 | 0x1F20C     |      127500 |
|      13 | 0x218B8     |      137400 |
|      14 | 0x1F978     |      129400 |
|      15 | 0x0D98      |        3480 |
|      16 | 0x2156E     |      136558 |
|      17 | 0x1F67F     |      128639 |

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 00      S........tlk0. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               5B                 [
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 00     ..........tlk1. 
```

#### Opcodes

```
  0: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               53                 S
0030: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 00           ........tlk1.   
```

#### Opcodes

```
  0: 0x002F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x003C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 57 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         5B 00 80               [..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 53 F8 FF FF  ........tlk0S...
0050: 7F F8 FF FF 7F 74 6C 6B  30 5B 00 80 F8 FF FF 7F  .....tlk0[......
0060: F8 FF FF 7F 74 6C 6B 31  53 F8 FF FF 7F F8 FF FF  ....tlk1S.......
0070: 7F 74 6C 6B 31 00                                 .tlk1.          
```

#### Opcodes

```
  0: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x004C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0059 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  3: 0x0068 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  4: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0076   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   5B 00  80 F8 FF FF 7F F8 FF FF        [.........
0080: 7F 74 68 6B 30 00                                 .thk0.          
```

#### Opcodes

```
  0: 0x0076 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   53 F8  FF FF 7F F8 FF FF 7F 74        S........t
0090: 68 6B 30 00                                       hk0.            
```

#### Opcodes

```
  0: 0x0086 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk0" with entities [EventEntity, EventEntity]
  1: 0x0093 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             5B 00 80 F8  FF FF 7F F8 FF FF 7F 74      [..........t
00A0: 68 6B 31 00                                       hk1.            
```

#### Opcodes

```
  0: 0x0094 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             53 F8 FF FF  7F F8 FF FF 7F 74 68 6B      S........thk
00B0: 31 00                                             1.              
```

#### Opcodes

```
  0: 0x00A4 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       5B 00 80 F8 FF FF  7F F8 FF FF 7F 74 68 6B    [..........thk
00C0: 32 00                                             2.              
```

#### Opcodes

```
  0: 0x00B2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x00C1 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C2   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       53 F8 FF FF 7F F8  FF FF 7F 74 68 6B 32 00    S........thk2.
```

#### Opcodes

```
  0: 0x00C2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x00CF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 5B 01 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 00  [..........thk1.
```

#### Opcodes

```
  0: 0x00D0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=25*
  1: 0x00DF [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E0   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 31 00        S........thk1.  
```

#### Opcodes

```
  0: 0x00E0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x00ED [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            5B 01                [.
00F0: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        .........thk2.  
```

#### Opcodes

```
  0: 0x00EE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=25*
  1: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            53 F8                S.
0100: FF FF 7F F8 FF FF 7F 74  68 6B 32 00              .......thk2.    
```

#### Opcodes

```
  0: 0x00FE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x010B [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      5B 01 80 F8              [...
0110: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x010C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=25*
  1: 0x011B [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011C   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                      53 F8 FF FF              S...
0120: 7F F8 FF FF 7F 74 6C 6B  30 00                    .....tlk0.      
```

#### Opcodes

```
  0: 0x011C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                5B 01 80 F8 FF FF            [.....
0130: 7F F8 FF FF 7F 74 6C 6B  31 00                    .....tlk1.      
```

#### Opcodes

```
  0: 0x012A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=25*
  1: 0x0139 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                53 F8 FF FF 7F F8            S.....
0140: FF FF 7F 74 6C 6B 31 00                           ...tlk1.        
```

#### Opcodes

```
  0: 0x013A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  1: 0x0147 [0x00] END_REQSTACK()
```

### Event 762

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0148   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                          92 01 F8 FF FF 7F 94 01          ........
0150: F8 FF FF 7F A4 00 00                              .......         
```

#### Opcodes

```
  0: 0x0148 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x014E [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0154 [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  3: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      37  02 80 03 80 04 80 05 80         7........
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x0157 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=96.432*, z=134.046*, y=-0.520*, direction=50.4°*
  1: 0x0160 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0161   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:    37 06 80 07 80 08 80  09 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0161 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=133.000*, z=125.000*, y=6.499*, direction=331.1°*
  1: 0x016A [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                   32 0A 80 1F 00             2....
0170: 0B 80 0C 80 08 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x016B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x016E [0x1F] MOVE_ENTITY: EventEntity moves to X=135.500*, Z=127.500*, Y=6.499*
  2: 0x0176 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0178 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0179 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                32 0A 80 1F 00 0D            2.....
0180: 80 0E 80 08 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x017A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x017D [0x1F] MOVE_ENTITY: EventEntity moves to X=137.400*, Z=129.400*, Y=6.499*
  2: 0x0185 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0187 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0188 [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0189   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                             32 0A 80 1F 00 0B 80           2......
0190: 0C 80 08 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0189 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x018C [0x1F] MOVE_ENTITY: EventEntity moves to X=135.500*, Z=127.500*, Y=6.499*
  2: 0x0194 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0196 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0197 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0198   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          37 0B 80 0C 80 08 80 0F          7.......
01A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0198 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=135.500*, z=127.500*, y=6.499*, direction=305.9°*
  1: 0x01A1 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A2   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:       32 0A 80 1F 00 10  80 11 80 08 80 1F 01 6F    2............o
01B0: 00                                                .               
```

#### Opcodes

```
  0: 0x01A2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=136.558*, Z=128.639*, Y=6.499*
  2: 0x01AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01B0 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B1   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:    32 0A 80 1F 00 0B 80  0C 80 08 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x01B1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x01B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=135.500*, Z=127.500*, Y=6.499*
  2: 0x01BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01BE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01BF [0x00] END_REQSTACK()
```

### Event 761

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F A4 00 00     ............... 
```

#### Opcodes

```
  0: 0x01C0 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x01C6 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x01CC [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  3: 0x01CE [0x00] END_REQSTACK()
```
