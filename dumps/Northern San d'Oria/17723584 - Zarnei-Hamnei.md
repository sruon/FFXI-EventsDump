# 17723584 - Zarnei-Hamnei

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 260 bytes                     |
| Total Events     | 10                            |
| References Count | 15                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [41](#event-41)          | 0x0001       |     10 |              2 |
| [15](#event-15)          | 0x000B       |     12 |              3 |
| [65535.1](#event-655351) | 0x0017       |     20 |              6 |
| [65535.2](#event-655352) | 0x002B       |     20 |              6 |
| [65535.3](#event-655353) | 0x003F       |     13 |              4 |
| [65535.4](#event-655354) | 0x004C       |     19 |              3 |
| [65535.5](#event-655355) | 0x005F       |     19 |              3 |
| [65535.6](#event-655356) | 0x0072       |     19 |              3 |
| [65535.7](#event-655357) | 0x0085       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DF8      |        7672 |
|       1 | 0x78B8      |       30904 |
|       2 | 0x01F4      |         500 |
|       3 | 0x05D1      |        1489 |
|       4 | 0x1A86      |        6790 |
|       5 | 0x7F6A      |       32618 |
|       6 | 0x0C38      |        3128 |
|       7 | 0x0015      |          21 |
|       8 | 0x0E6B      |        3691 |
|       9 | 0x693C      |       26940 |
|      10 | 0x01F3      |         499 |
|      11 | 0x169D      |        5789 |
|      12 | 0x6E4D      |       28237 |
|      13 | 0x0055      |          85 |
|      14 | 0x001E      |          30 |

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

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=7.672*, z=30.904*, y=0.500*, direction=130.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   22 01 37 04 80             ".7..
0010: 05 80 02 80 06 80 00                              .......         
```

#### Opcodes

```
  0: 0x000B [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.790*, z=32.618*, y=0.500*, direction=274.9°*
  2: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      32  07 80 1F 00 08 80 09 80         2........
0020: 0A 80 1F 01 6F 1E 09 70  0E 01 00                 ....o..p...     
```

#### Opcodes

```
  0: 0x0017 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x001A [0x1F] MOVE_ENTITY: EventEntity moves to X=3.691*, Z=26.940*, Y=0.499*
  2: 0x0022 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0024 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0025 [0x1E] EventEntity looks at Ailbeche (ID: 17723401/0x010E7009) and starts talking
  5: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 07 80 1F 00             2....
0030: 0B 80 0C 80 0A 80 1F 01  6F 1E 09 70 0E 01 00     ........o..p... 
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x002E [0x1F] MOVE_ENTITY: EventEntity moves to X=5.789*, Z=28.237*, Y=0.499*
  2: 0x0036 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0038 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0039 [0x1E] EventEntity looks at Ailbeche (ID: 17723401/0x010E7009) and starts talking
  5: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               1F                 .
0040: 00 04 80 05 80 02 80 1F  01 22 01 00              ........."..    
```

#### Opcodes

```
  0: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=6.790*, Z=32.618*, Y=0.500*
  1: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0049 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      5B 0D 80 F8              [...
0050: FF FF 7F F8 FF FF 7F 74  68 6B 31 1C 0E 80 00     .......thk1.... 
```

#### Opcodes

```
  0: 0x004C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=85*
  1: 0x005B [0x1C] WAIT(30* ticks)
  2: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               5B                 [
0060: 0D 80 F8 FF FF 7F F8 FF  FF 7F 74 68 6B 32 1C 0E  ..........thk2..
0070: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x005F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=85*
  1: 0x006E [0x1C] WAIT(30* ticks)
  2: 0x0071 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0072   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:       5B 0D 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B    [..........tlk
0080: 30 1C 0E 80 00                                    0....           
```

#### Opcodes

```
  0: 0x0072 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0081 [0x1C] WAIT(30* ticks)
  2: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0085  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                5E 69 64  6C 30 1C 0E 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0085 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x008A [0x1C] WAIT(30* ticks)
  2: 0x008D [0x00] END_REQSTACK()
```
