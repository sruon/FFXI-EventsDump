# 16994362 - Tsotsoroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 360 bytes        |
| Total Events     | 14               |
| References Count | 31               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [267](#event-267)        | 0x0001       |     55 |             13 |
| [291](#event-291)        | 0x0038       |      1 |              1 |
| [65535.1](#event-655351) | 0x0039       |     10 |              2 |
| [65535.2](#event-655352) | 0x0043       |     11 |              3 |
| [65535.3](#event-655353) | 0x004E       |     10 |              2 |
| [65535.4](#event-655354) | 0x0058       |     10 |              2 |
| [65535.5](#event-655355) | 0x0062       |     14 |              4 |
| [65535.6](#event-655356) | 0x0070       |     14 |              4 |
| [65535.7](#event-655357) | 0x007E       |     10 |              2 |
| [65535.8](#event-655358) | 0x0088       |     10 |              2 |
| [65535.9](#event-655359) | 0x0092       |     15 |              3 |
| [303](#event-303)        | 0x00A1       |      1 |              1 |
| [312](#event-312)        | 0x00A2       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x034B      |         843 |
|       2 | 0x2947      |       10567 |
|       3 | 0x2948      |       10568 |
|       4 | 0x2949      |       10569 |
|       5 | 0x3648      |       13896 |
|       6 | 0xFFFF6AC2  |  4294929090 |
|       7 | 0x0000      |           0 |
|       8 | 0x0445      |        1093 |
|       9 | 0x35B6      |       13750 |
|      10 | 0xFFFF6136  |  4294926646 |
|      11 | 0x36BA      |       14010 |
|      12 | 0xFFFF7476  |  4294931574 |
|      13 | 0x03AF      |         943 |
|      14 | 0x2A72      |       10866 |
|      15 | 0xFFFF6081  |  4294926465 |
|      16 | 0x0372      |         882 |
|      17 | 0x000D      |          13 |
|      18 | 0x2E3B      |       11835 |
|      19 | 0xFFFF59CF  |  4294924751 |
|      20 | 0x2BDB      |       11227 |
|      21 | 0xFFFF5D79  |  4294925689 |
|      22 | 0x1290      |        4752 |
|      23 | 0xFFFF88F8  |  4294936824 |
|      24 | 0x0360      |         864 |
|      25 | 0xFFFFF3B8  |  4294964152 |
|      26 | 0xFFFF7CCB  |  4294933707 |
|      27 | 0x0E29      |        3625 |
|      28 | 0x3E62      |       15970 |
|      29 | 0xFFFF53F3  |  4294923251 |
|      30 | 0x0B72      |        2930 |

## String References

- **10567**: Spaaarkle! Shiiiny! Spoooaaarkle! Too bright! Aaah! Tsotsoroon's eyes! Gold, gold! Shiiiny! Oooh!
- **10568**: Tsotsoroon saw, Tsotsoroon saaaw! At Talacca Cooove! Mooountains of gold! Spaaarkly gold! Shiiiny gold! Tsotsoroon never sleep again!
- **10569**: Spaaarkle! Spoooaaarkle! Ahahahaaa!

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

### Event 267

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 55 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 5B 01 80 F8 FF FF 7F   ........[......
0010: F8 FF FF 7F 68 61 70 30  1D 02 80 23 1D 03 80 23  ....hap0...#...#
0020: 5B 01 80 F8 FF FF 7F F8  FF FF 7F 68 61 70 30 1C  [..........hap0.
0030: 00 80 1D 04 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [EventEntity, EventEntity], work=843*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=10567*)
    → "Spaaarkle! Shiiiny! Spoooaaarkle! Too bright! Aaah! Tsotsoroon's eyes! Gold, gold! Shiiiny! Oooh!"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=10568*)
    → "Tsotsoroon saw, Tsotsoroon saaaw! At Talacca Cooove! Mooountains of gold! Spaaarkly gold! Shiiiny gold! Tsotsoroon never sleep again!"
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hap0" with entities [EventEntity, EventEntity], work=843*
  8: 0x002F [0x1C] WAIT(30* ticks)
  9: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=10569*)
    → "Spaaarkle! Spoooaaarkle! Ahahahaaa!"
 10: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0036 [0x21] END_EVENT
 12: 0x0037 [0x00] END_REQSTACK()
```

### Event 291

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0038  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          00                               .       
```

#### Opcodes

```
  0: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             37 05 80 06 80 07 80           7......
0040: 08 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0039 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=13.896*, z=-38.206*, y=0.000*, direction=96.1°*
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          1F 00 09 80 0A  80 07 80 1F 01 00           ...........  
```

#### Opcodes

```
  0: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=13.750*, Z=-40.650*, Y=0.000*
  1: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x004D [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            37 0B                7.
0050: 80 0C 80 07 80 0D 80 00                           ........        
```

#### Opcodes

```
  0: 0x004E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.010*, z=-35.722*, y=0.000*, direction=82.9°*
  1: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          37 0E 80 0F 80 07 80 10          7.......
0060: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0058 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=10.866*, z=-40.831*, y=0.000*, direction=77.5°*
  1: 0x0061 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0062   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:       32 11 80 1F 00 12  80 13 80 07 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0062 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0065 [0x1F] MOVE_ENTITY: EventEntity moves to X=11.835*, Z=-42.545*, Y=0.000*
  2: 0x006D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0070   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070: 1F 00 14 80 15 80 07 80  1F 01 39 10 80 00        ..........9...  
```

#### Opcodes

```
  0: 0x0070 [0x1F] MOVE_ENTITY: EventEntity moves to X=11.227*, Z=-41.607*, Y=0.000*
  1: 0x0078 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x007A [0x39] SET_ENTITY_DIRECTION(direction=4.8°*)
  3: 0x007D [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            37 16                7.
0080: 80 17 80 07 80 18 80 00                           ........        
```

#### Opcodes

```
  0: 0x007E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=4.752*, z=-30.472*, y=0.000*, direction=75.9°*
  1: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          37 19 80 1A 80 07 80 1B          7.......
0090: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0088 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-3.144*, z=-33.589*, y=0.000*, direction=318.6°*
  1: 0x0091 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0092   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:       37 1C 80 1D 80 07  80 1E 80 1E 6F 50 03 01    7.........oP..
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0092 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=15.970*, z=-44.045*, y=0.000*, direction=257.5°*
  1: 0x009B [0x1E] EventEntity looks at Elisabeth (ID: 16994415/0x0103506F) and starts talking
  2: 0x00A0 [0x00] END_REQSTACK()
```

### Event 303

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    00                                              .              
```

#### Opcodes

```
  0: 0x00A1 [0x00] END_REQSTACK()
```

### Event 312

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       00                                            .             
```

#### Opcodes

```
  0: 0x00A2 [0x00] END_REQSTACK()
```
