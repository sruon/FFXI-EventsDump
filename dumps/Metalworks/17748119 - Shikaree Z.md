# 17748119 - Shikaree Z

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 288 bytes            |
| Total Events     | 8                    |
| References Count | 26                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [855](#event-855)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     38 |             10 |
| [65535.2](#event-655352) | 0x0037       |     16 |              5 |
| [856](#event-856)        | 0x0047       |     10 |              2 |
| [857](#event-857)        | 0x0051       |     10 |              2 |
| [65535.3](#event-655353) | 0x005B       |     15 |              5 |
| [65535.4](#event-655354) | 0x006A       |     29 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF6D3E  |  4294929726 |
|       1 | 0xFFFFF81F  |  4294965279 |
|       2 | 0xFFFFD8F1  |  4294957297 |
|       3 | 0x0032      |          50 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF83BC  |  4294935484 |
|       6 | 0xFFFFF883  |  4294965379 |
|       7 | 0xFFFFD8F0  |  4294957296 |
|       8 | 0xFFFF935C  |  4294939484 |
|       9 | 0xFFFFF448  |  4294964296 |
|      10 | 0xFFFF9904  |  4294940932 |
|      11 | 0xFFFFF305  |  4294963973 |
|      12 | 0x0C1C      |        3100 |
|      13 | 0x16D9D     |       93597 |
|      14 | 0x37CF      |       14287 |
|      15 | 0xFFFFB127  |  4294947111 |
|      16 | 0x0334      |         820 |
|      17 | 0xFFFF9047  |  4294938695 |
|      18 | 0x02DE      |         734 |
|      19 | 0x000C      |          12 |
|      20 | 0xFFFFA7B7  |  4294944695 |
|      21 | 0x003C      |          60 |
|      22 | 0xFFFF6FCD  |  4294930381 |
|      23 | 0xFFFFF95B  |  4294965595 |
|      24 | 0xFFFF6072  |  4294926450 |
|      25 | 0xFFFFE98B  |  4294961547 |

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
0000: 92 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 855

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      37  00 80 01 80 02 80 03 80         7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-37.570*, z=-2.017*, y=-9.999*, direction=4.4°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 1F 00   2..............
0020: 08 80 09 80 07 80 1F 01  1F 00 0A 80 0B 80 07 80  ................
0030: 1F 01 6F 39 0C 80 00                              ..o9...         
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-31.812*, Z=-1.917*, Y=-10.000*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x1F] MOVE_ENTITY: EventEntity moves to X=-27.812*, Z=-3.000*, Y=-10.000*
  4: 0x0026 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-26.364*, Z=-3.323*, Y=-10.000*
  6: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0033 [0x39] SET_ENTITY_DIRECTION(direction=17.0°*)
  9: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      32  04 80 1F 00 00 80 01 80         2........
0040: 02 80 1F 01 22 01 00                              ...."..         
```

#### Opcodes

```
  0: 0x0037 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=-37.570*, Z=-2.017*, Y=-9.999*
  2: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0044 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0046 [0x00] END_REQSTACK()
```

### Event 856

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      37  0D 80 0E 80 0F 80 10 80         7........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0047 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=93.597*, z=14.287*, y=-20.185*, direction=72.1°*
  1: 0x0050 [0x00] END_REQSTACK()
```

### Event 857

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    37 11 80 12 80 02 80  13 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0051 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-28.601*, z=0.734*, y=-9.999*, direction=1.1°*
  1: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   32 04 80 1F 00             2....
0060: 14 80 12 80 02 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x005B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005E [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.601*, Z=0.734*, Y=-9.999*
  2: 0x0066 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0068 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 29 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                1C 15 80 32 04 80            ...2..
0070: 1F 00 16 80 17 80 02 80  1F 01 1F 00 18 80 19 80  ................
0080: 02 80 1F 01 22 01 00                              ...."..         
```

#### Opcodes

```
  0: 0x006A [0x1C] WAIT(60* ticks)
  1: 0x006D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.915*, Z=-1.701*, Y=-9.999*
  3: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.846*, Z=-5.749*, Y=-9.999*
  5: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0084 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  7: 0x0086 [0x00] END_REQSTACK()
```
