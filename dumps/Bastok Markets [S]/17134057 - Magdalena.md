# 17134057 - Magdalena

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 76 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [158](#event-158)     | 0x0001       |     33 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0013      |          19 |
|       2 | 0x3017      |       12311 |
|       3 | 0x3018      |       12312 |

## String References

- **12311**: I'll admit, I wasn't sure how things would turn out when Selbina suddenly declared its independence.
- **12312**: Senator Werner dispatched the Republican Legion and took control of the situation with such incredible speed. Even the president himself was amazed by the senator's show of skill.

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

### Event 158

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
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=19*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=12311*)
    → "I'll admit, I wasn't sure how things would turn out when Selbina suddenly declared its independence."
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=12312*)
    → "Senator Werner dispatched the Republican Legion and took control of the situation with such incredible speed. Even the president himself was amazed by the senator's show of skill."
  6: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0020 [0x21] END_EVENT
  8: 0x0021 [0x00] END_REQSTACK()
```
