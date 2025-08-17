# 16883754 - Nagmolada

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 172 bytes                   |
| Total Events     | 6                           |
| References Count | 16                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [113](#event-113)        | 0x0001       |     13 |              3 |
| [65535.1](#event-655351) | 0x000E       |     10 |              2 |
| [65535.2](#event-655352) | 0x0018       |     10 |              2 |
| [65535.3](#event-655353) | 0x0022       |      9 |              3 |
| [65535.4](#event-655354) | 0x002B       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x13430     |       78896 |
|       1 | 0x11BF8     |       72696 |
|       2 | 0xFFFF7B30  |  4294933296 |
|       3 | 0x03C1      |         961 |
|       4 | 0x439F      |       17311 |
|       5 | 0x09AD      |        2477 |
|       6 | 0xFFFF9139  |  4294938937 |
|       7 | 0x06CE      |        1742 |
|       8 | 0x26C3      |        9923 |
|       9 | 0xFFFFFE0C  |  4294966796 |
|      10 | 0xFFFFFC98  |  4294966424 |
|      11 | 0xFFFFAA92  |  4294945426 |
|      12 | 0x0C70      |        3184 |
|      13 | 0x000D      |          13 |
|      14 | 0x1D5D      |        7517 |
|      15 | 0xFFFFA9E4  |  4294945252 |

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

### Event 113

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 94  01 F8 FF FF 7F 00         .............  
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            37 00                7.
0010: 80 01 80 02 80 03 80 00                           ........        
```

#### Opcodes

```
  0: 0x000E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=78.896*, z=72.696*, y=-34.000*, direction=84.5°*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          37 04 80 05 80 06 80 07          7.......
0020: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0018 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=17.311*, z=2.477*, y=-28.359*, direction=153.1°*
  1: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0022  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       2B 2B A0 01 01 08  80 23 00                   ++.....#.     
```

#### Opcodes

```
  0: 0x0022 [0x2B] Justinius (ID: 16883755/0x0101A02B) [9923*]:
    → "Ah, your timing is excellent. Our leader has returned."
  1: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   37 09 80 0A 80             7....
0030: 0B 80 0C 80 32 0D 80 1F  00 09 80 0E 80 0F 80 1F  ....2...........
0040: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x002B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-0.500*, z=-0.872*, y=-21.870*, direction=279.8°*
  1: 0x0034 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.500*, Z=7.517*, Y=-22.044*
  3: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0041 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0042 [0x00] END_REQSTACK()
```
