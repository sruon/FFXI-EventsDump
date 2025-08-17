# 16994361 - Chuchuroon

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Nashmau (ID: 53) |
| Block Size       | 144 bytes        |
| Total Events     | 4                |
| References Count | 10               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [266](#event-266)        | 0x0001       |     58 |             14 |
| [281](#event-281)        | 0x003B       |      1 |              1 |
| [65535.1](#event-655351) | 0x003C       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2944      |       10564 |
|       1 | 0x2945      |       10565 |
|       2 | 0x034A      |         842 |
|       3 | 0x001E      |          30 |
|       4 | 0x2946      |       10566 |
|       5 | 0x003C      |          60 |
|       6 | 0xFFFFE579  |  4294960505 |
|       7 | 0xFFFF592D  |  4294924589 |
|       8 | 0x0000      |           0 |
|       9 | 0x0466      |        1126 |

## String References

- **10564**: Chuchuroon now traaaining muscle.
- **10565**: Chuchuroon strooong, no? Chuchuroon faaast, no? Chuchuroon like mercenary, no?
- **10566**: ... Okay, you think that enough exercise to become mercenary, no?

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

### Event 266

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 58 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 5B 02   ........#...#[.
0010: 80 F8 FF FF 7F F8 FF FF  7F 74 68 6B 30 1C 03 80  .........thk0...
0020: 1D 04 80 1C 03 80 23 5B  02 80 F8 FF FF 7F F8 FF  ......#[........
0030: FF 7F 74 68 6B 31 1C 05  80 21 00                 ..thk1...!.     
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=10564*)
    → "Chuchuroon now traaaining muscle."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=10565*)
    → "Chuchuroon strooong, no? Chuchuroon faaast, no? Chuchuroon like mercenary, no?"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk0" with entities [EventEntity, EventEntity], work=842*
  6: 0x001D [0x1C] WAIT(30* ticks)
  7: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=10566*)
    → "... Okay, you think that enough exercise to become mercenary, no?"
  8: 0x0023 [0x1C] WAIT(30* ticks)
  9: 0x0026 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=842*
 11: 0x0036 [0x1C] WAIT(60* ticks)
 12: 0x0039 [0x21] END_EVENT
 13: 0x003A [0x00] END_REQSTACK()
```

### Event 281

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   00                         .    
```

#### Opcodes

```
  0: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      37 06 80 07              7...
0040: 80 08 80 09 80 00                                 ......          
```

#### Opcodes

```
  0: 0x003C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-6.791*, z=-42.707*, y=0.000*, direction=99.0°*
  1: 0x0045 [0x00] END_REQSTACK()
```
