# 17526911 - Legion Tome

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Maquette Abdhaljs-LegionA (ID: 183) |
| Block Size       | 176 bytes                           |
| Total Events     | 2                                   |
| References Count | 8                                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [10003](#event-10003) | 0x0001       |    119 |             27 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1BA3      |        7075 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x1BA4      |        7076 |
|       4 | 0x1BA5      |        7077 |
|       5 | 0x00FF      |         255 |
|       6 | 0x0078      |         120 |
|       7 | 0x40000000  |  1073741824 |

## String References

- **7075**: Exit the maquette? [Yes, exit./No, remain.]
- **7076**: Reentry will not be permitted. Do you still wish to leave?
- **7077**: Truly exit the maquette? [Yes, exit./No, remain.]

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

### Event 10003

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 119 bytes |
| Instructions | 27        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 0E 00 02 10 24  00 80 01 80 02 80 25 02   B.....$......%.
0010: 00 10 02 80 00 66 00 48  03 80 23 24 04 80 01 80  .....f.H..#$....
0020: 02 80 25 02 00 10 02 80  00 53 00 03 01 10 05 80  ..%......S......
0030: 43 00 43 01 06 01 10 62  01 80 F0 FF FF 7F F0 FF  C.C....b........
0040: FF 7F 6D 61 69 6E 02 80  1C 06 80 03 01 10 01 80  ..main..........
0050: 01 63 00 02 00 10 01 80  00 63 00 03 01 10 07 80  .c.......c......
0060: 01 63 00 01 76 00 02 00  10 01 80 00 76 00 03 01  .c..v.......v...
0070: 10 07 80 01 76 00 21 00                           ....v.!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[14] = Work_Zone[2]
  2: 0x0007 [0x24] CREATE_DIALOG(message_id=7075*, default_option=1*, option_flags=0*)
    → "Exit the maquette? [Yes, exit./No, remain.]"
  3: 0x000E [0x25] WAIT_DIALOG_SELECT()
  4: 0x000F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0066
  5: 0x0017 [0x48] [System] [7076*]:
    → "Reentry will not be permitted. Do you still wish to leave?"
  6: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001B [0x24] CREATE_DIALOG(message_id=7077*, default_option=1*, option_flags=0*)
    → "Truly exit the maquette? [Yes, exit./No, remain.]"
  8: 0x0022 [0x25] WAIT_DIALOG_SELECT()
  9: 0x0023 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0053
 10: 0x002B [0x03] Work_Zone[1] = 255*
 11: 0x0030 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0032 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x0034 [0x06] Work_Zone[1] = 0
 14: 0x0037 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
 15: 0x0048 [0x1C] WAIT(120* ticks)
 16: 0x004B [0x03] Work_Zone[1] = 1*
 17: 0x0050 [0x01] GOTO 0x0063
 18: 0x0053 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0063
 19: 0x005B [0x03] Work_Zone[1] = 1073741824*
 20: 0x0060 [0x01] GOTO 0x0063

SUBROUTINE_0063:
 21: 0x0063 [0x01] GOTO 0x0076
 22: 0x0066 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0076
 23: 0x006E [0x03] Work_Zone[1] = 1073741824*
 24: 0x0073 [0x01] GOTO 0x0076

SUBROUTINE_0076:
 25: 0x0076 [0x21] END_EVENT
 26: 0x0077 [0x00] END_REQSTACK()
```
