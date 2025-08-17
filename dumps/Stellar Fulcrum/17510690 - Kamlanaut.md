# 17510690 - Kamlanaut

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 1304 bytes                |
| Total Events     | 34                        |
| References Count | 31                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      7 |              2 |
| [0](#event-0)              | 0x0007       |     55 |              5 |
| [6](#event-6)              | 0x003E       |     10 |              2 |
| [17](#event-17)            | 0x0048       |     57 |              6 |
| [65535.1](#event-655351)   | 0x0081       |     29 |              3 |
| [65535.2](#event-655352)   | 0x009E       |     29 |              3 |
| [65535.3](#event-655353)   | 0x00BB       |     29 |              3 |
| [65535.4](#event-655354)   | 0x00D8       |     29 |              3 |
| [65535.5](#event-655355)   | 0x00F5       |     19 |              3 |
| [65535.6](#event-655356)   | 0x0108       |     29 |              3 |
| [65535.7](#event-655357)   | 0x0125       |     19 |              3 |
| [65535.8](#event-655358)   | 0x0138       |     29 |              3 |
| [65535.9](#event-655359)   | 0x0155       |     29 |              3 |
| [65535.10](#event-6553510) | 0x0172       |     29 |              3 |
| [65535.11](#event-6553511) | 0x018F       |     10 |              2 |
| [65535.12](#event-6553512) | 0x0199       |     10 |              2 |
| [65535.13](#event-6553513) | 0x01A3       |     29 |              3 |
| [65535.14](#event-6553514) | 0x01C0       |     29 |              3 |
| [65535.15](#event-6553515) | 0x01DD       |     29 |              3 |
| [65535.16](#event-6553516) | 0x01FA       |     29 |              3 |
| [65535.17](#event-6553517) | 0x0217       |     33 |              3 |
| [65535.18](#event-6553518) | 0x0238       |     10 |              2 |
| [65535.19](#event-6553519) | 0x0242       |     10 |              2 |
| [65535.20](#event-6553520) | 0x024C       |     45 |              5 |
| [65535.21](#event-6553521) | 0x0279       |     25 |              3 |
| [65535.22](#event-6553522) | 0x0292       |     29 |              3 |
| [65535.23](#event-6553523) | 0x02AF       |     29 |              3 |
| [65535.24](#event-6553524) | 0x02CC       |     29 |              3 |
| [65535.25](#event-6553525) | 0x02E9       |     29 |              3 |
| [65535.26](#event-6553526) | 0x0306       |     19 |              3 |
| [65535.27](#event-6553527) | 0x0319       |    169 |             17 |
| [65535.28](#event-6553528) | 0x03C2       |     32 |              5 |
| [65535.29](#event-6553529) | 0x03E2       |     32 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0xE452      |       58450 |
|       2 | 0xFFFFEC75  |  4294962293 |
|       3 | 0x0C00      |        3072 |
|       4 | 0x0201      |         513 |
|       5 | 0x0202      |         514 |
|       6 | 0x024C      |         588 |
|       7 | 0xE625      |       58917 |
|       8 | 0x0400      |        1024 |
|       9 | 0xA39E      |       41886 |
|      10 | 0x09C3      |        2499 |
|      11 | 0x0200      |         512 |
|      12 | 0x0118      |         280 |
|      13 | 0x00B4      |         180 |
|      14 | 0x0300      |         768 |
|      15 | 0x0038      |          56 |
|      16 | 0x005A      |          90 |
|      17 | 0x0078      |         120 |
|      18 | 0x003C      |          60 |
|      19 | 0x0050      |          80 |
|      20 | 0x002B      |          43 |
|      21 | 0x0080      |         128 |
|      22 | 0x004F      |          79 |
|      23 | 0x0064      |         100 |
|      24 | 0x00F0      |         240 |
|      25 | 0x00AA      |         170 |
|      26 | 0x0046      |          70 |
|      27 | 0x0039      |          57 |
|      28 | 0x01F4      |         500 |
|      29 | 0x001E      |          30 |
|      30 | 0x0001      |           1 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 55 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 5B 04 80 F0 FF FF 7F F0  FF FF 7F 00 FE FE FE 5B  [..............[
0020: 05 80 F0 FF FF 7F F0 FF  FF 7F 00 FE FE FE 5B 06  ..............[.
0030: 80 F0 FF FF 7F F0 FF FF  7F 00 FE FE FE 00        ..............  
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=58.450*, y=-5.003*, direction=270.0°*
  1: 0x0010 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=513*
  2: 0x001F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=514*
  3: 0x002E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=588*
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            37 00                7.
0040: 80 07 80 02 80 08 80 00                           ........        
```

#### Opcodes

```
  0: 0x003E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=58.917*, y=-5.003*, direction=90.0°*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 57 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          22 01 37 00 80 09 80 0A          ".7.....
0050: 80 0B 80 5B 04 80 F0 FF  FF 7F F0 FF FF 7F 00 FE  ...[............
0060: FE FE 5B 05 80 F0 FF FF  7F F0 FF FF 7F 00 FE FE  ..[.............
0070: FE 5B 06 80 F0 FF FF 7F  F0 FF FF 7F 00 FE FE FE  .[..............
0080: 00                                                .               
```

#### Opcodes

```
  0: 0x0048 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=41.886*, y=2.499*, direction=45.0°*
  2: 0x0053 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=513*
  3: 0x0062 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=514*
  4: 0x0071 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [LocalPlayer, LocalPlayer], work=588*
  5: 0x0080 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0081   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:    5B 04 80 F8 FF FF 7F  F8 FF FF 7F 64 6C 30 30   [..........dl00
0090: 53 F8 FF FF 7F F8 FF FF  7F 64 6C 30 30 00        S........dl00.  
```

#### Opcodes

```
  0: 0x0081 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl00" with entities [EventEntity, EventEntity], work=513*
  1: 0x0090 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl00" with entities [EventEntity, EventEntity]
  2: 0x009D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009E   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            5B 04                [.
00A0: 80 F8 FF FF 7F F8 FF FF  7F 64 6C 30 31 53 F8 FF  .........dl01S..
00B0: FF 7F F8 FF FF 7F 64 6C  30 31 00                 ......dl01.     
```

#### Opcodes

```
  0: 0x009E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl01" with entities [EventEntity, EventEntity], work=513*
  1: 0x00AD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl01" with entities [EventEntity, EventEntity]
  2: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   5B 04 80 F8 FF             [....
00C0: FF 7F F8 FF FF 7F 64 6C  30 32 53 F8 FF FF 7F F8  ......dl02S.....
00D0: FF FF 7F 64 6C 30 32 00                           ...dl02.        
```

#### Opcodes

```
  0: 0x00BB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl02" with entities [EventEntity, EventEntity], work=513*
  1: 0x00CA [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl02" with entities [EventEntity, EventEntity]
  2: 0x00D7 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D8   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                          5B 04 80 F8 FF FF 7F F8          [.......
00E0: FF FF 7F 64 6C 30 33 53  F8 FF FF 7F F8 FF FF 7F  ...dl03S........
00F0: 64 6C 30 33 00                                    dl03.           
```

#### Opcodes

```
  0: 0x00D8 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl03" with entities [EventEntity, EventEntity], work=513*
  1: 0x00E7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl03" with entities [EventEntity, EventEntity]
  2: 0x00F4 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F5   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                5B 04 80  F8 FF FF 7F F8 FF FF 7F       [..........
0100: 64 6C 30 34 1C 0C 80 00                           dl04....        
```

#### Opcodes

```
  0: 0x00F5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl04" with entities [EventEntity, EventEntity], work=513*
  1: 0x0104 [0x1C] WAIT(280* ticks)
  2: 0x0107 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0108   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          5B 05 80 F8 FF FF 7F F8          [.......
0110: FF FF 7F 64 6C 30 35 53  F8 FF FF 7F F8 FF FF 7F  ...dl05S........
0120: 64 6C 30 35 00                                    dl05.           
```

#### Opcodes

```
  0: 0x0108 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl05" with entities [EventEntity, EventEntity], work=514*
  1: 0x0117 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl05" with entities [EventEntity, EventEntity]
  2: 0x0124 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0125   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                5B 05 80  F8 FF FF 7F F8 FF FF 7F       [..........
0130: 64 6C 30 36 1C 0D 80 00                           dl06....        
```

#### Opcodes

```
  0: 0x0125 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl06" with entities [EventEntity, EventEntity], work=514*
  1: 0x0134 [0x1C] WAIT(180* ticks)
  2: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0138   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          5B 05 80 F8 FF FF 7F F8          [.......
0140: FF FF 7F 64 6C 30 37 53  F8 FF FF 7F F8 FF FF 7F  ...dl07S........
0150: 64 6C 30 37 00                                    dl07.           
```

#### Opcodes

```
  0: 0x0138 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl07" with entities [EventEntity, EventEntity], work=514*
  1: 0x0147 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl07" with entities [EventEntity, EventEntity]
  2: 0x0154 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0155   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                5B 05 80  F8 FF FF 7F F8 FF FF 7F       [..........
0160: 64 6C 30 38 53 F8 FF FF  7F F8 FF FF 7F 64 6C 30  dl08S........dl0
0170: 38 00                                             8.              
```

#### Opcodes

```
  0: 0x0155 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl08" with entities [EventEntity, EventEntity], work=514*
  1: 0x0164 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl08" with entities [EventEntity, EventEntity]
  2: 0x0171 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0172   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:       5B 05 80 F8 FF FF  7F F8 FF FF 7F 64 6C 30    [..........dl0
0180: 39 53 F8 FF FF 7F F8 FF  FF 7F 64 6C 30 39 00     9S........dl09. 
```

#### Opcodes

```
  0: 0x0172 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl09" with entities [EventEntity, EventEntity], work=514*
  1: 0x0181 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl09" with entities [EventEntity, EventEntity]
  2: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               37                 7
0190: 00 80 07 80 02 80 0E 80  00                       .........       
```

#### Opcodes

```
  0: 0x018F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=58.917*, y=-5.003*, direction=67.5°*
  1: 0x0198 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0199   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             37 00 80 07 80 02 80           7......
01A0: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0199 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.000*, z=58.917*, y=-5.003*, direction=90.0°*
  1: 0x01A2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A3   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:          5B 05 80 F8 FF  FF 7F F8 FF FF 7F 64 6C     [..........dl
01B0: 31 30 53 F8 FF FF 7F F8  FF FF 7F 64 6C 31 30 00  10S........dl10.
```

#### Opcodes

```
  0: 0x01A3 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl10" with entities [EventEntity, EventEntity], work=514*
  1: 0x01B2 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl10" with entities [EventEntity, EventEntity]
  2: 0x01BF [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C0   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0: 5B 05 80 F8 FF FF 7F F8  FF FF 7F 64 6C 31 31 53  [..........dl11S
01D0: F8 FF FF 7F F8 FF FF 7F  64 6C 31 31 00           ........dl11.   
```

#### Opcodes

```
  0: 0x01C0 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl11" with entities [EventEntity, EventEntity], work=514*
  1: 0x01CF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl11" with entities [EventEntity, EventEntity]
  2: 0x01DC [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01DD   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                                         5B 05 80               [..
01E0: F8 FF FF 7F F8 FF FF 7F  64 6C 31 32 53 F8 FF FF  ........dl12S...
01F0: 7F F8 FF FF 7F 64 6C 31  32 00                    .....dl12.      
```

#### Opcodes

```
  0: 0x01DD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl12" with entities [EventEntity, EventEntity], work=514*
  1: 0x01EC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl12" with entities [EventEntity, EventEntity]
  2: 0x01F9 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01FA   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                                5B 05 80 F8 FF FF            [.....
0200: 7F F8 FF FF 7F 64 6C 31  33 53 F8 FF FF 7F F8 FF  .....dl13S......
0210: FF 7F 64 6C 31 33 00                              ..dl13.         
```

#### Opcodes

```
  0: 0x01FA [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl13" with entities [EventEntity, EventEntity], work=514*
  1: 0x0209 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl13" with entities [EventEntity, EventEntity]
  2: 0x0216 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0217   |
| Data Size    | 33 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0210:                      5B  06 80 F8 FF FF 7F F8 FF         [........
0220: FF 7F 64 6C 31 34 62 0F  80 22 31 0B 01 22 31 0B  ..dl14b.."1.."1.
0230: 01 6D 61 69 6E 00 80 00                           .main...        
```

#### Opcodes

```
  0: 0x0217 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl14" with entities [EventEntity, EventEntity], work=588*
  1: 0x0226 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Kam'lanaut (ID: 17510690/0x010B3122), Kam'lanaut (ID: 17510690/0x010B3122)], work=[56*, 0*]
  2: 0x0237 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0238   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:                          6C F8 FF FF 7F 10 80 11          l.......
0240: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0238 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=90*, fade_time=120*)
  1: 0x0241 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0242   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:       6C F8 FF FF 7F 00  80 12 80 00                l.........    
```

#### Opcodes

```
  0: 0x0242 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=60*)
  1: 0x024B [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024C   |
| Data Size    | 45 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                      1C 13 80 62              ...b
0250: 14 80 F8 FF FF 7F F8 FF  FF 7F 6D 61 69 6E 00 80  ..........main..
0260: 6C 22 31 0B 01 15 80 0D  80 55 16 80 F0 FF FF 7F  l"1......U......
0270: F0 FF FF 7F 78 30 30 31  00                       ....x001.       
```

#### Opcodes

```
  0: 0x024C [0x1C] WAIT(80* ticks)
  1: 0x024F [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [EventEntity, EventEntity], work=[43*, 0*]
  2: 0x0260 [0x6C] FADE_ENTITY_COLOR(entity_id=Kam'lanaut (ID: 17510690/0x010B3122), end_alpha=128*, fade_time=180*)
  3: 0x0269 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x001" with entities [LocalPlayer, LocalPlayer], work=79*
  4: 0x0278 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0279   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0270:                             6C 22 31 0B 01 00 80           l"1....
0280: 00 80 5B 06 80 F8 FF FF  7F F8 FF FF 7F 64 6C 31  ..[..........dl1
0290: 35 00                                             5.              
```

#### Opcodes

```
  0: 0x0279 [0x6C] FADE_ENTITY_COLOR(entity_id=Kam'lanaut (ID: 17510690/0x010B3122), end_alpha=0*, fade_time=0*)
  1: 0x0282 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl15" with entities [EventEntity, EventEntity], work=588*
  2: 0x0291 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0292   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0290:       5B 06 80 F8 FF FF  7F F8 FF FF 7F 64 6C 31    [..........dl1
02A0: 36 53 F8 FF FF 7F F8 FF  FF 7F 64 6C 31 36 00     6S........dl16. 
```

#### Opcodes

```
  0: 0x0292 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl16" with entities [EventEntity, EventEntity], work=588*
  1: 0x02A1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl16" with entities [EventEntity, EventEntity]
  2: 0x02AE [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02AF   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02A0:                                               5B                 [
02B0: 06 80 F8 FF FF 7F F8 FF  FF 7F 64 6C 31 37 53 F8  ..........dl17S.
02C0: FF FF 7F F8 FF FF 7F 64  6C 31 37 00              .......dl17.    
```

#### Opcodes

```
  0: 0x02AF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl17" with entities [EventEntity, EventEntity], work=588*
  1: 0x02BE [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl17" with entities [EventEntity, EventEntity]
  2: 0x02CB [0x00] END_REQSTACK()
```

### Event 65535.24

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02CC   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02C0:                                      5B 06 80 F8              [...
02D0: FF FF 7F F8 FF FF 7F 64  6C 31 38 53 F8 FF FF 7F  .......dl18S....
02E0: F8 FF FF 7F 64 6C 31 38  00                       ....dl18.       
```

#### Opcodes

```
  0: 0x02CC [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl18" with entities [EventEntity, EventEntity], work=588*
  1: 0x02DB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl18" with entities [EventEntity, EventEntity]
  2: 0x02E8 [0x00] END_REQSTACK()
```

### Event 65535.25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02E9   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02E0:                             5B 06 80 F8 FF FF 7F           [......
02F0: F8 FF FF 7F 64 6C 31 39  53 F8 FF FF 7F F8 FF FF  ....dl19S.......
0300: 7F 64 6C 31 39 00                                 .dl19.          
```

#### Opcodes

```
  0: 0x02E9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl19" with entities [EventEntity, EventEntity], work=588*
  1: 0x02F8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl19" with entities [EventEntity, EventEntity]
  2: 0x0305 [0x00] END_REQSTACK()
```

### Event 65535.26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0306   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0300:                   5B 06  80 F8 FF FF 7F F8 FF FF        [.........
0310: 7F 64 6C 32 30 1C 0D 80  00                       .dl20....       
```

#### Opcodes

```
  0: 0x0306 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl20" with entities [EventEntity, EventEntity], work=588*
  1: 0x0315 [0x1C] WAIT(180* ticks)
  2: 0x0318 [0x00] END_REQSTACK()
```

### Event 65535.27

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0319    |
| Data Size    | 169 bytes |
| Instructions | 17        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0310:                             5B 06 80 F8 FF FF 7F           [......
0320: F8 FF FF 7F 64 6C 32 31  1C 17 80 5D 12 80 18 80  ....dl21...]....
0330: 1C 19 80 45 16 80 F0 FF  FF 7F F0 FF FF 7F 78 30  ...E..........x0
0340: 32 31 00 80 1C 1A 80 45  16 80 F0 FF FF 7F F0 FF  21.....E........
0350: FF 7F 7A 73 65 39 00 80  53 F8 FF FF 7F F8 FF FF  ..zse9..S.......
0360: 7F 64 6C 32 31 62 1B 80  22 31 0B 01 22 31 0B 01  .dl21b.."1.."1..
0370: 6D 61 69 6E 00 80 55 16  80 F0 FF FF 7F F0 FF FF  main..U.........
0380: 7F 78 30 32 31 45 16 80  F0 FF FF 7F F0 FF FF 7F  .x021E..........
0390: 78 30 32 32 00 80 27 03  27 31 0B 01 0E 1C 1C 80  x022..'.'1......
03A0: 55 1B 80 22 31 0B 01 22  31 0B 01 6D 61 69 6E 55  U.."1.."1..mainU
03B0: 16 80 F0 FF FF 7F F0 FF  FF 7F 78 30 32 32 1C 1D  ..........x022..
03C0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0319 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "dl21" with entities [EventEntity, EventEntity], work=588*
  1: 0x0328 [0x1C] WAIT(100* ticks)
  2: 0x032B [0x5D] SET_MUSIC_VOLUME(volume=60*, fade_time=240*)
  3: 0x0330 [0x1C] WAIT(170* ticks)
  4: 0x0333 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x021" with entities [LocalPlayer, LocalPlayer], work=[79*, 0*]
  5: 0x0344 [0x1C] WAIT(70* ticks)
  6: 0x0347 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "zse9" with entities [LocalPlayer, LocalPlayer], work=[79*, 0*]
  7: 0x0358 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "dl21" with entities [EventEntity, EventEntity]
  8: 0x0365 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [Kam'lanaut (ID: 17510690/0x010B3122), Kam'lanaut (ID: 17510690/0x010B3122)], work=[57*, 0*]
  9: 0x0376 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x021" with entities [LocalPlayer, LocalPlayer], work=79*
 10: 0x0385 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "x022" with entities [LocalPlayer, LocalPlayer], work=[79*, 0*]
 11: 0x0396 [0x27] REQ_SET(priority=0x03, entity_id=Eald'narche (ID: 17510695/0x010B3127), tag_num=0x0E)
 12: 0x039D [0x1C] WAIT(500* ticks)
 13: 0x03A0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "main" with entities [Kam'lanaut (ID: 17510690/0x010B3122), Kam'lanaut (ID: 17510690/0x010B3122)], work=57*
 14: 0x03AF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "x022" with entities [LocalPlayer, LocalPlayer], work=79*
 15: 0x03BE [0x1C] WAIT(30* ticks)
 16: 0x03C1 [0x00] END_REQSTACK()
```

### Event 65535.28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03C2   |
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03C0:       6C F8 FF FF 7F 00  80 1E 80 22 00 3B 27 31    l........".;'1
03D0: 0B 01 00 00 01 00 02 00  37 00 00 01 00 02 00 00  ........7.......
03E0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x03C2 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x03CB [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x03CD [0x3B] GET_ENTITY_POSITION(entity=Eald'narche (ID: 17510695/0x010B3127), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  3: 0x03D8 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=0.0°*
  4: 0x03E1 [0x00] END_REQSTACK()
```

### Event 65535.29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03E2   |
| Data Size    | 32 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03E0:       6C F8 FF FF 7F 00  80 1E 80 22 00 3B F0 FF    l........".;..
03F0: FF 7F 00 00 01 00 02 00  37 00 00 01 00 02 00 00  ........7.......
0400: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x03E2 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x03EB [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x03ED [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  3: 0x03F8 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=0.0°*
  4: 0x0401 [0x00] END_REQSTACK()
```
