# 16883812 - Korbi-Marobi

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 132 bytes                   |
| Total Events     | 3                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [324](#event-324)     | 0x0001       |     49 |             11 |
| [325](#event-325)     | 0x0032       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B2E      |       11054 |
|       1 | 0x0028      |          40 |
|       2 | 0x2B2F      |       11055 |
|       3 | 0x2B30      |       11056 |
|       4 | 0x2B31      |       11057 |
|       5 | 0x2B32      |       11058 |

## String References

- **11054**: The Tavnazian and San d'Orian Cathedrals both have roots in the same faith that originated centuries ago in the Elvaan kingdom.
- **11055**: However, under the guidance of Cardinal Mildaurion C Giloumet, the Tavnazian Cathedral eventually branched from the original teachings of the San d'Orian church and began to evolve separately.
- **11056**: Unfortunately, the Great War put an end to any further development of the Marquisate's culture...
- **11057**: Now that Jeuno has reinstated ties with Tavnazia, it's only a matter of time before talks with the San d'Orian Cathedral are held.
- **11058**: But I wonder if San d'Oria will really offer to help us...

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

### Event 324

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 49 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 66 01 80 F8 FF FF   ........#f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 1D 02 80 23 66 01 80  .....tlk0...#f..
0020: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 1D 03 80 23  ........tlk1...#
0030: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11054*)
    → "The Tavnazian and San d'Orian Cathedrals both have roots in the same faith that originated centuries ago in the Elvaan kingdom."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=11055*)
    → "However, under the guidance of Cardinal Mildaurion C Giloumet, the Tavnazian Cathedral eventually branched from the original teachings of the San d'Orian church and began to evolve separately."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  7: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=11056*)
    → "Unfortunately, the Great War put an end to any further development of the Marquisate's culture..."
  8: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0030 [0x21] END_EVENT
 10: 0x0031 [0x00] END_REQSTACK()
```

### Event 325

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0032   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:       1E F0 FF FF 7F 1D  04 80 23 66 01 80 F8 FF    ........#f....
0040: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 05 80 23 21 00  ......tlk0...#!.
```

#### Opcodes

```
  0: 0x0032 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=11057*)
    → "Now that Jeuno has reinstated ties with Tavnazia, it's only a matter of time before talks with the San d'Orian Cathedral are held."
  2: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x003B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x004A [0x1D] PRINT_EVENT_MESSAGE(message_id=11058*)
    → "But I wonder if San d'Oria will really offer to help us..."
  5: 0x004D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x004E [0x21] END_EVENT
  7: 0x004F [0x00] END_REQSTACK()
```
