# 17068520 - Gate The Pit

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | The Colosseum (ID: 71) |
| Block Size       | 136 bytes              |
| Total Events     | 2                      |
| References Count | 7                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [51](#event-51)       | 0x0001       |     80 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C3E      |        7230 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x010C      |         268 |
|       6 | 0x00B4      |         180 |

## String References

- **7230**: Return to Aht Urhgan Whitegate? [Yes./No.]

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

### Event 51

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 80 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  02 80 25 02 00 10 02 80    .$......%.....
0010: 00 44 00 42 03 01 10 01  80 45 03 80 F0 FF FF 7F  .D.B.....E......
0020: F0 FF FF 7F 66 64 6F 31  02 80 1C 04 80 45 05 80  ....fdo1.....E..
0030: F0 FF FF 7F F0 FF FF 7F  64 6F 72 32 02 80 1C 06  ........dor2....
0040: 80 01 4F 00 02 00 10 01  80 00 4F 00 01 4F 00 21  ..O.......O..O.!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7230*, default_option=1*, option_flags=0*)
    → "Return to Aht Urhgan Whitegate? [Yes./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0044
  4: 0x0013 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  5: 0x0014 [0x03] Work_Zone[1] = 1*
  6: 0x0019 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  7: 0x002A [0x1C] WAIT(60* ticks)
  8: 0x002D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dor2" with entities [LocalPlayer, LocalPlayer], work=[268*, 0*]
  9: 0x003E [0x1C] WAIT(180* ticks)
 10: 0x0041 [0x01] GOTO 0x004F
 11: 0x0044 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004F
 12: 0x004C [0x01] GOTO 0x004F

SUBROUTINE_004F:
 13: 0x004F [0x21] END_EVENT
 14: 0x0050 [0x00] END_REQSTACK()
```
