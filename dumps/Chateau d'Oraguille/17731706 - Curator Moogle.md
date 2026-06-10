# 17731706 - Curator Moogle

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 876 bytes                     |
| Total Events     | 2                             |
| References Count | 47                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [611](#event-611)     | 0x0001       |    661 |             76 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2462      |        9314 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0xFFFFFFFF  |  4294967295 |
|       4 | 0x0007      |           7 |
|       5 | 0x0008      |           8 |
|       6 | 0x0014      |          20 |
|       7 | 0x2463      |        9315 |
|       8 | 0x2467      |        9319 |
|       9 | 0x2464      |        9316 |
|      10 | 0x0002      |           2 |
|      11 | 0x2466      |        9318 |
|      12 | 0x0004      |           4 |
|      13 | 0x2465      |        9317 |
|      14 | 0x010F      |         271 |
|      15 | 0x50AF      |       20655 |
|      16 | 0x0005      |           5 |
|      17 | 0x6731      |       26417 |
|      18 | 0x28BD      |       10429 |
|      19 | 0x677A      |       26490 |
|      20 | 0x0003      |           3 |
|      21 | 0x0E62      |        3682 |
|      22 | 0x010B      |         267 |
|      23 | 0x2735      |       10037 |
|      24 | 0x2736      |       10038 |
|      25 | 0x2737      |       10039 |
|      26 | 0x2734      |       10036 |
|      27 | 0x50B9      |       20665 |
|      28 | 0x00BC      |         188 |
|      29 | 0x1262      |        4706 |
|      30 | 0x1263      |        4707 |
|      31 | 0x10CA      |        4298 |
|      32 | 0x672C      |       26412 |
|      33 | 0x00BD      |         189 |
|      34 | 0x12F2      |        4850 |
|      35 | 0x10CE      |        4302 |
|      36 | 0x6852      |       26706 |
|      37 | 0x5623      |       22051 |
|      38 | 0x1A32      |        6706 |
|      39 | 0x03A1      |         929 |
|      40 | 0x033B      |         827 |
|      41 | 0x1656      |        5718 |
|      42 | 0x6CCF      |       27855 |
|      43 | 0x02E9      |         745 |
|      44 | 0x02CE      |         718 |
|      45 | 0x5624      |       22052 |
|      46 | 0x05AA      |        1450 |

## String References

- **9314**: Hail, adventurer! Take a look and see if there's anything you like, kupo! No gil necessary, just a quick little item in exchange!
- **9316**: If so, then I require that you trade me the following all at once in exchange for the $30.
- **9317**: $ $0 .
- **9318**: $ $0 .
- **9319**: Come again soon, kupo!

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

### Event 611

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 661 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 05 03 00 03   .....op...#....
0010: 04 00 01 80 02 03 00 02  80 00 A2 00 03 00 00 03  ................
0020: 80 03 02 00 01 80 03 0D  00 01 80 02 02 00 04 80  ................
0030: 03 5B 00 3D 00 00 02 00  02 80 9D 00 46 01 01 00  .[.=........F...
0040: 0D 00 9D 05 16 01 01 00  02 00 D4 03 02 00 01 00  ................
0050: 0B 02 00 07 0D 00 05 80  01 2B 00 3D 00 00 06 80  .........+.=....
0060: 02 80 D4 02 07 80 04 00  00 00 25 02 00 10 06 80  ..........%.....
0070: 00 7D 00 1D 08 80 23 06  03 00 01 9F 00 02 00 10  .}....#.........
0080: 06 80 03 9C 00 03 04 00  00 10 9D 00 16 01 16 17  ................
0090: 04 00 1D 09 80 23 1A A4  00 01 9F 00 06 03 00 01  .....#..........
00A0: 14 00 21 00 03 0D 00 04  00 14 0D 00 05 80 07 0D  ..!.............
00B0: 00 0A 80 9D 00 46 01 10  00 0D 00 03 0D 00 04 00  .....F..........
00C0: 14 0D 00 05 80 03 0E 00  01 80 03 18 00 01 80 02  ................
00D0: 0E 00 10 00 03 15 01 9D  00 B6 01 17 17 0D 00 9D  ................
00E0: 00 26 02 18 17 0D 00 0B  18 00 0B 0D 00 02 18 00  .&..............
00F0: 10 00 00 FC 00 48 0B 80  23 01 0F 01 02 18 00 0C  .....H..#.......
0100: 80 00 0B 01 48 0B 80 23  01 0F 01 48 0D 80 23 0B  ....H..#...H..#.
0110: 0E 00 01 CF 00 1B 02 10  03 10 04 10 05 10 06 10  ................
0120: 07 10 08 10 09 10 00 17  01 17 02 17 03 17 04 17  ................
0130: 05 17 06 17 07 17 08 17  09 17 0A 17 0B 17 0C 17  ................
0140: 0D 17 0E 17 0F 17 0E 80  02 80 0C 80 01 80 01 80  ................
0150: 01 80 01 80 01 80 0F 80  02 80 10 80 01 80 01 80  ................
0160: 01 80 01 80 01 80 11 80  02 80 0C 80 01 80 01 80  ................
0170: 01 80 01 80 01 80 12 80  02 80 10 80 01 80 01 80  ................
0180: 01 80 01 80 01 80 13 80  02 80 14 80 01 80 01 80  ................
0190: 01 80 01 80 01 80 15 80  02 80 0C 80 01 80 01 80  ................
01A0: 01 80 01 80 01 80 16 80  02 80 14 80 01 80 01 80  ................
01B0: 01 80 01 80 01 80 17 80  18 80 19 80 1A 80 01 80  ................
01C0: 01 80 01 80 01 80 1B 80  1C 80 1D 80 1E 80 1F 80  ................
01D0: 01 80 01 80 01 80 20 80  21 80 22 80 23 80 01 80  ...... .!.".#...
01E0: 01 80 01 80 01 80 24 80  25 80 26 80 27 80 28 80  ......$.%.&.'.(.
01F0: 01 80 01 80 01 80 20 80  18 80 29 80 01 80 01 80  ...... ...).....
0200: 01 80 01 80 01 80 2A 80  2B 80 2C 80 1A 80 01 80  ......*.+.,.....
0210: 01 80 01 80 01 80 17 80  2D 80 2E 80 01 80 01 80  ........-.......
0220: 01 80 01 80 01 80 02 80  02 80 02 80 14 80 01 80  ................
0230: 01 80 01 80 01 80 02 80  02 80 02 80 02 80 02 80  ................
0240: 01 80 01 80 01 80 02 80  02 80 02 80 02 80 01 80  ................
0250: 01 80 01 80 01 80 02 80  02 80 02 80 02 80 02 80  ................
0260: 01 80 01 80 01 80 02 80  02 80 0C 80 01 80 01 80  ................
0270: 01 80 01 80 01 80 02 80  02 80 02 80 14 80 01 80  ................
0280: 01 80 01 80 01 80 02 80  02 80 02 80 01 80 01 80  ................
0290: 01 80 01 80 01 80                                 ......          
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=9314*)
    → "Hail, adventurer! Take a look and see if there's anything you like, kupo! No gil necessary, just a quick little item in exchange!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x05] ExtData[1]->WorkLocal[3] = 1
  6: 0x000F [0x03] ExtData[1]->WorkLocal[4] = 0*
  7: 0x0014 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x00A2
  8: 0x001C [0x03] ExtData[1]->WorkLocal[0] = 4294967295*
  9: 0x0021 [0x03] ExtData[1]->WorkLocal[2] = 0*
 10: 0x0026 [0x03] ExtData[1]->WorkLocal[13] = 0*
 11: 0x002B [0x02] IF !(ExtData[1]->WorkLocal[2] >= 7*) GOTO 0x005B
 12: 0x0033 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=ExtData[1]->WorkLocal[2], condition_work_offset=1*)
 13: 0x003A [0x9D] ExtData[1]->WorkLocal[1] = 0x0146[ExtData[1]->WorkLocal[13]] // Read WORD
 14: 0x0042 [0x9D] 0x0116[ExtData[1]->WorkLocal[2] * 2] = ExtData[1]->WorkLocal[1] // Write WORD
 15: 0x004A [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[02 00 01 00 0B 02 00 07...])
 16: 0x0068 [0x00] END_REQSTACK()
 17: 0x0069 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Data Section: 0x0116 (306 bytes)
     0x0116: 02 10 03 10 04 10 05 10 06 10 07 10 08 10 09 10
     0x0126: 00 17 01 17 02 17 03 17 04 17 05 17 06 17 07 17
     0x0136: 08 17 09 17 0A 17 0B 17 0C 17 0D 17 0E 17 0F 17
     0x0146: 0E 80 02 80 0C 80 01 80 01 80 01 80 01 80 01 80
     0x0156: 0F 80 02 80 10 80 01 80 01 80 01 80 01 80 01 80
     0x0166: 11 80 02 80 0C 80 01 80 01 80 01 80 01 80 01 80
     0x0176: 12 80 02 80 10 80 01 80 01 80 01 80 01 80 01 80
     0x0186: 13 80 02 80 14 80 01 80 01 80 01 80 01 80 01 80
     0x0196: 15 80 02 80 0C 80 01 80 01 80 01 80 01 80 01 80
     0x01A6: 16 80 02 80 14 80 01 80 01 80 01 80 01 80 01 80
     0x01B6: 17 80 18 80 19 80 1A 80 01 80 01 80 01 80 01 80
     0x01C6: 1B 80 1C 80 1D 80 1E 80 1F 80 01 80 01 80 01 80
     0x01D6: 20 80 21 80 22 80 23 80 01 80 01 80 01 80 01 80
     0x01E6: 24 80 25 80 26 80 27 80 28 80 01 80 01 80 01 80
     0x01F6: 20 80 18 80 29 80 01 80 01 80 01 80 01 80 01 80
     0x0206: 2A 80 2B 80 2C 80 1A 80 01 80 01 80 01 80 01 80
     0x0216: 17 80 2D 80 2E 80 01 80 01 80 01 80 01 80 01 80
     0x0226: 02 80 02 80 02 80 14 80 01 80 01 80 01 80 01 80
     0x0236: 02 80 02 80 02 80 02 80 02 80 01 80 01 80 01 80
     0x0246: 02 80
