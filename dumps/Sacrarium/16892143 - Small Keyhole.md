# 16892143 - Small Keyhole

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Sacrarium (ID: 28) |
| Block Size       | 192 bytes          |
| Total Events     | 2                  |
| References Count | 7                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |    137 |             32 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x00A0      |         160 |
|       3 | 0x1C49      |        7241 |
|       4 | 0x0002      |           2 |
|       5 | 0x1C4A      |        7242 |
|       6 | 0x0003      |           3 |

## String References

- **7241**: <Player> is holding the lock open...
- **7242**: <Player>'s hand has grown numb!

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 137 bytes |
| Instructions | 24        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 42 03 01 10 00  80 43 00 43 01 02 02 10    .B.....C.C....
0010: 01 80 00 1B 00 01 88 00  01 2C 00 45 02 80 F8 FF  .........,.E....
0020: FF 7F F8 FF FF 7F 32 37  73 77 00 80 03 01 10 01  ......27sw......
0030: 80 43 00 43 01 02 02 10  01 80 00 43 00 01 88 00  .C.C.......C....
0040: 01 46 00 48 03 80 03 01  10 04 80 43 00 43 01 02  .F.H.......C.C..
0050: 02 10 01 80 00 5D 00 01  88 00 01 60 00 48 05 80  .....].....`.H..
0060: 03 01 10 06 80 43 00 43  01 02 02 10 01 80 00 77  .....C.C.......w
0070: 00 01 88 00 01 88 00 45  02 80 F8 FF FF 7F F8 FF  .......E........
0080: FF 7F 32 37 73 77 00 80  21 00                    ..27sw..!.      
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0004 [0x03] Work_Zone[1] = 0*
  3: 0x0009 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  4: 0x000B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  5: 0x000D [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x001B
  6: 0x0015 [0x01] GOTO 0x0088

SUBROUTINE_002C:
  7: 0x002C [0x03] Work_Zone[1] = 1*
  8: 0x0031 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  9: 0x0033 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 10: 0x0035 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0043
 11: 0x003D [0x01] GOTO 0x0088

SUBROUTINE_0046:
 12: 0x0046 [0x03] Work_Zone[1] = 2*
 13: 0x004B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 14: 0x004D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 15: 0x004F [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x005D
 16: 0x0057 [0x01] GOTO 0x0088

SUBROUTINE_0060:
 17: 0x0060 [0x03] Work_Zone[1] = 3*
 18: 0x0065 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 19: 0x0067 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 20: 0x0069 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0077
 21: 0x0071 [0x01] GOTO 0x0088

SUBROUTINE_0088:
 22: 0x0088 [0x21] END_EVENT
 23: 0x0089 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0018 [0x01] GOTO 0x002C
# Dead code (unreachable instructions):
     0x0040 [0x01] GOTO 0x0046
# Dead code (unreachable instructions):
     0x005A [0x01] GOTO 0x0060
# Dead code (unreachable instructions):
     0x0074 [0x01] GOTO 0x0088
```
