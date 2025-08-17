# 16794013 - Rhalo Davigoh

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Bibiki Bay (ID: 4) |
| Block Size       | 392 bytes          |
| Total Events     | 14                 |
| References Count | 7                  |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |      9 |              3 |
| [65535.3](#event-655353)   | 0x001A       |     16 |              2 |
| [65535.4](#event-655354)   | 0x002A       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0038       |     16 |              2 |
| [65535.6](#event-655356)   | 0x0048       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0056       |      9 |              3 |
| [65535.8](#event-655358)   | 0x005F       |     28 |              4 |
| [65535.9](#event-655359)   | 0x007B       |     26 |              4 |
| [65535.10](#event-6553510) | 0x0095       |     22 |              3 |
| [65535.11](#event-6553511) | 0x00AB       |     20 |              3 |
| [38](#event-38)            | 0x00BF       |     51 |             16 |
| [39](#event-39)            | 0x00F2       |     47 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0x1D59      |        7513 |
|       3 | 0x1D5A      |        7514 |
|       4 | 0x1D5B      |        7515 |
|       5 | 0x1D5C      |        7516 |
|       6 | 0x1D5D      |        7517 |

## String References

- **7513**: Earn a fortune working on a lazy trrropical island.t
- **7514**: ...Or at least that's what the brrrochure said.
- **7515**: All I do is lug heavy boxes around all day, and get ignored by tourrrists.
- **7516**: Goldmane? I've never heard that name, but there's a blonde Elvaan who's always hanging arrround the boat on the west side of the island.
- **7517**: You know, a Hume girl and her moogle friend just asked me the same question. Must be some new tourrrist attrrraction...

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=358*
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

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                5B 00 80 F8 FF FF            [.....
0020: 7F F8 FF FF 7F 74 68 6B  31 00                    .....thk1.      
```

#### Opcodes

```
  0: 0x001A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=358*
  1: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                53 F8 FF FF 7F F8            S.....
0030: FF FF 7F 74 68 6B 31 00                           ...thk1.        
```

#### Opcodes

```
  0: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          5B 00 80 F8 FF FF 7F F8          [.......
0040: FF FF 7F 74 68 6B 32 00                           ...thk2.        
```

#### Opcodes

```
  0: 0x0038 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=358*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          53 F8 FF FF 7F F8 FF FF          S.......
0050: 7F 74 68 6B 32 00                                 .thk2.          
```

#### Opcodes

```
  0: 0x0048 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   5E 69  64 6C 30 1C 01 80 00           ^idl0.... 
```

#### Opcodes

```
  0: 0x0056 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x005B [0x1C] WAIT(30* ticks)
  2: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               7C                 |
0060: 00 F8 FF FF 7F 81 00 F8  FF FF 7F 5B 00 80 F8 FF  ...........[....
0070: FF 7F F8 FF FF 7F 61 6E  67 30 00                 ......ang0.     
```

#### Opcodes

```
  0: 0x005F [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0065 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x006B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=358*
  3: 0x007A [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   53 F8 FF FF 7F             S....
0080: F8 FF FF 7F 61 6E 67 30  7C 01 F8 FF FF 7F 81 01  ....ang0|.......
0090: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x007B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x0088 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x008E [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                81 00 F8  FF FF 7F 5B 00 80 F8 FF       ......[....
00A0: FF 7F F8 FF FF 7F 73 69  73 30 00                 ......sis0.     
```

#### Opcodes

```
  0: 0x0095 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x009B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sis0" with entities [EventEntity, EventEntity], work=358*
  2: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   53 F8 FF FF 7F             S....
00B0: F8 FF FF 7F 73 69 73 30  81 01 F8 FF FF 7F 00     ....sis0....... 
```

#### Opcodes

```
  0: 0x00AB [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sis0" with entities [EventEntity, EventEntity]
  1: 0x00B8 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x00BE [0x00] END_REQSTACK()
```

### Event 38

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 51 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               1E                 .
00C0: F0 FF FF 7F 6F 70 29 08  9D 41 00 01 01 1D 02 80  ....op)..A......
00D0: 23 1D 03 80 23 29 08 9D  41 00 01 02 29 08 9D 41  #...#)..A...)..A
00E0: 00 01 08 1D 04 80 23 29  08 9D 41 00 01 09 20 00  ......#)..A... .
00F0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x00BF [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x01)
  4: 0x00CD [0x1D] PRINT_EVENT_MESSAGE(message_id=7513*)
    → "Earn a fortune working on a lazy trrropical island.t"
  5: 0x00D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00D1 [0x1D] PRINT_EVENT_MESSAGE(message_id=7514*)
    → "...Or at least that's what the brrrochure said."
  7: 0x00D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00D5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x02)
  9: 0x00DC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x08)
 10: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7515*)
    → "All I do is lug heavy boxes around all day, and get ignored by tourrrists."
 11: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00E7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x09)
 13: 0x00EE [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 14: 0x00F0 [0x21] END_EVENT
 15: 0x00F1 [0x00] END_REQSTACK()
```

### Event 39

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       1E F0 FF FF 7F 6F  70 29 08 9D 41 00 01 03    .....op)..A...
0100: 1D 05 80 23 1D 06 80 23  29 08 9D 41 00 01 04 29  ...#...#)..A...)
0110: 08 9D 41 00 01 05 29 08  9D 41 00 01 06 20 00 21  ..A...)..A... .!
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x00F2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00F8 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00F9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x03)
  4: 0x0100 [0x1D] PRINT_EVENT_MESSAGE(message_id=7516*)
    → "Goldmane? I've never heard that name, but there's a blonde Elvaan who's always hanging arrround the boat on the west side of the island."
  5: 0x0103 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0104 [0x1D] PRINT_EVENT_MESSAGE(message_id=7517*)
    → "You know, a Hume girl and her moogle friend just asked me the same question. Must be some new tourrrist attrrraction..."
  7: 0x0107 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0108 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x04)
  9: 0x010F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x05)
 10: 0x0116 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rhalo Davigoh (ID: 16794013/0x0100419D), tag_num=0x06)
 11: 0x011D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x011F [0x21] END_EVENT
 13: 0x0120 [0x00] END_REQSTACK()
```
