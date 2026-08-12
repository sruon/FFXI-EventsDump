# 17744185 - Phantom gems Box

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 572 bytes             |
| Total Events     | 2                     |
| References Count | 41                    |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [481](#event-481)     | 0x0001       |    380 |             73 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000A      |          10 |
|       1 | 0x0000      |           0 |
|       2 | 0x001A      |          26 |
|       3 | 0x0001      |           1 |
|       4 | 0x001B      |          27 |
|       5 | 0x001C      |          28 |
|       6 | 0x001D      |          29 |
|       7 | 0x001E      |          30 |
|       8 | 0x342E      |       13358 |
|       9 | 0x0019      |          25 |
|      10 | 0x342F      |       13359 |
|      11 | 0x001F      |          31 |
|      12 | 0x000F      |          15 |
|      13 | 0x0010      |          16 |
|      14 | 0x3430      |       13360 |
|      15 | 0x09A4      |        2468 |
|      16 | 0x09A6      |        2470 |
|      17 | 0x09A5      |        2469 |
|      18 | 0x09A7      |        2471 |
|      19 | 0x09A8      |        2472 |
|      20 | 0x09A9      |        2473 |
|      21 | 0x09AA      |        2474 |
|      22 | 0x09AB      |        2475 |
|      23 | 0x09AC      |        2476 |
|      24 | 0x09F1      |        2545 |
|      25 | 0x09F2      |        2546 |
|      26 | 0x09FC      |        2556 |
|      27 | 0x09FD      |        2557 |
|      28 | 0x0A23      |        2595 |
|      29 | 0x0A3B      |        2619 |
|      30 | 0x0B6B      |        2923 |
|      31 | 0x0B6C      |        2924 |
|      32 | 0x0B6D      |        2925 |
|      33 | 0x0BAB      |        2987 |
|      34 | 0x0BAC      |        2988 |
|      35 | 0x0C71      |        3185 |
|      36 | 0x0C72      |        3186 |
|      37 | 0x0C73      |        3187 |
|      38 | 0x0C74      |        3188 |
|      39 | 0x0CBD      |        3261 |
|      40 | 0x0D1C      |        3356 |

## String References

- **13358**: Select a phantom gem to receive.
- **13359**: Which would you like? ($31 left) [3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./Never mind.]
- **13360**: Receive the $3? [Yes./No.]

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

### Event 481

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 380 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 01 00 02 10 03 04  00 03 10 2C F8 FF FF 7F   ..........,....
0010: F8 FF FF 7F 6F 70 65 6E  1C 00 80 03 00 00 01 80  ....open........
0020: 3C 00 00 02 80 03 80 3C  00 00 04 80 03 80 3C 00  <......<......<.
0030: 00 05 80 03 80 3C 00 00  06 80 03 80 3C 00 00 07  .....<......<...
0040: 80 03 80 03 06 00 01 80  48 08 80 23 03 02 00 01  ........H..#....
0050: 80 03 05 00 02 80 0C 05  00 02 02 00 09 80 05 8C  ................
0060: 00 3E 01 00 02 00 7F 00  9D 0A FD 00 03 00 02 00  .>..............
0070: 02 80 9D 0F 3D 01 03 00  02 00 02 80 01 86 00 3C  ....=..........<
0080: 00 00 02 00 03 80 0B 02  00 01 59 00 03 17 17 04  ..........Y.....
0090: 00 24 0A 80 06 00 00 00  25 02 00 10 0B 80 00 A9  .$......%.......
00A0: 00 03 01 10 01 80 01 C0  00 03 06 00 00 10 40 01  ..............@.
00B0: 80 0C 80 01 10 00 10 40  0D 80 0B 80 01 10 03 80  .......@........
00C0: 02 01 10 01 80 00 CB 00  01 FB 00 9D 0A FD 00 02  ................
00D0: 10 00 10 02 80 24 0E 80  03 80 01 80 25 02 00 10  .....$......%...
00E0: 01 80 00 E8 00 01 FB 00  02 00 10 03 80 00 FB 00  ................
00F0: 03 01 10 01 80 01 4C 00  01 FB 00 21 00 0F 80 10  ......L....!....
0100: 80 11 80 12 80 13 80 14  80 15 80 16 80 17 80 18  ................
0110: 80 19 80 1A 80 1B 80 1C  80 1D 80 1E 80 1F 80 20  ............... 
0120: 80 21 80 22 80 23 80 24  80 25 80 26 80 27 80 28  .!.".#.$.%.&.'.(
0130: 80 01 80 01 80 01 80 01  80 01 80 01 80 02 10 03  ................
0140: 10 04 10 05 10 06 10 07  10 08 10 09 10 00 17 01  ................
0150: 17 02 17 03 17 04 17 05  17 06 17 07 17 08 17 09  ................
0160: 17 0A 17 0B 17 0C 17 0D  17 0E 17 0F 17 10 17 11  ................
0170: 17 12 17 13 17 14 17 15  17 16 17 01 80           .............   
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[3]
  2: 0x000B [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "open" with entities [EventEntity, EventEntity]
  3: 0x0018 [0x1C] WAIT(10* ticks)
  4: 0x001B [0x03] ExtData[1]->WorkLocal[0] = 0*
  5: 0x0020 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=26*, condition_work_offset=1*)
  6: 0x0027 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=27*, condition_work_offset=1*)
  7: 0x002E [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=28*, condition_work_offset=1*)
  8: 0x0035 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=29*, condition_work_offset=1*)
  9: 0x003C [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=30*, condition_work_offset=1*)
 10: 0x0043 [0x03] ExtData[1]->WorkLocal[6] = 0*
 11: 0x0048 [0x48] [System] [13358*]:
    → "Select a phantom gem to receive."
 12: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x004C [0x03] ExtData[1]->WorkLocal[2] = 0*
 14: 0x0051 [0x03] ExtData[1]->WorkLocal[5] = 26*
 15: 0x0056 [0x0C] ExtData[1]->WorkLocal[5]--
 16: 0x0059 [0x02] IF !(ExtData[1]->WorkLocal[2] > 25*) GOTO 0x008C
 17: 0x0061 [0x3E] IF !(ExtData[1]->WorkLocal[1] bit ExtData[1]->WorkLocal[2]) GOTO 0x007F
 18: 0x0068 [0x9D] IF (0xFD) ExtData[1]->WorkLocal[2] = ExtData[1]->WorkLocal[3] // extra=0x8002
 19: 0x0072 [0x9D] Table[0x013D] = ExtData[1]->WorkLocal[3] // p3=ExtData[1]->WorkLocal[2], p4=0x8002
 20: 0x007C [0x01] GOTO 0x0086
 21: 0x007F [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=ExtData[1]->WorkLocal[2], condition_work_offset=1*)

