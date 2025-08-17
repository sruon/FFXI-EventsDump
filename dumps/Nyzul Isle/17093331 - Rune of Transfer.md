# 17093331 - Rune of Transfer

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Nyzul Isle (ID: 77) |
| Block Size       | 264 bytes           |
| Total Events     | 2                   |
| References Count | 10                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [201](#event-201)     | 0x0001       |    196 |             53 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFFFFFF  |  4294967295 |
|       1 | 0x1CC2      |        7362 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x1D15      |        7445 |
|       5 | 0x0002      |           2 |
|       6 | 0x0003      |           3 |
|       7 | 0x0004      |           4 |
|       8 | 0x0005      |           5 |
|       9 | 0x0006      |           6 |

## String References

- **7362**: Travel to the next floor? [Not yet./Exit the Assault area./Travel to the next floor./Travel to the floor on the right./Travel to the floor on the left./Travel to Floor $1./Travel to Floor ???.]
- **7445**: Do you really want to exit? [Yes./No.]

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

### Event 201

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 196 bytes |
| Instructions | 53        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 03 00 00 02 10  03 01 00 00 80 0F 01 00    ..............
0010: 00 00 24 01 80 02 80 01  00 25 02 00 10 02 80 00  ..$......%......
0020: 25 00 01 C1 00 02 00 10  03 80 00 58 00 24 04 80  %..........X.$..
0030: 03 80 02 80 25 02 00 10  02 80 00 4A 00 43 00 43  ....%......J.C.C
0040: 01 42 03 01 10 03 80 01  55 00 02 00 10 03 80 00  .B......U.......
0050: 55 00 01 55 00 01 C1 00  02 00 10 05 80 00 6D 00  U..U..........m.
0060: 43 00 43 01 42 03 01 10  05 80 01 C1 00 02 00 10  C.C.B...........
0070: 06 80 00 82 00 43 00 43  01 42 03 01 10 06 80 01  .....C.C.B......
0080: C1 00 02 00 10 07 80 00  97 00 43 00 43 01 42 03  ..........C.C.B.
0090: 01 10 07 80 01 C1 00 02  00 10 08 80 00 AC 00 43  ...............C
00A0: 00 43 01 42 03 01 10 08  80 01 C1 00 02 00 10 09  .C.B............
00B0: 80 00 C1 00 43 00 43 01  42 03 01 10 09 80 01 C1  ....C.C.B.......
00C0: 00 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  2: 0x0008 [0x03] ExtData[1]->WorkLocal[1] = 4294967295*
  3: 0x000D [0x0F] ExtData[1]->WorkLocal[1] ^= ExtData[1]->WorkLocal[0]
  4: 0x0012 [0x24] CREATE_DIALOG(message_id=7362*, default_option=0*, option_flags=ExtData[1]->WorkLocal[1])
    → "Travel to the next floor? [Not yet./Exit the Assault area./Travel to the next floor./Travel to the floor on the right./Travel to the floor on the left./Travel to Floor $1./Travel to Floor ???.]"
  5: 0x0019 [0x25] WAIT_DIALOG_SELECT()
  6: 0x001A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0025
  7: 0x0022 [0x01] GOTO 0x00C1
  8: 0x0025 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0058
  9: 0x002D [0x24] CREATE_DIALOG(message_id=7445*, default_option=1*, option_flags=0*)
    → "Do you really want to exit? [Yes./No.]"
 10: 0x0034 [0x25] WAIT_DIALOG_SELECT()
 11: 0x0035 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004A
 12: 0x003D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 13: 0x003F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 14: 0x0041 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0042 [0x03] Work_Zone[1] = 1*
 16: 0x0047 [0x01] GOTO 0x0055
 17: 0x004A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0055
 18: 0x0052 [0x01] GOTO 0x0055

SUBROUTINE_0055:
 19: 0x0055 [0x01] GOTO 0x00C1
 20: 0x0058 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x006D
 21: 0x0060 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 22: 0x0062 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 23: 0x0064 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 24: 0x0065 [0x03] Work_Zone[1] = 2*
 25: 0x006A [0x01] GOTO 0x00C1
 26: 0x006D [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0082
 27: 0x0075 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 28: 0x0077 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 29: 0x0079 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 30: 0x007A [0x03] Work_Zone[1] = 3*
 31: 0x007F [0x01] GOTO 0x00C1
 32: 0x0082 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0097
 33: 0x008A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 34: 0x008C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 35: 0x008E [0x42] SET_CLI_EVENT_CANCEL_DATA()
 36: 0x008F [0x03] Work_Zone[1] = 4*
 37: 0x0094 [0x01] GOTO 0x00C1
 38: 0x0097 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00AC
 39: 0x009F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 40: 0x00A1 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 41: 0x00A3 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 42: 0x00A4 [0x03] Work_Zone[1] = 5*
 43: 0x00A9 [0x01] GOTO 0x00C1
 44: 0x00AC [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00C1
 45: 0x00B4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 46: 0x00B6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 47: 0x00B8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 48: 0x00B9 [0x03] Work_Zone[1] = 6*
 49: 0x00BE [0x01] GOTO 0x00C1

SUBROUTINE_00C1:
 50: 0x00C1 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 51: 0x00C3 [0x21] END_EVENT
 52: 0x00C4 [0x00] END_REQSTACK()
```
