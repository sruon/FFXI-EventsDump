# 17952898 - Legion Libretto

## Common Data

| Field            | Value                               |
|------------------|-------------------------------------|
| Zone             | Maquette Abdhaljs-LegionB (ID: 287) |
| Block Size       | 680 bytes                           |
| Total Events     | 2                                   |
| References Count | 19                                  |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1500](#event-1500)   | 0x0001       |    578 |            128 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C62      |        7266 |
|       1 | 0x0000      |           0 |
|       2 | 0x1C63      |        7267 |
|       3 | 0x40000000  |  1073741824 |
|       4 | 0x0009      |           9 |
|       5 | 0x000A      |          10 |
|       6 | 0x000F      |          15 |
|       7 | 0x00FE      |         254 |
|       8 | 0x0010      |          16 |
|       9 | 0x001F      |          31 |
|      10 | 0x1C64      |        7268 |
|      11 | 0x0001      |           1 |
|      12 | 0x0008      |           8 |
|      13 | 0x0002      |           2 |
|      14 | 0x0003      |           3 |
|      15 | 0x0004      |           4 |
|      16 | 0x0005      |           5 |
|      17 | 0x0006      |           6 |
|      18 | 0x0007      |           7 |

## String References

- **7266**: The tome contains the symphonic scores for a veritable host of rousing battle fanfares.
- **7267**: Select a new battle fanfare? [Not now./Belief./Fighters of the Crystal./Conflict: March of the Hero./The Colosseum./Run Maggot, Run!/Iron Colossus./Ragnarok./Feast of the Ladies./Random selection./Restore default./@]
- **7268**: Fight to this fanfare? [Yes./No, select another.]

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

### Event 1500

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 578 bytes |
| Instructions | 112       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 03  00 03 10 48 00 80 23 05   ..........H..#.
0010: 02 00 02 02 00 01 80 02  DF 00 24 02 80 00 00 03  ..........$.....
0020: 00 25 02 00 10 01 80 00  35 00 03 01 10 03 80 06  .%......5.......
0030: 02 00 01 35 00 42 03 01  00 00 10 02 01 00 01 80  ...5.B..........
0040: 02 DC 00 02 01 00 04 80  80 56 00 03 00 00 01 00  .........V......
0050: 1A E1 00 01 6B 00 02 01  00 05 80 80 6B 00 03 00  ....k.......k...
0060: 00 01 80 03 01 00 01 80  01 6B 00 40 01 80 06 80  .........k.@....
0070: 01 10 07 80 40 08 80 09  80 01 10 01 00 43 00 43  ....@........C.C
0080: 01 06 01 10 24 0A 80 01  80 01 80 25 02 00 10 01  ....$......%....
0090: 80 00 B1 00 40 01 80 06  80 01 10 07 80 40 08 80  ....@........@..
00A0: 09 80 01 10 01 00 03 00  00 01 00 06 02 00 01 DC  ................
00B0: 00 02 00 10 0B 80 00 DC  00 02 01 00 01 80 00 C6  ................
00C0: 00 03 01 00 05 80 02 00  00 04 80 00 D3 00 03 01  ................
00D0: 00 04 80 03 00 00 01 00  2E 01 DC 00 01 12 00 21  ...............!
00E0: 00 03 04 00 0C 80 06 01  00 3E 03 00 0B 80 F3 00  .........>......
00F0: 0C 04 00 3E 03 00 0D 80  FD 00 0C 04 00 3E 03 00  ...>.........>..
0100: 0E 80 07 01 0C 04 00 3E  03 00 0F 80 11 01 0C 04  .......>........
0110: 00 3E 03 00 10 80 1B 01  0C 04 00 3E 03 00 11 80  .>.........>....
0120: 25 01 0C 04 00 3E 03 00  12 80 2F 01 0C 04 00 3E  %....>..../....>
0130: 03 00 0C 80 39 01 0C 04  00 02 04 00 01 80 00 47  ....9..........G
0140: 01 06 01 00 01 42 02 0C  04 00 06 01 00 13 01 00  .....B..........
0150: 04 00 3E 03 00 0B 80 5C  01 01 70 01 02 01 00 01  ..>....\..p.....
0160: 80 00 6D 01 03 01 00 0B  80 1B 01 70 01 0C 01 00  ..m........p....
0170: 3E 03 00 0D 80 7A 01 01  8E 01 02 01 00 01 80 00  >....z..........
0180: 8B 01 03 01 00 0D 80 1B  01 8E 01 0C 01 00 3E 03  ..............>.
0190: 00 0E 80 98 01 01 AC 01  02 01 00 01 80 00 A9 01  ................
01A0: 03 01 00 0E 80 1B 01 AC  01 0C 01 00 3E 03 00 0F  ............>...
01B0: 80 B6 01 01 CA 01 02 01  00 01 80 00 C7 01 03 01  ................
01C0: 00 0F 80 1B 01 CA 01 0C  01 00 3E 03 00 10 80 D4  ..........>.....
01D0: 01 01 E8 01 02 01 00 01  80 00 E5 01 03 01 00 10  ................
01E0: 80 1B 01 E8 01 0C 01 00  3E 03 00 11 80 F2 01 01  ........>.......
01F0: 06 02 02 01 00 01 80 00  03 02 03 01 00 11 80 1B  ................
0200: 01 06 02 0C 01 00 3E 03  00 12 80 10 02 01 24 02  ......>.......$.
0210: 02 01 00 01 80 00 21 02  03 01 00 12 80 1B 01 24  ......!........$
0220: 02 0C 01 00 3E 03 00 0C  80 2E 02 01 42 02 02 01  ....>.......B...
0230: 00 01 80 00 3F 02 03 01  00 0C 80 1B 01 42 02 06  ....?........B..
0240: 01 00 1B                                          ...             
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[3]
  2: 0x000B [0x48] [System] [7266*]:
    → "The tome contains the symphonic scores for a veritable host of rousing battle fanfares."
  3: 0x000E [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000F [0x05] ExtData[1]->WorkLocal[2] = 1
  5: 0x0012 [0x02] IF !(ExtData[1]->WorkLocal[2] <= 0*) GOTO 0x00DF
  6: 0x001A [0x24] CREATE_DIALOG(message_id=7267*, default_option=ExtData[1]->WorkLocal[0], option_flags=ExtData[1]->WorkLocal[3])
    → "Select a new battle fanfare? [Not now./Belief./Fighters of the Crystal./Conflict: March of the Hero./The Colosseum./Run Maggot, Run!/Iron Colossus./Ragnarok./Feast of the Ladies./Random selection./Restore default./@]"
  7: 0x0021 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0022 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0035
  9: 0x002A [0x03] Work_Zone[1] = 1073741824*
 10: 0x002F [0x06] ExtData[1]->WorkLocal[2] = 0
 11: 0x0032 [0x01] GOTO 0x0035

SUBROUTINE_0035:
 12: 0x0035 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 13: 0x0036 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[0]
 14: 0x003B [0x02] IF !(ExtData[1]->WorkLocal[1] <= 0*) GOTO 0x00DC
 15: 0x0043 [0x02] IF !(ExtData[1]->WorkLocal[1] == 9*) GOTO 0x0056
 16: 0x004B [0x03] ExtData[1]->WorkLocal[0] = ExtData[1]->WorkLocal[1]
 17: 0x0050 [0x1A] CALL_SUBROUTINE(address=0x00E1)
 18: 0x0053 [0x01] GOTO 0x006B
 19: 0x0056 [0x02] IF !(ExtData[1]->WorkLocal[1] == 10*) GOTO 0x006B
 20: 0x005E [0x03] ExtData[1]->WorkLocal[0] = 0*
 21: 0x0063 [0x03] ExtData[1]->WorkLocal[1] = 0*
 22: 0x0068 [0x01] GOTO 0x006B

SUBROUTINE_006B:
 23: 0x006B [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=254*)
 24: 0x0074 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 25: 0x007D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 26: 0x007F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 27: 0x0081 [0x06] Work_Zone[1] = 0
 28: 0x0084 [0x24] CREATE_DIALOG(message_id=7268*, default_option=0*, option_flags=0*)
    → "Fight to this fanfare? [Yes./No, select another.]"
 29: 0x008B [0x25] WAIT_DIALOG_SELECT()
 30: 0x008C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00B1
 31: 0x0094 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=254*)
 32: 0x009D [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[1])
 33: 0x00A6 [0x03] ExtData[1]->WorkLocal[0] = ExtData[1]->WorkLocal[1]
 34: 0x00AB [0x06] ExtData[1]->WorkLocal[2] = 0
 35: 0x00AE [0x01] GOTO 0x00DC
 36: 0x00B1 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00DC
 37: 0x00B9 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00C6
 38: 0x00C1 [0x03] ExtData[1]->WorkLocal[1] = 10*
 39: 0x00C6 [0x02] IF !(ExtData[1]->WorkLocal[0] == 9*) GOTO 0x00D3
 40: 0x00CE [0x03] ExtData[1]->WorkLocal[1] = 9*
 41: 0x00D3 [0x03] ExtData[1]->WorkLocal[0] = ExtData[1]->WorkLocal[1]
 42: 0x00D8 [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 43: 0x00D9 [0x01] GOTO 0x00DC

SUBROUTINE_00DC:
 44: 0x00DC [0x01] GOTO 0x0012
 45: 0x00DF [0x21] END_EVENT
 46: 0x00E0 [0x00] END_REQSTACK()

SUBROUTINE_00E1:
 47: 0x00E1 [0x03] ExtData[1]->WorkLocal[4] = 8*
 48: 0x00E6 [0x06] ExtData[1]->WorkLocal[1] = 0
 49: 0x00E9 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 1*) GOTO 0x00F3
 50: 0x00F0 [0x0C] ExtData[1]->WorkLocal[4]--
 51: 0x00F3 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 2*) GOTO 0x00FD
 52: 0x00FA [0x0C] ExtData[1]->WorkLocal[4]--
 53: 0x00FD [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 3*) GOTO 0x0107
 54: 0x0104 [0x0C] ExtData[1]->WorkLocal[4]--
 55: 0x0107 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 4*) GOTO 0x0111
 56: 0x010E [0x0C] ExtData[1]->WorkLocal[4]--
 57: 0x0111 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 5*) GOTO 0x011B
 58: 0x0118 [0x0C] ExtData[1]->WorkLocal[4]--
 59: 0x011B [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 6*) GOTO 0x0125
 60: 0x0122 [0x0C] ExtData[1]->WorkLocal[4]--
 61: 0x0125 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 7*) GOTO 0x012F
 62: 0x012C [0x0C] ExtData[1]->WorkLocal[4]--
 63: 0x012F [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 8*) GOTO 0x0139
 64: 0x0136 [0x0C] ExtData[1]->WorkLocal[4]--
 65: 0x0139 [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x0147
 66: 0x0141 [0x06] ExtData[1]->WorkLocal[1] = 0
 67: 0x0144 [0x01] GOTO 0x0242
 68: 0x0147 [0x0C] ExtData[1]->WorkLocal[4]--
 69: 0x014A [0x06] ExtData[1]->WorkLocal[1] = 0
 70: 0x014D [0x13] ExtData[1]->WorkLocal[1] = rand() % ExtData[1]->WorkLocal[4]
 71: 0x0152 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 1*) GOTO 0x015C
 72: 0x0159 [0x01] GOTO 0x0170
 73: 0x015C [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x016D
 74: 0x0164 [0x03] ExtData[1]->WorkLocal[1] = 1*
 75: 0x0169 [0x1B] RETURN

SUBROUTINE_0170:
 76: 0x0170 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 2*) GOTO 0x017A
 77: 0x0177 [0x01] GOTO 0x018E
 78: 0x017A [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x018B
 79: 0x0182 [0x03] ExtData[1]->WorkLocal[1] = 2*
 80: 0x0187 [0x1B] RETURN

SUBROUTINE_018E:
 81: 0x018E [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 3*) GOTO 0x0198
 82: 0x0195 [0x01] GOTO 0x01AC
 83: 0x0198 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x01A9
 84: 0x01A0 [0x03] ExtData[1]->WorkLocal[1] = 3*
 85: 0x01A5 [0x1B] RETURN

SUBROUTINE_01AC:
 86: 0x01AC [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 4*) GOTO 0x01B6
 87: 0x01B3 [0x01] GOTO 0x01CA
 88: 0x01B6 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x01C7
 89: 0x01BE [0x03] ExtData[1]->WorkLocal[1] = 4*
 90: 0x01C3 [0x1B] RETURN

SUBROUTINE_01CA:
 91: 0x01CA [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 5*) GOTO 0x01D4
 92: 0x01D1 [0x01] GOTO 0x01E8
 93: 0x01D4 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x01E5
 94: 0x01DC [0x03] ExtData[1]->WorkLocal[1] = 5*
 95: 0x01E1 [0x1B] RETURN

SUBROUTINE_01E8:
 96: 0x01E8 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 6*) GOTO 0x01F2
 97: 0x01EF [0x01] GOTO 0x0206
 98: 0x01F2 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0203
 99: 0x01FA [0x03] ExtData[1]->WorkLocal[1] = 6*
