# 17776703 - Crooked Arrow

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 288 bytes             |
| Total Events     | 5                     |
| References Count | 29                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [207](#event-207)        | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     32 |              8 |
| [65535.2](#event-655352) | 0x0037       |     21 |              7 |
| [65535.3](#event-655353) | 0x004C       |     59 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF0CAA  |  4294905002 |
|       1 | 0x3E01      |       15873 |
|       2 | 0x03E8      |        1000 |
|       3 | 0x04A2      |        1186 |
|       4 | 0x000A      |          10 |
|       5 | 0x0028      |          40 |
|       6 | 0xFFFF1074  |  4294905972 |
|       7 | 0x2BFF      |       11263 |
|       8 | 0x0320      |         800 |
|       9 | 0xFFFF1239  |  4294906425 |
|      10 | 0x27D0      |       10192 |
|      11 | 0x018E      |         398 |
|      12 | 0x0032      |          50 |
|      13 | 0xFFFF11C2  |  4294906306 |
|      14 | 0x22E0      |        8928 |
|      15 | 0x0000      |           0 |
|      16 | 0x0238      |         568 |
|      17 | 0x001E      |          30 |
|      18 | 0xFFFF0FD8  |  4294905816 |
|      19 | 0x2D59      |       11609 |
|      20 | 0xFFFF375B  |  4294915931 |
|      21 | 0x63FD      |       25597 |
|      22 | 0x03E7      |         999 |
|      23 | 0xFFFF8862  |  4294936674 |
|      24 | 0x96BE      |       38590 |
|      25 | 0xFFFFA4F9  |  4294943993 |
|      26 | 0x9079      |       36985 |
|      27 | 0xFFFFC5A6  |  4294952358 |
|      28 | 0x5EBB      |       24251 |

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

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 37 00 80   ............7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-62.294*, z=15.873*, y=1.000*, direction=104.2°*
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 32 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1C  04 80 32 05 80 1F 00 06         ...2.....
0020: 80 07 80 08 80 1F 01 1F  00 09 80 0A 80 0B 80 1F  ................
0030: 01 1E 39 40 0F 01 00                              ..9@...         
```

#### Opcodes

```
  0: 0x0017 [0x1C] WAIT(10* ticks)
  1: 0x001A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.324*, Z=11.263*, Y=0.800*
  3: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.871*, Z=10.192*, Y=0.398*
  5: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0031 [0x1E] EventEntity looks at Unnamed NPC (ID: 17776697/0x010F4039) and starts talking
  7: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      1C  0C 80 32 05 80 1F 00 0D         ...2.....
0040: 80 0E 80 0F 80 1F 01 6F  39 10 80 00              .......o9...    
```

#### Opcodes

```
  0: 0x0037 [0x1C] WAIT(50* ticks)
  1: 0x003A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.990*, Z=8.928*, Y=0.000*
  3: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0048 [0x39] SET_ENTITY_DIRECTION(direction=3.1°*)
  6: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 59 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      1C 11 80 32              ...2
0050: 05 80 1F 00 12 80 13 80  02 80 1F 01 1F 00 14 80  ................
0060: 15 80 16 80 1F 01 1F 00  17 80 18 80 0F 80 1F 01  ................
0070: 1F 00 19 80 1A 80 0F 80  1F 01 1F 00 1B 80 1C 80  ................
0080: 0F 80 1F 01 22 01 00                              ...."..         
```

#### Opcodes

```
  0: 0x004C [0x1C] WAIT(30* ticks)
  1: 0x004F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.480*, Z=11.609*, Y=1.000*
  3: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x005C [0x1F] MOVE_ENTITY: EventEntity moves to X=-51.365*, Z=25.597*, Y=0.999*
  5: 0x0064 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=-30.622*, Z=38.590*, Y=0.000*
  7: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=-23.303*, Z=36.985*, Y=0.000*
  9: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 10: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.938*, Z=24.251*, Y=0.000*
 11: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x0084 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 13: 0x0086 [0x00] END_REQSTACK()
```
