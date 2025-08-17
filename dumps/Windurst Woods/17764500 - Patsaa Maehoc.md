# 17764500 - Patsaa Maehoc

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 128 bytes                |
| Total Events     | 5                        |
| References Count | 4                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [65535.3](#event-655353) | 0x001A       |      9 |              3 |
| [427](#event-427)        | 0x0023       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x2153      |        8531 |
|       3 | 0x2154      |        8532 |

## String References

- **8531**: It's purrr-etty darn hard to catch a dhalmel, you know? Only we Mithra have the necessary abilities to do it propurrrly!
- **8532**: To carry out that ability, you need something in purrrticular. To give you a hint, it's something that only Mithra have... Purrr...

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
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

### Event 427

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          86 00 F8 FF FF  7F 1E F0 FF FF 7F 6F 70     ...........op
0030: 29 08 94 10 0F 01 01 1D  02 80 23 1D 03 80 23 29  ).........#...#)
0040: 08 94 10 0F 01 02 20 00  21 00                    ...... .!.      
```

#### Opcodes

```
  0: 0x0023 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0029 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x002F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0030 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Patsaa Maehoc (ID: 17764500/0x010F1094), tag_num=0x01)
  5: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=8531*)
    → "It's purrr-etty darn hard to catch a dhalmel, you know? Only we Mithra have the necessary abilities to do it propurrrly!"
  6: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x003B [0x1D] PRINT_EVENT_MESSAGE(message_id=8532*)
    → "To carry out that ability, you need something in purrrticular. To give you a hint, it's something that only Mithra have... Purrr..."
  8: 0x003E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x003F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Patsaa Maehoc (ID: 17764500/0x010F1094), tag_num=0x02)
 10: 0x0046 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0048 [0x21] END_EVENT
 12: 0x0049 [0x00] END_REQSTACK()
```
