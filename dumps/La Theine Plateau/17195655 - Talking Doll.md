# 17195655 - Talking Doll

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 112 bytes                   |
| Total Events     | 2                           |
| References Count | 6                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [125](#event-125)     | 0x0001       |     61 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x1D9B      |        7579 |
|       2 | 0x1D9D      |        7581 |
|       3 | 0x1D9C      |        7580 |
|       4 | 0x00C8      |         200 |
|       5 | 0x0000      |           0 |

## String References

- **7579**: The $0 jumps in your hands.
- **7580**: Ahahahahaha! I can sense the power of the ring! Get yourself moving [north/northeast/east/southeast/south/southwest/west/northwest]!
- **7581**: Ahahahahaha! Don't slow down now, slacker! The readings are coming from the [north/northeast/east/southeast/south/southwest/west/northwest]!

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

### Event 125

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 61 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1C 00 80 43 00 43  01 1C 00 80 48 01 80 23   B...C.C....H..#
0010: 02 09 10 00 80 00 1F 00  1D 02 80 23 01 23 00 1D  ...........#.#..
0020: 03 80 23 4E 00 F0 FF FF  7F 45 04 80 F8 FF FF 7F  ..#N.....E......
0030: F8 FF FF 7F 66 64 69 31  05 80 20 00 21 00        ....fdi1.. .!.  
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1C] WAIT(1* ticks)
  2: 0x0005 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0007 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x0009 [0x1C] WAIT(1* ticks)
  5: 0x000C [0x48] [System] [7579*]:
    → "The $0 jumps in your hands."
  6: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0010 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x001F
  8: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7581*)
    → "Ahahahahaha! Don't slow down now, slacker! The readings are coming from the [north/northeast/east/southeast/south/southwest/west/northwest]!"
  9: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x001C [0x01] GOTO 0x0023
 11: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7580*)
    → "Ahahahahaha! I can sense the power of the ring! Get yourself moving [north/northeast/east/southeast/south/southwest/west/northwest]!"
 12: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0023:
 13: 0x0023 [0x4E] SET_ENTITY_HIDE_FLAG: Show LocalPlayer
 14: 0x0029 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [EventEntity, EventEntity], work=[200*, 0*]
 15: 0x003A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x003C [0x21] END_EVENT
 17: 0x003D [0x00] END_REQSTACK()
```
