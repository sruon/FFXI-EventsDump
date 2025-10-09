# 16933555 - Swirling Vortex

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Apollyon (ID: 38) |
| Block Size       | 192 bytes         |
| Total Events     | 2                 |
| References Count | 8                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [123](#event-123)     | 0x0001       |    134 |             28 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C4A      |        7242 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0002      |           2 |
|       4 | 0xFFF6B900  |  4294359296 |
|       5 | 0xFFF6D840  |  4294367296 |
|       6 | 0x07E8      |        2024 |
|       7 | 0x94700     |      608000 |

## String References

- **7242**: Return to entrance? [Yes (Entrance 1)./Yes (Entrance 2)./No.]

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

### Event 123

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 134 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  01 80 25 02 00 10 01 80    .$......%.....
0010: 00 1B 00 03 01 10 02 80  01 3B 00 02 00 10 02 80  .........;......
0020: 00 2B 00 03 01 10 03 80  01 3B 00 02 00 10 03 80  .+.......;......
0030: 00 3B 00 03 01 10 01 80  01 3B 00 02 01 10 01 80  .;.......;......
0040: 00 46 00 01 83 00 42 29  01 F0 FF FF 7F 02 02 01  .F....B)........
0050: 10 02 80 80 65 00 47 00  04 80 05 80 01 80 06 80  ....e.G.........
0060: 47 01 01 7C 00 02 01 10  03 80 80 7C 00 47 00 07  G..|.......|.G..
0070: 80 05 80 01 80 01 80 47  01 01 7C 00 29 01 F0 FF  .......G..|.)...
0080: FF 7F 03 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=7242*, default_option=0*, option_flags=0*)
    → "Return to entrance? [Yes (Entrance 1)./Yes (Entrance 2)./No.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x001B
  4: 0x0013 [0x03] Work_Zone[1] = 1*
  5: 0x0018 [0x01] GOTO 0x003B
  6: 0x001B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x002B
  7: 0x0023 [0x03] Work_Zone[1] = 2*
  8: 0x0028 [0x01] GOTO 0x003B
  9: 0x002B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x003B
 10: 0x0033 [0x03] Work_Zone[1] = 0*
 11: 0x0038 [0x01] GOTO 0x003B

SUBROUTINE_003B:
 12: 0x003B [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x0046
 13: 0x0043 [0x01] GOTO 0x0083
 14: 0x0046 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0047 [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x02)
 16: 0x004E [0x02] IF !(Work_Zone[1] == 1*) GOTO 0x0065
 17: 0x0056 [0x47] UPDATE_PLAYER_POS(-608.000*, -600.000*, 0.000*, yaw=177.9°*)
 18: 0x0060 [0x47] WAIT_PLAYER_POS_UPDATE
 19: 0x0062 [0x01] GOTO 0x007C
 20: 0x0065 [0x02] IF !(Work_Zone[1] == 2*) GOTO 0x007C
 21: 0x006D [0x47] UPDATE_PLAYER_POS(608.000*, -600.000*, 0.000*, yaw=0.0°*)
 22: 0x0077 [0x47] WAIT_PLAYER_POS_UPDATE
 23: 0x0079 [0x01] GOTO 0x007C

SUBROUTINE_007C:
 24: 0x007C [0x29] REQ_SET_WAIT(priority=0x01, entity_id=LocalPlayer, tag_num=0x03)

SUBROUTINE_0083:
 25: 0x0083 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 26: 0x0085 [0x21] END_EVENT
 27: 0x0086 [0x00] END_REQSTACK()
```
