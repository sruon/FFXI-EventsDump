# 17064138 - Gate Chocobo Circuit

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Chocobo Circuit (ID: 70) |
| Block Size       | 316 bytes                |
| Total Events     | 2                        |
| References Count | 10                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [247](#event-247)     | 0x0001       |    251 |             39 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2514      |        9492 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x00C8      |         200 |
|       4 | 0x003C      |          60 |
|       5 | 0x010C      |         268 |
|       6 | 0x00B4      |         180 |
|       7 | 0x0002      |           2 |
|       8 | 0x0003      |           3 |
|       9 | 0x0004      |           4 |

## String References

- **9492**: Head to Jeuno? [No, thank you./Yes, to Ru'Lude Gardens./Yes, to Upper Jeuno./Yes, to Lower Jeuno./Yes, to Port Jeuno.]

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

### Event 247

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 251 bytes |
| Instructions | 39        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 24 00 80 01 80  01 80 25 02 00 10 01 80    .$......%.....
0010: 00 16 00 01 FA 00 02 00  10 02 80 00 4F 00 42 03  ............O.B.
0020: 01 10 02 80 45 03 80 F0  FF FF 7F F0 FF FF 7F 66  ....E..........f
0030: 64 6F 31 01 80 1C 04 80  45 05 80 F0 FF FF 7F F0  do1.....E.......
0040: FF FF 7F 64 6F 72 32 01  80 1C 06 80 01 FA 00 02  ...dor2.........
0050: 00 10 07 80 00 88 00 42  03 01 10 07 80 45 03 80  .......B.....E..
0060: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 1C 04  ........fdo1....
0070: 80 45 05 80 F0 FF FF 7F  F0 FF FF 7F 64 6F 72 32  .E..........dor2
0080: 01 80 1C 06 80 01 FA 00  02 00 10 08 80 00 C1 00  ................
0090: 42 03 01 10 08 80 45 03  80 F0 FF FF 7F F0 FF FF  B.....E.........
00A0: 7F 66 64 6F 31 01 80 1C  04 80 45 05 80 F0 FF FF  .fdo1.....E.....
00B0: 7F F0 FF FF 7F 64 6F 72  32 01 80 1C 06 80 01 FA  .....dor2.......
00C0: 00 02 00 10 09 80 00 FA  00 42 03 01 10 09 80 45  .........B.....E
00D0: 03 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 01 80  ..........fdo1..
00E0: 1C 04 80 45 05 80 F0 FF  FF 7F F0 FF FF 7F 64 6F  ...E..........do
00F0: 72 32 01 80 1C 06 80 01  FA 00 21 00              r2........!.    
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x24] CREATE_DIALOG(message_id=9492*, default_option=0*, option_flags=0*)
    → "Head to Jeuno? [No, thank you./Yes, to Ru'Lude Gardens./Yes, to Upper Jeuno./Yes, to Lower Jeuno./Yes, to Port Jeuno.]"
  2: 0x000A [0x25] WAIT_DIALOG_SELECT()
  3: 0x000B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0016
  4: 0x0013 [0x01] GOTO 0x00FA
  5: 0x0016 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004F
  6: 0x001E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  7: 0x001F [0x03] Work_Zone[1] = 1*
  8: 0x0024 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  9: 0x0035 [0x1C] WAIT(60* ticks)
 10: 0x0038 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dor2" with entities [LocalPlayer, LocalPlayer], work=[268*, 0*]
 11: 0x0049 [0x1C] WAIT(180* ticks)
 12: 0x004C [0x01] GOTO 0x00FA
 13: 0x004F [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0088
 14: 0x0057 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0058 [0x03] Work_Zone[1] = 2*
 16: 0x005D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x006E [0x1C] WAIT(60* ticks)
 18: 0x0071 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dor2" with entities [LocalPlayer, LocalPlayer], work=[268*, 0*]
 19: 0x0082 [0x1C] WAIT(180* ticks)
 20: 0x0085 [0x01] GOTO 0x00FA
 21: 0x0088 [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x00C1
 22: 0x0090 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 23: 0x0091 [0x03] Work_Zone[1] = 3*
 24: 0x0096 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 25: 0x00A7 [0x1C] WAIT(60* ticks)
 26: 0x00AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dor2" with entities [LocalPlayer, LocalPlayer], work=[268*, 0*]
 27: 0x00BB [0x1C] WAIT(180* ticks)
 28: 0x00BE [0x01] GOTO 0x00FA
 29: 0x00C1 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x00FA
 30: 0x00C9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 31: 0x00CA [0x03] Work_Zone[1] = 4*
 32: 0x00CF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 33: 0x00E0 [0x1C] WAIT(60* ticks)
 34: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dor2" with entities [LocalPlayer, LocalPlayer], work=[268*, 0*]
 35: 0x00F4 [0x1C] WAIT(180* ticks)
 36: 0x00F7 [0x01] GOTO 0x00FA

SUBROUTINE_00FA:
 37: 0x00FA [0x21] END_EVENT
 38: 0x00FB [0x00] END_REQSTACK()
```
