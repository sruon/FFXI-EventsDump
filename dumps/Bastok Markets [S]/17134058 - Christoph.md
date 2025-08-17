# 17134058 - Christoph

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 148 bytes                   |
| Total Events     | 6                           |
| References Count | 6                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [157](#event-157)        | 0x0001       |     33 |              9 |
| [172](#event-172)        | 0x0022       |     33 |              9 |
| [63](#event-63)          | 0x0043       |      1 |              1 |
| [65535.1](#event-655351) | 0x0044       |     13 |              3 |
| [608](#event-608)        | 0x0051       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0009      |           9 |
|       2 | 0x302C      |       12332 |
|       3 | 0x302D      |       12333 |
|       4 | 0x302E      |       12334 |
|       5 | 0x002B      |          43 |

## String References

- **12332**: Senator Werner is adamant about having a technologically advanced military. He even goes so far as to visit the Metalworks from time to time.
- **12333**: It seems Chief Engineer Cid is extremely busy after taking up the additional post as head of the Gunpowder Room.
- **12334**: Senator Werner was always adamant about having a technologically advanced military. He even used to go so far as to visit the Metalworks from time to time.

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

### Event 157

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 F8 FF FF 7F   ........f......
0010: F8 FF FF 7F 74 6C 6B 30  1D 02 80 23 1D 03 80 23  ....tlk0...#...#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12332*)
    → "Senator Werner is adamant about having a technologically advanced military. He even goes so far as to visit the Metalworks from time to time."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12333*)
    → "It seems Chief Engineer Cid is extremely busy after taking up the additional post as head of the Gunpowder Room."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```

### Event 172

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       1E F0 FF FF 7F 1C  00 80 66 01 80 F8 FF FF    ........f.....
0030: 7F F8 FF FF 7F 74 6C 6B  30 1D 04 80 23 1D 03 80  .....tlk0...#...
0040: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0022 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0027 [0x1C] WAIT(30* ticks)
  2: 0x002A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=9*
  3: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=12334*)
    → "Senator Werner was always adamant about having a technologically advanced military. He even used to go so far as to visit the Metalworks from time to time."
  4: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=12333*)
    → "It seems Chief Engineer Cid is extremely busy after taking up the additional post as head of the Gunpowder Room."
  6: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0041 [0x21] END_EVENT
  8: 0x0042 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          00                                          .            
```

#### Opcodes

```
  0: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             6E F8 FF FF  7F 05 80 99 F8 FF FF 7F      n...........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0044 [0x6E] EventEntity uses emote 43*
  1: 0x004B [0x99] Wait for EventEntity animation to complete
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 608

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0051  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    00                                              .              
```

#### Opcodes

```
  0: 0x0051 [0x00] END_REQSTACK()
```
