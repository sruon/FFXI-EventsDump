# 17780989 - Eternal Flame

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 220 bytes             |
| Total Events     | 7                     |
| References Count | 17                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20037](#event-20037)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     44 |             10 |
| [20047](#event-20047)    | 0x002E       |      1 |              1 |
| [65535.2](#event-655352) | 0x002F       |     24 |              6 |
| [65535.3](#event-655353) | 0x0047       |     13 |              3 |
| [65535.4](#event-655354) | 0x0054       |     22 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF72BE  |  4294931134 |
|       2 | 0xFFFF2FAE  |  4294913966 |
|       3 | 0x0000      |           0 |
|       4 | 0xFFFF70F7  |  4294930679 |
|       5 | 0xFFFF2DBC  |  4294913468 |
|       6 | 0x01F3      |         499 |
|       7 | 0xFFFF6F13  |  4294930195 |
|       8 | 0xFFFF294B  |  4294912331 |
|       9 | 0x03E7      |         999 |
|      10 | 0xFFFF64BE  |  4294927550 |
|      11 | 0xFFFF18CD  |  4294908109 |
|      12 | 0x0DAB      |        3499 |
|      13 | 0xFFFF5294  |  4294922900 |
|      14 | 0xFFFF4656  |  4294919766 |
|      15 | 0x0014      |          20 |
|      16 | 0x000E      |          14 |

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

### Event 20037

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
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 5A 00 01  80 02 80 03 80 5A 01 5A    2..Z.......Z.Z
0010: 00 04 80 05 80 06 80 5A  01 5A 00 07 80 08 80 09  .......Z.Z......
0020: 80 5A 01 5A 00 0A 80 0B  80 0C 80 5A 01 00        .Z.Z.......Z..  
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-36.162*, Z=-53.330*, Y=0.000*
  2: 0x000D [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x000F [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-36.617*, Z=-53.828*, Y=0.499*
  4: 0x0017 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x0019 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-37.101*, Z=-54.965*, Y=0.999*
  6: 0x0021 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x0023 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-39.746*, Z=-59.187*, Y=3.499*
  8: 0x002B [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  9: 0x002D [0x00] END_REQSTACK()
```

### Event 20047

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            00                   . 
```

#### Opcodes

```
  0: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               32                 2
0030: 00 80 1F 00 0D 80 0E 80  03 80 1F 01 6F 4A F8 FF  ............oJ..
0040: FF 7F F6 50 0F 01 00                              ...P...         
```

#### Opcodes

```
  0: 0x002F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0032 [0x1F] MOVE_ENTITY: EventEntity moves to X=-44.396*, Z=-47.530*, Y=0.000*
  2: 0x003A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003D [0x4A] EventEntity looks at Nantoto (ID: 17780982/0x010F50F6)
  5: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      1C  0F 80 4A F8 FF FF 7F F0         ...J.....
0050: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0047 [0x1C] WAIT(20* ticks)
  1: 0x004A [0x4A] EventEntity looks at LocalPlayer
  2: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 22 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             2A 08 F0 FF  FF 7F 1C 0F 80 6E F8 FF      *........n..
0060: FF 7F 10 80 99 F8 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x0054 [0x2A] GET_REQ_LEVEL(level=8, entity_id=LocalPlayer)
  1: 0x005A [0x1C] WAIT(20* ticks)
  2: 0x005D [0x6E] EventEntity uses emote 14*
  3: 0x0064 [0x99] Wait for EventEntity animation to complete
  4: 0x0069 [0x00] END_REQSTACK()
```
