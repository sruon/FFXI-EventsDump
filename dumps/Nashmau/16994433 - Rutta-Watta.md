# 16994433 - Rutta-Watta

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 420 bytes        |
| Total Events     | 17               |
| References Count | 27               |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [308](#event-308)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     15 |              5 |
| [65535.2](#event-655352)   | 0x0011       |     15 |              5 |
| [65535.3](#event-655353)   | 0x0020       |     15 |              5 |
| [65535.4](#event-655354)   | 0x002F       |     15 |              5 |
| [65535.5](#event-655355)   | 0x003E       |     15 |              5 |
| [65535.6](#event-655356)   | 0x004D       |     15 |              5 |
| [65535.7](#event-655357)   | 0x005C       |     15 |              5 |
| [65535.8](#event-655358)   | 0x006B       |     15 |              5 |
| [65535.9](#event-655359)   | 0x007A       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0089       |     15 |              5 |
| [311](#event-311)          | 0x0098       |      1 |              1 |
| [312](#event-312)          | 0x0099       |      1 |              1 |
| [65535.11](#event-6553511) | 0x009A       |     15 |              5 |
| [65535.12](#event-6553512) | 0x00A9       |      4 |              2 |
| [65535.13](#event-6553513) | 0x00AD       |     55 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x161D      |        5661 |
|       2 | 0xFFFFA3B7  |  4294943671 |
|       3 | 0x0000      |           0 |
|       4 | 0x0026      |          38 |
|       5 | 0x44AD      |       17581 |
|       6 | 0xFFFF9A5F  |  4294941279 |
|       7 | 0x427D      |       17021 |
|       8 | 0xFFFF9D7B  |  4294942075 |
|       9 | 0x0028      |          40 |
|      10 | 0x4791      |       18321 |
|      11 | 0xFFFF961D  |  4294940189 |
|      12 | 0x44D3      |       17619 |
|      13 | 0xFFFF9762  |  4294940514 |
|      14 | 0x440C      |       17420 |
|      15 | 0xFFFF9BAF  |  4294941615 |
|      16 | 0xFFFFD5A9  |  4294956457 |
|      17 | 0xFFFF99D0  |  4294941136 |
|      18 | 0xFFFFFF9F  |  4294967199 |
|      19 | 0xFFFF05D1  |  4294903249 |
|      20 | 0x00A0      |         160 |
|      21 | 0x0008      |           8 |
|      22 | 0x001E      |          30 |
|      23 | 0xFFFFD3B9  |  4294955961 |
|      24 | 0x72F5      |       29429 |
|      25 | 0xFFFFD55E  |  4294956382 |
|      26 | 0x75A0      |       30112 |

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

### Event 308

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 6F    2............o
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=5.661*, Z=-23.625*, Y=0.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 03 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.581*, Z=-26.017*, Y=0.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 04 80 1F 00 07 80 08  80 03 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.021*, Z=-25.221*, Y=0.000*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 00 80 1F 00 05 80 06 80  03 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.581*, Z=-26.017*, Y=0.000*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            32 09                2.
0040: 80 1F 00 0A 80 0B 80 03  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x003E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.321*, Z=-27.107*, Y=0.000*
  2: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         32 04 80               2..
0050: 1F 00 0C 80 0D 80 03 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x004D [0x32] ExtData[1]->MainSpeed = 38* * 0.1
  1: 0x0050 [0x1F] MOVE_ENTITY: EventEntity moves to X=17.619*, Z=-26.782*, Y=0.000*
  2: 0x0058 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x005B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      32 09 80 1F              2...
0060: 00 05 80 06 80 03 80 1F  01 6F 00                 .........o.     
```

#### Opcodes

```
  0: 0x005C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x005F [0x1F] MOVE_ENTITY: EventEntity moves to X=17.581*, Z=-26.017*, Y=0.000*
  2: 0x0067 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0069 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   32 00 80 1F 00             2....
0070: 0E 80 0F 80 03 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x006B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=17.420*, Z=-25.681*, Y=0.000*
  2: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 00 80 1F 00 05            2.....
0080: 80 06 80 03 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007D [0x1F] MOVE_ENTITY: EventEntity moves to X=17.581*, Z=-26.017*, Y=0.000*
  2: 0x0085 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0087 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             32 00 80 1F 00 10 80           2......
0090: 11 80 03 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0089 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x008C [0x1F] MOVE_ENTITY: EventEntity moves to X=-10.839*, Z=-26.160*, Y=0.000*
  2: 0x0094 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0096 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0097 [0x00] END_REQSTACK()
```

### Event 311

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0098  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          00                               .       
```

#### Opcodes

```
  0: 0x0098 [0x00] END_REQSTACK()
```

### Event 312

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0099  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             00                             .      
```

#### Opcodes

```
  0: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                32 00 80 1F 00 12            2.....
00A0: 80 13 80 03 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x009A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x009D [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.097*, Z=-64.047*, Y=0.000*
  2: 0x00A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A9  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             1C 14 80 00                    ....   
```

#### Opcodes

```
  0: 0x00A9 [0x1C] WAIT(160* ticks)
  1: 0x00AC [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AD   |
| Data Size    | 55 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                         02 87 7F               ...
00B0: 15 80 00 E3 00 1E F0 FF  FF 7F 1C 16 80 32 09 80  .............2..
00C0: 1F 00 17 80 18 80 03 80  1F 01 6F 1C 16 80 1E F0  ..........o.....
00D0: FF FF 7F 6F 70 32 00 80  1F 00 19 80 1A 80 03 80  ...op2..........
00E0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x00AD [0x02] IF !(LocalPlayer->Race == 8*) GOTO 0x00E3
  1: 0x00B5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00BA [0x1C] WAIT(30* ticks)
  3: 0x00BD [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  4: 0x00C0 [0x1F] MOVE_ENTITY: EventEntity moves to X=-11.335*, Z=29.429*, Y=0.000*
  5: 0x00C8 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00CA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00CB [0x1C] WAIT(30* ticks)
  8: 0x00CE [0x1E] EventEntity looks at LocalPlayer and starts talking
  9: 0x00D3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x00D4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 11: 0x00D5 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
 12: 0x00D8 [0x1F] MOVE_ENTITY: EventEntity moves to X=-10.914*, Z=30.112*, Y=0.000*
 13: 0x00E0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x00E2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 15: 0x00E3 [0x00] END_REQSTACK()
```
