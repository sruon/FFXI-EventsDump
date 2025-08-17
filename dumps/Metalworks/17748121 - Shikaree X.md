# 17748121 - Shikaree X

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 296 bytes            |
| Total Events     | 8                    |
| References Count | 28                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [855](#event-855)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     41 |             11 |
| [65535.2](#event-655352) | 0x003A       |     16 |              5 |
| [856](#event-856)        | 0x004A       |     10 |              2 |
| [857](#event-857)        | 0x0054       |     10 |              2 |
| [65535.3](#event-655353) | 0x005E       |     15 |              5 |
| [65535.4](#event-655354) | 0x006D       |     26 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF6956  |  4294928726 |
|       1 | 0xFFFFF81F  |  4294965279 |
|       2 | 0xFFFFD8F1  |  4294957297 |
|       3 | 0x0032      |          50 |
|       4 | 0x000D      |          13 |
|       5 | 0x0028      |          40 |
|       6 | 0xFFFF7FD4  |  4294934484 |
|       7 | 0xFFFFF883  |  4294965379 |
|       8 | 0xFFFFD8F0  |  4294957296 |
|       9 | 0xFFFF8F74  |  4294938484 |
|      10 | 0xFFFFF448  |  4294964296 |
|      11 | 0xFFFF936C  |  4294939500 |
|      12 | 0xFFFFF5DA  |  4294964698 |
|      13 | 0x0F22      |        3874 |
|      14 | 0xFFFF6D3E  |  4294929726 |
|      15 | 0x16ADA     |       92890 |
|      16 | 0x3D1E      |       15646 |
|      17 | 0xFFFFB136  |  4294947126 |
|      18 | 0x0348      |         840 |
|      19 | 0xFFFF8B34  |  4294937396 |
|      20 | 0x0444      |        1092 |
|      21 | 0x0FC3      |        4035 |
|      22 | 0xFFFFA68C  |  4294944396 |
|      23 | 0x0764      |        1892 |
|      24 | 0xFFFF6FCD  |  4294930381 |
|      25 | 0xFFFFF95B  |  4294965595 |
|      26 | 0xFFFF6072  |  4294926450 |
|      27 | 0xFFFFE98B  |  4294961547 |

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
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-38.570*, z=-2.017*, y=-9.999*, direction=4.4°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 41 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1C 05 80 1F  00 06 80 07 80 08 80 1F   2..............
0020: 01 1F 00 09 80 0A 80 08  80 1F 01 1F 00 0B 80 0C  ................
0030: 80 08 80 1F 01 6F 39 0D  80 00                    .....o9...      
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1C] WAIT(40* ticks)
  2: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=-32.812*, Z=-1.917*, Y=-10.000*
  3: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=-28.812*, Z=-3.000*, Y=-10.000*
  5: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x002B [0x1F] MOVE_ENTITY: EventEntity moves to X=-27.796*, Z=-2.598*, Y=-10.000*
  7: 0x0033 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0036 [0x39] SET_ENTITY_DIRECTION(direction=21.3°*)
 10: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                32 04 80 1F 00 0E            2.....
0040: 80 01 80 02 80 1F 01 22  01 00                    ......."..      
```

#### Opcodes

```
  0: 0x003A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003D [0x1F] MOVE_ENTITY: EventEntity moves to X=-37.570*, Z=-2.017*, Y=-9.999*
  2: 0x0045 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0047 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0049 [0x00] END_REQSTACK()
```

### Event 856

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                37 0F 80 10 80 11            7.....
0050: 80 12 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=92.890*, z=15.646*, y=-20.170*, direction=73.8°*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 857

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             37 13 80 14  80 02 80 15 80 00            7.........  
```

#### Opcodes

```
  0: 0x0054 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-29.900*, z=1.092*, y=-9.999*, direction=354.6°*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 04                2.
0060: 80 1F 00 16 80 17 80 02  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.900*, Z=1.892*, Y=-9.999*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         32 04 80               2..
0070: 1F 00 18 80 19 80 02 80  1F 01 1F 00 1A 80 1B 80  ................
0080: 02 80 1F 01 22 01 00                              ...."..         
```

#### Opcodes

```
  0: 0x006D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=-36.915*, Z=-1.701*, Y=-9.999*
  2: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-40.846*, Z=-5.749*, Y=-9.999*
  4: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0084 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x0086 [0x00] END_REQSTACK()
```
