# 17748027 - Unlucky Rat

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 192 bytes            |
| Total Events     | 5                    |
| References Count | 9                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [550](#event-550)     | 0x0001       |     11 |              5 |
| [556](#event-556)     | 0x000C       |     30 |              8 |
| [557](#event-557)     | 0x002A       |     66 |             13 |
| [559](#event-559)     | 0x006C       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1ED8      |        7896 |
|       1 | 0x1ED5      |        7893 |
|       2 | 0x0037      |          55 |
|       3 | 0x1ED6      |        7894 |
|       4 | 0x027D      |         637 |
|       5 | 0x1ED7      |        7895 |
|       6 | 0x00C9      |         201 |
|       7 | 0x0000      |           0 |
|       8 | 0x1FC5      |        8133 |

## String References

- **7893**: Hmm...this machine's been acting up lately. I wonder if the oil's gone bad...
- **7894**: This machine needs oiling, but we're all out of machine oil. What could I use as a substitute, I wonder?
- **7895**: $7? Of course! Why didn't I think of that? Thank you. Here, take this as payment.
- **7896**: My job's not that bad, really. Working with machines beats working in the mines any day.
- **8133**: I've heard an adventurer say that there were these oily monsters in Beadeaux sometimes. I wonder...

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

### Event 550

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7896*)
    → "My job's not that bad, really. Working with machines beats working in the mines any day."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 556

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 5B 02 80  F8 FF FF 7F F8 FF FF 7F  ....#[..........
0020: 74 6C 6B 30 1D 03 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7893*)
    → "Hmm...this machine's been acting up lately. I wonder if the oil's gone bad..."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  4: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7894*)
    → "This machine needs oiling, but we're all out of machine oil. What could I use as a substitute, I wonder?"
  5: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0028 [0x21] END_EVENT
  7: 0x0029 [0x00] END_REQSTACK()
```

### Event 557

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 66 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                03 09 10 04 80 42            .....B
0030: 20 01 1E F0 FF FF 7F 6F  70 5B 02 80 F8 FF FF 7F   ......op[......
0040: F8 FF FF 7F 70 61 73 30  1D 05 80 23 45 06 80 F8  ....pas0...#E...
0050: FF FF 7F F8 FF FF 7F 71  73 74 63 07 80 53 F8 FF  .......qstc..S..
0060: FF 7F F8 FF FF 7F 70 61  73 30 21 00              ......pas0!.    
```

#### Opcodes

```
  0: 0x002A [0x03] Work_Zone[9] = 637*
  1: 0x002F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0030 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x0032 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0038 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0039 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=55*
  7: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=7895*)
    → "$7? Of course! Why didn't I think of that? Thank you. Here, take this as payment."
  8: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 10: 0x005D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 11: 0x006A [0x21] END_EVENT
 12: 0x006B [0x00] END_REQSTACK()
```

### Event 559

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      1E F0 FF FF              ....
0070: 7F 1D 08 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x006C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=8133*)
    → "I've heard an adventurer say that there were these oily monsters in Beadeaux sometimes. I wonder..."
  2: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0075 [0x21] END_EVENT
  4: 0x0076 [0x00] END_REQSTACK()
```
