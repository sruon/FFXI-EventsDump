# 17756217 - Augu-Maugu

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 224 bytes                |
| Total Events     | 10                       |
| References Count | 14                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [65535.3](#event-655353) | 0x0021       |     10 |              2 |
| [65535.4](#event-655354) | 0x002B       |     27 |              7 |
| [11](#event-11)          | 0x0046       |      1 |              1 |
| [65535.5](#event-655355) | 0x0047       |      1 |              1 |
| [260](#event-260)        | 0x0048       |     33 |             12 |
| [532](#event-532)        | 0x0069       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0xFFFF8AB9  |  4294937273 |
|       3 | 0x21D03     |      138499 |
|       4 | 0xFFFFC181  |  4294951297 |
|       5 | 0x06E0      |        1760 |
|       6 | 0xFFFF6AD0  |  4294929104 |
|       7 | 0x208A9     |      133289 |
|       8 | 0x000D      |          13 |
|       9 | 0xFFFEF390  |  4294898576 |
|      10 | 0x1C536     |      116022 |
|      11 | 0xFFFFD8F0  |  4294957296 |
|      12 | 0x1E0E      |        7694 |
|      13 | 0x1E0F      |        7695 |

## String References

- **7694**: Cross this bridge and follow the path to reach-a-weach the entrance of Windurst's residential area.
- **7695**: In the residential area's Mog Houses and Rent-a-Rooms, you can put-a-wut important belongings into safekeeping or just store-a-wore away items that are getting in your way. These can be very convenient facilities if you make good use-a-wuse of them.

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    37 02 80 03 80 04 80  05 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0021 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-30.023*, z=138.499*, y=-15.999*, direction=154.7°*
  1: 0x002A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002B   |
| Data Size    | 27 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                   32 00 80 5A 00             2..Z.
0030: 06 80 07 80 04 80 5A 01  32 08 80 5A 00 09 80 0A  ......Z.2..Z....
0040: 80 0B 80 5A 01 00                                 ...Z..          
```

#### Opcodes

```
  0: 0x002B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x002E [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-38.192*, Z=133.289*, Y=-15.999*
  2: 0x0036 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0038 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x003B [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-68.720*, Z=116.022*, Y=-10.000*
  5: 0x0043 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  6: 0x0045 [0x00] END_REQSTACK()
```

### Event 11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0046  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   00                                    .         
```

#### Opcodes

```
  0: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0047  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      00                                  .        
```

#### Opcodes

```
  0: 0x0047 [0x00] END_REQSTACK()
```

### Event 260

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1E F0 FF FF 7F 6F 70 29          .....op)
0050: 0B 39 F0 0E 01 01 1D 0C  80 23 1D 0D 80 23 29 0B  .9.......#...#).
0060: 39 F0 0E 01 02 20 00 21  00                       9.... .!.       
```

#### Opcodes

```
  0: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Augu-Maugu (ID: 17756217/0x010EF039), tag_num=0x01)
  4: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=7694*)
    → "Cross this bridge and follow the path to reach-a-weach the entrance of Windurst's residential area."
  5: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=7695*)
    → "In the residential area's Mog Houses and Rent-a-Rooms, you can put-a-wut important belongings into safekeeping or just store-a-wore away items that are getting in your way. These can be very convenient facilities if you make good use-a-wuse of them."
  7: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Augu-Maugu (ID: 17756217/0x010EF039), tag_num=0x02)
  9: 0x0065 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0067 [0x21] END_EVENT
 11: 0x0068 [0x00] END_REQSTACK()
```

### Event 532

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             92 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x0069 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x006F [0x00] END_REQSTACK()
```
