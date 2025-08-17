# 16904347 - Kukki-Chebukki

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Monarch Linn (ID: 31) |
| Block Size       | 256 bytes             |
| Total Events     | 8                     |
| References Count | 18                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [32000](#event-32000)    | 0x000D       |     10 |              2 |
| [65535.1](#event-655351) | 0x0017       |     40 |              7 |
| [65535.2](#event-655352) | 0x003F       |     16 |              2 |
| [65535.3](#event-655353) | 0x004F       |     16 |              2 |
| [65535.4](#event-655354) | 0x005F       |     17 |              4 |
| [65535.5](#event-655355) | 0x0070       |     14 |              4 |
| [32001](#event-32001)    | 0x007E       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x9AB55     |      633685 |
|       1 | 0x922B3     |      598707 |
|       2 | 0xFAB2      |       64178 |
|       3 | 0x07CC      |        1996 |
|       4 | 0xFFFFFC18  |  4294966296 |
|       5 | 0xFFFFFF9C  |  4294967196 |
|       6 | 0x01AF      |         431 |
|       7 | 0x9E067     |      647271 |
|       8 | 0x91E17     |      597527 |
|       9 | 0xF86B      |       63595 |
|      10 | 0x0811      |        2065 |
|      11 | 0x0028      |          40 |
|      12 | 0x9A1A8     |      631208 |
|      13 | 0x923F1     |      599025 |
|      14 | 0x9C260     |      639584 |
|      15 | 0x925BF     |      599487 |
|      16 | 0xF934      |       63796 |
|      17 | 0x0793      |        1939 |

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
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=633.685*, z=598.707*, y=64.178*, direction=175.4°*
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
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               5B                 [
0050: 06 80 F8 FF FF 7F F8 FF  FF 7F 66 75 6B 31 00     ..........fuk1. 
```

#### Opcodes

```
  0: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "fuk1" with entities [EventEntity, EventEntity], work=431*
  1: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 17 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               5E                 ^
0060: 69 64 6C 30 37 07 80 08  80 09 80 0A 80 33 00 00  idl07........3..
```

#### Opcodes

```
  0: 0x005F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0064 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=647.271*, z=597.527*, y=63.595*, direction=181.5°*
  2: 0x006D [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  3: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 32 0B 80 1F 00 0C 80 0D  80 02 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0070 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=631.208*, Z=599.025*, Y=64.178*
  2: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x007D [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            37 0E                7.
0080: 80 0F 80 10 80 11 80 00                           ........        
```

#### Opcodes

```
  0: 0x007E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=639.584*, z=599.487*, y=63.796*, direction=170.4°*
  1: 0x0087 [0x00] END_REQSTACK()
```
