# 17748007 - Hungry Wolf

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 216 bytes            |
| Total Events     | 7                    |
| References Count | 11                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [421](#event-421)     | 0x0001       |      6 |              4 |
| [428](#event-428)     | 0x0007       |     48 |             14 |
| [429](#event-429)     | 0x0037       |     67 |             12 |
| [905](#event-905)     | 0x007A       |      1 |              1 |
| [917](#event-917)     | 0x007B       |      1 |              1 |
| [924](#event-924)     | 0x007C       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D59      |        7513 |
|       1 | 0x112B      |        4395 |
|       2 | 0x1D5A      |        7514 |
|       3 | 0x0037      |          55 |
|       4 | 0x1D5B      |        7515 |
|       5 | 0x1D5C      |        7516 |
|       6 | 0x1D5D      |        7517 |
|       7 | 0x000A      |          10 |
|       8 | 0x1D5E      |        7518 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0000      |           0 |

## String References

- **7513**: I'm hungry...no, I mean, I'm starved.
- **7514**: The food here isn't bad, but a little more variety wouldn't hurt, you know what I mean?
- **7515**: My friend, Offa, has been telling me that $7 are exquisite! I wish I could have some, someday.
- **7516**: He told me that there was an easy but dangerous way of making them, but--hey, speaking of Offa, he hasn't been coming to work lately...
- **7517**: Hmm, he's probably loafing around in his house in the Markets District again.
- **7518**: Hey! Is that $7? Let me have it! Here, I'll give you this!

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

### Event 421

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 6 bytes |
| Instructions | 4       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 21 00                               ...#!.         
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7513*)
    → "I'm hungry...no, I mean, I'm starved."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x21] END_EVENT
  3: 0x0006 [0x00] END_REQSTACK()
```

### Event 428

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0007   |
| Data Size    | 48 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      03  09 10 01 80 1E F0 FF FF         .........
0010: 7F 1D 02 80 23 5B 03 80  F8 FF FF 7F F8 FF FF 7F  ....#[..........
0020: 74 6C 6B 30 1D 04 80 23  1D 05 80 23 5E 69 64 6C  tlk0...#...#^idl
0030: 30 1D 06 80 23 21 00                              0...#!.         
```

#### Opcodes

```
  0: 0x0007 [0x03] Work_Zone[9] = 4395*
  1: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7514*)
    → "The food here isn't bad, but a little more variety wouldn't hurt, you know what I mean?"
  3: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0015 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=55*
  5: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7515*)
    → "My friend, Offa, has been telling me that $7 are exquisite! I wish I could have some, someday."
  6: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7516*)
    → "He told me that there was an easy but dangerous way of making them, but--hey, speaking of Offa, he hasn't been coming to work lately..."
  8: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x002C [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7517*)
    → "Hmm, he's probably loafing around in his house in the Markets District again."
 11: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0035 [0x21] END_EVENT
 13: 0x0036 [0x00] END_REQSTACK()
```

### Event 429

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 67 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      03  09 10 01 80 42 20 01 1E         .....B ..
0040: F0 FF FF 7F 1C 07 80 5B  03 80 F8 FF FF 7F F8 FF  .......[........
0050: FF 7F 70 61 73 30 1D 08  80 23 53 F8 FF FF 7F F8  ..pas0...#S.....
0060: FF FF 7F 70 61 73 30 45  09 80 F0 FF FF 7F F0 FF  ...pas0E........
0070: FF 7F 71 73 74 63 0A 80  21 00                    ..qstc..!.      
```

#### Opcodes

```
  0: 0x0037 [0x03] Work_Zone[9] = 4395*
  1: 0x003C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x003D [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  3: 0x003F [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0044 [0x1C] WAIT(10* ticks)
  5: 0x0047 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=55*
  6: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=7518*)
    → "Hey! Is that $7? Let me have it! Here, I'll give you this!"
  7: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x005A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  9: 0x0067 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0078 [0x21] END_EVENT
 11: 0x0079 [0x00] END_REQSTACK()
```

### Event 905

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                00                           .     
```

#### Opcodes

```
  0: 0x007A [0x00] END_REQSTACK()
```

### Event 917

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   00                         .    
```

#### Opcodes

```
  0: 0x007B [0x00] END_REQSTACK()
```

### Event 924

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      00                       .   
```

#### Opcodes

```
  0: 0x007C [0x00] END_REQSTACK()
```
