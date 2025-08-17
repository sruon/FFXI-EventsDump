# 17772707 - Francmage

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 248 bytes                 |
| Total Events     | 4                         |
| References Count | 28                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10008](#event-10008)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     92 |             20 |
| [65535.2](#event-655352) | 0x005E       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0009      |           9 |
|       1 | 0x17FB2     |       98226 |
|       2 | 0x7A86      |       31366 |
|       3 | 0xFFFFA239  |  4294943289 |
|       4 | 0x17F71     |       98161 |
|       5 | 0x739B      |       29595 |
|       6 | 0xFFFFA22E  |  4294943278 |
|       7 | 0x17DE3     |       97763 |
|       8 | 0x688A      |       26762 |
|       9 | 0xFFFFA202  |  4294943234 |
|      10 | 0x17B18     |       97048 |
|      11 | 0x5CD3      |       23763 |
|      12 | 0xFFFFA240  |  4294943296 |
|      13 | 0x17556     |       95574 |
|      14 | 0x55BF      |       21951 |
|      15 | 0xFFFFA23D  |  4294943293 |
|      16 | 0x16B30     |       92976 |
|      17 | 0x52B9      |       21177 |
|      18 | 0xFFFFA1F4  |  4294943220 |
|      19 | 0x15C34     |       89140 |
|      20 | 0x4E6C      |       20076 |
|      21 | 0x14E0A     |       85514 |
|      22 | 0x4E58      |       20056 |
|      23 | 0xFFFFA209  |  4294943241 |
|      24 | 0x193C7     |      103367 |
|      25 | 0x0F1A      |        3866 |
|      26 | 0xFFFFA21E  |  4294943262 |
|      27 | 0x05F6      |        1526 |

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

### Event 10008

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
| Data Size    | 92 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 05 80 06 80 1F  01 1F 00 07 80 08 80 09  ................
0020: 80 1F 01 1F 00 0A 80 0B  80 0C 80 1F 01 27 10 A4  .............'..
0030: 30 0F 01 02 1F 00 0D 80  0E 80 0F 80 1F 01 1F 00  0...............
0040: 10 80 11 80 12 80 1F 01  1F 00 13 80 14 80 0C 80  ................
0050: 1F 01 1F 00 15 80 16 80  17 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=98.226*, Z=31.366*, Y=-24.007*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=98.161*, Z=29.595*, Y=-24.018*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x1F] MOVE_ENTITY: EventEntity moves to X=97.763*, Z=26.762*, Y=-24.062*
  6: 0x0021 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=97.048*, Z=23.763*, Y=-24.000*
  8: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x002D [0x27] REQ_SET(priority=0x10, entity_id=Courisaille (ID: 17772708/0x010F30A4), tag_num=0x02)
 10: 0x0034 [0x1F] MOVE_ENTITY: EventEntity moves to X=95.574*, Z=21.951*, Y=-24.003*
 11: 0x003C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 12: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=92.976*, Z=21.177*, Y=-24.076*
 13: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 14: 0x0048 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.140*, Z=20.076*, Y=-24.000*
 15: 0x0050 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 16: 0x0052 [0x1F] MOVE_ENTITY: EventEntity moves to X=85.514*, Z=20.056*, Y=-24.055*
 17: 0x005A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 18: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 19: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            37 18                7.
0060: 80 19 80 1A 80 1B 80 00                           ........        
```

#### Opcodes

```
  0: 0x005E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=103.367*, z=3.866*, y=-24.034*, direction=134.1°*
  1: 0x0067 [0x00] END_REQSTACK()
```
