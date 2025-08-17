# 17469830 - Tome of Magic

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Toraimarai Canal (ID: 169) |
| Block Size       | 56 bytes                   |
| Total Events     | 2                          |
| References Count | 3                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [66](#event-66)       | 0x0001       |     16 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D25      |        7461 |
|       1 | 0x1D26      |        7462 |
|       2 | 0x1D27      |        7463 |

## String References

- **7461**: This book contains a history of the Horutoto Ruins.
- **7462**: "According to books on the towers, the mage who lost his life during the height of the tower battle was attempting to summon the great beast that lurked in the Full Moon Fountain..."
- **7463**: "With the destruction of the magical gizmos in the north tower, the great beast was freed to roam Sarutabaruta on nights of the full moon."

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

### Event 66

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
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7461*)
    → "This book contains a history of the Horutoto Ruins."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=7462*)
    → ""According to books on the towers, the mage who lost his life during the height of the tower battle was attempting to summon the great beast that lurked in the Full Moon Fountain...""
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7463*)
    → ""With the destruction of the magical gizmos in the north tower, the great beast was freed to roam Sarutabaruta on nights of the full moon.""
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  7: 0x000F [0x21] END_EVENT
  8: 0x0010 [0x00] END_REQSTACK()
```
