# 17752194 - Akee Yonji

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 180 bytes                 |
| Total Events     | 6                         |
| References Count | 5                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [594](#event-594)        | 0x0030       |     37 |             14 |
| [595](#event-595)        | 0x0055       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0165      |         357 |
|       1 | 0x001E      |          30 |
|       2 | 0x229A      |        8858 |
|       3 | 0x229B      |        8859 |
|       4 | 0x229C      |        8860 |

## String References

- **8858**: When I look at these flowerrrs, I feel like having a drrrink. But then again, I feel like having a drrrink all of the time.
- **8859**: If only I had some fluoro-flora juice. It's as bitterrr as uncooked gysahl greens, but the taste rrreminds me of home.
- **8860**: The orrriginal fluoro-flora seeds are from the Mithra homeland, you see...

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=357*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 594

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 37 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 82 E0 0E 01 01 1D 02  .....op)........
0040: 80 23 1D 03 80 23 1D 04  80 23 29 08 82 E0 0E 01  .#...#...#).....
0050: 03 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Akee Yonji (ID: 17752194/0x010EE082), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8858*)
    → "When I look at these flowerrrs, I feel like having a drrrink. But then again, I feel like having a drrrink all of the time."
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8859*)
    → "If only I had some fluoro-flora juice. It's as bitterrr as uncooked gysahl greens, but the taste rrreminds me of home."
  7: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=8860*)
    → "The orrriginal fluoro-flora seeds are from the Mithra homeland, you see..."
  9: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x004A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Akee Yonji (ID: 17752194/0x010EE082), tag_num=0x03)
 11: 0x0051 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x0053 [0x21] END_EVENT
 13: 0x0054 [0x00] END_REQSTACK()
```

### Event 595

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                1E F0 FF  FF 7F 6F 70 29 08 82 E0       .....op)...
0060: 0E 01 01 1D 03 80 23 1D  04 80 23 29 08 82 E0 0E  ......#...#)....
0070: 01 03 20 00 21 00                                 .. .!.          
```

#### Opcodes

```
  0: 0x0055 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Akee Yonji (ID: 17752194/0x010EE082), tag_num=0x01)
  4: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=8859*)
    → "If only I had some fluoro-flora juice. It's as bitterrr as uncooked gysahl greens, but the taste rrreminds me of home."
  5: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=8860*)
    → "The orrriginal fluoro-flora seeds are from the Mithra homeland, you see..."
  7: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x006B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Akee Yonji (ID: 17752194/0x010EE082), tag_num=0x03)
  9: 0x0072 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0074 [0x21] END_EVENT
 11: 0x0075 [0x00] END_REQSTACK()
```
