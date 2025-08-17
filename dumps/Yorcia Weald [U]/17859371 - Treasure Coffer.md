# 17859371 - Treasure Coffer

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Yorcia Weald [U] (ID: 264) |
| Block Size       | 436 bytes                  |
| Total Events     | 2                          |
| References Count | 10                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      6 |              2 |
| [2011](#event-2011)   | 0x0006       |    364 |             67 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x000F      |          15 |
|       3 | 0x0010      |          16 |
|       4 | 0x001F      |          31 |
|       5 | 0x1CCC      |        7372 |
|       6 | 0x000B      |          11 |
|       7 | 0x1CCD      |        7373 |
|       8 | 0x1CCE      |        7374 |
|       9 | 0xFFFFFFFF  |  4294967295 |

## String References

- **7372**: Which will you obtain? [Nothing./#./$1./$2./$3./$4./$5./$6./$7./$8./$9./All the spoils!]
- **7373**: Obtain this item?
- **7374**: Obtain the $0? [Yes./No.]

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 00 00 00 80 00                                 ......          
```

#### Opcodes

```
  0: 0x0000 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 2011

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0006    |
| Data Size    | 364 bytes |
| Instructions | 66        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   41 01  80 02 80 02 10 01 00 41        A........A
0010: 03 80 04 80 02 10 02 00  41 01 80 02 80 03 10 03  ........A.......
0020: 00 41 03 80 04 80 03 10  04 00 41 01 80 02 80 04  .A........A.....
0030: 10 05 00 41 03 80 04 80  04 10 06 00 41 01 80 02  ...A........A...
0040: 80 05 10 07 00 41 03 80  04 80 05 10 08 00 41 01  .....A........A.
0050: 80 02 80 06 10 09 00 41  03 80 04 80 06 10 0A 00  .......A........
0060: 1A 34 01 06 0B 00 02 0B  00 01 80 00 32 01 03 02  .4..........2...
0070: 10 01 00 03 03 10 02 00  03 04 10 03 00 03 05 10  ................
0080: 04 00 03 06 10 05 00 03  07 10 06 00 03 08 10 07  ................
0090: 00 03 09 10 08 00 03 00  17 09 00 03 01 17 0A 00  ................
00A0: 24 05 80 01 80 0C 00 25  02 00 10 01 80 00 B6 00  $......%........
00B0: 05 0B 00 01 B6 00 02 0B  00 01 80 00 2F 01 03 0D  ............/...
00C0: 00 00 10 02 0D 00 06 80  03 15 01 0C 0D 00 9D 00  ................
00D0: 52 01 0E 00 0D 00 93 0E  00 48 07 80 23 93 01 80  R........H..#...
00E0: 0B 0D 00 03 02 10 0E 00  24 08 80 00 80 01 80 25  ........$......%
00F0: 02 00 10 01 80 00 12 01  03 01 10 0D 00 43 00 43  .............C.C
0100: 01 1A 34 01 02 09 10 00  80 00 0F 01 05 0B 00 01  ..4.............
0110: 12 01 01 2F 01 03 01 10  0D 00 43 00 43 01 02 09  .../......C.C...
0120: 10 00 80 00 2C 01 05 0B  00 01 2F 01 05 0B 00 01  ....,...../.....
0130: 66 00 21 00 03 0C 00 08  10 10 0C 00 00 80 0F 0C  f.!.............
0140: 00 09 80 3D 0C 00 01 80  00 80 3D 0C 00 06 80 00  ...=......=.....
0150: 80 1B 01 00 02 00 03 00  04 00 05 00 06 00 07 00  ................
0160: 08 00 09 00 0A 00 01 80  01 80 01 80 01 80 01 80  ................
0170: 01 80                                             ..              
```

#### Opcodes

```
  0: 0x0006 [0x41] ExtData[1]->WorkLocal[1] = Work_Zone[2] (bits 0*-15*)
  1: 0x000F [0x41] ExtData[1]->WorkLocal[2] = Work_Zone[2] (bits 16*-31*)
  2: 0x0018 [0x41] ExtData[1]->WorkLocal[3] = Work_Zone[3] (bits 0*-15*)
  3: 0x0021 [0x41] ExtData[1]->WorkLocal[4] = Work_Zone[3] (bits 16*-31*)
  4: 0x002A [0x41] ExtData[1]->WorkLocal[5] = Work_Zone[4] (bits 0*-15*)
  5: 0x0033 [0x41] ExtData[1]->WorkLocal[6] = Work_Zone[4] (bits 16*-31*)
  6: 0x003C [0x41] ExtData[1]->WorkLocal[7] = Work_Zone[5] (bits 0*-15*)
  7: 0x0045 [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[5] (bits 16*-31*)
  8: 0x004E [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[6] (bits 0*-15*)
  9: 0x0057 [0x41] ExtData[1]->WorkLocal[10] = Work_Zone[6] (bits 16*-31*)
 10: 0x0060 [0x1A] CALL_SUBROUTINE(address=0x0134)
 11: 0x0063 [0x06] ExtData[1]->WorkLocal[11] = 0
 12: 0x0066 [0x02] IF !(ExtData[1]->WorkLocal[11] == 0*) GOTO 0x0132
 13: 0x006E [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 14: 0x0073 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[2]
 15: 0x0078 [0x03] Work_Zone[4] = ExtData[1]->WorkLocal[3]
 16: 0x007D [0x03] Work_Zone[5] = ExtData[1]->WorkLocal[4]
 17: 0x0082 [0x03] Work_Zone[6] = ExtData[1]->WorkLocal[5]
 18: 0x0087 [0x03] Work_Zone[7] = ExtData[1]->WorkLocal[6]
 19: 0x008C [0x03] Work_Zone[8] = ExtData[1]->WorkLocal[7]
 20: 0x0091 [0x03] Work_Zone[9] = ExtData[1]->WorkLocal[8]
 21: 0x0096 [0x03] Work_Zone_1700[0] = ExtData[1]->WorkLocal[9]
 22: 0x009B [0x03] Work_Zone_1700[1] = ExtData[1]->WorkLocal[10]
 23: 0x00A0 [0x24] CREATE_DIALOG(message_id=7372*, default_option=0*, option_flags=ExtData[1]->WorkLocal[12])
    → "Which will you obtain? [Nothing./#./$1./$2./$3./$4./$5./$6./$7./$8./$9./All the spoils!]"
 24: 0x00A7 [0x25] WAIT_DIALOG_SELECT()
 25: 0x00A8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B6
 26: 0x00B0 [0x05] ExtData[1]->WorkLocal[11] = 1
 27: 0x00B3 [0x01] GOTO 0x00B6

SUBROUTINE_00B6:
 28: 0x00B6 [0x02] IF !(ExtData[1]->WorkLocal[11] == 0*) GOTO 0x012F
 29: 0x00BE [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[0]
 30: 0x00C3 [0x02] IF !(ExtData[1]->WorkLocal[13] >= 11*) GOTO 0x0115
 31: 0x00CB [0x0C] ExtData[1]->WorkLocal[13]--
 32: 0x00CE [0x9D] ExtData[1]->WorkLocal[14] = 0x0152[ExtData[1]->WorkLocal[13]] // Read WORD
 33: 0x00D6 [0x93] DISPLAY_ITEM_INFO(item_id=ExtData[1]->WorkLocal[14])
 34: 0x00D9 [0x48] [System] [7373*]:
    → "Obtain this item?"
 35: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00DD [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 37: 0x00E0 [0x0B] ExtData[1]->WorkLocal[13]++
 38: 0x00E3 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[14]
 39: 0x00E8 [0x24] CREATE_DIALOG(message_id=7374*, default_option=1*, option_flags=0*)
    → "Obtain the $0? [Yes./No.]"
 40: 0x00EF [0x25] WAIT_DIALOG_SELECT()
 41: 0x00F0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0112
 42: 0x00F8 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
 43: 0x00FD [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 44: 0x00FF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 45: 0x0101 [0x1A] CALL_SUBROUTINE(address=0x0134)
 46: 0x0104 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x010F
 47: 0x010C [0x05] ExtData[1]->WorkLocal[11] = 1
 48: 0x010F [0x01] GOTO 0x0112

SUBROUTINE_0112:
 49: 0x0112 [0x01] GOTO 0x012F
 50: 0x0115 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
 51: 0x011A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 52: 0x011C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 53: 0x011E [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x012C
 54: 0x0126 [0x05] ExtData[1]->WorkLocal[11] = 1
 55: 0x0129 [0x01] GOTO 0x012F
 56: 0x012C [0x05] ExtData[1]->WorkLocal[11] = 1

SUBROUTINE_012F:
 57: 0x012F [0x01] GOTO 0x0066
 58: 0x0132 [0x21] END_EVENT
 59: 0x0133 [0x00] END_REQSTACK()

SUBROUTINE_0134:
 60: 0x0134 [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[8]
 61: 0x0139 [0x10] ExtData[1]->WorkLocal[12] <<= 1*
 62: 0x013E [0x0F] ExtData[1]->WorkLocal[12] ^= 4294967295*
 63: 0x0143 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[12], bit_index_work_offset=0*, condition_work_offset=1*)
 64: 0x014A [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[12], bit_index_work_offset=11*, condition_work_offset=1*)
 65: 0x0151 [0x1B] RETURN
```

#### Data or dead code:

```
# Data Section: 0x0152 (32 bytes)
     0x0152: 01 00 02 00 03 00 04 00 05 00 06 00 07 00 08 00
     0x0162: 09 00 0A 00 01 80 01 80 01 80 01 80 01 80 01 80
```
