# 17900036 - Liseran Door Exit

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Outer Ra'Kaznar (ID: 274) |
| Block Size       | 136 bytes                 |
| Total Events     | 2                         |
| References Count | 5                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [28](#event-28)       | 0x0001       |     89 |             17 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x1B75      |        7029 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x00C8      |         200 |

## String References

- **7029**: Leave? [Yes./No.]

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

### Event 28

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 89 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 01 10 00 80 24 01  80 02 80 02 80 25 02 00   .....$......%..
0010: 10 02 80 00 48 00 42 03  01 10 03 80 43 00 43 01  ....H.B.....C.C.
0020: 45 04 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 02  E..........fdo1.
0030: 80 55 04 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .U..........fdo1
0040: 03 01 10 03 80 01 58 00  02 00 10 03 80 00 58 00  ......X.......X.
0050: 03 01 10 00 80 01 58 00  21 00                    ......X.!.      
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[1] = 2*
  1: 0x0006 [0x24] CREATE_DIALOG(message_id=7029*, default_option=0*, option_flags=0*)
    → "Leave? [Yes./No.]"
  2: 0x000D [0x25] WAIT_DIALOG_SELECT()
  3: 0x000E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0048
  4: 0x0016 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0017 [0x03] Work_Zone[1] = 1*
  6: 0x001C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  7: 0x001E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  8: 0x0020 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0031 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 10: 0x0040 [0x03] Work_Zone[1] = 1*
 11: 0x0045 [0x01] GOTO 0x0058
 12: 0x0048 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0058
 13: 0x0050 [0x03] Work_Zone[1] = 2*
 14: 0x0055 [0x01] GOTO 0x0058

SUBROUTINE_0058:
 15: 0x0058 [0x21] END_EVENT
 16: 0x0059 [0x00] END_REQSTACK()
```
