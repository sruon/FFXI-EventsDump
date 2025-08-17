# 17744030 - Louverance

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 196 bytes             |
| Total Events     | 5                     |
| References Count | 19                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [306](#event-306)        | 0x0007       |     10 |              2 |
| [65535.1](#event-655351) | 0x0011       |     26 |              7 |
| [65535.2](#event-655352) | 0x002B       |     14 |              5 |
| [65535.3](#event-655353) | 0x0039       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFEC787  |  4294887303 |
|       1 | 0xFFFF9C4C  |  4294941772 |
|       2 | 0x074C      |        1868 |
|       3 | 0x0BC2      |        3010 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFEC6A9  |  4294887081 |
|       6 | 0xFFFFE77D  |  4294961021 |
|       7 | 0x0773      |        1907 |
|       8 | 0xFFFEC720  |  4294887200 |
|       9 | 0xFFFFFF41  |  4294967105 |
|      10 | 0xFFFFF5E0  |  4294964704 |
|      11 | 0xFFFEC9B4  |  4294887860 |
|      12 | 0x1E49      |        7753 |
|      13 | 0xFFFFF5C9  |  4294964681 |
|      14 | 0xFFFEB56B  |  4294882667 |
|      15 | 0x2685      |        9861 |
|      16 | 0xFFFFF7CB  |  4294965195 |
|      17 | 0xFFFE5A4F  |  4294859343 |
|      18 | 0x0CF0      |        3312 |

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

### Event 306

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
  0: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-79.993*, z=-25.524*, y=1.868*, direction=264.5°*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 33 01   2............3.
0020: 5A 00 08 80 09 80 0A 80  5A 01 00                 Z.......Z..     
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-80.215*, Z=-6.275*, Y=1.907*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  4: 0x0020 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-80.096*, Z=-0.191*, Y=-2.592*
  5: 0x0028 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  6: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 14 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   33 00 1F 00 0B             3....
0030: 80 0C 80 0D 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x002B [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  1: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=-79.436*, Z=7.753*, Y=-2.615*
  2: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             32 04 80 1F 00 0E 80           2......
0040: 0F 80 10 80 1F 01 1F 00  11 80 12 80 10 80 1F 01  ................
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-84.629*, Z=9.861*, Y=-2.101*
  2: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0046 [0x1F] MOVE_ENTITY: EventEntity moves to X=-107.953*, Z=3.312*, Y=-2.101*
  4: 0x004E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0050 [0x00] END_REQSTACK()
```
