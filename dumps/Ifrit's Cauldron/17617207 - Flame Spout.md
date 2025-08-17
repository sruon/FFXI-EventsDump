# 17617207 - Flame Spout

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Ifrit's Cauldron (ID: 205) |
| Block Size       | 240 bytes                  |
| Total Events     | 2                          |
| References Count | 11                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [13](#event-13)       | 0x0001       |    170 |             35 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C46      |        7238 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0x000B      |          11 |
|       5 | 0x000C      |          12 |
|       6 | 0x0003      |           3 |
|       7 | 0x000D      |          13 |
|       8 | 0x0004      |           4 |
|       9 | 0x000E      |          14 |
|      10 | 0x0005      |           5 |

## String References

- **7238**: Hold the vines up to the flames? [Yes./Not yet.]

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

### Event 13

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 170 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    24 00 80 01 80 01 80  25 02 00 10 01 80 00 97   $......%.......
0010: 00 42 03 01 10 01 80 02  02 10 02 80 00 37 00 02  .B...........7..
0020: 04 10 03 80 00 2F 00 03  01 10 04 80 01 34 00 03  ...../.......4..
0030: 01 10 02 80 01 94 00 02  02 10 03 80 00 57 00 02  .............W..
0040: 04 10 03 80 00 4F 00 03  01 10 05 80 01 54 00 03  .....O.......T..
0050: 01 10 03 80 01 94 00 02  02 10 06 80 00 77 00 02  .............w..
0060: 04 10 03 80 00 6F 00 03  01 10 07 80 01 74 00 03  .....o.......t..
0070: 01 10 06 80 01 94 00 02  02 10 08 80 00 94 00 02  ................
0080: 04 10 03 80 00 8F 00 03  01 10 09 80 01 94 00 03  ................
0090: 01 10 08 80 01 A7 00 02  00 10 02 80 00 A7 00 03  ................
00A0: 01 10 0A 80 01 A7 00 20  00 21 00                 ....... .!.     
```

#### Opcodes

```
  0: 0x0001 [0x24] CREATE_DIALOG(message_id=7238*, default_option=0*, option_flags=0*)
    → "Hold the vines up to the flames? [Yes./Not yet.]"
  1: 0x0008 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0009 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0097
  3: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0012 [0x03] Work_Zone[1] = 0*
  5: 0x0017 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0037
  6: 0x001F [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x002F
  7: 0x0027 [0x03] Work_Zone[1] = 11*
  8: 0x002C [0x01] GOTO 0x0034
  9: 0x002F [0x03] Work_Zone[1] = 1*

SUBROUTINE_0034:
 10: 0x0034 [0x01] GOTO 0x0094
 11: 0x0037 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0057
 12: 0x003F [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x004F
 13: 0x0047 [0x03] Work_Zone[1] = 12*
 14: 0x004C [0x01] GOTO 0x0054
 15: 0x004F [0x03] Work_Zone[1] = 2*

SUBROUTINE_0054:
 16: 0x0054 [0x01] GOTO 0x0094
 17: 0x0057 [0x02] IF !(Work_Zone[2] == 3*) GOTO 0x0077
 18: 0x005F [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x006F
 19: 0x0067 [0x03] Work_Zone[1] = 13*
 20: 0x006C [0x01] GOTO 0x0074
 21: 0x006F [0x03] Work_Zone[1] = 3*

SUBROUTINE_0074:
 22: 0x0074 [0x01] GOTO 0x0094
 23: 0x0077 [0x02] IF !(Work_Zone[2] == 4*) GOTO 0x0094
 24: 0x007F [0x02] IF !(Work_Zone[4] == 2*) GOTO 0x008F
 25: 0x0087 [0x03] Work_Zone[1] = 14*
 26: 0x008C [0x01] GOTO 0x0094
 27: 0x008F [0x03] Work_Zone[1] = 4*

SUBROUTINE_0094:
 28: 0x0094 [0x01] GOTO 0x00A7
 29: 0x0097 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A7
 30: 0x009F [0x03] Work_Zone[1] = 5*
 31: 0x00A4 [0x01] GOTO 0x00A7

SUBROUTINE_00A7:
 32: 0x00A7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 33: 0x00A9 [0x21] END_EVENT
 34: 0x00AA [0x00] END_REQSTACK()
```
