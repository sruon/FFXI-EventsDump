# 17764497 - Chihpi Kapirapehro

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 120 bytes                |
| Total Events     | 5                        |
| References Count | 4                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |      9 |              3 |
| [429](#event-429)        | 0x0023       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x2157      |        8535 |
|       3 | 0x2158      |        8536 |

## String References

- **8535**: You know about that mad hatter in the Tarutaru district of Windurst Waters, rrright?
- **8536**: Well, those Tarutaru have nothing on us Mithra in Windurst Woods! Why, we have our own mad apothecary herrre!

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

### Event 429

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  6F 70 29 08 91 10 0F 01     .....op).....
0030: 01 1D 02 80 23 1D 03 80  23 29 08 91 10 0F 01 02  ....#...#)......
0040: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0029 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chihpi Kapirapehro (ID: 17764497/0x010F1091), tag_num=0x01)
  4: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=8535*)
    → "You know about that mad hatter in the Tarutaru district of Windurst Waters, rrright?"
  5: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=8536*)
    → "Well, those Tarutaru have nothing on us Mithra in Windurst Woods! Why, we have our own mad apothecary herrre!"
  7: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0039 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chihpi Kapirapehro (ID: 17764497/0x010F1091), tag_num=0x02)
  9: 0x0040 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0042 [0x21] END_EVENT
 11: 0x0043 [0x00] END_REQSTACK()
```
