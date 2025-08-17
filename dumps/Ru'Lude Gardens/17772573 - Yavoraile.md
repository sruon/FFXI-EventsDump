# 17772573 - Yavoraile

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 236 bytes                 |
| Total Events     | 7                         |
| References Count | 13                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10094](#event-10094)    | 0x0001       |     10 |              2 |
| [118](#event-118)        | 0x000B       |     56 |             10 |
| [10092](#event-10092)    | 0x0043       |     52 |             12 |
| [10097](#event-10097)    | 0x0077       |      7 |              2 |
| [10235](#event-10235)    | 0x007E       |      1 |              1 |
| [65535.1](#event-655351) | 0x007F       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x855F      |       34143 |
|       1 | 0xEA56      |       59990 |
|       2 | 0x07CB      |        1995 |
|       3 | 0x0BEC      |        3052 |
|       4 | 0x000A      |          10 |
|       5 | 0x2803      |       10243 |
|       6 | 0x3610      |       13840 |
|       7 | 0x001E      |          30 |
|       8 | 0x3617      |       13847 |
|       9 | 0x3618      |       13848 |
|      10 | 0x8D91      |       36241 |
|      11 | 0x117AB     |       71595 |
|      12 | 0x04F2      |        1266 |

## String References

- **10243**: The archduke hosts so many dignitaries, every night is a banquet. Composing original menus makes me fret!
- **13840**: <Player>'s badge flashes brightly.
- **13847**: Near Eastern cuisine is all the rage now. Lately I've been studying up on it to add some spice to the palace banquets.
- **13848**: Near Eastern cooking is considered one of the leading cuisines in Vana'diel, so I am sure the archduke will be most pleased.

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

### Event 10094

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=34.143*, z=59.990*, y=1.995*, direction=268.2°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 56 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1E F0 FF FF 7F             .....
0010: 6F 70 5B 04 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  op[..........tlk
0020: 30 1D 05 80 23 5B 04 80  F8 FF FF 7F F8 FF FF 7F  0...#[..........
0030: 74 6C 6B 31 53 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  tlk1S........tlk
0040: 31 21 00                                          1!.             
```

#### Opcodes

```
  0: 0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0012 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  4: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=10243*)
    → "The archduke hosts so many dignitaries, every night is a banquet. Composing original menus makes me fret!"
  5: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0025 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=10*
  7: 0x0034 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  8: 0x0041 [0x21] END_EVENT
  9: 0x0042 [0x00] END_REQSTACK()
```

### Event 10092

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          42 48 06 80 1E  F0 FF FF 7F 1C 07 80 5B     BH..........[
0050: 04 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 08  ..........tlk0..
0060: 80 23 1D 09 80 23 5B 04  80 F8 FF FF 7F F8 FF FF  .#...#[.........
0070: 7F 74 6C 6B 31 21 00                              .tlk1!.         
```

#### Opcodes

```
  0: 0x0043 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0044 [0x48] [System] [13840*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0047 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x004C [0x1C] WAIT(30* ticks)
  4: 0x004F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  5: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=13847*)
    → "Near Eastern cuisine is all the rage now. Lately I've been studying up on it to add some spice to the palace banquets."
  6: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0062 [0x1D] PRINT_EVENT_MESSAGE(message_id=13848*)
    → "Near Eastern cooking is considered one of the leading cuisines in Vana'diel, so I am sure the archduke will be most pleased."
  8: 0x0065 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0066 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=10*
 10: 0x0075 [0x21] END_EVENT
 11: 0x0076 [0x00] END_REQSTACK()
```

### Event 10097

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0077  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0077 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x007D [0x00] END_REQSTACK()
```

### Event 10235

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            00                   . 
```

#### Opcodes

```
  0: 0x007E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               37                 7
0080: 0A 80 0B 80 02 80 0C 80  00                       .........       
```

#### Opcodes

```
  0: 0x007F [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=36.241*, z=71.595*, y=1.995*, direction=111.3°*
  1: 0x0088 [0x00] END_REQSTACK()
```
