# 16982327 - Elisabeth

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Aht Urhgan Whitegate (ID: 50) |
| Block Size       | 160 bytes                     |
| Total Events     | 8                             |
| References Count | 13                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [774](#event-774)        | 0x0001       |      1 |              1 |
| [786](#event-786)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     10 |              2 |
| [65535.2](#event-655352) | 0x000D       |     23 |              7 |
| [65535.3](#event-655353) | 0x0024       |      7 |              3 |
| [65535.4](#event-655354) | 0x002B       |      7 |              3 |
| [65535.5](#event-655355) | 0x0032       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE7C8F  |  4294868111 |
|       1 | 0xFFFFE9B5  |  4294961589 |
|       2 | 0x0000      |           0 |
|       3 | 0x0830      |        2096 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFE5FA6  |  4294860710 |
|       6 | 0xFFFFE7D3  |  4294961107 |
|       7 | 0x0BF3      |        3059 |
|       8 | 0x002F      |          47 |
|       9 | 0x17A5B     |       96859 |
|      10 | 0xFFFF96AD  |  4294940333 |
|      11 | 0xFFFFE891  |  4294961297 |
|      12 | 0x06D7      |        1751 |

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

### Event 774

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

### Event 786

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          37 00 80 01 80  02 80 03 80 00              7.........   
```

#### Opcodes

```
  0: 0x0003 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.185*, z=-5.707*, y=0.000*, direction=184.2°*
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         32 04 80               2..
0010: 1F 00 05 80 06 80 02 80  1F 01 4B 37 21 03 01 07  ..........K7!...
0020: 80 6F 70 00                                       .op.            
```

#### Opcodes

```
  0: 0x000D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-106.586*, Z=-6.189*, Y=0.000*
  2: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001A [0x4B] UPDATE_ENTITY_YAW(entity=Elisabeth (ID: 16982327/0x01032137), yaw=16.8°*)
  4: 0x0021 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0022 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             AB 03 AC 01  08 80 00                     .......     
```

#### Opcodes

```
  0: 0x0024 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0026 [0xAC] EventEntity->StatusEvent = 47*
  2: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002B  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   AC 01 02 80 AB             .....
0030: 04 00                                             ..              
```

#### Opcodes

```
  0: 0x002B [0xAC] EventEntity->StatusEvent = 0*
  1: 0x002F [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0031 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       37 09 80 0A 80 0B  80 0C 80 00                7.........    
```

#### Opcodes

```
  0: 0x0032 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=96.859*, z=-26.963*, y=-5.999*, direction=153.9°*
  1: 0x003B [0x00] END_REQSTACK()
```
