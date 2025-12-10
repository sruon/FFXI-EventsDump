# 17768575 - Curator Moogle

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Heavens Tower (ID: 242) |
| Block Size       | 468 bytes               |
| Total Events     | 2                       |
| References Count | 20                      |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [464](#event-464)     | 0x0001       |    360 |             59 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x25D0      |        9680 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0xFFFFFFFF  |  4294967295 |
|       4 | 0x0008      |           8 |
|       5 | 0x0014      |          20 |
|       6 | 0x25D1      |        9681 |
|       7 | 0x25D5      |        9685 |
|       8 | 0x25D2      |        9682 |
|       9 | 0x0002      |           2 |
|      10 | 0x25D4      |        9684 |
|      11 | 0x0004      |           4 |
|      12 | 0x25D3      |        9683 |
|      13 | 0x0E09      |        3593 |
|      14 | 0x0005      |           5 |
|      15 | 0x5D3A      |       23866 |
|      16 | 0x02EA      |         746 |
|      17 | 0x02CC      |         716 |
|      18 | 0x0A95      |        2709 |
|      19 | 0x15B6      |        5558 |

## String References

- **9680**: Hail, adventurer! Take a look and see if there's anything you like, kupo! No gil necessary, jusst a quick little item in exchange!
- **9682**: If so, then I require that you trade me the following all at once in exchange for the $30.
- **9683**: $ $0 .
- **9684**: $ $0 .
- **9685**: Come again soon, kupo!

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

### Event 464

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 360 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 05 03 00 03   .....op...#....
0010: 04 00 01 80 02 03 00 02  80 00 A2 00 03 00 00 03  ................
0020: 80 03 02 00 01 80 03 0D  00 01 80 02 02 00 02 80  ................
0030: 03 5B 00 3D 00 00 02 00  02 80 9D 00 39 01 01 00  .[.=........9...
0040: 0D 00 9D 05 09 01 01 00  02 00 D4 03 02 00 01 00  ................
0050: 0B 02 00 07 0D 00 04 80  01 2B 00 3D 00 00 05 80  .........+.=....
0060: 02 80 D4 02 06 80 04 00  00 00 25 02 00 10 05 80  ..........%.....
0070: 00 7D 00 1D 07 80 23 06  03 00 01 9F 00 02 00 10  .}....#.........
0080: 05 80 03 9C 00 03 04 00  00 10 9D 00 09 01 16 17  ................
0090: 04 00 1D 08 80 23 1A A4  00 01 9F 00 06 03 00 01  .....#..........
00A0: 14 00 21 00 03 0D 00 04  00 14 0D 00 04 80 07 0D  ..!.............
00B0: 00 09 80 9D 00 39 01 10  00 0D 00 03 0E 00 01 80  .....9..........
00C0: 03 18 00 01 80 02 0E 00  10 00 03 08 01 9D 00 49  ...............I
00D0: 01 17 17 18 00 9D 00 59  01 18 17 18 00 0B 18 00  .......Y........
00E0: 02 18 00 10 00 00 EF 00  48 0A 80 23 01 02 01 02  ........H..#....
00F0: 18 00 0B 80 00 FE 00 48  0A 80 23 01 02 01 48 0C  .......H..#...H.
0100: 80 23 0B 0E 00 01 C5 00  1B 02 10 03 10 04 10 05  .#..............
0110: 10 06 10 07 10 08 10 09  10 00 17 01 17 02 17 03  ................
0120: 17 04 17 05 17 06 17 07  17 08 17 09 17 0A 17 0B  ................
0130: 17 0C 17 0D 17 0E 17 0F  17 0D 80 02 80 0E 80 01  ................
0140: 80 01 80 01 80 01 80 01  80 0F 80 10 80 11 80 12  ................
0150: 80 13 80 01 80 01 80 01  80 02 80 02 80 02 80 02  ................
0160: 80 02 80 01 80 01 80 01  80                       .........       
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=9680*)
    → "Hail, adventurer! Take a look and see if there's anything you like, kupo! No gil necessary, jusst a quick little item in exchange!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x05] ExtData[1]->WorkLocal[3] = 1
  6: 0x000F [0x03] ExtData[1]->WorkLocal[4] = 0*
  7: 0x0014 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x00A2
  8: 0x001C [0x03] ExtData[1]->WorkLocal[0] = 4294967295*
  9: 0x0021 [0x03] ExtData[1]->WorkLocal[2] = 0*
 10: 0x0026 [0x03] ExtData[1]->WorkLocal[13] = 0*
 11: 0x002B [0x02] IF !(ExtData[1]->WorkLocal[2] >= 1*) GOTO 0x005B
 12: 0x0033 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=ExtData[1]->WorkLocal[2], condition_work_offset=1*)
 13: 0x003A [0x9D] ExtData[1]->WorkLocal[1] = 0x0139[ExtData[1]->WorkLocal[13]] // Read WORD
 14: 0x0042 [0x9D] 0x0109[ExtData[1]->WorkLocal[2] * 2] = ExtData[1]->WorkLocal[1] // Write WORD
 15: 0x004A [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[02 00 01 00 0B 02 00 07...])
 16: 0x0068 [0x00] END_REQSTACK()
 17: 0x0069 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Data Section: 0x0109 (96 bytes)
     0x0109: 02 10 03 10 04 10 05 10 06 10 07 10 08 10 09 10
     0x0119: 00 17 01 17 02 17 03 17 04 17 05 17 06 17 07 17
     0x0129: 08 17 09 17 0A 17 0B 17 0C 17 0D 17 0E 17 0F 17
     0x0139: 0D 80 02 80 0E 80 01 80 01 80 01 80 01 80 01 80
     0x0149: 0F 80 10 80 11 80 12 80 13 80 01 80 01 80 01 80
     0x0159: 02 80 02 80 02 80 02 80 02 80 01 80 01 80 01 80
