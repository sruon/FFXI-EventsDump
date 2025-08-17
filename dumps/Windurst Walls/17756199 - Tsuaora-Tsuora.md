# 17756199 - Tsuaora-Tsuora

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 284 bytes                |
| Total Events     | 8                        |
| References Count | 21                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [42](#event-42)          | 0x001A       |     29 |             10 |
| [11](#event-11)          | 0x0037       |      1 |              1 |
| [65535.3](#event-655353) | 0x0038       |     10 |              2 |
| [65535.4](#event-655354) | 0x0042       |     55 |             13 |
| [50](#event-50)          | 0x0079       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1C2C      |        7212 |
|       3 | 0x14C04     |       84996 |
|       4 | 0xFFFE556A  |  4294858090 |
|       5 | 0xFFFFF63C  |  4294964796 |
|       6 | 0x0BFC      |        3068 |
|       7 | 0x000D      |          13 |
|       8 | 0x14B58     |       84824 |
|       9 | 0xFFFE6D65  |  4294864229 |
|      10 | 0x14611     |       83473 |
|      11 | 0xFFFE7E58  |  4294868568 |
|      12 | 0x13795     |       79765 |
|      13 | 0xFFFE9419  |  4294874137 |
|      14 | 0x10266     |       66150 |
|      15 | 0xFFFED1FE  |  4294889982 |
|      16 | 0xFFFFF666  |  4294964838 |
|      17 | 0xFAAA      |       64170 |
|      18 | 0xFFFEFBE5  |  4294900709 |
|      19 | 0xFFFFF63D  |  4294964797 |
|      20 | 0x1C3D      |        7229 |

## String References

- **7212**: We are the local courier-wouriers. We deliver the goods that people leave with the girly-wirlies over therey-wherey.
- **7229**: The last time something like this happened, it was the Savanna Rarabs that made off with most of our maily-waily. Seems they think they can make a comfy-womfy nest out of our letters.

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

### Event 42

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                1E F0 FF FF 7F 6F            .....o
0020: 70 29 0B 27 F0 0E 01 01  1D 02 80 23 29 0B 27 F0  p).'.......#).'.
0030: 0E 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tsuaora-Tsuora (ID: 17756199/0x010EF027), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7212*)
    → "We are the local courier-wouriers. We deliver the goods that people leave with the girly-wirlies over therey-wherey."
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tsuaora-Tsuora (ID: 17756199/0x010EF027), tag_num=0x02)
  7: 0x0033 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0035 [0x21] END_EVENT
  9: 0x0036 [0x00] END_REQSTACK()
```

### Event 11

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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          37 03 80 04 80 05 80 06          7.......
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0038 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=84.996*, z=-109.206*, y=-2.500*, direction=269.6°*
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 55 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 07 80 1F 00 08  80 09 80 05 80 1F 01 1F    2.............
0050: 00 0A 80 0B 80 05 80 1F  01 1F 00 0C 80 0D 80 05  ................
0060: 80 1F 01 1F 00 0E 80 0F  80 10 80 1F 01 1F 00 11  ................
0070: 80 12 80 13 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=84.824*, Z=-103.067*, Y=-2.500*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x1F] MOVE_ENTITY: EventEntity moves to X=83.473*, Z=-98.728*, Y=-2.500*
  4: 0x0057 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=79.765*, Z=-93.159*, Y=-2.500*
  6: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=66.150*, Z=-77.314*, Y=-2.458*
  8: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=64.170*, Z=-66.587*, Y=-2.499*
 10: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x0077 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x0078 [0x00] END_REQSTACK()
```

### Event 50

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             1E F0 FF FF 7F 6F 70           .....op
0080: 29 0B 27 F0 0E 01 01 1D  14 80 23 29 0B 27 F0 0E  ).'.......#).'..
0090: 01 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0079 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x007E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x007F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0080 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tsuaora-Tsuora (ID: 17756199/0x010EF027), tag_num=0x01)
  4: 0x0087 [0x1D] PRINT_EVENT_MESSAGE(message_id=7229*)
    → "The last time something like this happened, it was the Savanna Rarabs that made off with most of our maily-waily. Seems they think they can make a comfy-womfy nest out of our letters."
  5: 0x008A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Tsuaora-Tsuora (ID: 17756199/0x010EF027), tag_num=0x02)
  7: 0x0092 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0094 [0x21] END_EVENT
  9: 0x0095 [0x00] END_REQSTACK()
```
