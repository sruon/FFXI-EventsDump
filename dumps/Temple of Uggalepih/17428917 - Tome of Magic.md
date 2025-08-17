# 17428917 - Tome of Magic

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Temple of Uggalepih (ID: 159) |
| Block Size       | 64 bytes                      |
| Total Events     | 2                             |
| References Count | 4                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [22](#event-22)       | 0x0001       |     20 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CE9      |        7401 |
|       1 | 0x1CEA      |        7402 |
|       2 | 0x1CEB      |        7403 |
|       3 | 0x1CEC      |        7404 |

## String References

- **7401**: A tome written on the subject of Fei'Yin.
- **7402**: "I would like to bring attention to the many small chambers that exist in the subterranean levels of the ruins of Fei'Yin."
- **7403**: "In each of these chambers stands an automaton. A golem, or giant, if you will. Were these golems given the task of sentry, or simply employed as servants?"
- **7404**: "It is possible to conclude from the artifacts discovered in these ruins that it was once the abode of an ancient people. One can further deduce from the evidence that this civilization was wiped out by some sudden calamity."

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

### Event 22

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 20 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 1D 02 80 23 1D 03 80   ...#...#...#...
0010: 23 20 00 21 00                                    # .!.           
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7401*)
    → "A tome written on the subject of Fei'Yin."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=7402*)
    → ""I would like to bring attention to the many small chambers that exist in the subterranean levels of the ruins of Fei'Yin.""
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=7403*)
    → ""In each of these chambers stands an automaton. A golem, or giant, if you will. Were these golems given the task of sentry, or simply employed as servants?""
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=7404*)
    → ""It is possible to conclude from the artifacts discovered in these ruins that it was once the abode of an ancient people. One can further deduce from the evidence that this civilization was wiped out by some sudden calamity.""
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0013 [0x21] END_EVENT
 10: 0x0014 [0x00] END_REQSTACK()
```
