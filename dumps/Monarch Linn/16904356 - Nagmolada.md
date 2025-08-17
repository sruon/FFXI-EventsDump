# 16904356 - Nagmolada

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Monarch Linn (ID: 31) |
| Block Size       | 516 bytes             |
| Total Events     | 20                    |
| References Count | 9                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     13 |              3 |
| [32000](#event-32000)      | 0x000D       |     10 |              2 |
| [65535.1](#event-655351)   | 0x0017       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0027       |     16 |              2 |
| [65535.3](#event-655353)   | 0x0037       |     36 |              4 |
| [32001](#event-32001)      | 0x005B       |      1 |              1 |
| [65535.4](#event-655354)   | 0x005C       |     16 |              2 |
| [65535.5](#event-655355)   | 0x006C       |     29 |              3 |
| [65535.6](#event-655356)   | 0x0089       |     16 |              2 |
| [65535.7](#event-655357)   | 0x0099       |     16 |              2 |
| [65535.8](#event-655358)   | 0x00A9       |     29 |              3 |
| [65535.9](#event-655359)   | 0x00C6       |     16 |              2 |
| [65535.10](#event-6553510) | 0x00D6       |     16 |              2 |
| [65535.11](#event-6553511) | 0x00E6       |     29 |              3 |
| [65535.12](#event-6553512) | 0x0103       |     16 |              2 |
| [65535.13](#event-6553513) | 0x0113       |     29 |              3 |
| [65535.14](#event-6553514) | 0x0130       |     16 |              2 |
| [65535.15](#event-6553515) | 0x0140       |     29 |              3 |
| [65535.16](#event-6553516) | 0x015D       |     16 |              2 |
| [65535.17](#event-6553517) | 0x016D       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x97E93     |      622227 |
|       1 | 0x92714     |      599828 |
|       2 | 0xFA74      |       64116 |
|       3 | 0x07F7      |        2039 |
|       4 | 0x01D3      |         467 |
|       5 | 0x0000      |           0 |
|       6 | 0x01D6      |         470 |
|       7 | 0x01D1      |         465 |
|       8 | 0x0283      |         643 |

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
0000: 94 01 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=622.227*, z=599.828*, y=64.116*, direction=179.2°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      5B  04 80 F8 FF FF 7F F8 FF         [........
0020: FF 7F 73 6E 62 30 00                              ..snb0.         
```

#### Opcodes

```
  0: 0x0017 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "snb0" with entities [EventEntity, EventEntity], work=467*
  1: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5B  04 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 73 6E 62 31 00                              ..snb1.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "snb1" with entities [EventEntity, EventEntity], work=467*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      3B  F8 FF FF 7F 00 00 01 00         ;........
0040: 02 00 37 00 00 01 00 02  00 05 80 5B 06 80 F8 FF  ..7........[....
0050: FF 7F F8 FF FF 7F 63 34  31 32 00                 ......c412.     
```

#### Opcodes

```
  0: 0x0037 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x0042 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=0.0°*
  2: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "c412" with entities [EventEntity, EventEntity], work=470*
  3: 0x005A [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   00                         .    
```

#### Opcodes

```
  0: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      5B 07 80 F8              [...
0060: FF FF 7F F8 FF FF 7F 74  6C 61 30 00              .......tla0.    
```

#### Opcodes

```
  0: 0x005C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [EventEntity, EventEntity], work=465*
  1: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      5B 07 80 F8              [...
0070: FF FF 7F F8 FF FF 7F 74  6C 61 31 53 F8 FF FF 7F  .......tla1S....
0080: F8 FF FF 7F 74 6C 61 31  00                       ....tla1.       
```

#### Opcodes

```
  0: 0x006C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [EventEntity, EventEntity], work=465*
  1: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tla1" with entities [EventEntity, EventEntity]
  2: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             5B 07 80 F8 FF FF 7F           [......
0090: F8 FF FF 7F 74 61 68 61  00                       ....taha.       
```

#### Opcodes

```
  0: 0x0089 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "taha" with entities [EventEntity, EventEntity], work=465*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             5B 07 80 F8 FF FF 7F           [......
00A0: F8 FF FF 7F 74 6C 62 30  00                       ....tlb0.       
```

#### Opcodes

```
  0: 0x0099 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             5B 07 80 F8 FF FF 7F           [......
00B0: F8 FF FF 7F 74 6C 62 31  53 F8 FF FF 7F F8 FF FF  ....tlb1S.......
00C0: 7F 74 6C 62 31 00                                 .tlb1.          
```

#### Opcodes

```
  0: 0x00A9 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00B8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlb1" with entities [EventEntity, EventEntity]
  2: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   5B 07  80 F8 FF FF 7F F8 FF FF        [.........
00D0: 7F 74 62 68 61 00                                 .tbha.          
```

#### Opcodes

```
  0: 0x00C6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tbha" with entities [EventEntity, EventEntity], work=465*
  1: 0x00D5 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D6   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   5B 07  80 F8 FF FF 7F F8 FF FF        [.........
00E0: 7F 74 68 62 30 00                                 .thb0.          
```

#### Opcodes

```
  0: 0x00D6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb0" with entities [EventEntity, EventEntity], work=465*
  1: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   5B 07  80 F8 FF FF 7F F8 FF FF        [.........
00F0: 7F 74 68 62 31 53 F8 FF  FF 7F F8 FF FF 7F 74 68  .thb1S........th
0100: 62 31 00                                          b1.             
```

#### Opcodes

```
  0: 0x00E6 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thb1" with entities [EventEntity, EventEntity], work=465*
  1: 0x00F5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thb1" with entities [EventEntity, EventEntity]
  2: 0x0102 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0103   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:          5B 08 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     [..........tl
0110: 63 30 00                                          c0.             
```

#### Opcodes

```
  0: 0x0103 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc0" with entities [EventEntity, EventEntity], work=643*
  1: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0113   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          5B 08 80 F8 FF  FF 7F F8 FF FF 7F 74 6C     [..........tl
0120: 63 31 53 F8 FF FF 7F F8  FF FF 7F 74 6C 63 31 00  c1S........tlc1.
```

#### Opcodes

```
  0: 0x0113 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlc1" with entities [EventEntity, EventEntity], work=643*
  1: 0x0122 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlc1" with entities [EventEntity, EventEntity]
  2: 0x012F [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0130   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130: 5B 08 80 F8 FF FF 7F F8  FF FF 7F 74 6C 64 30 00  [..........tld0.
```

#### Opcodes

```
  0: 0x0130 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tld0" with entities [EventEntity, EventEntity], work=643*
  1: 0x013F [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0140   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140: 5B 08 80 F8 FF FF 7F F8  FF FF 7F 74 6C 64 31 53  [..........tld1S
0150: F8 FF FF 7F F8 FF FF 7F  74 6C 64 31 00           ........tld1.   
```

#### Opcodes

```
  0: 0x0140 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tld1" with entities [EventEntity, EventEntity], work=643*
  1: 0x014F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tld1" with entities [EventEntity, EventEntity]
  2: 0x015C [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x015D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                                         5B 08 80               [..
0160: F8 FF FF 7F F8 FF FF 7F  74 72 30 30 00           ........tr00.   
```

#### Opcodes

```
  0: 0x015D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr00" with entities [EventEntity, EventEntity], work=643*
  1: 0x016C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                         5B 08 80               [..
0170: F8 FF FF 7F F8 FF FF 7F  74 72 30 31 00           ........tr01.   
```

#### Opcodes

```
  0: 0x016D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tr01" with entities [EventEntity, EventEntity], work=643*
  1: 0x017C [0x00] END_REQSTACK()
```
