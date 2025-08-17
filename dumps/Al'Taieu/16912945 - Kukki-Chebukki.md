# 16912945 - Kukki-Chebukki

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Al'Taieu (ID: 33) |
| Block Size       | 220 bytes         |
| Total Events     | 7                 |
| References Count | 19                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      7 |              2 |
| [162](#event-162)        | 0x0007       |     12 |              3 |
| [65535.1](#event-655351) | 0x0013       |     18 |              6 |
| [65535.2](#event-655352) | 0x0025       |     18 |              6 |
| [65535.3](#event-655353) | 0x0037       |     17 |              6 |
| [65535.4](#event-655354) | 0x0048       |     16 |              5 |
| [163](#event-163)        | 0x0058       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFE9BF  |  4294961599 |
|       1 | 0xFFF4C20C  |  4294230540 |
|       2 | 0xFFFFF08B  |  4294963339 |
|       3 | 0x009C      |         156 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFFF3F1  |  4294964209 |
|       6 | 0xFFF4C2E5  |  4294230757 |
|       7 | 0xFFFFF059  |  4294963289 |
|       8 | 0xFFFFFBC9  |  4294966217 |
|       9 | 0xFFF4C259  |  4294230617 |
|      10 | 0x000A      |          10 |
|      11 | 0xFFFFFE22  |  4294966818 |
|      12 | 0xFFF4C4D9  |  4294231257 |
|      13 | 0xFFFFFEF4  |  4294967028 |
|      14 | 0xFFF50701  |  4294248193 |
|      15 | 0xFFFFF428  |  4294964264 |
|      16 | 0xA66D8     |      681688 |
|      17 | 0xFFFC9E56  |  4294745686 |
|      18 | 0x0778      |        1912 |

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

### Event 162

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      33  01 37 00 80 01 80 02 80         3.7......
0010: 03 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0007 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0009 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-5.697*, z=-736.756*, y=-3.957*, direction=13.7°*
  2: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          32 04 80 33 01  5A 00 05 80 06 80 07 80     2..3.Z.......
0020: 5A 01 33 00 00                                    Z.3..           
```

#### Opcodes

```
  0: 0x0013 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0016 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0018 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-3.087*, Z=-736.539*, Y=-4.007*
  3: 0x0020 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  4: 0x0022 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  5: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                32 04 80  1F 00 08 80 09 80 07 80       2..........
0030: 1F 01 6F 1C 0A 80 00                              ..o....         
```

#### Opcodes

```
  0: 0x0025 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.079*, Z=-736.679*, Y=-4.007*
  2: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0033 [0x1C] WAIT(10* ticks)
  5: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 17 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      AB  08 32 04 80 1F 00 0B 80         ..2......
0040: 0C 80 07 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x0037 [0xAB] EventEntity->Render.Flags2 |= 0x02 // Set bit 1
  1: 0x0039 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x003C [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.478*, Z=-736.039*, Y=-4.007*
  3: 0x0044 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0046 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          AB 07 32 04 80 1F 00 0D          ..2.....
0050: 80 0E 80 0F 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x0048 [0xAB] EventEntity->Render.Flags2 |= 0x01 // Set bit 0
  1: 0x004A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=-0.268*, Z=-719.103*, Y=-3.032*
  3: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0057 [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          37 10 80 11 80 07 80 12          7.......
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0058 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=681.688*, z=-221.610*, y=-4.007*, direction=168.0°*
  1: 0x0061 [0x00] END_REQSTACK()
```
