# 17940508 - Door Back to Town

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Celennia Memorial Library (ID: 284) |
| Block Size       | 128 bytes                           |
| Total Events     | 2                                   |
| References Count | 5                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [26](#event-26)       | 0x0001       |     80 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E11      |        7697 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x00C8      |         200 |
|       4 | 0x0002      |           2 |

## String References

- **7697**: Leave the library? [Yes./No.]

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

### Event 26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 80 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 3F   $......%......?
0010: 00 42 03 01 10 02 80 45  03 80 F0 FF FF 7F F0 FF  .B.....E........
0020: FF 7F 66 64 6F 31 01 80  55 03 80 F0 FF FF 7F F0  ..fdo1..U.......
0030: FF FF 7F 66 64 6F 31 03  01 10 02 80 01 4F 00 02  ...fdo1......O..
0040: 00 10 02 80 00 4F 00 03  01 10 04 80 01 4F 00 21  .....O.......O.!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7697*, default_option=0*, option_flags=0*)
    → "Leave the library? [Yes./No.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003F
  3: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0012 [0x03] Work_Zone[1] = 1*
  5: 0x0017 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x0028 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  7: 0x0037 [0x03] Work_Zone[1] = 1*
  8: 0x003C [0x01] GOTO 0x004F
  9: 0x003F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004F
 10: 0x0047 [0x03] Work_Zone[1] = 2*
 11: 0x004C [0x01] GOTO 0x004F

SUBROUTINE_004F:
 12: 0x004F [0x21] END_EVENT
 13: 0x0050 [0x00] END_REQSTACK()
```