SUBROUTINE_0086:
 22: 0x0086 [0x0B] ExtData[1]->WorkLocal[2]++
 23: 0x0089 [0x01] GOTO 0x0059
 24: 0x008C [0x03] Work_Zone_1700[23] = ExtData[1]->WorkLocal[4]
 25: 0x0091 [0x24] CREATE_DIALOG(message_id=13359*, default_option=ExtData[1]->WorkLocal[6], option_flags=ExtData[1]->WorkLocal[0])
    → "Which would you like? ($31 left) [3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./$3./Never mind.]"
 26: 0x0098 [0x25] WAIT_DIALOG_SELECT()
 27: 0x0099 [0x02] IF !(Work_Zone[0] == 31*) GOTO 0x00A9
 28: 0x00A1 [0x03] Work_Zone[1] = 0*
 29: 0x00A6 [0x01] GOTO 0x00C0
 30: 0x00A9 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[0]
 31: 0x00AE [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=Work_Zone[0])
 32: 0x00B7 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=1*)

SUBROUTINE_00C0:
 33: 0x00C0 [0x02] IF !(Work_Zone[1] == 0*) GOTO 0x00CB
 34: 0x00C8 [0x01] GOTO 0x00FB
 35: 0x00CB [0x9D] IF (0xFD) Work_Zone[0] = Work_Zone[2] // extra=0x8002
 36: 0x00D5 [0x24] CREATE_DIALOG(message_id=13360*, default_option=1*, option_flags=0*)
    → "Receive the $3? [Yes./No.]"
 37: 0x00DC [0x25] WAIT_DIALOG_SELECT()
 38: 0x00DD [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00E8
 39: 0x00E5 [0x01] GOTO 0x00FB
 40: 0x00E8 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00FB
 41: 0x00F0 [0x03] Work_Zone[1] = 0*
 42: 0x00F5 [0x01] GOTO 0x004C

SUBROUTINE_00FB:
 43: 0x00FB [0x21] END_EVENT
 44: 0x00FC [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x00F8 [0x01] GOTO 0x00FB
# Dead code (unreachable instructions):
     0x00FD [0x0F] 0x1080 ^= 0x1180
     0x0102 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148761618/0x80138012))
     0x0107 [0x14] 0x1580 *= 0x1680
     0x010C [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149089303/0x80188017))
     0x0111 [0x19] SWAP(0x1A80, 0x1B80)
     0x0116 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149416988/0x801D801C))
     0x011B [0x1E] EventEntity looks at Unknown NPC (ID: 545267584/0x20801F80) and starts talking
     0x0120 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149744673/0x80228021))
     0x0125 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0126 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149941284/0x80258024))
     0x012B [0x26] DEPRECATED_YIELD
     0x012C [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2150137895/0x80288027))
     0x0131 [0x01] GOTO 0x0180
     0x0134 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x0139 [0x01] GOTO 0x0180
     0x013C [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 268636162/0x10031002))
     0x0141 [0x04] DEPRECATED_NOP(unused=0x0510)
     0x0144 [0x10] Work_Zone[6] <<= Work_Zone[7]
     0x0149 [0x08] 0x0910 -= ExtData[1]->WorkLocal[16]
     0x014E [0x17] Work_Zone_1700[1] = cos(Work_Zone_1700[2]) * Work_Zone_1700[3]
     0x0155 [0x04] DEPRECATED_NOP(unused=0x0517)
     0x0158 [0x17] Work_Zone_1700[6] = cos(Work_Zone_1700[7]) * Work_Zone_1700[8]
     0x015F [0x09] 0x0A17 |= (1 << 0x0B17)
     0x0164 [0x17] Work_Zone_1700[12] = cos(Work_Zone_1700[13]) * Work_Zone_1700[14]
     0x016B [0x0F] Work_Zone[23] ^= Work_Zone_Memorize[23]
     0x0170 [0x17] Work_Zone_1700[18] = cos(Work_Zone_1700[19]) * Work_Zone_1700[20]
     0x0177 [0x15] 0x1617 /= 0x0117
```
