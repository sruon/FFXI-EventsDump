# 17756198 - Orudoba-Sondeba

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 296 bytes                |
| Total Events     | 9                        |
| References Count | 19                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [43](#event-43)          | 0x001A       |     29 |             10 |
| [11](#event-11)          | 0x0037       |      1 |              1 |
| [65535.3](#event-655353) | 0x0038       |     10 |              2 |
| [65535.4](#event-655354) | 0x0042       |     45 |             11 |
| [65535.5](#event-655355) | 0x006F       |     25 |              8 |
| [51](#event-51)          | 0x0088       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1C2D      |        7213 |
|       3 | 0x14180     |       82304 |
|       4 | 0xFFFE60FC  |  4294861052 |
|       5 | 0xFFFFF63D  |  4294964797 |
|       6 | 0x0C28      |        3112 |
|       7 | 0x000D      |          13 |
|       8 | 0x13D41     |       81217 |
|       9 | 0xFFFE7EF8  |  4294868728 |
|      10 | 0x1331C     |       78620 |
|      11 | 0xFFFE95D7  |  4294874583 |
|      12 | 0xF87A      |       63610 |
|      13 | 0xFFFED664  |  4294891108 |
|      14 | 0xFFFFF68F  |  4294964879 |
|      15 | 0xE13A      |       57658 |
|      16 | 0xFFFEE1F7  |  4294894071 |
|      17 | 0xFFFFF68E  |  4294964878 |
|      18 | 0x1C3E      |        7230 |

## String References

- **7213**: If you wantaru participate in the auction, then step rightaru up to the counters lining the wall over there.
- **7230**: Look outaru for those Savanna Dhalmels. They just love to eataru our mail!

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

### Event 43

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
0020: 70 29 0B 26 F0 0E 01 01  1D 02 80 23 29 0B 26 F0  p).&.......#).&.
0030: 0E 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0020 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0021 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Orudoba-Sondeba (ID: 17756198/0x010EF026), tag_num=0x01)
  4: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7213*)
    → "If you wantaru participate in the auction, then step rightaru up to the counters lining the wall over there."
  5: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x002C [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Orudoba-Sondeba (ID: 17756198/0x010EF026), tag_num=0x02)
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
  0: 0x0038 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=82.304*, z=-106.244*, y=-2.499*, direction=273.5°*
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       32 07 80 1F 00 08  80 09 80 05 80 1F 01 1F    2.............
0050: 00 0A 80 0B 80 05 80 1F  01 1F 00 0C 80 0D 80 0E  ................
0060: 80 1F 01 1F 00 0F 80 10  80 11 80 1F 01 6F 00     .............o. 
```

#### Opcodes

```
  0: 0x0042 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=81.217*, Z=-98.568*, Y=-2.499*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x1F] MOVE_ENTITY: EventEntity moves to X=78.620*, Z=-92.713*, Y=-2.499*
  4: 0x0057 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=63.610*, Z=-76.188*, Y=-2.417*
  6: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=57.658*, Z=-73.225*, Y=-2.418*
  8: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x006D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 10: 0x006E [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006F   |
| Data Size    | 25 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                               1E                 .
0070: F0 FF FF 7F 6F 70 29 0B  26 F0 0E 01 01 29 0B 26  ....op).&....).&
0080: F0 0E 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x006F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0075 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0076 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Orudoba-Sondeba (ID: 17756198/0x010EF026), tag_num=0x01)
  4: 0x007D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Orudoba-Sondeba (ID: 17756198/0x010EF026), tag_num=0x02)
  5: 0x0084 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  6: 0x0086 [0x21] END_EVENT
  7: 0x0087 [0x00] END_REQSTACK()
```

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          1E F0 FF FF 7F 6F 70 29          .....op)
0090: 0B 26 F0 0E 01 01 1D 12  80 23 29 0B 26 F0 0E 01  .&.......#).&...
00A0: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0088 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x008E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x008F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Orudoba-Sondeba (ID: 17756198/0x010EF026), tag_num=0x01)
  4: 0x0096 [0x1D] PRINT_EVENT_MESSAGE(message_id=7230*)
    → "Look outaru for those Savanna Dhalmels. They just love to eataru our mail!"
  5: 0x0099 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x009A [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Orudoba-Sondeba (ID: 17756198/0x010EF026), tag_num=0x02)
  7: 0x00A1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00A3 [0x21] END_EVENT
  9: 0x00A4 [0x00] END_REQSTACK()
```
