# 17720034 - Repairer Moogle

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 124 bytes                     |
| Total Events     | 4                             |
| References Count | 7                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3620](#event-3620)   | 0x0001       |     24 |             10 |
| [3621](#event-3621)   | 0x0019       |     21 |              9 |
| [3622](#event-3622)   | 0x002E       |     16 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x51A3      |       20899 |
|       1 | 0x4176      |       16758 |
|       2 | 0x4177      |       16759 |
|       3 | 0x4178      |       16760 |
|       4 | 0x4179      |       16761 |
|       5 | 0x417A      |       16762 |
|       6 | 0x417B      |       16763 |

## String References

- **16758**: Good day, adventurer! I am able to repair any broken item data related to $0.
- **16759**: If you are unable to deliver $0, it's possible that the item data has been corrupted.
- **16760**: Please trade your $0 to me so that I may fix it.
- **16761**: I have confirmed that the item data for your $0 has been corrupted. We apologize for the inconvenience.
- **16762**: I have restored it to its intended functionality. Here you are!
- **16763**: It appears that your item is working as intended.

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

### Event 3620

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 24 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 03 02  10 00 80 1D 01 80 23 1D   .............#.
0010: 02 80 23 1D 03 80 23 21  00                       ..#...#!.       
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x03] Work_Zone[2] = 20899*
  2: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=16758*)
    → "Good day, adventurer! I am able to repair any broken item data related to $0."
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x1D] PRINT_EVENT_MESSAGE(message_id=16759*)
    → "If you are unable to deliver $0, it's possible that the item data has been corrupted."
  5: 0x0012 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0013 [0x1D] PRINT_EVENT_MESSAGE(message_id=16760*)
    → "Please trade your $0 to me so that I may fix it."
  7: 0x0016 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0017 [0x21] END_EVENT
  9: 0x0018 [0x00] END_REQSTACK()
```

### Event 3621

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 21 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             42 1E F0 FF FF 7F 03           B......
0020: 02 10 00 80 1D 04 80 23  1D 05 80 23 21 00        .......#...#!.  
```

#### Opcodes

```
  0: 0x0019 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x001A [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001F [0x03] Work_Zone[2] = 20899*
  3: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=16761*)
    → "I have confirmed that the item data for your $0 has been corrupted. We apologize for the inconvenience."
  4: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=16762*)
    → "I have restored it to its intended functionality. Here you are!"
  6: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x002C [0x21] END_EVENT
  8: 0x002D [0x00] END_REQSTACK()
```

### Event 3622

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002E   |
| Data Size    | 16 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            1E F0                ..
0030: FF FF 7F 03 02 10 00 80  1D 06 80 23 21 00        ...........#!.  
```

#### Opcodes

```
  0: 0x002E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0033 [0x03] Work_Zone[2] = 20899*
  2: 0x0038 [0x1D] PRINT_EVENT_MESSAGE(message_id=16763*)
    → "It appears that your item is working as intended."
  3: 0x003B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x003C [0x21] END_EVENT
  5: 0x003D [0x00] END_REQSTACK()
```
