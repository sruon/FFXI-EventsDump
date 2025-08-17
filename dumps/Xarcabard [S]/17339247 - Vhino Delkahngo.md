# 17339247 - Vhino Delkahngo

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 400 bytes               |
| Total Events     | 17                      |
| References Count | 27                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [21](#event-21)            | 0x0044       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0045       |     35 |              6 |
| [65535.9](#event-655359)   | 0x0068       |     30 |              7 |
| [22](#event-22)            | 0x0086       |      1 |              1 |
| [41](#event-41)            | 0x0087       |     10 |              3 |
| [65535.10](#event-6553510) | 0x0091       |     14 |              4 |
| [65535.11](#event-6553511) | 0x009F       |     21 |              2 |
| [65535.12](#event-6553512) | 0x00B4       |     21 |              2 |
| [65535.13](#event-6553513) | 0x00C9       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0xCE32      |       52786 |
|       5 | 0xFFFCAA6D  |  4294748781 |
|       6 | 0xFFFFA426  |  4294943782 |
|       7 | 0x05FC      |        1532 |
|       8 | 0x0024      |          36 |
|       9 | 0xCD46      |       52550 |
|      10 | 0xFFFC9059  |  4294742105 |
|      11 | 0xFFFFA47D  |  4294943869 |
|      12 | 0x128D3     |       75987 |
|      13 | 0xFFFC36F0  |  4294719216 |
|      14 | 0xFFFFA153  |  4294943059 |
|      15 | 0x0028      |          40 |
|      16 | 0xFFFDC83A  |  4294821946 |
|      17 | 0x00C2      |         194 |
|      18 | 0xFFFFC416  |  4294951958 |
|      19 | 0x0007      |           7 |
|      20 | 0x000F      |          15 |
|      21 | 0x0010      |          16 |
|      22 | 0x00A7      |         167 |
|      23 | 0x0006      |           6 |
|      24 | 0x0086      |         134 |
|      25 | 0x005B      |          91 |
|      26 | 0x0032      |          50 |

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0044  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             00                                        .           
```

#### Opcodes

```
  0: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 35 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                59 04 F8  FF FF 7F 03 80 1F 00 04       Y..........
0050: 80 05 80 06 80 1F 01 6F  5B 07 80 F8 FF FF 7F F8  .......o[.......
0060: FF FF 7F 76 69 62 30 00                           ...vib0.        
```

#### Opcodes

```
  0: 0x0045 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=52.786*, Z=-218.515*, Y=-23.514*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0058 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "vib0" with entities [EventEntity, EventEntity], work=1532*
  5: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 30 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          59 04 F8 FF FF 7F 08 80          Y.......
0070: 1F 00 09 80 0A 80 0B 80  1F 01 1F 00 0C 80 0D 80  ................
0080: 0E 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0068 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 36* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=52.550*, Z=-225.191*, Y=-23.427*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=75.987*, Z=-248.080*, Y=-24.237*
  4: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0085 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0086  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   00                                    .         
```

#### Opcodes

```
  0: 0x0086 [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 10 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      92  01 F8 FF FF 7F C0 01 80         .........
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x008D [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  2: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    32 0F 80 1F 00 10 80  11 80 12 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0091 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0094 [0x1F] MOVE_ENTITY: EventEntity moves to X=-145.350*, Z=0.194*, Y=-15.338*
  2: 0x009C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               B6                 .
00A0: 0B 13 80 00 80 14 80 15  80 15 80 15 80 14 80 14  ................
00B0: 80 16 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=0*, head=15*, body=16*, hands=16*, legs=16*, feet=15*, main=15*, sub=167*)
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             B6 0B 13 80  17 80 18 80 18 80 18 80      ............
00C0: 14 80 18 80 19 80 1A 80  00                       .........       
```

#### Opcodes

```
  0: 0x00B4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=6*, head=134*, body=134*, hands=134*, legs=15*, feet=134*, main=91*, sub=50*)
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C9  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             C0 00 80 00                    ....   
```

#### Opcodes

```
  0: 0x00C9 [0xC0] EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from 0*)
  1: 0x00CC [0x00] END_REQSTACK()
```
