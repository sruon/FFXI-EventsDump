# 17764495 - Mheca Khetashipah

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 212 bytes                |
| Total Events     | 7                        |
| References Count | 8                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |      9 |              3 |
| [426](#event-426)        | 0x0023       |     33 |             12 |
| [79](#event-79)          | 0x0044       |     33 |             12 |
| [83](#event-83)          | 0x0065       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x2151      |        8529 |
|       3 | 0x2152      |        8530 |
|       4 | 0x1DAE      |        7598 |
|       5 | 0x1DAF      |        7599 |
|       6 | 0x1DB5      |        7605 |
|       7 | 0x1DB6      |        7606 |

## String References

- **7598**: Humph... Looks like that Nanaa Mihgo, better known as the Cat Burglar, is at her home forrr once.
- **7599**: An adventurer such as yourself ought to be careful, lest you get burrrned.
- **7605**: What's that? You're contemplating taking something to Nanaa Mihgo?
- **7606**: I recommend you forrrget that! She'll take you in, all right, but not the way you expect! Haven't you heard that she's involved with some nasty foreign mob? Be carrreful!
- **8529**: I don't think we've achieved any rrreal peace by making a pact with those Yagudo beastmen!
- **8530**: But try explaining that to the Tarutaru, and they'll just be all stubborrrn and insist that it's the Star Sibyl's will!

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                5E 69 64 6C 30 1C            ^idl0.
0020: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x001A [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x001F [0x1C] WAIT(30* ticks)
  2: 0x0022 [0x00] END_REQSTACK()
```

### Event 426

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  6F 70 29 08 8F 10 0F 01     .....op).....
0030: 01 1D 02 80 23 1D 03 80  23 29 08 8F 10 0F 01 02  ....#...#)......
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mheca Khetashipah (ID: 17764495/0x010F108F), tag_num=0x01)
  4: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=8529*)
    → "I don't think we've achieved any rrreal peace by making a pact with those Yagudo beastmen!"
  5: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8530*)
    → "But try explaining that to the Tarutaru, and they'll just be all stubborrrn and insist that it's the Star Sibyl's will!"
  7: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0039 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mheca Khetashipah (ID: 17764495/0x010F108F), tag_num=0x02)
  9: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0042 [0x21] END_EVENT
 11: 0x0043 [0x00] END_REQSTACK()
```

### Event 79

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             1E F0 FF FF  7F 6F 70 29 08 8F 10 0F      .....op)....
0050: 01 01 1D 04 80 23 1D 05  80 23 29 08 8F 10 0F 01  .....#...#).....
0060: 02 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0044 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x004A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x004B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mheca Khetashipah (ID: 17764495/0x010F108F), tag_num=0x01)
  4: 0x0052 [0x1D] PRINT_EVENT_MESSAGE(message_id=7598*)
    → "Humph... Looks like that Nanaa Mihgo, better known as the Cat Burglar, is at her home forrr once."
  5: 0x0055 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=7599*)
    → "An adventurer such as yourself ought to be careful, lest you get burrrned."
  7: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mheca Khetashipah (ID: 17764495/0x010F108F), tag_num=0x02)
  9: 0x0061 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0063 [0x21] END_EVENT
 11: 0x0064 [0x00] END_REQSTACK()
```

### Event 83

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                1E F0 FF  FF 7F 6F 70 29 08 8F 10       .....op)...
0070: 0F 01 01 1D 06 80 23 1D  07 80 23 29 08 8F 10 0F  ......#...#)....
0080: 01 02 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0065 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x006A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x006B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x006C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mheca Khetashipah (ID: 17764495/0x010F108F), tag_num=0x01)
  4: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=7605*)
    → "What's that? You're contemplating taking something to Nanaa Mihgo?"
  5: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0077 [0x1D] PRINT_EVENT_MESSAGE(message_id=7606*)
    → "I recommend you forrrget that! She'll take you in, all right, but not the way you expect! Haven't you heard that she's involved with some nasty foreign mob? Be carrreful!"
  7: 0x007A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x007B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Mheca Khetashipah (ID: 17764495/0x010F108F), tag_num=0x02)
  9: 0x0082 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0084 [0x21] END_EVENT
 11: 0x0085 [0x00] END_REQSTACK()
```
