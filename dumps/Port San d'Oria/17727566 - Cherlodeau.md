# 17727566 - Cherlodeau

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 280 bytes                 |
| Total Events     | 4                         |
| References Count | 13                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4](#event-4)         | 0x0001       |      1 |              1 |
| [590](#event-590)     | 0x0002       |     91 |             24 |
| [748](#event-748)     | 0x005D       |    101 |             23 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1ED6      |        7894 |
|       2 | 0x1ED7      |        7895 |
|       3 | 0x1ED8      |        7896 |
|       4 | 0x003C      |          60 |
|       5 | 0x1ED9      |        7897 |
|       6 | 0x1EDA      |        7898 |
|       7 | 0x21F2      |        8690 |
|       8 | 0x21F9      |        8697 |
|       9 | 0x21FA      |        8698 |
|      10 | 0x21FB      |        8699 |
|      11 | 0x21FC      |        8700 |
|      12 | 0x21FD      |        8701 |

## String References

- **7894**: Hmph. A new recruit, are you? Let me give you some advice. There's Orcs outside our walls, more now than ever.
- **7895**: Best not to face them before you're ready. They're known to attack without warning... Nasty things!
- **7896**: Heh. Fighting is good, but discretion is the better part of valor! Run back to the gates if you need to.
- **8690**: <Player>'s badge flashes brightly.
- **8697**: Hmph, thinking of becoming a mercenary, are you? Let me give you some advice: The beastmen of the Near East are far more savage than the fiends of Ronfaure.
- **8698**: I would avoid those lands until I was sure of my strength. They care not who they kill--in that respect, they are much like the Orcs.
- **8699**: In war, survival is key. Picking your battles is also a valid strategy.

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

### Event 4

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

### Event 590

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 91 bytes |
| Instructions | 24       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 6F  70 5B 00 80 F8 FF FF 7F    .....op[......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 1C 00 80 1D  ....tlk0...#....
0020: 02 80 23 1C 00 80 1D 03  80 23 5E 69 64 6C 30 1C  ..#......#^idl0.
0030: 04 80 2B 4C 80 0E 01 05  80 23 27 66 F0 FF FF 7F  ..+L.....#'f....
0040: 14 2A 66 F0 FF FF 7F 2B  4D 80 0E 01 06 80 23 4A  .*f....+M.....#J
0050: F0 FF FF 7F 4E 80 0E 01  1C 00 80 21 00           ....N......!.   
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0009 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7894*)
    → "Hmph. A new recruit, are you? Let me give you some advice. There's Orcs outside our walls, more now than ever."
  5: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001C [0x1C] WAIT(30* ticks)
  7: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7895*)
    → "Best not to face them before you're ready. They're known to attack without warning... Nasty things!"
  8: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0023 [0x1C] WAIT(30* ticks)
 10: 0x0026 [0x1D] PRINT_EVENT_MESSAGE(message_id=7896*)
    → "Heh. Fighting is good, but discretion is the better part of valor! Run back to the gates if you need to."
 11: 0x0029 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x002A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x002F [0x1C] WAIT(60* ticks)
 14: 0x0032 [0x2B] Artinien (ID: 17727564/0x010E804C) [7897*]:
    → "That's called a strategic retreat, that is!"
 15: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x003A [0x27] REQ_SET(priority=0x66, entity_id=LocalPlayer, tag_num=0x14)
 17: 0x0041 [0x2A] GET_REQ_LEVEL(level=102, entity_id=LocalPlayer)
 18: 0x0047 [0x2B] Brifalien (ID: 17727565/0x010E804D) [7898*]:
    → "Yeah, a tradegic stretreat!"
 19: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x004F [0x4A] LocalPlayer looks at Cherlodeau (ID: 17727566/0x010E804E)
 21: 0x0058 [0x1C] WAIT(30* ticks)
 22: 0x005B [0x21] END_EVENT
 23: 0x005C [0x00] END_REQSTACK()
```

### Event 748

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x005D    |
| Data Size    | 101 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         42 48 07               BH.
0060: 80 1E F0 FF FF 7F 1C 00  80 1D 08 80 23 5B 00 80  ............#[..
0070: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 30 1D 09 80 23  ........tlk0...#
0080: 1D 0A 80 23 5B 00 80 F8  FF FF 7F F8 FF FF 7F 74  ...#[..........t
0090: 6C 6B 31 5E 69 64 6C 30  1C 04 80 2B 4C 80 0E 01  lk1^idl0...+L...
00A0: 0B 80 23 4A F0 FF FF 7F  4C 80 0E 01 2B 4D 80 0E  ..#J....L...+M..
00B0: 01 0C 80 23 4A F0 FF FF  7F 4E 80 0E 01 1C 00 80  ...#J....N......
00C0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x005D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x005E [0x48] [System] [8690*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0061 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0066 [0x1C] WAIT(30* ticks)
  4: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=8697*)
    → "Hmph, thinking of becoming a mercenary, are you? Let me give you some advice: The beastmen of the Near East are far more savage than the fiends of Ronfaure."
  5: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x006D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  7: 0x007C [0x1D] PRINT_EVENT_MESSAGE(message_id=8698*)
    → "I would avoid those lands until I was sure of my strength. They care not who they kill--in that respect, they are much like the Orcs."
  8: 0x007F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0080 [0x1D] PRINT_EVENT_MESSAGE(message_id=8699*)
    → "In war, survival is key. Picking your battles is also a valid strategy."
 10: 0x0083 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0084 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=30*
 12: 0x0093 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 13: 0x0098 [0x1C] WAIT(60* ticks)
 14: 0x009B [0x2B] Artinien (ID: 17727564/0x010E804C) [8700*]:
    → "That's called "Knowing your enemy," that is!"
 15: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00A3 [0x4A] LocalPlayer looks at Artinien (ID: 17727564/0x010E804C)
 17: 0x00AC [0x2B] Brifalien (ID: 17727565/0x010E804D) [8701*]:
    → "Yeah! "Knowing your anemone!""
 18: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x00B4 [0x4A] LocalPlayer looks at Cherlodeau (ID: 17727566/0x010E804E)
 20: 0x00BD [0x1C] WAIT(30* ticks)
 21: 0x00C0 [0x21] END_EVENT
 22: 0x00C1 [0x00] END_REQSTACK()
```