100: 0x01FF [0x1B] RETURN

SUBROUTINE_0206:
101: 0x0206 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 7*) GOTO 0x0210
102: 0x020D [0x01] GOTO 0x0224
103: 0x0210 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0221
104: 0x0218 [0x03] ExtData[1]->WorkLocal[1] = 7*
105: 0x021D [0x1B] RETURN

SUBROUTINE_0224:
106: 0x0224 [0x3E] IF !(ExtData[1]->WorkLocal[3] bit 8*) GOTO 0x022E
107: 0x022B [0x01] GOTO 0x0242
108: 0x022E [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x023F
109: 0x0236 [0x03] ExtData[1]->WorkLocal[1] = 8*
110: 0x023B [0x1B] RETURN

SUBROUTINE_0242:
111: 0x0242 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x016A [0x01] GOTO 0x0170
# Dead code (unreachable instructions):
     0x0188 [0x01] GOTO 0x018E
# Dead code (unreachable instructions):
     0x01A6 [0x01] GOTO 0x01AC
# Dead code (unreachable instructions):
     0x01C4 [0x01] GOTO 0x01CA
# Dead code (unreachable instructions):
     0x01E2 [0x01] GOTO 0x01E8
# Dead code (unreachable instructions):
     0x0200 [0x01] GOTO 0x0206
# Dead code (unreachable instructions):
     0x021E [0x01] GOTO 0x0224
# Dead code (unreachable instructions):
     0x023C [0x01] GOTO 0x0242
```
