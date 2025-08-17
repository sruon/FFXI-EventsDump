# 17510734 - Seed Crystal

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Stellar Fulcrum (ID: 179) |
| Block Size       | 568 bytes                 |
| Total Events     | 26                        |
| References Count | 8                         |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [12](#event-12)            | 0x0001       |      1 |              1 |
| [32000](#event-32000)      | 0x0002       |      1 |              1 |
| [13](#event-13)            | 0x0003       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0004       |     26 |              6 |
| [65535.2](#event-655352)   | 0x001E       |      8 |              3 |
| [65535.3](#event-655353)   | 0x0026       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0030       |     18 |              2 |
| [65535.5](#event-655355)   | 0x0042       |     18 |              2 |
| [65535.6](#event-655356)   | 0x0054       |     18 |              2 |
| [65535.7](#event-655357)   | 0x0066       |     18 |              2 |
| [65535.8](#event-655358)   | 0x0078       |     18 |              2 |
| [65535.9](#event-655359)   | 0x008A       |     18 |              2 |
| [65535.10](#event-6553510) | 0x009C       |     18 |              2 |
| [65535.11](#event-6553511) | 0x00AE       |     18 |              2 |
| [65535.12](#event-6553512) | 0x00C0       |     18 |              2 |
| [65535.13](#event-6553513) | 0x00D2       |     18 |              2 |
| [65535.14](#event-6553514) | 0x00E4       |     18 |              2 |
| [65535.15](#event-6553515) | 0x00F6       |     18 |              2 |
| [65535.16](#event-6553516) | 0x0108       |     18 |              2 |
| [65535.17](#event-6553517) | 0x011A       |     18 |              2 |
| [65535.18](#event-6553518) | 0x012C       |     18 |              2 |
| [65535.19](#event-6553519) | 0x013E       |     35 |              3 |
| [65535.20](#event-6553520) | 0x0161       |     35 |              3 |
| [65535.21](#event-6553521) | 0x0184       |     14 |              2 |
| [65535.22](#event-6553522) | 0x0192       |     14 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x092F      |        2351 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00B4      |         180 |
|       4 | 0x005E      |          94 |
|       5 | 0x005A      |          90 |
|       6 | 0x005F      |          95 |
|       7 | 0x005D      |          93 |

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 32000

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             4E 00 4E 31  0B 01 B6 00 00 80 92 01      N.N1........
0010: 4E 31 0B 01 94 01 4E 31  0B 01 C0 01 80 00        N1....N1......  
```

#### Opcodes

```
  0: 0x0004 [0x4E] SET_ENTITY_HIDE_FLAG: Show Seed Crystal (ID: 17510734/0x010B314E)
  1: 0x000A [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2351*)
  2: 0x000E [0x92] Seed Crystal (ID: 17510734/0x010B314E)->Render.Flags3 ^= 0x01
  3: 0x0014 [0x94] Seed Crystal (ID: 17510734/0x010B314E)->Render.Flags3 ^= 0x01
  4: 0x001A [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  5: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            B6 00                ..
0020: 00 80 C0 01 80 00                                 ......          
```

#### Opcodes

```
  0: 0x001E [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2351*)
  1: 0x0022 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   6C 4E  31 0B 01 02 80 03 80 00        lN1.......
```

#### Opcodes

```
  0: 0x0026 [0x6C] FADE_ENTITY_COLOR(entity_id=Seed Crystal (ID: 17510734/0x010B314E), end_alpha=0*, fade_time=180*)
  1: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: C5 04 80 4E 31 0B 01 4E  31 0B 01 73 30 30 30 02  ...N1..N1..s000.
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0030 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023030 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=94*, param=12403
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       C5 04 80 4E 31 0B  01 4E 31 0B 01 73 30 30    ...N1..N1..s00
0050: 31 02 80 00                                       1...            
```

#### Opcodes

```
  0: 0x0042 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023130 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=94*, param=12403
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             C5 04 80 4E  31 0B 01 4E 31 0B 01 6B      ...N1..N1..k
0060: 69 6C 30 02 80 00                                 il0...          
```

#### Opcodes

```
  0: 0x0054 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002306C for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=94*, param=26987
  1: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   C5 05  80 4E 31 0B 01 4E 31 0B        ...N1..N1.
0070: 01 73 30 30 30 02 80 00                           .s000...        
```

#### Opcodes

```
  0: 0x0066 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023030 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=90*, param=12403
  1: 0x0077 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          C5 05 80 4E 31 0B 01 4E          ...N1..N
0080: 31 0B 01 73 30 30 31 02  80 00                    1..s001...      
```

#### Opcodes

```
  0: 0x0078 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023130 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=90*, param=12403
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                C5 05 80 4E 31 0B            ...N1.
0090: 01 4E 31 0B 01 73 74 70  30 02 80 00              .N1..stp0...    
```

#### Opcodes

```
  0: 0x008A [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023070 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=90*, param=29811
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009C   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      C5 05 80 4E              ...N
00A0: 31 0B 01 4E 31 0B 01 73  74 70 31 02 80 00        1..N1..stp1...  
```

#### Opcodes

```
  0: 0x009C [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023170 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=90*, param=29811
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            C5 05                ..
00B0: 80 4E 31 0B 01 4E 31 0B  01 6B 69 6C 30 02 80 00  .N1..N1..kil0...
```

#### Opcodes

```
  0: 0x00AE [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002306C for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=90*, param=26987
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C0   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: C5 05 80 4E 31 0B 01 4E  31 0B 01 6B 69 6C 31 02  ...N1..N1..kil1.
00D0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00C0 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002316C for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=90*, param=26987
  1: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D2   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       C5 06 80 4E 31 0B  01 4E 31 0B 01 73 30 30    ...N1..N1..s00
00E0: 30 02 80 00                                       0...            
```

#### Opcodes

```
  0: 0x00D2 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023030 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=12403
  1: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             C5 06 80 4E  31 0B 01 4E 31 0B 01 73      ...N1..N1..s
00F0: 30 30 31 02 80 00                                 001...          
```

#### Opcodes

```
  0: 0x00E4 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023130 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=12403
  1: 0x00F5 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F6   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                   C5 06  80 4E 31 0B 01 4E 31 0B        ...N1..N1.
0100: 01 73 30 30 32 02 80 00                           .s002...        
```

#### Opcodes

```
  0: 0x00F6 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023230 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=12403
  1: 0x0107 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0108   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          C5 06 80 4E 31 0B 01 4E          ...N1..N
0110: 31 0B 01 73 30 30 33 02  80 00                    1..s003...      
```

#### Opcodes

```
  0: 0x0108 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023330 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=12403
  1: 0x0119 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011A   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                C5 07 80 4E 31 0B            ...N1.
0120: 01 4E 31 0B 01 73 30 30  31 02 80 00              .N1..s001...    
```

#### Opcodes

```
  0: 0x011A [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023130 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=93*, param=12403
  1: 0x012B [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012C   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                      C5 07 80 4E              ...N
0130: 31 0B 01 4E 31 0B 01 73  30 30 32 02 80 00        1..N1..s002...  
```

#### Opcodes

```
  0: 0x012C [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80023230 for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=93*, param=12403
  1: 0x013D [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013E   |
| Data Size    | 35 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                            C5 06                ..
0140: 80 4E 31 0B 01 4E 31 0B  01 6C 6F 6F 30 02 80 C5  .N1..N1..loo0...
0150: 06 80 4E 31 0B 01 4E 31  0B 01 6C 6F 6F 31 02 80  ..N1..N1..loo1..
0160: 00                                                .               
```

#### Opcodes

```
  0: 0x013E [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002306F for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=28524
  1: 0x014F [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002316F for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=28524
  2: 0x0160 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0161   |
| Data Size    | 35 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:    C5 06 80 4E 31 0B 01  4E 31 0B 01 6B 69 6C 30   ...N1..N1..kil0
0170: 02 80 C5 06 80 4E 31 0B  01 4E 31 0B 01 6B 69 6C  .....N1..N1..kil
0180: 31 02 80 00                                       1...            
```

#### Opcodes

```
  0: 0x0161 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002306C for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=26987
  1: 0x0172 [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x8002316C for entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)], work=95*, param=26987
  2: 0x0183 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0184   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:             2C 4E 31 0B  01 4E 31 0B 01 74 61 6C      ,N1..N1..tal
0190: 6B 00                                             k.              
```

#### Opcodes

```
  0: 0x0184 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "talk" with entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)]
  1: 0x0191 [0x00] END_REQSTACK()
```

### Event 65535.22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0192   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:       2C 4E 31 0B 01 4E  31 0B 01 64 65 61 64 00    ,N1..N1..dead.
```

#### Opcodes

```
  0: 0x0192 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "dead" with entities [Seed Crystal (ID: 17510734/0x010B314E), Seed Crystal (ID: 17510734/0x010B314E)]
  1: 0x019F [0x00] END_REQSTACK()
```
