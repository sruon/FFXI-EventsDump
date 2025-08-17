# 17469834 - Transporter

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Toraimarai Canal (ID: 169) |
| Block Size       | 244 bytes                  |
| Total Events     | 2                          |
| References Count | 8                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [71](#event-71)       | 0x0001       |    184 |             35 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D1F      |        7455 |
|       1 | 0x1D20      |        7456 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x00C8      |         200 |
|       5 | 0x003C      |          60 |
|       6 | 0x1D21      |        7457 |
|       7 | 0x0002      |           2 |

## String References

- **7455**: A gentle voice whispers: "I will guide you to the first floor of Heavens Tower."
- **7456**: Warp to the first floor of Heavens Tower? [Yes./No.]
- **7457**: Are you sure you're finished here? [Return to Heavens Tower./Keep looking around.]

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

### Event 71

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 184 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 48 00 80 23  24 01 80 02 80 03 80 25    .BH..#$......%
0010: 02 00 10 03 80 00 A5 00  02 05 10 03 80 00 51 00  ..............Q.
0020: 03 01 10 02 80 43 00 43  01 62 02 80 F0 FF FF 7F  .....C.C.b......
0030: F0 FF FF 7F 6D 61 69 6E  03 80 45 04 80 F0 FF FF  ....main..E.....
0040: 7F F0 FF FF 7F 66 64 6F  31 03 80 1C 05 80 01 A2  .....fdo1.......
0050: 00 24 06 80 02 80 03 80  25 02 00 10 03 80 00 92  .$......%.......
0060: 00 03 01 10 02 80 43 00  43 01 62 02 80 F0 FF FF  ......C.C.b.....
0070: 7F F0 FF FF 7F 6D 61 69  6E 03 80 45 04 80 F0 FF  .....main..E....
0080: FF 7F F0 FF FF 7F 66 64  6F 31 03 80 1C 05 80 01  ......fdo1......
0090: A2 00 02 00 10 02 80 00  A2 00 03 01 10 07 80 01  ................
00A0: A2 00 01 B5 00 02 00 10  02 80 00 B5 00 03 01 10  ................
00B0: 07 80 01 B5 00 20 00 21  00                       ..... .!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x48] [System] [7455*]:
    → "A gentle voice whispers: "I will guide you to the first floor of Heavens Tower.""
  3: 0x0007 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0008 [0x24] CREATE_DIALOG(message_id=7456*, default_option=1*, option_flags=0*)
    → "Warp to the first floor of Heavens Tower? [Yes./No.]"
  5: 0x000F [0x25] WAIT_DIALOG_SELECT()
  6: 0x0010 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A5
  7: 0x0018 [0x02] IF !(Work_Zone[5] == 0*) GOTO 0x0051
  8: 0x0020 [0x03] Work_Zone[1] = 1*
  9: 0x0025 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 10: 0x0027 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 11: 0x0029 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
 12: 0x003A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x004B [0x1C] WAIT(60* ticks)
 14: 0x004E [0x01] GOTO 0x00A2
 15: 0x0051 [0x24] CREATE_DIALOG(message_id=7457*, default_option=1*, option_flags=0*)
    → "Are you sure you're finished here? [Return to Heavens Tower./Keep looking around.]"
 16: 0x0058 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0059 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0092
 18: 0x0061 [0x03] Work_Zone[1] = 1*
 19: 0x0066 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 20: 0x0068 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 21: 0x006A [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
 22: 0x007B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x008C [0x1C] WAIT(60* ticks)
 24: 0x008F [0x01] GOTO 0x00A2
 25: 0x0092 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A2
 26: 0x009A [0x03] Work_Zone[1] = 2*
 27: 0x009F [0x01] GOTO 0x00A2

SUBROUTINE_00A2:
 28: 0x00A2 [0x01] GOTO 0x00B5
 29: 0x00A5 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00B5
 30: 0x00AD [0x03] Work_Zone[1] = 2*
 31: 0x00B2 [0x01] GOTO 0x00B5

SUBROUTINE_00B5:
 32: 0x00B5 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x00B7 [0x21] END_EVENT
 34: 0x00B8 [0x00] END_REQSTACK()
```
