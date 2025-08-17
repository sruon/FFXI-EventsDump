# 17825940 - Lhe Lhangavo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 428 bytes                 |
| Total Events     | 20                        |
| References Count | 31                        |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [5023](#event-5023)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351)   | 0x0008       |     14 |              4 |
| [5028](#event-5028)        | 0x0016       |      7 |              2 |
| [65535.2](#event-655352)   | 0x001D       |     15 |              5 |
| [135](#event-135)          | 0x002C       |      1 |              1 |
| [65535.3](#event-655353)   | 0x002D       |     14 |              4 |
| [65535.4](#event-655354)   | 0x003B       |     14 |              4 |
| [154](#event-154)          | 0x0049       |      1 |              1 |
| [65535.5](#event-655355)   | 0x004A       |     17 |              5 |
| [65535.6](#event-655356)   | 0x005B       |     15 |              5 |
| [158](#event-158)          | 0x006A       |      1 |              1 |
| [185](#event-185)          | 0x006B       |      7 |              2 |
| [65535.7](#event-655357)   | 0x0072       |     14 |              4 |
| [65535.8](#event-655358)   | 0x0080       |      5 |              2 |
| [65535.9](#event-655359)   | 0x0085       |      5 |              2 |
| [5221](#event-5221)        | 0x008A       |      7 |              2 |
| [65535.10](#event-6553510) | 0x0091       |     22 |              6 |
| [5225](#event-5225)        | 0x00A7       |      7 |              2 |
| [65535.11](#event-6553511) | 0x00AE       |     34 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE9D3F  |  4294876479 |
|       2 | 0xFFFFF7E2  |  4294965218 |
|       3 | 0x0D15      |        3349 |
|       4 | 0xFFFE9CF1  |  4294876401 |
|       5 | 0x1A13      |        6675 |
|       6 | 0xFFFE9D66  |  4294876518 |
|       7 | 0x28DB      |       10459 |
|       8 | 0x0D16      |        3350 |
|       9 | 0xFFFEA6FB  |  4294878971 |
|      10 | 0x2A45      |       10821 |
|      11 | 0xFFFEA20A  |  4294877706 |
|      12 | 0x2A38      |       10808 |
|      13 | 0x001E      |          30 |
|      14 | 0xFFFEA298  |  4294877848 |
|      15 | 0x2554      |        9556 |
|      16 | 0x02B4      |         692 |
|      17 | 0xFFFFBF8B  |  4294950795 |
|      18 | 0x0000      |           0 |
|      19 | 0x05F3      |        1523 |
|      20 | 0x0A9A      |        2714 |
|      21 | 0xFFFF81D4  |  4294934996 |
|      22 | 0xFFFE825C  |  4294869596 |
|      23 | 0xFFFFFD76  |  4294966646 |
|      24 | 0x000A      |          10 |
|      25 | 0xFFFE9F44  |  4294876996 |
|      26 | 0x2238      |        8760 |
|      27 | 0xFFFEA138  |  4294877496 |
|      28 | 0x27CE      |       10190 |
|      29 | 0xFFFEA4A8  |  4294878376 |
|      30 | 0x2A94      |       10900 |

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

### Event 5023

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          32 00 80 1F 00 01 80 02          2.......
0010: 80 03 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0008 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000B [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.817*, Z=-2.078*, Y=3.349*
  2: 0x0013 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0015 [0x00] END_REQSTACK()
```

### Event 5028

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0016 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         32 00 80               2..
0020: 1F 00 04 80 05 80 03 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x001D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0020 [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.895*, Z=6.675*, Y=3.349*
  2: 0x0028 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002B [0x00] END_REQSTACK()
```

### Event 135

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      00                       .   
```

#### Opcodes

```
  0: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 00 80               2..
0030: 1F 00 06 80 07 80 08 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.778*, Z=10.459*, Y=3.350*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 00 80 1F 00             2....
0040: 09 80 0A 80 08 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=-88.325*, Z=10.821*, Y=3.350*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x00] END_REQSTACK()
```

### Event 154

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             00                             .      
```

#### Opcodes

```
  0: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 00 80 1F 00 0B            2.....
0050: 80 0C 80 03 80 1F 01 1C  0D 80 00                 ...........     
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.590*, Z=10.808*, Y=3.349*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x1C] WAIT(30* ticks)
  4: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 00 80 1F 00             2....
0060: 0E 80 0F 80 03 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.448*, Z=9.556*, Y=3.349*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0069 [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                00                           .     
```

#### Opcodes

```
  0: 0x006A [0x00] END_REQSTACK()
```

### Event 185

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   92 01 F8 FF FF             .....
0070: 7F 00                                             ..              
```

#### Opcodes

```
  0: 0x006B [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       32 00 80 1F 00 10  80 11 80 12 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0072 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0075 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.692*, Z=-16.501*, Y=0.000*
  2: 0x007D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007F [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0080  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080: B6 00 13 80 00                                    .....           
```

#### Opcodes

```
  0: 0x0080 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=1523*)
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0085  |
| Data Size    | 5 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                B6 00 14  80 00                         .....      
```

#### Opcodes

```
  0: 0x0085 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2714*)
  1: 0x0089 [0x00] END_REQSTACK()
```

### Event 5221

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                92 01 F8 FF FF 7F            ......
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x008A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0090 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0091   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:    32 00 80 1F 00 15 80  16 80 17 80 1F 01 1C 18   2..............
00A0: 80 1E 91 00 10 01 00                              .......         
```

#### Opcodes

```
  0: 0x0091 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0094 [0x1F] MOVE_ENTITY: EventEntity moves to X=-32.300*, Z=-97.700*, Y=-0.650*
  2: 0x009C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x009E [0x1C] WAIT(10* ticks)
  4: 0x00A1 [0x1E] EventEntity looks at Levil (ID: 17825937/0x01100091) and starts talking
  5: 0x00A6 [0x00] END_REQSTACK()
```

### Event 5225

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A7  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x00A7 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00AD [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AE   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                            32 00                2.
00B0: 80 1F 00 19 80 1A 80 08  80 1F 01 1F 00 1B 80 1C  ................
00C0: 80 08 80 1F 01 1F 00 1D  80 1E 80 08 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x00AE [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B1 [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.300*, Z=8.760*, Y=3.350*
  2: 0x00B9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BB [0x1F] MOVE_ENTITY: EventEntity moves to X=-89.800*, Z=10.190*, Y=3.350*
  4: 0x00C3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00C5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-88.920*, Z=10.900*, Y=3.350*
  6: 0x00CD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x00CF [0x00] END_REQSTACK()
```
