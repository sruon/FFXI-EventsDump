# 17387994 - Wailing Pond

## Common Data

| Field            | Value           |
|------------------|-----------------|
| Zone             | Davoi (ID: 149) |
| Block Size       | 260 bytes       |
| Total Events     | 2               |
| References Count | 11              |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [52](#event-52)       | 0x0001       |    189 |             29 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0013      |          19 |
|       1 | 0x00C8      |         200 |
|       2 | 0x0000      |           0 |
|       3 | 0x003C      |          60 |
|       4 | 0x005E      |          94 |
|       5 | 0x0001      |           1 |
|       6 | 0x0002      |           2 |
|       7 | 0x0003      |           3 |
|       8 | 0x012C      |         300 |
|       9 | 0x0101      |         257 |
|      10 | 0x00F0      |         240 |

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

### Event 52

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 189 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 46 01 38 00 80 45  01 80 F0 FF FF 7F F0 FF   BF.8..E........
0010: FF 7F 66 64 6F 31 02 80  1C 03 80 45 04 80 F0 FF  ..fdo1.....E....
0020: FF 7F F0 FF FF 7F 64 76  30 33 02 80 27 01 F0 FF  ......dv03..'...
0030: FF 7F 06 45 01 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ...E..........fd
0040: 69 31 02 80 02 03 10 02  80 80 54 00 03 01 10 02  i1........T.....
0050: 80 01 92 00 02 03 10 05  80 80 64 00 03 01 10 05  ..........d.....
0060: 80 01 92 00 02 03 10 06  80 80 74 00 03 01 10 06  ..........t.....
0070: 80 01 92 00 02 03 10 07  80 80 92 00 03 01 10 07  ................
0080: 80 1C 08 80 73 09 80 DA  51 09 01 F0 FF FF 7F 01  ....s...Q.......
0090: 92 00 1C 0A 80 45 01 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
00A0: 66 64 6F 31 02 80 1C 03  80 46 00 45 01 80 F0 FF  fdo1.....F.E....
00B0: FF 7F F0 FF FF 7F 66 64  69 31 02 80 21 00        ......fdi1..!.  
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0004 [0x38] SET_CLIENT_EVENT_MODE(mode=19*)
  3: 0x0007 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0018 [0x1C] WAIT(60* ticks)
  5: 0x001B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "dv03" with entities [LocalPlayer, LocalPlayer], work=[94*, 0*]
  6: 0x002C [0x27] REQ_SET(priority=0x01, entity_id=LocalPlayer, tag_num=0x06)
  7: 0x0033 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  8: 0x0044 [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x0054
  9: 0x004C [0x03] Work_Zone[1] = 0*
 10: 0x0051 [0x01] GOTO 0x0092
 11: 0x0054 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0064
 12: 0x005C [0x03] Work_Zone[1] = 1*
 13: 0x0061 [0x01] GOTO 0x0092
 14: 0x0064 [0x02] IF !(Work_Zone[3] == 2*) GOTO 0x0074
 15: 0x006C [0x03] Work_Zone[1] = 2*
 16: 0x0071 [0x01] GOTO 0x0092
 17: 0x0074 [0x02] IF !(Work_Zone[3] == 3*) GOTO 0x0092
 18: 0x007C [0x03] Work_Zone[1] = 3*
 19: 0x0081 [0x1C] WAIT(300* ticks)
 20: 0x0084 [0x73] Wailing Pond (ID: 17387994/0x010951DA) casts magic 257* on LocalPlayer
 21: 0x008F [0x01] GOTO 0x0092

SUBROUTINE_0092:
 22: 0x0092 [0x1C] WAIT(240* ticks)
 23: 0x0095 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 24: 0x00A6 [0x1C] WAIT(60* ticks)
 25: 0x00A9 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00BC [0x21] END_EVENT
 28: 0x00BD [0x00] END_REQSTACK()
```
