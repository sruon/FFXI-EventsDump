# 17232276 - Iron Grate

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Beaucedine Glacier (ID: 111) |
| Block Size       | 140 bytes                    |
| Total Events     | 2                            |
| References Count | 7                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [204](#event-204)     | 0x0001       |     84 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CB9      |        7353 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x005E      |          94 |
|       6 | 0x00B4      |         180 |

## String References

- **7353**: Proceed onward? [Yes./No.]

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

### Event 204

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 84 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 48 00 42 43 00 43 01  03 01 10 01 80 45 03 80  .H.BC.C......E..
0020: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
0030: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 73 61 6B 75  .E..........saku
0040: 02 80 1C 06 80 01 53 00  02 00 10 01 80 00 53 00  ......S.......S.
0050: 01 53 00 21 00                                    .S.!.           
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7353*, default_option=1*, option_flags=0*)
    → "Proceed onward? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0048
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0018 [0x03] Work_Zone[1] = 1*
  8: 0x001D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x002E [0x1C] WAIT(60* ticks)
 10: 0x0031 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "saku" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
 11: 0x0042 [0x1C] WAIT(180* ticks)
 12: 0x0045 [0x01] GOTO 0x0053
 13: 0x0048 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0053
 14: 0x0050 [0x01] GOTO 0x0053

SUBROUTINE_0053:
 15: 0x0053 [0x21] END_EVENT
 16: 0x0054 [0x00] END_REQSTACK()
```
