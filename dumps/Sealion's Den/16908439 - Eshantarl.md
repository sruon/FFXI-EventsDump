# 16908439 - Eshantarl

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 712 bytes              |
| Total Events     | 25                     |
| References Count | 16                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     13 |              3 |
| [33](#event-33)            | 0x000D       |     22 |              4 |
| [65535.1](#event-655351)   | 0x0023       |     14 |              4 |
| [65535.2](#event-655352)   | 0x0031       |     17 |              5 |
| [65535.3](#event-655353)   | 0x0042       |     10 |              2 |
| [65535.4](#event-655354)   | 0x004C       |     16 |              2 |
| [65535.5](#event-655355)   | 0x005C       |     16 |              2 |
| [65535.6](#event-655356)   | 0x006C       |     16 |              2 |
| [65535.7](#event-655357)   | 0x007C       |     16 |              2 |
| [65535.8](#event-655358)   | 0x008C       |     16 |              2 |
| [65535.9](#event-655359)   | 0x009C       |     29 |              3 |
| [65535.10](#event-6553510) | 0x00B9       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00C9       |     29 |              3 |
| [65535.12](#event-6553512) | 0x00E6       |     16 |              2 |
| [65535.13](#event-6553513) | 0x00F6       |     29 |              3 |
| [65535.14](#event-6553514) | 0x0113       |     29 |              3 |
| [65535.15](#event-6553515) | 0x0130       |     29 |              3 |
| [65535.16](#event-6553516) | 0x014D       |     29 |              3 |
| [65535.17](#event-6553517) | 0x016A       |     29 |              3 |
| [65535.18](#event-6553518) | 0x0187       |     16 |              2 |
| [65535.19](#event-6553519) | 0x0197       |     29 |              3 |
| [65535.20](#event-6553520) | 0x01B4       |     19 |              3 |
| [65535.21](#event-6553521) | 0x01C7       |     29 |              3 |
| [65535.22](#event-6553522) | 0x01E4       |     29 |              3 |
| [65535.23](#event-6553523) | 0x0201       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF63C18  |  4294327320 |
|       1 | 0x7B40D     |      504845 |
|       2 | 0xFFFC6BCE  |  4294732750 |
|       3 | 0x0AA2      |        2722 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFF63B7C  |  4294327164 |
|       6 | 0x7B9BC     |      506300 |
|       7 | 0x0028      |          40 |
|       8 | 0xFFF63BBA  |  4294327226 |
|       9 | 0x7C06C     |      508012 |
|      10 | 0x0C09      |        3081 |
|      11 | 0x01C4      |         452 |
|      12 | 0x01C5      |         453 |
|      13 | 0x01C2      |         450 |
|      14 | 0x01C3      |         451 |
|      15 | 0x005A      |          90 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         33 01 37               3.7
0010: 00 80 01 80 02 80 03 80  79 00 F8 FF FF 7F A0 00  ........y.......
0020: 02 01 00                                          ...             
```

#### Opcodes

```
  0: 0x000D [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x000F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-639.976*, z=504.845*, y=-234.546*, direction=239.2°*
  2: 0x0018 [0x79] EventEntity looks at Nag'molada (ID: 16908448/0x010200A0) (Basic look)
  3: 0x0022 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          32 04 80 1F 00  05 80 06 80 02 80 1F 01     2............
0030: 00                                                .               
```

#### Opcodes

```
  0: 0x0023 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0026 [0x1F] MOVE_ENTITY: EventEntity moves to X=-640.132*, Z=506.300*, Y=-234.546*
  2: 0x002E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0030 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0031   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:    32 07 80 1F 00 08 80  09 80 02 80 1F 01 39 0A   2............9.
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0031 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=-640.070*, Z=508.012*, Y=-234.546*
  2: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003E [0x39] SET_ENTITY_DIRECTION(direction=16.9°*)
  4: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       37 08 80 09 80 02  80 0A 80 00                7.........    
```

#### Opcodes

```
  0: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-640.070*, z=508.012*, y=-234.546*, direction=270.8°*
  1: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      5B 0B 80 F8              [...
0050: FF FF 7F F8 FF FF 7F 73  6A 69 30 00              .......sji0.    
```

#### Opcodes

```
  0: 0x004C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sji0" with entities [EventEntity, EventEntity], work=452*
  1: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      5B 0B 80 F8              [...
0060: FF FF 7F F8 FF FF 7F 73  6A 69 31 00              .......sji1.    
```

#### Opcodes

```
  0: 0x005C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sji1" with entities [EventEntity, EventEntity], work=452*
  1: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      5B 0C 80 F8              [...
0070: FF FF 7F F8 FF FF 7F 6D  65 69 30 00              .......mei0.    
```

#### Opcodes

```
  0: 0x006C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mei0" with entities [EventEntity, EventEntity], work=453*
  1: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      5B 0C 80 F8              [...
0080: FF FF 7F F8 FF FF 7F 6D  65 69 31 00              .......mei1.    
```

#### Opcodes

```
  0: 0x007C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "mei1" with entities [EventEntity, EventEntity], work=453*
  1: 0x008B [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      5B 0D 80 F8              [...
0090: FF FF 7F F8 FF FF 7F 74  6C 61 30 00              .......tla0.    
```

#### Opcodes

```
  0: 0x008C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=450*
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      5B 0D 80 F8              [...
00A0: FF FF 7F F8 FF FF 7F 74  6C 61 31 53 F8 FF FF 7F  .......tla1S....
00B0: F8 FF FF 7F 74 6C 61 31  00                       ....tla1.       
```

#### Opcodes

```
  0: 0x009C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=450*
  1: 0x00AB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  2: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             5B 0D 80 F8 FF FF 7F           [......
00C0: F8 FF FF 7F 74 6C 62 30  00                       ....tlb0.       
```

#### Opcodes

```
  0: 0x00B9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=450*
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             5B 0D 80 F8 FF FF 7F           [......
00D0: F8 FF FF 7F 74 6C 62 31  53 F8 FF FF 7F F8 FF FF  ....tlb1S.......
00E0: 7F 74 6C 62 31 00                                 .tlb1.          
```

#### Opcodes

```
  0: 0x00C9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=450*
  1: 0x00D8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  2: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   5B 0D  80 F8 FF FF 7F F8 FF FF        [.........
00F0: 7F 74 6C 63 30 00                                 .tlc0.          
```

#### Opcodes

```
  0: 0x00E6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=450*
  1: 0x00F5 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F6   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                   5B 0D  80 F8 FF FF 7F F8 FF FF        [.........
0100: 7F 74 6C 63 31 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  .tlc1S........tl
0110: 63 31 00                                          c1.             
```

#### Opcodes

```
  0: 0x00F6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=450*
  1: 0x0105 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  2: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          5B 0D 80 F8 FF  FF 7F F8 FF FF 7F 74 62     [..........tb
0120: 61 30 53 F8 FF FF 7F F8  FF FF 7F 74 62 61 30 00  a0S........tba0.
```

#### Opcodes

```
  0: 0x0113 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tba0" with entities [EventEntity, EventEntity], work=450*
  1: 0x0122 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tba0" with entities [EventEntity, EventEntity]
  2: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 5B 0D 80 F8 FF FF 7F F8  FF FF 7F 74 61 62 30 53  [..........tab0S
0140: F8 FF FF 7F F8 FF FF 7F  74 61 62 30 00           ........tab0.   
```

#### Opcodes

```
  0: 0x0130 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tab0" with entities [EventEntity, EventEntity], work=450*
  1: 0x013F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tab0" with entities [EventEntity, EventEntity]
  2: 0x014C [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014D   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                         5B 0D 80               [..
0150: F8 FF FF 7F F8 FF FF 7F  74 61 74 68 53 F8 FF FF  ........tathS...
0160: 7F F8 FF FF 7F 74 61 74  68 00                    .....tath.      
```

#### Opcodes

```
  0: 0x014D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tath" with entities [EventEntity, EventEntity], work=450*
  1: 0x015C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tath" with entities [EventEntity, EventEntity]
  2: 0x0169 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                5B 0D 80 F8 FF FF            [.....
0170: 7F F8 FF FF 7F 74 61 63  30 53 F8 FF FF 7F F8 FF  .....tac0S......
0180: FF 7F 74 61 63 30 00                              ..tac0.         
```

#### Opcodes

```
  0: 0x016A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tac0" with entities [EventEntity, EventEntity], work=450*
  1: 0x0179 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tac0" with entities [EventEntity, EventEntity]
  2: 0x0186 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0187   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                      5B  0D 80 F8 FF FF 7F F8 FF         [........
0190: FF 7F 74 68 6B 30 00                              ..thk0.         
```

#### Opcodes

```
  0: 0x0187 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [EventEntity, EventEntity], work=450*
  1: 0x0196 [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      5B  0D 80 F8 FF FF 7F F8 FF         [........
01A0: FF 7F 74 68 6B 31 53 F8  FF FF 7F F8 FF FF 7F 74  ..thk1S........t
01B0: 68 6B 31 00                                       hk1.            
```

#### Opcodes

```
  0: 0x0197 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=450*
  1: 0x01A6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x01B3 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B4   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             5B 0E 80 F8  FF FF 7F F8 FF FF 7F 75      [..........u
01C0: 74 75 30 1C 0F 80 00                              tu0....         
```

#### Opcodes

```
  0: 0x01B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "utu0" with entities [EventEntity, EventEntity], work=451*
  1: 0x01C3 [0x1C] WAIT(90* ticks)
  2: 0x01C6 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C7   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                      5B  0E 80 F8 FF FF 7F F8 FF         [........
01D0: FF 7F 75 74 75 31 53 F8  FF FF 7F F8 FF FF 7F 75  ..utu1S........u
01E0: 74 75 31 00                                       tu1.            
```

#### Opcodes

```
  0: 0x01C7 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "utu1" with entities [EventEntity, EventEntity], work=451*
  1: 0x01D6 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "utu1" with entities [EventEntity, EventEntity]
  2: 0x01E3 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01E4   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01E0:             5B 0C 80 F8  FF FF 7F F8 FF FF 7F 74      [..........t
01F0: 6C 68 30 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 68 30  lh0S........tlh0
0200: 00                                                .               
```

#### Opcodes

```
  0: 0x01E4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlh0" with entities [EventEntity, EventEntity], work=453*
  1: 0x01F3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlh0" with entities [EventEntity, EventEntity]
  2: 0x0200 [0x00] END_REQSTACK()
```

### Event 65535.23

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0201   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200:    5B 0C 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 68 31   [..........tlh1
0210: 00                                                .               
```

#### Opcodes

```
  0: 0x0201 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlh1" with entities [EventEntity, EventEntity], work=453*
  1: 0x0210 [0x00] END_REQSTACK()
```
