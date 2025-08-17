# 17658629 - Monberaux

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 56 bytes                    |
| Total Events     | 2                           |
| References Count | 3                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [381](#event-381)     | 0x0001       |     19 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2086      |        8326 |
|       1 | 0x2087      |        8327 |
|       2 | 0x2088      |        8328 |

## String References

- **8326**: How curious. Other than a few scrapes, you seem to be a picture of perfect health.
- **8327**: A good number of the survivors have experienced significant trouble breathing since arriving here in Attohwa. For some of them, it seems even to have affected their minds...
- **8328**: Do take care of yourself, friend.

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

### Event 381

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 19 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8326*)
    → "How curious. Other than a few scrapes, you seem to be a picture of perfect health."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8327*)
    → "A good number of the survivors have experienced significant trouble breathing since arriving here in Attohwa. For some of them, it seems even to have affected their minds..."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=8328*)
    → "Do take care of yourself, friend."
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x21] END_EVENT
  8: 0x0013 [0x00] END_REQSTACK()
```