# Dead code (unreachable instructions):
     0x006A [0x25] WAIT_DIALOG_SELECT()
     0x006B [0x02] IF !(Work_Zone[0] == 20*) GOTO 0x007D
     0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=9685*)
    → "Come again soon, kupo!"
     0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0077 [0x06] ExtData[1]->WorkLocal[3] = 0
     0x007A [0x01] GOTO 0x009F
     0x007D [0x02] IF !(Work_Zone[0] >= 20*) GOTO 0x009C
     0x0085 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
     0x008A [0x9D] Work_Zone_1700[22] = 0x0109[ExtData[1]->WorkLocal[4]] // Read WORD
     0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=9682*)
    → "If so, then I require that you trade me the following all at once in exchange for the $30."
     0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0096 [0x1A] CALL_SUBROUTINE(address=0x00A4)
     0x0099 [0x01] GOTO 0x009F
     0x009C [0x06] ExtData[1]->WorkLocal[3] = 0
     0x009F [0x01] GOTO 0x0014
     0x00A4 [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[4]
     0x00A9 [0x14] ExtData[1]->WorkLocal[13] *= 8*
     0x00AE [0x07] ExtData[1]->WorkLocal[13] += 2*
     0x00B3 [0x9D] ExtData[1]->WorkLocal[16] = 0x0139[ExtData[1]->WorkLocal[13]] // Read WORD
     0x00BB [0x03] ExtData[1]->WorkLocal[14] = 0*
     0x00C0 [0x03] ExtData[1]->WorkLocal[24] = 0*
     0x00C5 [0x02] IF !(ExtData[1]->WorkLocal[14] >= ExtData[1]->WorkLocal[16]) GOTO 0x0108
     0x00CD [0x9D] Work_Zone_1700[23] = 0x0149[ExtData[1]->WorkLocal[24]] // Read WORD
     0x00D5 [0x9D] Work_Zone_1700[24] = 0x0159[ExtData[1]->WorkLocal[24]] // Read WORD
     0x00DD [0x0B] ExtData[1]->WorkLocal[24]++
     0x00E0 [0x02] IF !(ExtData[1]->WorkLocal[24] == ExtData[1]->WorkLocal[16]) GOTO 0x00EF
     0x00E8 [0x48] [System] [9684*]:
    → "$ $0 ."
     0x00EB [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00EC [0x01] GOTO 0x0102
     0x00EF [0x02] IF !(ExtData[1]->WorkLocal[24] == 4*) GOTO 0x00FE
     0x00F7 [0x48] [System] [9684*]:
    → "$ $0 ."
     0x00FA [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x00FB [0x01] GOTO 0x0102
     0x00FE [0x48] [System] [9683*]:
    → "$ $0 ."
     0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0102 [0x0B] ExtData[1]->WorkLocal[14]++
     0x0105 [0x01] GOTO 0x00C5
     0x0108 [0x1B] RETURN
```
