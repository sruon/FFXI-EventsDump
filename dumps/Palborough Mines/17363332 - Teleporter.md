# 17363332 - Teleporter

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 144 bytes                  |
| Total Events     | 2                          |
| References Count | 7                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |     90 |             20 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CBD      |        7357 |
|       1 | 0x1CBE      |        7358 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0002      |           2 |
|       5 | 0x0003      |           3 |
|       6 | 0x1CC1      |        7361 |

## String References

- **7357**: Welcome to the Palborough Mines. You may teleport to different sections of the mines from here.
- **7358**: Teleport where? [Raft docks./Mythril Refiner./Elevator./Old toolboxes./Cancel.]
- **7361**: Canceled.

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

### Event 100

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 90 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 24 01 80  02 80 02 80 25 02 00 10   ...#$......%...
0010: 02 80 00 1F 00 27 20 F0  FF FF 7F 28 01 5A 00 02  .....' ....(.Z..
0020: 00 10 03 80 00 31 00 27  20 F0 FF FF 7F 29 01 5A  .....1.' ....).Z
0030: 00 02 00 10 04 80 00 43  00 27 20 F0 FF FF 7F 2A  .......C.' ....*
0040: 01 5A 00 02 00 10 05 80  00 55 00 27 20 F0 FF FF  .Z.......U.' ...
0050: 7F 2B 01 5A 00 1D 06 80  23 21 00                 .+.Z....#!.     
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=7357*)
    → "Welcome to the Palborough Mines. You may teleport to different sections of the mines from here."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x24] CREATE_DIALOG(message_id=7358*, default_option=0*, option_flags=0*)
    → "Teleport where? [Raft docks./Mythril Refiner./Elevator./Old toolboxes./Cancel.]"
  3: 0x000C [0x25] WAIT_DIALOG_SELECT()
  4: 0x000D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001F
  5: 0x0015 [0x27] REQ_SET(priority=0x20, entity_id=LocalPlayer, tag_num=0x28)
  6: 0x001C [0x01] GOTO 0x005A
  7: 0x001F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0031
  8: 0x0027 [0x27] REQ_SET(priority=0x20, entity_id=LocalPlayer, tag_num=0x29)
  9: 0x002E [0x01] GOTO 0x005A
 10: 0x0031 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0043
 11: 0x0039 [0x27] REQ_SET(priority=0x20, entity_id=LocalPlayer, tag_num=0x2A)
 12: 0x0040 [0x01] GOTO 0x005A
 13: 0x0043 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0055
 14: 0x004B [0x27] REQ_SET(priority=0x20, entity_id=LocalPlayer, tag_num=0x2B)
 15: 0x0052 [0x01] GOTO 0x005A
 16: 0x0055 [0x1D] PRINT_EVENT_MESSAGE(message_id=7361*)
    → "Canceled."
 17: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0059 [0x21] END_EVENT

SUBROUTINE_005A:
 19: 0x005A [0x00] END_REQSTACK()
```
