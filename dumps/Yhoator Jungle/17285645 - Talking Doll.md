# 17285645 - Talking Doll

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Yhoator Jungle (ID: 124) |
| Block Size       | 136 bytes                |
| Total Events     | 2                        |
| References Count | 8                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4](#event-4)         | 0x0001       |     76 |             22 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1DFD      |        7677 |
|       2 | 0x0064      |         100 |
|       3 | 0x1E00      |        7680 |
|       4 | 0x1DFF      |        7679 |
|       5 | 0x1DFE      |        7678 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0000      |           0 |

## String References

- **7677**: The $0 jumps in your hands.
- **7678**: Ahahahahaha! I can sense the power of the ring! Get yourself moving [north/northeast/east/southeast/south/southwest/west/northwest]!
- **7679**: Ahahahahaha! Don't slow down now, slacker! The readings are coming from the [north/northeast/east/southeast/south/southwest/west/northwest]!
- **7680**: Ahahahahaha! You're getting close now! I can feel the ring's power from the next area!

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

### Event 4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 76 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1C 00 80 43 00 43  01 1C 00 80 48 01 80 23   B...C.C....H..#
0010: 02 09 10 00 80 00 2E 00  02 08 10 02 80 00 27 00  ..............'.
0020: 1D 03 80 23 01 2B 00 1D  04 80 23 01 32 00 1D 05  ...#.+....#.2...
0030: 80 23 4E 00 F0 FF FF 7F  45 06 80 F8 FF FF 7F F8  .#N.....E.......
0040: FF FF 7F 66 64 69 31 07  80 20 00 21 00           ...fdi1.. .!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1C] WAIT(1* ticks)
  2: 0x0005 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0007 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0009 [0x1C] WAIT(1* ticks)
  5: 0x000C [0x48] [System] [7677*]:
    → "The $0 jumps in your hands."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x002E
  8: 0x0018 [0x02] IF !(Work_Zone[8] == 100*) GOTO 0x0027
  9: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7680*)
    → "Ahahahahaha! You're getting close now! I can feel the ring's power from the next area!"
 10: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0024 [0x01] GOTO 0x002B
 12: 0x0027 [0x1D] PRINT_EVENT_MESSAGE(message_id=7679*)
    → "Ahahahahaha! Don't slow down now, slacker! The readings are coming from the [north/northeast/east/southeast/south/southwest/west/northwest]!"
 13: 0x002A [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_002B:
 14: 0x002B [0x01] GOTO 0x0032
 15: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=7678*)
    → "Ahahahahaha! I can sense the power of the ring! Get yourself moving [north/northeast/east/southeast/south/southwest/west/northwest]!"
 16: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0032:
 17: 0x0032 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 18: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 19: 0x0049 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x004B [0x21] END_EVENT
 21: 0x004C [0x00] END_REQSTACK()
```
