# 17780738 - Pherimociel

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 168 bytes             |
| Total Events     | 4                     |
| References Count | 12                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [86](#event-86)          | 0x000D       |     20 |              3 |
| [65535.1](#event-655351) | 0x0021       |     31 |              9 |
| [65535.2](#event-655352) | 0x0040       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x74E4      |       29924 |
|       1 | 0xFFFFCEE3  |  4294954723 |
|       2 | 0xFFFFFF91  |  4294967185 |
|       3 | 0x0159      |         345 |
|       4 | 0x000D      |          13 |
|       5 | 0x7F26      |       32550 |
|       6 | 0xFFFFC8DE  |  4294953182 |
|       7 | 0x8472      |       33906 |
|       8 | 0xFFFFC1FD  |  4294951421 |
|       9 | 0xFFFFFF9C  |  4294967196 |
|      10 | 0x54F6      |       21750 |
|      11 | 0xFFFFE0D1  |  4294959313 |

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

### Event 86

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 79 00  F8 FF FF 7F F0 FF FF 7F  ......y.........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=29.924*, z=-12.573*, y=-0.111*, direction=30.3°*
  1: 0x0016 [0x79] EventEntity looks at LocalPlayer (Basic look)
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 04 80 1F 00 05 80  06 80 02 80 1F 01 1F 00   2..............
0030: 07 80 08 80 09 80 1F 01  1E F0 FF FF 7F 6F 70 00  .............op.
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=32.550*, Z=-14.114*, Y=-0.111*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=33.906*, Z=-15.875*, Y=-0.100*
  4: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x003E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  8: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 32 04 80 1F 00 05 80 06  80 02 80 1F 01 1F 00 0A  2...............
0050: 80 0B 80 02 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0040 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=32.550*, Z=-14.114*, Y=-0.111*
  2: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=21.750*, Z=-7.983*, Y=-0.111*
  4: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0057 [0x00] END_REQSTACK()
```
