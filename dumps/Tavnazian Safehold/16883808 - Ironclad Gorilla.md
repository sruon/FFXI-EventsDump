# 16883808 - Ironclad Gorilla

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 108 bytes                   |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [305](#event-305)     | 0x0001       |     30 |              8 |
| [306](#event-306)     | 0x001F       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B1B      |       11035 |
|       1 | 0x0045      |          69 |
|       2 | 0x2B1C      |       11036 |
|       3 | 0x2B1D      |       11037 |

## String References

- **11035**: This cave leads to the Sealion's Den.
- **11036**: The cave was once used as a private port for the Tavnazian Cathedral, but now...
- **11037**: Recently, with all the supply ships from Jeuno coming and going, the port has been very active.

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

### Event 305

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 66 01 80 F8 FF FF   ........#f.....
0010: 7F F8 FF FF 7F 74 77 62  30 1D 02 80 23 21 00     .....twb0...#!. 
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11035*)
    → "This cave leads to the Sealion's Den."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [EventEntity, EventEntity], work=69*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=11036*)
    → "The cave was once used as a private port for the Tavnazian Cathedral, but now..."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x21] END_EVENT
  7: 0x001E [0x00] END_REQSTACK()
```

### Event 306

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: F0 FF FF 7F 1D 00 80 23  66 01 80 F8 FF FF 7F F8  .......#f.......
0030: FF FF 7F 74 77 62 30 1D  03 80 23 21 00           ...twb0...#!.   
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=11035*)
    → "This cave leads to the Sealion's Den."
  2: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0028 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "twb0" with entities [EventEntity, EventEntity], work=69*
  4: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=11037*)
    → "Recently, with all the supply ships from Jeuno coming and going, the port has been very active."
  5: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x003B [0x21] END_EVENT
  7: 0x003C [0x00] END_REQSTACK()
```
