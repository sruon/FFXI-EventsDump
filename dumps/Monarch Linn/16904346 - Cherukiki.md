# 16904346 - Cherukiki

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Monarch Linn (ID: 31) |
| Block Size       | 292 bytes             |
| Total Events     | 8                     |
| References Count | 22                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [32000](#event-32000)    | 0x000D       |     10 |              2 |
| [65535.1](#event-655351) | 0x0017       |     40 |              7 |
| [65535.2](#event-655352) | 0x003F       |     16 |              2 |
| [65535.3](#event-655353) | 0x004F       |     36 |              4 |
| [65535.4](#event-655354) | 0x0073       |     17 |              4 |
| [65535.5](#event-655355) | 0x0084       |     14 |              4 |
| [32001](#event-32001)    | 0x0092       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x9AEE3     |      634595 |
|       1 | 0x93183     |      602499 |
|       2 | 0xF99D      |       63901 |
|       3 | 0x0812      |        2066 |
|       4 | 0xFFFFFC18  |  4294966296 |
|       5 | 0xFFFFFF9C  |  4294967196 |
|       6 | 0x01AF      |         431 |
|       7 | 0x000A      |          10 |
|       8 | 0x0048      |          72 |
|       9 | 0x0000      |           0 |
|      10 | 0x9D91C     |      645404 |
|      11 | 0x93185     |      602501 |
|      12 | 0xF8EB      |       63723 |
|      13 | 0x07F6      |        2038 |
|      14 | 0x0028      |          40 |
|      15 | 0x9A080     |      630912 |
|      16 | 0x92CCE     |      601294 |
|      17 | 0xFA28      |       64040 |
|      18 | 0x9C50C     |      640268 |
|      19 | 0x92668     |      599656 |
|      20 | 0xF915      |       63765 |
|      21 | 0x0801      |        2049 |

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
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=634.595*, z=602.499*, y=63.901*, direction=181.6°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 40 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      33  01 3B F8 FF FF 7F 00 00         3.;......
0020: 01 00 02 00 3A F8 FF FF  7F 03 00 07 01 00 04 80  ....:...........
0030: 07 02 00 05 80 37 00 00  01 00 02 00 03 00 00     .....7......... 
```

#### Opcodes

```
  0: 0x0017 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0019 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  2: 0x0024 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[3])
  3: 0x002B [0x07] ExtData[1]->WorkLocal[1] += 4294966296*
  4: 0x0030 [0x07] ExtData[1]->WorkLocal[2] += 4294967196*
  5: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=ExtData[1]->WorkLocal[2], direction=ExtData[1]->WorkLocal[3]
  6: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               5B                 [
0040: 06 80 F8 FF FF 7F F8 FF  FF 7F 66 75 6B 30 00     ..........fuk0. 
```

#### Opcodes

```
  0: 0x003F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fuk0" with entities [EventEntity, EventEntity], work=431*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004F   |
| Data Size    | 36 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               5B                 [
0050: 06 80 F8 FF FF 7F F8 FF  FF 7F 66 75 6B 31 1C 07  ..........fuk1..
0060: 80 45 08 80 F8 FF FF 7F  F8 FF FF 7F 73 30 37 35  .E..........s075
0070: 09 80 00                                          ...             
```

#### Opcodes

```
  0: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fuk1" with entities [EventEntity, EventEntity], work=431*
  1: 0x005E [0x1C] WAIT(10* ticks)
  2: 0x0061 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s075" with entities [EventEntity, EventEntity], work=[72*, 0*]
  3: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 17 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          5E 69 64 6C 30  37 0A 80 0B 80 0C 80 0D     ^idl07.......
0080: 80 33 00 00                                       .3..            
```

#### Opcodes

```
  0: 0x0073 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0078 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=645.404*, z=602.501*, y=63.723*, direction=179.1°*
  2: 0x0081 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  3: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             32 0E 80 1F  00 0F 80 10 80 11 80 1F      2...........
0090: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0084 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0087 [0x1F] MOVE_ENTITY: EventEntity moves to X=630.912*, Z=601.294*, Y=64.040*
  2: 0x008F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0091 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       37 12 80 13 80 14  80 15 80 00                7.........    
```

#### Opcodes

```
  0: 0x0092 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=640.268*, z=599.656*, y=63.765*, direction=180.1°*
  1: 0x009B [0x00] END_REQSTACK()
```
