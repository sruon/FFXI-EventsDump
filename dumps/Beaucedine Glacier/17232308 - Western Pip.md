# 17232308 - Western Pip

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Beaucedine Glacier (ID: 111) |
| Block Size       | 620 bytes                    |
| Total Events     | 2                            |
| References Count | 20                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [511](#event-511)     | 0x0001       |    514 |            141 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x0008      |           8 |
|       3 | 0x000B      |          11 |
|       4 | 0x0002      |           2 |
|       5 | 0x000C      |          12 |
|       6 | 0x0003      |           3 |
|       7 | 0x000A      |          10 |
|       8 | 0x0004      |           4 |
|       9 | 0x0009      |           9 |
|      10 | 0x0005      |           5 |
|      11 | 0x000D      |          13 |
|      12 | 0x0006      |           6 |
|      13 | 0x000E      |          14 |
|      14 | 0x0007      |           7 |
|      15 | 0x000F      |          15 |
|      16 | 0x0078      |         120 |
|      17 | 0x006F      |         111 |
|      18 | 0x1D0E      |        7438 |
|      19 | 0x003C      |          60 |

## String References

- **7438**: The mark of [Fire/Earth/Water/Wind/Ice/Lightning/Light/Dark] has been inscribed on your $3!

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

### Event 511

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 514 bytes |
| Instructions | 56        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 42 43  00 43 01 20 01 03 01 00   .....BC.C. ....
0010: 02 10 03 02 00 03 10 03  03 00 04 10 03 04 00 05  ................
0020: 10 03 06 00 06 10 02 04  00 01 80 80 36 00 03 05  ............6...
0030: 00 02 80 01 A6 00 02 04  00 00 80 80 46 00 03 05  ............F...
0040: 00 03 80 01 A6 00 02 04  00 04 80 80 56 00 03 05  ............V...
0050: 00 05 80 01 A6 00 02 04  00 06 80 80 66 00 03 05  ............f...
0060: 00 07 80 01 A6 00 02 04  00 08 80 80 76 00 03 05  ............v...
0070: 00 09 80 01 A6 00 02 04  00 0A 80 80 86 00 03 05  ................
0080: 00 0B 80 01 A6 00 02 04  00 0C 80 80 96 00 03 05  ................
0090: 00 0D 80 01 A6 00 02 04  00 0E 80 80 A6 00 03 05  ................
00A0: 00 0F 80 01 A6 00 03 02  10 01 00 03 03 10 02 00  ................
00B0: 03 04 10 03 00 03 05 10  05 00 29 80 B2 F1 06 01  ..........).....
00C0: 07 1C 10 80 89 11 80 02  04 00 01 80 80 EB 00 8B  ................
00D0: 11 80 00 00 01 00 02 00  46 69 72 65 00 00 00 00  ........Fire....
00E0: 00 00 00 00 00 00 00 00  01 E7 01 02 04 00 00 80  ................
00F0: 80 0F 01 8B 11 80 00 00  01 00 02 00 45 61 72 74  ............Eart
0100: 68 00 00 00 00 00 00 00  00 00 00 00 01 E7 01 02  h...............
0110: 04 00 04 80 80 33 01 8B  11 80 00 00 01 00 02 00  .....3..........
0120: 57 61 74 65 72 00 00 00  00 00 00 00 00 00 00 00  Water...........
0130: 01 E7 01 02 04 00 06 80  80 57 01 8B 11 80 00 00  .........W......
0140: 01 00 02 00 57 69 6E 64  00 00 00 00 00 00 00 00  ....Wind........
0150: 00 00 00 00 01 E7 01 02  04 00 08 80 80 7B 01 8B  .............{..
0160: 11 80 00 00 01 00 02 00  49 63 65 00 00 00 00 00  ........Ice.....
0170: 00 00 00 00 00 00 00 00  01 E7 01 02 04 00 0A 80  ................
0180: 80 9F 01 8B 11 80 00 00  01 00 02 00 4C 69 67 68  ............Ligh
0190: 74 6E 69 6E 67 00 00 00  00 00 00 00 01 E7 01 02  tning...........
01A0: 04 00 0C 80 80 C3 01 8B  11 80 00 00 01 00 02 00  ................
01B0: 4C 69 67 68 74 00 00 00  00 00 00 00 00 00 00 00  Light...........
01C0: 01 E7 01 02 04 00 0E 80  80 E7 01 8B 11 80 00 00  ................
01D0: 01 00 02 00 44 61 72 6B  00 00 00 00 00 00 00 00  ....Dark........
01E0: 00 00 00 00 01 E7 01 03  02 10 06 00 03 03 10 04  ................
01F0: 00 48 12 80 23 8A 1C 13  80 0B 04 00 03 01 10 04  .H..#...........
0200: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x0006 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0007 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
  3: 0x0009 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
  4: 0x000B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  5: 0x000D [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  6: 0x0012 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[3]
  7: 0x0017 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[4]
  8: 0x001C [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[5]
  9: 0x0021 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[6]
 10: 0x0026 [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x0036
 11: 0x002E [0x03] ExtData[1]->WorkLocal[5] = 8*
 12: 0x0033 [0x01] GOTO 0x00A6
 13: 0x0036 [0x02] IF !(ExtData[1]->WorkLocal[4] == 1*) GOTO 0x0046
 14: 0x003E [0x03] ExtData[1]->WorkLocal[5] = 11*
 15: 0x0043 [0x01] GOTO 0x00A6
 16: 0x0046 [0x02] IF !(ExtData[1]->WorkLocal[4] == 2*) GOTO 0x0056
 17: 0x004E [0x03] ExtData[1]->WorkLocal[5] = 12*
 18: 0x0053 [0x01] GOTO 0x00A6
 19: 0x0056 [0x02] IF !(ExtData[1]->WorkLocal[4] == 3*) GOTO 0x0066
 20: 0x005E [0x03] ExtData[1]->WorkLocal[5] = 10*
 21: 0x0063 [0x01] GOTO 0x00A6
 22: 0x0066 [0x02] IF !(ExtData[1]->WorkLocal[4] == 4*) GOTO 0x0076
 23: 0x006E [0x03] ExtData[1]->WorkLocal[5] = 9*
 24: 0x0073 [0x01] GOTO 0x00A6
 25: 0x0076 [0x02] IF !(ExtData[1]->WorkLocal[4] == 5*) GOTO 0x0086
 26: 0x007E [0x03] ExtData[1]->WorkLocal[5] = 13*
 27: 0x0083 [0x01] GOTO 0x00A6
 28: 0x0086 [0x02] IF !(ExtData[1]->WorkLocal[4] == 6*) GOTO 0x0096
 29: 0x008E [0x03] ExtData[1]->WorkLocal[5] = 14*
 30: 0x0093 [0x01] GOTO 0x00A6
 31: 0x0096 [0x02] IF !(ExtData[1]->WorkLocal[4] == 7*) GOTO 0x00A6
 32: 0x009E [0x03] ExtData[1]->WorkLocal[5] = 15*
 33: 0x00A3 [0x01] GOTO 0x00A6

SUBROUTINE_00A6:
 34: 0x00A6 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 35: 0x00AB [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 36: 0x00B0 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 37: 0x00B5 [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[5]
 38: 0x00BA [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Element (ID: 17232306/0x0106F1B2), tag_num=0x07)
 39: 0x00C1 [0x1C] WAIT(120* ticks)
 40: 0x00C4 [0x89] OPEN_MAP(map_id=0x00008011)
 41: 0x00C7 [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x00EB
 42: 0x00CF [0x8B] SET_EVENT_MARK: Add/update map marker on map 111* at (ExtData[1]->WorkLocal[1], ExtData[1]->WorkLocal[2]), index=ExtData[1]->WorkLocal[0], name=(no name)
 43: 0x00D8 [0x46] CAMERA_CONTROL: Unknown mode 0x69
 44: 0x00DA [0x72] LOAD_EVENT_WEATHER: Unknown mode 101, weather_id=ExtData[1]->WorkLocal[0]
 45: 0x00DE [0x00] END_REQSTACK()

SUBROUTINE_01E7:
 46: 0x01E7 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[6]
 47: 0x01EC [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[4]
 48: 0x01F1 [0x48] [System] [7438*]:
    → "The mark of [Fire/Earth/Water/Wind/Ice/Lightning/Light/Dark] has been inscribed on your $3!"
 49: 0x01F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x01F5 [0x8A] CLOSE_MAP()
 51: 0x01F6 [0x1C] WAIT(60* ticks)
 52: 0x01F9 [0x0B] ExtData[1]->WorkLocal[4]++
 53: 0x01FC [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[4]
 54: 0x0201 [0x21] END_EVENT
 55: 0x0202 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00DF [0x00] END_REQSTACK()
     0x00E0 [0x00] END_REQSTACK()
     0x00E1 [0x00] END_REQSTACK()
     0x00E2 [0x00] END_REQSTACK()
     0x00E3 [0x00] END_REQSTACK()
     0x00E4 [0x00] END_REQSTACK()
     0x00E5 [0x00] END_REQSTACK()
     0x00E6 [0x00] END_REQSTACK()
     0x00E7 [0x00] END_REQSTACK()
     0x00E8 [0x01] GOTO 0x01E7
     0x0112 [0x04] DEPRECATED_NOP(unused=0x8080)
     0x0115 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
     0x0117 [0x8B] SET_EVENT_MARK: Add/update map marker on map 111* at (ExtData[1]->WorkLocal[1], ExtData[1]->WorkLocal[2]), index=ExtData[1]->WorkLocal[0], name=(no name)
     0x0120 [0x57] CREATE_FRAME_DELAY(delay=0x7461)
     0x0123 [0x65] CALCULATE_3D_DISTANCE(result=0x72, entity1=Unknown NPC (ID: 0/0x00000000), entity2=Unknown NPC (ID: 0/0x00000000))
     0x012E [0x00] END_REQSTACK()
     0x012F [0x00] END_REQSTACK()
     0x0130 [0x01] GOTO 0x01E7
     0x0153 [0x00] END_REQSTACK()
     0x0154 [0x01] GOTO 0x01E7
     0x0170 [0x00] END_REQSTACK()
     0x0171 [0x00] END_REQSTACK()
     0x0172 [0x00] END_REQSTACK()
     0x0173 [0x00] END_REQSTACK()
     0x0174 [0x00] END_REQSTACK()
     0x0175 [0x00] END_REQSTACK()
     0x0176 [0x00] END_REQSTACK()
     0x0177 [0x00] END_REQSTACK()
     0x0178 [0x01] GOTO 0x01E7
     0x0199 [0x00] END_REQSTACK()
     0x019A [0x00] END_REQSTACK()
     0x019B [0x00] END_REQSTACK()
     0x019C [0x01] GOTO 0x01E7
     0x01B6 [0x00] END_REQSTACK()
     0x01B7 [0x00] END_REQSTACK()
     0x01B8 [0x00] END_REQSTACK()
     0x01B9 [0x00] END_REQSTACK()
     0x01BA [0x00] END_REQSTACK()
     0x01BB [0x00] END_REQSTACK()
     0x01BC [0x00] END_REQSTACK()
     0x01BD [0x00] END_REQSTACK()
     0x01BE [0x00] END_REQSTACK()
     0x01BF [0x00] END_REQSTACK()
     0x01C0 [0x01] GOTO 0x01E7
     0x01DA [0x00] END_REQSTACK()
     0x01DB [0x00] END_REQSTACK()
     0x01DC [0x00] END_REQSTACK()
     0x01DD [0x00] END_REQSTACK()
     0x01DE [0x00] END_REQSTACK()
     0x01DF [0x00] END_REQSTACK()
     0x01E0 [0x00] END_REQSTACK()
     0x01E1 [0x00] END_REQSTACK()
     0x01E2 [0x00] END_REQSTACK()
     0x01E3 [0x00] END_REQSTACK()
     0x01E4 [0x01] GOTO 0x01E7
```
