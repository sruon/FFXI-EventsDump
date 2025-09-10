# 17031690 - Decorative Bronze Gate

## Common Data

| Field            | Value            |
|------------------|------------------|
| Zone             | Halvung (ID: 62) |
| Block Size       | 144 bytes        |
| Total Events     | 2                |
| References Count | 7                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [215](#event-215)     | 0x0001       |     88 |             19 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EFC      |        7932 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x010C      |         268 |
|       6 | 0x00B4      |         180 |

## String References

- **7932**: Exit? (You cannot reenter here.) [Yes./Not now.]

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

### Event 215

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 88 bytes |
| Instructions | 19       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 20 01 24 00 80 01  80 02 80 25 02 00 10 02   B .$......%....
0010: 80 00 4A 00 43 00 43 01  03 01 10 01 80 45 03 80  ..J.C.C......E..
0020: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 02 80 1C 04  ........fdo1....
0030: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 64 6F 72 34  .E..........dor4
0040: 02 80 1C 06 80 46 00 01  55 00 02 00 10 01 80 00  .....F..U.......
0050: 55 00 01 55 00 20 00 21  00                       U..U. .!.       
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0004 [0x24] CREATE_DIALOG(message_id=7932*, default_option=1*, option_flags=0*)
    → "Exit? (You cannot reenter here.) [Yes./Not now.]"
  3: 0x000B [0x25] WAIT_DIALOG_SELECT()
  4: 0x000C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004A
  5: 0x0014 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  6: 0x0016 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  7: 0x0018 [0x03] Work_Zone[1] = 1*
  8: 0x001D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x002E [0x1C] WAIT(60* ticks)
 10: 0x0031 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dor4" with entities [LocalPlayer, LocalPlayer], work=[268*, 0*]
 11: 0x0042 [0x1C] WAIT(180* ticks)
 12: 0x0045 [0x46] CAMERA_CONTROL: Restore default settings
 13: 0x0047 [0x01] GOTO 0x0055
 14: 0x004A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0055
 15: 0x0052 [0x01] GOTO 0x0055

SUBROUTINE_0055:
 16: 0x0055 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 17: 0x0057 [0x21] END_EVENT
 18: 0x0058 [0x00] END_REQSTACK()
```
