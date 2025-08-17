# 17756247 - Horuni-Mawoni

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 176 bytes                |
| Total Events     | 6                        |
| References Count | 11                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |     16 |              3 |
| [65535.3](#event-655353) | 0x002A       |     14 |              4 |
| [303](#event-303)        | 0x0038       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFEDCC0  |  4294892736 |
|       3 | 0x1AF56     |      110422 |
|       4 | 0xFFFFD8F0  |  4294957296 |
|       5 | 0x0EC8      |        3784 |
|       6 | 0xFFFEFF64  |  4294901604 |
|       7 | 0x1C3C6     |      115654 |
|       8 | 0xFFFFD801  |  4294957057 |
|       9 | 0x1EE2      |        7906 |
|      10 | 0x1EE3      |        7907 |

## String References

- **7906**: The Star Sibyl permitted the Yagudo beastmen to live in Sarutabaruta. Thataru's why there is a Yagudo nest called Giddeus out in West Sarutabaruta.
- **7907**: But the Yagudo don'taru seem the least bit thankful. Annoying, isn'taru it?

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 37 02 80 03 80 04 80 05  80 00                    7.........      
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-74.560*, z=110.422*, y=-10.000*, direction=332.6°*
  2: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                32 00 80 5A 00 06            2..Z..
0030: 80 07 80 08 80 5A 01 00                           .....Z..        
```

#### Opcodes

```
  0: 0x002A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002D [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-65.692*, Z=115.654*, Y=-10.239*
  2: 0x0035 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0037 [0x00] END_REQSTACK()
```

### Event 303

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          1E F0 FF FF 7F 6F 70 29          .....op)
0040: 0B 57 F0 0E 01 01 1D 09  80 23 1D 0A 80 23 29 0B  .W.......#...#).
0050: 57 F0 0E 01 02 20 00 21  00                       W.... .!.       
```

#### Opcodes

```
  0: 0x0038 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Horuni-Mawoni (ID: 17756247/0x010EF057), tag_num=0x01)
  4: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=7906*)
    → "The Star Sibyl permitted the Yagudo beastmen to live in Sarutabaruta. Thataru's why there is a Yagudo nest called Giddeus out in West Sarutabaruta."
  5: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=7907*)
    → "But the Yagudo don'taru seem the least bit thankful. Annoying, isn'taru it?"
  7: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Horuni-Mawoni (ID: 17756247/0x010EF057), tag_num=0x02)
  9: 0x0055 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0057 [0x21] END_EVENT
 11: 0x0058 [0x00] END_REQSTACK()
```