# Dead code (unreachable instructions):
     0x006A [0x25] WAIT_DIALOG_SELECT()
     0x006B [0x02] IF !(Work_Zone[0] == 20*) GOTO 0x007D
     0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=9319*)
    → "Come again soon, kupo!"
     0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0077 [0x06] ExtData[1]->WorkLocal[3] = 0
     0x007A [0x01] GOTO 0x009F
     0x007D [0x02] IF !(Work_Zone[0] >= 20*) GOTO 0x009C
     0x0085 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
     0x008A [0x9D] Work_Zone_1700[22] = 0x0116[ExtData[1]->WorkLocal[4]] // Read WORD
     0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=9316*)
    → "If so, then I require that you trade me the following all at once in exchange for the $30."
     0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0096 [0x1A] CALL_SUBROUTINE(address=0x00A4)
     0x0099 [0x01] GOTO 0x009F
     0x009C [0x06] ExtData[1]->WorkLocal[3] = 0
     0x009F [0x01] GOTO 0x0014
     0x00A4 [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[4]
     0x00A9 [0x14] ExtData[1]->WorkLocal[13] *= 8*
     0x00AE [0x07] ExtData[1]->WorkLocal[13] += 2*
     0x00B3 [0x9D] ExtData[1]->WorkLocal[16] = 0x0146[ExtData[1]->WorkLocal[13]] // Read WORD
     0x00BB [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[4]
     0x00C0 [0x14] ExtData[1]->WorkLocal[13] *= 8*
     0x00C5 [0x03] ExtData[1]->WorkLocal[14] = 0*
     0x00CA [0x03] ExtData[1]->WorkLocal[24] = 0*
     0x00CF [0x02] IF !(ExtData[1]->WorkLocal[14] >= ExtData[1]->WorkLocal[16]) GOTO 0x0115
     0x00D7 [0x9D] Work_Zone_1700[23] = 0x01B6[ExtData[1]->WorkLocal[13]] // Read WORD
     0x00DF [0x9D] Work_Zone_1700[24] = 0x0226[ExtData[1]->WorkLocal[13]] // Read WORD
     0x00E7 [0x0B] ExtData[1]->WorkLocal[24]++
     0x00EA [0x0B] ExtData[1]->WorkLocal[13]++
     0x00ED [0x02] IF !(ExtData[1]->WorkLocal[24] == ExtData[1]->WorkLocal[16]) GOTO 0x00FC
     0x00F5 [0x48] [System] [9318*]:
    → "$ $0 ."
     0x00F8 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00F9 [0x01] GOTO 0x010F
     0x00FC [0x02] IF !(ExtData[1]->WorkLocal[24] == 4*) GOTO 0x010B
     0x0104 [0x48] [System] [9318*]:
    → "$ $0 ."
     0x0107 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0108 [0x01] GOTO 0x010F
     0x010B [0x48] [System] [9317*]:
    → "$ $0 ."
     0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x010F [0x0B] ExtData[1]->WorkLocal[14]++
     0x0112 [0x01] GOTO 0x00CF
     0x0115 [0x1B] RETURN
# Dead code (unreachable instructions):
     0x0248 [0x02] IF !(0x0280 == 0x0280) GOTO 0x8001
     0x0250 [0x01] GOTO 0x0180
     0x0253 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147647489/0x80028001))
     0x0258 [0x02] IF !(0x0280 == 0x0280) GOTO 0x8002
     0x0260 [0x01] GOTO 0x0180
     0x0263 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147647489/0x80028001))
     0x0268 [0x02] IF !(0x0C80 == 0x0180) GOTO 0x8001
     0x0270 [0x01] GOTO 0x0180
     0x0273 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147647489/0x80028001))
     0x0278 [0x02] IF !(0x0280 == 0x1480) GOTO 0x8001
     0x0280 [0x01] GOTO 0x0180
     0x0283 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147647489/0x80028001))
     0x0288 [0x02] IF !(0x0280 == 0x0180) GOTO 0x8001
     0x0290 [0x01] GOTO 0x0180
```
