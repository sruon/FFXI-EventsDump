# 17428915 - Tome of Magic

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 56 bytes                      |
| Total Events     | 2                             |
| References Count | 3                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [20](#event-20)       | 0x0001       |     16 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CE2      |        7394 |
|       1 | 0x1CE3      |        7395 |
|       2 | 0x1CE4      |        7396 |

## String References

- **7394**: A workbook written by Iru-Kuiru.
- **7395**: "That place was most definitely cursed. It was as if each of us were having our strings pulled by some unseen force..."
- **7396**: "The Goddess only knows what that power was. I knew fear like I had never known before, and was struck mindless with panic before the terror that lurked within those walls."

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

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 1D 02 80 23 20 00 21   ...#...#...# .!
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7394*)
    → "A workbook written by Iru-Kuiru."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=7395*)
    → ""That place was most definitely cursed. It was as if each of us were having our strings pulled by some unseen force...""
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7396*)
    → ""The Goddess only knows what that power was. I knew fear like I had never known before, and was struck mindless with panic before the terror that lurked within those walls.""
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x000F [0x21] END_EVENT
  8: 0x0010 [0x00] END_REQSTACK()
```
