# 16883778 - Pradiulot

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 276 bytes                   |
| Total Events     | 14                          |
| References Count | 17                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [202](#event-202)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      8 |              2 |
| [65535.2](#event-655352) | 0x000A       |      7 |              2 |
| [204](#event-204)        | 0x0011       |      1 |              1 |
| [65535.3](#event-655353) | 0x0012       |     14 |              4 |
| [65535.4](#event-655354) | 0x0020       |     23 |              5 |
| [206](#event-206)        | 0x0037       |      1 |              1 |
| [65535.5](#event-655355) | 0x0038       |     14 |              4 |
| [65535.6](#event-655356) | 0x0046       |     10 |              2 |
| [192](#event-192)        | 0x0050       |     11 |              5 |
| [193](#event-193)        | 0x005B       |     11 |              5 |
| [371](#event-371)        | 0x0066       |     30 |              8 |
| [514](#event-514)        | 0x0084       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF54FE  |  4294923518 |
|       1 | 0xFFFF5A34  |  4294924852 |
|       2 | 0xFFFFA9B5  |  4294945205 |
|       3 | 0x000D      |          13 |
|       4 | 0xFFFFA490  |  4294943888 |
|       5 | 0x1379      |        4985 |
|       6 | 0xFFFFAA10  |  4294945296 |
|       7 | 0xFFFFAF35  |  4294946613 |
|       8 | 0x201E      |        8222 |
|       9 | 0xFFFFB301  |  4294947585 |
|      10 | 0x1C20      |        7200 |
|      11 | 0x08B7      |        2231 |
|      12 | 0x2A9A      |       10906 |
|      13 | 0x2A9B      |       10907 |
|      14 | 0x2B5B      |       11099 |
|      15 | 0x0014      |          20 |
|      16 | 0x2B5C      |       11100 |

## String References

- **10906**: All clear... Day in and day out, it is always "all clear"... However, I guess I cannot complain...
- **10907**: Lately there has been an increase in the number of outsiders utilizing our safehold's facilities. More ruffians means more crime...and that is what I am here to prevent.
- **11099**: The other day, those three Tarutaru presented me with the charred remains of some awful beast and told me to try it because it was "mighty tasty."
- **11100**: Since they were children, I had always told the Chebukki brothers to never shun from a challenge, but to think I would be tested by my own words...

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

### Event 202

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 8 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       36 00 80 01 80 02  80 00                      6.......      
```

#### Opcodes

```
  0: 0x0002 [0x36] SET_ENTITY_EVENT_POSITION(pos_x=-43.778*, pos_z=-42.444*, pos_y=-22.091*)
  1: 0x0009 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                4E 01 42 A0 01 01            N.B...
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000A [0x4E] SET_ENTITY_HIDE_FLAG: Hide Pradiulot (ID: 16883778/0x0101A042)
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 204

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    00                                              .              
```

#### Opcodes

```
  0: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 03 80 1F 00 04  80 05 80 06 80 1F 01 00    2.............
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=-23.408*, Z=4.985*, Y=-22.000*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 32 03 80 1F 00 07 80 08  80 06 80 1F 01 4A 42 A0  2............JB.
0030: 01 01 F0 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=-20.683*, Z=8.222*, Y=-22.000*
  2: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002D [0x4A] Pradiulot (ID: 16883778/0x0101A042) looks at LocalPlayer
  4: 0x0036 [0x00] END_REQSTACK()
```

### Event 206

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      00                                  .        
```

#### Opcodes

```
  0: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 03 80 1F 00 09 80 0A          2.......
0040: 80 06 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=-19.711*, Z=7.200*, Y=-22.000*
  2: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   37 07  80 08 80 06 80 0B 80 00        7.........
```

#### Opcodes

```
  0: 0x0046 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-20.683*, z=8.222*, y=-22.000*, direction=196.1°*
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 192

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 1E F0 FF FF 7F 1D 0C 80  23 21 00                 ........#!.     
```

#### Opcodes

```
  0: 0x0050 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=10906*)
    → "All clear... Day in and day out, it is always "all clear"... However, I guess I cannot complain..."
  2: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0059 [0x21] END_EVENT
  4: 0x005A [0x00] END_REQSTACK()
```

### Event 193

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   1E F0 FF FF 7F             .....
0060: 1D 0D 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x005B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0060 [0x1D] PRINT_EVENT_MESSAGE(message_id=10907*)
    → "Lately there has been an increase in the number of outsiders utilizing our safehold's facilities. More ruffians means more crime...and that is what I am here to prevent."
  2: 0x0063 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0064 [0x21] END_EVENT
  4: 0x0065 [0x00] END_REQSTACK()
```

### Event 371

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0066   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   1E F0  FF FF 7F 1D 0E 80 23 66        ........#f
0070: 0F 80 42 A0 01 01 42 A0  01 01 74 6C 6B 30 1D 10  ..B...B...tlk0..
0080: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0066 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=11099*)
    → "The other day, those three Tarutaru presented me with the charred remains of some awful beast and told me to try it because it was "mighty tasty.""
  2: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x006F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Pradiulot (ID: 16883778/0x0101A042), Pradiulot (ID: 16883778/0x0101A042)], work=20*
  4: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=11100*)
    → "Since they were children, I had always told the Chebukki brothers to never shun from a challenge, but to think I would be tested by my own words..."
  5: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0082 [0x21] END_EVENT
  7: 0x0083 [0x00] END_REQSTACK()
```

### Event 514

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0084  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             00                                        .           
```

#### Opcodes

```
  0: 0x0084 [0x00] END_REQSTACK()
```
