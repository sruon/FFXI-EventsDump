# 17768540 - Talking Doll

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 108 bytes               |
| Total Events     | 7                       |
| References Count | 7                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [271](#event-271)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |      5 |              3 |
| [65535.2](#event-655352) | 0x0007       |      9 |              5 |
| [65535.3](#event-655353) | 0x0010       |      9 |              5 |
| [65535.4](#event-655354) | 0x0019       |      5 |              3 |
| [65535.5](#event-655355) | 0x001E       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F29      |        7977 |
|       1 | 0x1F2E      |        7982 |
|       2 | 0x1F2F      |        7983 |
|       3 | 0x1F33      |        7987 |
|       4 | 0x1F34      |        7988 |
|       5 | 0x1F36      |        7990 |
|       6 | 0x1F39      |        7993 |

## String References

- **7977**: Nowhere to go! Ha! You are trapped! Ha! Wasn't very smart to enter such small room!
- **7982**: That's right! Ha! Destroy me, destroy yourselves! Ha!
- **7983**: I'm special! Ha! Thanks to me, you made it here! Thanks to me! Ha!
- **7987**: Too late! Ha! Demons approaching from west! Quiet or loud, you're dead! Ha!
- **7988**: Don't try hiding! You're doomed anyway! Ha! Only I will be safe! Ha!
- **7990**: What are you doing!? You can't do this to me!
- **7993**: Witch! You evil witch! Curse you and all of Windurst!

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

### Event 271

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1D 00 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x0002 [0x1D] PRINT_EVENT_MESSAGE(message_id=7977*)
    → "Nowhere to go! Ha! You are trapped! Ha! Wasn't very smart to enter such small room!"
  1: 0x0005 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      1D  01 80 23 1D 02 80 23 00         ...#...#.
```

#### Opcodes

```
  0: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=7982*)
    → "That's right! Ha! Destroy me, destroy yourselves! Ha!"
  1: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x000B [0x1D] PRINT_EVENT_MESSAGE(message_id=7983*)
    → "I'm special! Ha! Thanks to me, you made it here! Thanks to me! Ha!"
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1D 03 80 23 1D 04 80 23  00                       ...#...#.       
```

#### Opcodes

```
  0: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=7987*)
    → "Too late! Ha! Demons approaching from west! Quiet or loud, you're dead! Ha!"
  1: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0014 [0x1D] PRINT_EVENT_MESSAGE(message_id=7988*)
    → "Don't try hiding! You're doomed anyway! Ha! Only I will be safe! Ha!"
  3: 0x0017 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0019  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1D 05 80 23 00                 ...#.  
```

#### Opcodes

```
  0: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=7990*)
    → "What are you doing!? You can't do this to me!"
  1: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            1D 06                ..
0020: 80 23 00                                          .#.             
```

#### Opcodes

```
  0: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7993*)
    → "Witch! You evil witch! Curse you and all of Windurst!"
  1: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0022 [0x00] END_REQSTACK()
```
