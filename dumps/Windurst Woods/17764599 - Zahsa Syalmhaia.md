# 17764599 - Zahsa Syalmhaia

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 68 bytes                 |
| Total Events     | 4                        |
| References Count | 3                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [797](#event-797)     | 0x0001       |     21 |             10 |
| [871](#event-871)     | 0x0016       |      1 |              1 |
| [872](#event-872)     | 0x0017       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x336D      |       13165 |
|       1 | 0x3371      |       13169 |
|       2 | 0x3372      |       13170 |

## String References

- **13165**: I am Zahsa Syalmhaia, captain of the mercenaries in charge of defending East Sarutabaruta.
- **13169**: And now, a question for you, adventurer--do you know of the stone maws being found across the land? Some might describe them as "cavernous."
- **13170**: Hmph! Then I shall enlighten you. They are large statues of hideous visage, and have been around for some time. These maws are more than they appear, I guarantee you.

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

### Event 797

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 1E F0 FF FF 7F  1D 00 80 23 1D 01 80 23    .........#...#
0010: 1D 02 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=13165*)
    → "I am Zahsa Syalmhaia, captain of the mercenaries in charge of defending East Sarutabaruta."
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=13169*)
    → "And now, a question for you, adventurer--do you know of the stone maws being found across the land? Some might describe them as "cavernous.""
  5: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=13170*)
    → "Hmph! Then I shall enlighten you. They are large statues of hideous visage, and have been around for some time. These maws are more than they appear, I guarantee you."
  7: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0014 [0x21] END_EVENT
  9: 0x0015 [0x00] END_REQSTACK()
```

### Event 871

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0016  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   00                                    .         
```

#### Opcodes

```
  0: 0x0016 [0x00] END_REQSTACK()
```

### Event 872

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0017  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      00                                  .        
```

#### Opcodes

```
  0: 0x0017 [0x00] END_REQSTACK()
```
