# 17776868 - Goblin Intimidator

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 404 bytes             |
| Total Events     | 21                    |
| References Count | 16                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     15 |              4 |
| [65535.2](#event-655352)   | 0x0010       |     10 |              2 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |      5 |              2 |
| [10180](#event-10180)      | 0x0029       |      1 |              1 |
| [10181](#event-10181)      | 0x002A       |      4 |              2 |
| [65535.5](#event-655355)   | 0x002E       |     18 |              2 |
| [10182](#event-10182)      | 0x0040       |      1 |              1 |
| [65535.6](#event-655356)   | 0x0041       |      8 |              3 |
| [65535.7](#event-655357)   | 0x0049       |     18 |              3 |
| [65535.8](#event-655358)   | 0x005B       |     16 |              2 |
| [65535.9](#event-655359)   | 0x006B       |     16 |              2 |
| [65535.10](#event-6553510) | 0x007B       |     16 |              2 |
| [65535.11](#event-6553511) | 0x008B       |     16 |              2 |
| [10184](#event-10184)      | 0x009B       |      1 |              1 |
| [65535.12](#event-6553512) | 0x009C       |      8 |              3 |
| [65535.13](#event-6553513) | 0x00A4       |     27 |              7 |
| [65535.14](#event-6553514) | 0x00BF       |     15 |              5 |
| [65535.15](#event-6553515) | 0x00CE       |     16 |              2 |
| [65535.16](#event-6553516) | 0x00DE       |     16 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0080      |         128 |
|       1 | 0x0000      |           0 |
|       2 | 0x0034      |          52 |
|       3 | 0x0001      |           1 |
|       4 | 0x007C      |         124 |
|       5 | 0x093C      |        2364 |
|       6 | 0x0A50      |        2640 |
|       7 | 0x01F1      |         497 |
|       8 | 0x000E      |          14 |
|       9 | 0xFFFEA967  |  4294879591 |
|      10 | 0x12F63     |       77667 |
|      11 | 0xFFFFFB50  |  4294966096 |
|      12 | 0x000F      |          15 |
|      13 | 0xFFFEB5D8  |  4294882776 |
|      14 | 0x11465     |       70757 |
|      15 | 0x00D7      |         215 |

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
| Data Size    | 15 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    22 00 92 01 F8 FF FF  7F 94 01 F8 FF FF 7F 00   "..............
```

#### Opcodes

```
  0: 0x0001 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0003 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0009 [0x94] EventEntity->Render.Flags3 ^= 0x01
  3: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0010 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=0*)
  1: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                6C F8 FF FF 7F 01            l.....
0020: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             B6 00 02 80  00                           .....       
```

#### Opcodes

```
  0: 0x0024 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=52*)
  1: 0x0028 [0x00] END_REQSTACK()
```

### Event 10180

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0029  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             00                             .      
```

#### Opcodes

```
  0: 0x0029 [0x00] END_REQSTACK()
```

### Event 10181

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002A  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                C0 03 80 00                  ....  
```

#### Opcodes

```
  0: 0x002A [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 18 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            C5 04                ..
0030: 80 F8 FF FF 7F F8 FF FF  7F 6D 61 69 6E 01 80 00  .........main...
```

#### Opcodes

```
  0: 0x002E [0xC5] LOAD_SCHEDULED_TASK_ALT3: Load scheduler 0x80016E69 for entities [EventEntity, EventEntity], work=124*, param=24941
  1: 0x003F [0x00] END_REQSTACK()
```

### Event 10182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0040  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0040 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0041  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    B6 00 05 80 C0 03 80  00                        ........       
```

#### Opcodes

```
  0: 0x0041 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2364*)
  1: 0x0045 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0049   |
| Data Size    | 18 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             22 00 5B 06 80 F8 FF           ".[....
0050: FF 7F F8 FF FF 7F 62 6B  61 30 00                 ......bka0.     
```

#### Opcodes

```
  0: 0x0049 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bka0" with entities [EventEntity, EventEntity], work=2640*
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   5B 06 80 F8 FF             [....
0060: FF 7F F8 FF FF 7F 62 6B  61 6C 00                 ......bkal.     
```

#### Opcodes

```
  0: 0x005B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bkal" with entities [EventEntity, EventEntity], work=2640*
  1: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   5B 06 80 F8 FF             [....
0070: FF 7F F8 FF FF 7F 62 6B  61 31 00                 ......bka1.     
```

#### Opcodes

```
  0: 0x006B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bka1" with entities [EventEntity, EventEntity], work=2640*
  1: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   5B 06 80 F8 FF             [....
0080: FF 7F F8 FF FF 7F 62 6B  72 30 00                 ......bkr0.     
```

#### Opcodes

```
  0: 0x007B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bkr0" with entities [EventEntity, EventEntity], work=2640*
  1: 0x008A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008B   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                   5B 06 80 F8 FF             [....
0090: FF 7F F8 FF FF 7F 62 6B  72 31 00                 ......bkr1.     
```

#### Opcodes

```
  0: 0x008B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bkr1" with entities [EventEntity, EventEntity], work=2640*
  1: 0x009A [0x00] END_REQSTACK()
```

### Event 10184

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   00                         .    
```

#### Opcodes

```
  0: 0x009B [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      B6 00 07 80              ....
00A0: C0 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009C [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=497*)
  1: 0x00A0 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             32 08 80 1F  00 09 80 0A 80 0B 80 1F      2...........
00B0: 01 6F 1C 0C 80 4A F8 FF  FF 7F E0 40 0F 01 00     .o...J.....@... 
```

#### Opcodes

```
  0: 0x00A4 [0x32] ExtData[1]->MainSpeed = 14* * 0.1
  1: 0x00A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-87.705*, Z=77.667*, Y=-1.200*
  2: 0x00AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00B1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00B2 [0x1C] WAIT(15* ticks)
  5: 0x00B5 [0x4A] EventEntity looks at Moogle (ID: 17776864/0x010F40E0)
  6: 0x00BE [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               32                 2
00C0: 08 80 1F 00 0D 80 0E 80  0B 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x00BF [0x32] ExtData[1]->MainSpeed = 14* * 0.1
  1: 0x00C2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-84.520*, Z=70.757*, Y=-1.200*
  2: 0x00CA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00CC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00CD [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            5B 0F                [.
00D0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 00        .........tlk0.  
```

#### Opcodes

```
  0: 0x00CE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=215*
  1: 0x00DD [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DE   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            5B 0F                [.
00E0: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 65 00        .........tlke.  
```

#### Opcodes

```
  0: 0x00DE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlke" with entities [EventEntity, EventEntity], work=215*
  1: 0x00ED [0x00] END_REQSTACK()
```
