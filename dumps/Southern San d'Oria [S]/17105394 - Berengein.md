# 17105394 - Berengein

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 84 bytes                         |
| Total Events     | 2                                |
| References Count | 3                                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [601](#event-601)     | 0x0001       |     45 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2F44      |       12100 |
|       2 | 0x2F45      |       12101 |

## String References

- **12100**: Hey you, whaddaya say to a little friendly wager? The Allied Forces of Altana or the Beastman Confederate? Where's your money?
- **12101**: Haha, I'm sorry, I'm sorry. Never mind me.

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

### Event 601

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 45 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 66 00  80 F2 01 05 01 F2 01 05   .....f.........
0010: 01 74 6C 6B 30 1D 01 80  23 1D 02 80 23 66 00 80  .tlk0...#...#f..
0020: F2 01 05 01 F2 01 05 01  74 6C 6B 31 21 00        ........tlk1!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Berengein (ID: 17105394/0x010501F2), Berengein (ID: 17105394/0x010501F2)], work=20*
  2: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=12100*)
    → "Hey you, whaddaya say to a little friendly wager? The Allied Forces of Altana or the Beastman Confederate? Where's your money?"
  3: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=12101*)
    → "Haha, I'm sorry, I'm sorry. Never mind me."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Berengein (ID: 17105394/0x010501F2), Berengein (ID: 17105394/0x010501F2)], work=20*
  7: 0x002C [0x21] END_EVENT
  8: 0x002D [0x00] END_REQSTACK()
```
