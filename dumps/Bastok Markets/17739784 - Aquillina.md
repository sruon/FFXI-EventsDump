# 17739784 - Aquillina

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 200 bytes                |
| Total Events     | 5                        |
| References Count | 11                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [116](#event-116)     | 0x0001       |     15 |              7 |
| [217](#event-217)     | 0x0010       |     20 |              8 |
| [218](#event-218)     | 0x0024       |     16 |              6 |
| [219](#event-219)     | 0x0034       |     67 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D63      |        7523 |
|       1 | 0x1D64      |        7524 |
|       2 | 0x0300      |         768 |
|       3 | 0x1D65      |        7525 |
|       4 | 0x1D66      |        7526 |
|       5 | 0x1D68      |        7528 |
|       6 | 0x0005      |           5 |
|       7 | 0x0046      |          70 |
|       8 | 0x1D67      |        7527 |
|       9 | 0x00C9      |         201 |
|      10 | 0x0000      |           0 |

## String References

- **7523**: My husband's always off adventuring, my son is out playing all day, and my stepfather keeps rambling about the strangest things...
- **7524**: Augh! I miss being single...
- **7525**: Oh, no! We're out of $7 again. I wonder why...
- **7526**: I can't cook without fire, but I don't have time to go shopping! Say, can you spare any $7? If you have four of them, I'll buy them off you.
- **7527**: Great! Thank you! Here's your money. Now, stand back! It's cooking time!
- **7528**: I'm sorry, I don't need any more $7 for now.

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

### Event 116

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7523*)
    → "My husband's always off adventuring, my son is out playing all day, and my stepfather keeps rambling about the strangest things..."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7524*)
    → "Augh! I miss being single..."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 217

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 20 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 03 09 10 02 80 1D 03 80  23 1E F0 FF FF 7F 1D 04  ........#.......
0020: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0010 [0x03] Work_Zone[9] = 768*
  1: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7525*)
    → "Oh, no! We're out of $7 again. I wonder why..."
  2: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7526*)
    → "I can't cook without fire, but I don't have time to go shopping! Say, can you spare any $7? If you have four of them, I'll buy them off you."
  5: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0022 [0x21] END_EVENT
  7: 0x0023 [0x00] END_REQSTACK()
```

### Event 218

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             03 09 10 02  80 1E F0 FF FF 7F 1D 05      ............
0030: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0024 [0x03] Work_Zone[9] = 768*
  1: 0x0029 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7528*)
    → "I'm sorry, I don't need any more $7 for now."
  3: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0032 [0x21] END_EVENT
  5: 0x0033 [0x00] END_REQSTACK()
```

### Event 219

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 67 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             20 01 42 03  09 10 02 80 1E F0 FF FF       .B.........
0040: 7F 1C 06 80 5B 07 80 F8  FF FF 7F F8 FF FF 7F 70  ....[..........p
0050: 61 73 30 1D 08 80 23 53  F8 FF FF 7F F8 FF FF 7F  as0...#S........
0060: 70 61 73 30 45 09 80 F0  FF FF 7F F0 FF FF 7F 71  pas0E..........q
0070: 73 74 63 0A 80 21 00                              stc..!.         
```

#### Opcodes

```
  0: 0x0034 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0036 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0037 [0x03] Work_Zone[9] = 768*
  3: 0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0041 [0x1C] WAIT(5* ticks)
  5: 0x0044 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=70*
  6: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7527*)
    → "Great! Thank you! Here's your money. Now, stand back! It's cooking time!"
  7: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0057 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  9: 0x0064 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 10: 0x0075 [0x21] END_EVENT
 11: 0x0076 [0x00] END_REQSTACK()
```
