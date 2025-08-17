# 17855007 - Augural Conveyor

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 2148 bytes             |
| Total Events     | 3                      |
| References Count | 52                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [5500](#event-5500)   | 0x0001       |    556 |            120 |
| [5502](#event-5502)   | 0x022D       |   1354 |            291 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0005      |           5 |
|       2 | 0x0001      |           1 |
|       3 | 0x001F      |          31 |
|       4 | 0xFFFFFFFF  |  4294967295 |
|       5 | 0x1EB7      |        7863 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x0010      |          16 |
|       8 | 0x0012      |          18 |
|       9 | 0x000C      |          12 |
|      10 | 0x000F      |          15 |
|      11 | 0x0004      |           4 |
|      12 | 0x000B      |          11 |
|      13 | 0x001D      |          29 |
|      14 | 0x0003      |           3 |
|      15 | 0x1EA3      |        7843 |
|      16 | 0x1EA4      |        7844 |
|      17 | 0x1EAB      |        7851 |
|      18 | 0x1EA6      |        7846 |
|      19 | 0x1EB1      |        7857 |
|      20 | 0x1EB0      |        7856 |
|      21 | 0x0002      |           2 |
|      22 | 0x0006      |           6 |
|      23 | 0x1EB2      |        7858 |
|      24 | 0x1EB3      |        7859 |
|      25 | 0x0325      |         805 |
|      26 | 0x0327      |         807 |
|      27 | 0x0326      |         806 |
|      28 | 0x0008      |           8 |
|      29 | 0x0320      |         800 |
|      30 | 0x0009      |           9 |
|      31 | 0x0103      |         259 |
|      32 | 0x0108      |         264 |
|      33 | 0x010F      |         271 |
|      34 | 0x0113      |         275 |
|      35 | 0x0007      |           7 |
|      36 | 0x1EA8      |        7848 |
|      37 | 0x003C      |          60 |
|      38 | 0x0078      |         120 |
|      39 | 0x1EA5      |        7845 |
|      40 | 0x005A      |          90 |
|      41 | 0x00C9      |         201 |
|      42 | 0x002D      |          45 |
|      43 | 0x00C8      |         200 |
|      44 | 0x000A      |          10 |
|      45 | 0x0107      |         263 |
|      46 | 0x032D      |         813 |
|      47 | 0x0335      |         821 |
|      48 | 0x0336      |         822 |
|      49 | 0x0337      |         823 |
|      50 | 0x032E      |         814 |
|      51 | 0x032F      |         815 |

## String References

- **7843**: Only party members present with you in this area will be transported to [/this skirmish in ////this alluvion skirmish in /]$8.
- **7844**: Proceed? [Yes./No.]
- **7845**: Now entering [/a skirmish in ////an alluvion skirmish in /]$8.
- **7846**: You have chosen not to enter [/this skirmish in ////this alluvion skirmish in /]$8.
- **7848**: You cannot enter at this time. Please wait a moment and try again.
- **7851**: Your request for entry is being considered...
- **7856**: What's the torso's size? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]
- **7857**: What's the visage's obtainment rate? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]
- **7858**: What rank are the legs' benefits? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]
- **7859**: Ready for an alluvion skirmish? [No./Alluvion A./Alluvion B./Alluvion C./Alluvion D./Alluvion E./Just a regular skirmish, please.]
- **7863**: Enter which battlefield? [None./Endeavoring to Awaken./Endeavoring to Awaken./ /Behind the Sluices./Stonewalled./The Gates./Saved by the Bell./Quiescence./The Charlatan./Yggdrasil Beckons./Yggdrasil Beckons./Watery Grave./Mistress of Ceremonies./A Barrel of Laughs./Sinister Reign./The Ygnas Directive 6./Skirmishes./[Fractures/Obscured Domains]./Alluvion skirmishes./The Silent Forest./Wind of Eternity./Phantasmic Heroes.]

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

### Event 5500

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 556 bytes |
| Instructions | 119       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 03 05 00 02 10 06  00 00 06 01 00 06 02 00   B..............
0010: 06 03 00 03 00 00 03 10  03 01 00 04 10 03 02 00  ................
0020: 05 10 03 03 00 06 10 03  12 00 08 10 03 11 00 09  ................
0030: 10 06 01 10 06 10 00 06  06 00 06 07 00 02 12 00  ................
0040: 00 80 02 5D 00 02 03 00  00 80 02 55 00 03 0E 00  ...].......U....
0050: 01 80 01 5A 00 03 0E 00  02 80 01 B5 00 06 0F 00  ...Z............
0060: 40 00 80 03 80 0F 00 04  80 0F 0F 00 11 00 10 0F  @...............
0070: 00 02 80 24 05 80 00 80  0F 00 25 02 00 10 00 80  ...$......%.....
0080: 00 8D 00 03 01 10 06 80  21 00 01 8D 00 03 10 00  ........!.......
0090: 00 10 0C 10 00 02 10 00  07 80 80 A5 00 03 0E 00  ................
00A0: 02 80 01 B5 00 02 10 00  08 80 80 B5 00 03 0E 00  ................
00B0: 01 80 01 B5 00 02 0E 00  02 80 80 36 01 3E 11 00  ...........6.>..
00C0: 08 80 0C 01 03 01 10 00  80 40 09 80 0A 80 01 10  .........@......
00D0: 0B 80 43 00 43 01 03 05  00 02 10 03 00 00 03 10  ..C.C...........
00E0: 03 01 00 04 10 03 02 00  05 10 03 03 00 06 10 1A  ................
00F0: 72 03 40 00 80 0C 80 01  10 06 00 40 07 80 0D 80  r.@........@....
0100: 01 10 07 00 03 0D 00 01  10 01 33 01 1A 72 03 40  ..........3..r.@
0110: 00 80 0C 80 01 10 06 00  40 07 80 0D 80 01 10 07  ........@.......
0120: 00 03 0D 00 01 10 40 09  80 0A 80 01 10 0E 80 43  ......@........C
0130: 00 43 01 01 B7 01 02 0E  00 01 80 80 B7 01 3E 11  .C............>.
0140: 00 07 80 8D 01 03 01 10  00 80 40 09 80 0A 80 01  ..........@.....
0150: 10 01 80 43 00 43 01 03  05 00 02 10 03 00 00 03  ...C.C..........
0160: 10 03 01 00 04 10 03 02  00 05 10 03 03 00 06 10  ................
0170: 1A 72 03 40 00 80 0C 80  01 10 06 00 40 07 80 0D  .r.@........@...
0180: 80 01 10 07 00 03 0D 00  01 10 01 B4 01 1A 72 03  ..............r.
0190: 40 00 80 0C 80 01 10 06  00 40 07 80 0D 80 01 10  @........@......
01A0: 07 00 03 0D 00 01 10 40  09 80 0A 80 01 10 0E 80  .......@........
01B0: 43 00 43 01 01 B7 01 06  04 00 05 08 00 02 04 00  C.C.............
01C0: 00 80 00 0E 02 1A 10 02  03 03 10 0E 00 48 0F 80  .............H..
01D0: 23 24 10 80 08 00 00 80  25 02 00 10 00 80 00 ED  #$......%.......
01E0: 01 06 08 00 48 11 80 1A  78 04 01 0B 02 02 00 10  ....H...x.......
01F0: 02 80 00 0B 02 03 01 10  06 80 1A 10 02 03 03 10  ................
0200: 0E 00 48 12 80 05 04 00  01 0B 02 01 BD 01 21 00  ..H...........!.
0210: 02 0E 00 02 80 80 1E 02  1A F7 03 01 2C 02 02 0E  ............,...
0220: 00 01 80 80 2C 02 1A F7  03 01 2C 02 1B           ....,.....,..   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
  2: 0x0007 [0x06] ExtData[1]->WorkLocal[0] = 0
  3: 0x000A [0x06] ExtData[1]->WorkLocal[1] = 0
  4: 0x000D [0x06] ExtData[1]->WorkLocal[2] = 0
  5: 0x0010 [0x06] ExtData[1]->WorkLocal[3] = 0
  6: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  7: 0x0018 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
  8: 0x001D [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[5]
  9: 0x0022 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[6]
 10: 0x0027 [0x03] ExtData[1]->WorkLocal[18] = Work_Zone[8]
 11: 0x002C [0x03] ExtData[1]->WorkLocal[17] = Work_Zone[9]
 12: 0x0031 [0x06] Work_Zone[1] = 0
 13: 0x0034 [0x06] ExtData[1]->WorkLocal[16] = 0
 14: 0x0037 [0x06] ExtData[1]->WorkLocal[6] = 0
 15: 0x003A [0x06] ExtData[1]->WorkLocal[7] = 0
 16: 0x003D [0x02] IF !(ExtData[1]->WorkLocal[18] <= 0*) GOTO 0x005D
 17: 0x0045 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x0055
 18: 0x004D [0x03] ExtData[1]->WorkLocal[14] = 5*
 19: 0x0052 [0x01] GOTO 0x005A
 20: 0x0055 [0x03] ExtData[1]->WorkLocal[14] = 1*

SUBROUTINE_005A:
 21: 0x005A [0x01] GOTO 0x00B5
 22: 0x005D [0x06] ExtData[1]->WorkLocal[15] = 0
 23: 0x0060 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=31*, target=ExtData[1]->WorkLocal[15], source=4294967295*)
 24: 0x0069 [0x0F] ExtData[1]->WorkLocal[15] ^= ExtData[1]->WorkLocal[17]
 25: 0x006E [0x10] ExtData[1]->WorkLocal[15] <<= 1*
 26: 0x0073 [0x24] CREATE_DIALOG(message_id=7863*, default_option=0*, option_flags=ExtData[1]->WorkLocal[15])
    → "Enter which battlefield? [None./Endeavoring to Awaken./Endeavoring to Awaken./ /Behind the Sluices./Stonewalled./The Gates./Saved by the Bell./Quiescence./The Charlatan./Yggdrasil Beckons./Yggdrasil Beckons./Watery Grave./Mistress of Ceremonies./A Barrel of Laughs./Sinister Reign./The Ygnas Directive 6./Skirmishes./[Fractures/Obscured Domains]./Alluvion skirmishes./The Silent Forest./Wind of Eternity./Phantasmic Heroes.]"
 27: 0x007A [0x25] WAIT_DIALOG_SELECT()
 28: 0x007B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x008D
 29: 0x0083 [0x03] Work_Zone[1] = 1073741824*
 30: 0x0088 [0x21] END_EVENT
 31: 0x0089 [0x00] END_REQSTACK()

SUBROUTINE_008D:
 32: 0x008D [0x03] ExtData[1]->WorkLocal[16] = Work_Zone[0]
 33: 0x0092 [0x0C] ExtData[1]->WorkLocal[16]--
 34: 0x0095 [0x02] IF !(ExtData[1]->WorkLocal[16] == 16*) GOTO 0x00A5
 35: 0x009D [0x03] ExtData[1]->WorkLocal[14] = 1*
 36: 0x00A2 [0x01] GOTO 0x00B5
 37: 0x00A5 [0x02] IF !(ExtData[1]->WorkLocal[16] == 18*) GOTO 0x00B5
 38: 0x00AD [0x03] ExtData[1]->WorkLocal[14] = 5*
 39: 0x00B2 [0x01] GOTO 0x00B5

SUBROUTINE_00B5:
 40: 0x00B5 [0x02] IF !(ExtData[1]->WorkLocal[14] == 1*) GOTO 0x0136
 41: 0x00BD [0x3E] IF !(ExtData[1]->WorkLocal[17] bit 18*) GOTO 0x010C
 42: 0x00C4 [0x03] Work_Zone[1] = 0*
 43: 0x00C9 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=4*)
 44: 0x00D2 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 45: 0x00D4 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 46: 0x00D6 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
 47: 0x00DB [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 48: 0x00E0 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
 49: 0x00E5 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[5]
 50: 0x00EA [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[6]
 51: 0x00EF [0x1A] CALL_SUBROUTINE(address=0x0372)
 52: 0x00F2 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 53: 0x00FB [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 54: 0x0104 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 55: 0x0109 [0x01] GOTO 0x0133
 56: 0x010C [0x1A] CALL_SUBROUTINE(address=0x0372)
 57: 0x010F [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 58: 0x0118 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 59: 0x0121 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 60: 0x0126 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=3*)
 61: 0x012F [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 62: 0x0131 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_0133:
 63: 0x0133 [0x01] GOTO 0x01B7
 64: 0x0136 [0x02] IF !(ExtData[1]->WorkLocal[14] == 5*) GOTO 0x01B7
 65: 0x013E [0x3E] IF !(ExtData[1]->WorkLocal[17] bit 16*) GOTO 0x018D
 66: 0x0145 [0x03] Work_Zone[1] = 0*
 67: 0x014A [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=5*)
 68: 0x0153 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 69: 0x0155 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 70: 0x0157 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
 71: 0x015C [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
 72: 0x0161 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
 73: 0x0166 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[5]
 74: 0x016B [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[6]
 75: 0x0170 [0x1A] CALL_SUBROUTINE(address=0x0372)
 76: 0x0173 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 77: 0x017C [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 78: 0x0185 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 79: 0x018A [0x01] GOTO 0x01B4
 80: 0x018D [0x1A] CALL_SUBROUTINE(address=0x0372)
 81: 0x0190 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 82: 0x0199 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 83: 0x01A2 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 84: 0x01A7 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=3*)
 85: 0x01B0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 86: 0x01B2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)

SUBROUTINE_01B4:
 87: 0x01B4 [0x01] GOTO 0x01B7

SUBROUTINE_01B7:
 88: 0x01B7 [0x06] ExtData[1]->WorkLocal[4] = 0
 89: 0x01BA [0x05] ExtData[1]->WorkLocal[8] = 1

SUBROUTINE_01BD:
 90: 0x01BD [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x020E
 91: 0x01C5 [0x1A] CALL_SUBROUTINE(address=0x0210)
 92: 0x01C8 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
 93: 0x01CD [0x48] [System] [7843*]:
    → "Only party members present with you in this area will be transported to [/this skirmish in ////this alluvion skirmish in /]$8."
 94: 0x01D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 95: 0x01D1 [0x24] CREATE_DIALOG(message_id=7844*, default_option=ExtData[1]->WorkLocal[8], option_flags=0*)
    → "Proceed? [Yes./No.]"
 96: 0x01D8 [0x25] WAIT_DIALOG_SELECT()
 97: 0x01D9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01ED
 98: 0x01E1 [0x06] ExtData[1]->WorkLocal[8] = 0
 99: 0x01E4 [0x48] [System] [7851*]:
    → "Your request for entry is being considered..."
100: 0x01E7 [0x1A] CALL_SUBROUTINE(address=0x0478)
101: 0x01EA [0x01] GOTO 0x020B
102: 0x01ED [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x020B
103: 0x01F5 [0x03] Work_Zone[1] = 1073741824*
104: 0x01FA [0x1A] CALL_SUBROUTINE(address=0x0210)
105: 0x01FD [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
106: 0x0202 [0x48] [System] [7846*]:
    → "You have chosen not to enter [/this skirmish in ////this alluvion skirmish in /]$8."
107: 0x0205 [0x05] ExtData[1]->WorkLocal[4] = 1
108: 0x0208 [0x01] GOTO 0x020B

SUBROUTINE_020B:
109: 0x020B [0x01] GOTO 0x01BD
110: 0x020E [0x21] END_EVENT
111: 0x020F [0x00] END_REQSTACK()

SUBROUTINE_0210:
112: 0x0210 [0x02] IF !(ExtData[1]->WorkLocal[14] == 1*) GOTO 0x021E
113: 0x0218 [0x1A] CALL_SUBROUTINE(address=0x03F7)
114: 0x021B [0x01] GOTO 0x022C
115: 0x021E [0x02] IF !(ExtData[1]->WorkLocal[14] == 5*) GOTO 0x022C
116: 0x0226 [0x1A] CALL_SUBROUTINE(address=0x03F7)
117: 0x0229 [0x01] GOTO 0x022C

SUBROUTINE_022C:
118: 0x022C [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008A [0x01] GOTO 0x008D
```

### Event 5502

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x022D     |
| Data Size    | 1354 bytes |
| Instructions | 263        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                         42 03 05               B..
0230: 00 02 10 06 00 00 06 01  00 06 02 00 06 03 00 24  ...............$
0240: 13 80 00 80 00 80 25 02  00 10 00 80 00 59 02 03  ......%......Y..
0250: 01 10 06 80 21 00 01 59  02 03 00 00 00 10 24 14  ....!..Y......$.
0260: 80 00 80 00 80 25 02 00  10 00 80 00 78 02 03 01  .....%......x...
0270: 10 06 80 21 00 01 78 02  03 01 00 00 10 06 01 10  ...!..x.........
0280: 03 03 10 15 80 03 04 10  0E 80 03 05 10 0B 80 03  ................
0290: 06 10 01 80 03 07 10 16  80 24 17 80 00 80 00 80  .........$......
02A0: 25 02 00 10 00 80 00 B3  02 03 01 10 06 80 21 00  %.............!.
02B0: 01 B3 02 06 01 10 03 02  00 00 10 24 18 80 00 80  ...........$....
02C0: 00 80 25 02 00 10 00 80  00 D5 02 03 01 10 06 80  ..%.............
02D0: 21 00 01 D5 02 06 01 10  03 03 00 00 10 02 03 00  !...............
02E0: 16 80 00 EA 02 03 03 00  00 80 02 03 00 00 80 02  ................
02F0: FA 02 03 0E 00 01 80 01  FF 02 03 0E 00 02 80 1A  ................
0300: 72 03 40 00 80 0C 80 01  10 06 00 40 07 80 0D 80  r.@........@....
0310: 01 10 07 00 03 0D 00 01  10 06 04 00 05 08 00 02  ................
0320: 04 00 00 80 00 70 03 1A  F7 03 03 03 10 0E 00 48  .....p.........H
0330: 0F 80 23 24 10 80 08 00  00 80 25 02 00 10 00 80  ..#$......%.....
0340: 00 4F 03 06 08 00 48 11  80 1A 78 04 01 6D 03 02  .O....H...x..m..
0350: 00 10 02 80 00 6D 03 03  01 10 06 80 1A F7 03 03  .....m..........
0360: 03 10 0E 00 48 12 80 05  04 00 01 6D 03 01 1F 03  ....H......m....
0370: 21 00 02 03 00 00 80 02  B8 03 02 05 00 00 80 80  !...............
0380: 8A 03 03 06 00 19 80 01  B5 03 02 05 00 02 80 80  ................
0390: 9A 03 03 06 00 1A 80 01  B5 03 02 05 00 15 80 80  ................
03A0: AA 03 03 06 00 1B 80 01  B5 03 02 05 00 0E 80 80  ................
03B0: B5 03 01 B5 03 01 CF 03  03 06 00 05 00 14 06 00  ................
03C0: 1C 80 07 06 00 01 00 0C  06 00 07 06 00 1D 80 06  ................
03D0: 07 00 40 00 80 15 80 07  00 00 00 40 0E 80 01 80  ..@........@....
03E0: 07 00 01 00 40 16 80 1C  80 07 00 02 00 40 1E 80  ....@........@..
03F0: 0C 80 07 00 03 00 1B 02  05 00 00 80 80 07 04 03  ................
0400: 02 10 1F 80 01 77 04 02  05 00 02 80 80 17 04 03  .....w..........
0410: 02 10 20 80 01 77 04 02  05 00 15 80 80 27 04 03  .. ..w.......'..
0420: 02 10 21 80 01 77 04 02  05 00 0E 80 80 37 04 03  ..!..w.......7..
0430: 02 10 22 80 01 77 04 02  05 00 0B 80 80 47 04 03  .."..w.......G..
0440: 02 10 0B 80 01 77 04 02  05 00 01 80 80 57 04 03  .....w.......W..
0450: 02 10 15 80 01 77 04 02  05 00 16 80 80 67 04 03  .....w.......g..
0460: 02 10 15 80 01 77 04 02  05 00 23 80 80 77 04 03  .....w....#..w..
0470: 02 10 15 80 01 77 04 1B  06 09 00 06 0C 00 06 0A  .....w..........
0480: 00 02 09 00 00 80 00 A8  04 02 0C 00 00 80 80 97  ................
0490: 04 1A A9 04 01 A5 04 02  0C 00 02 80 80 A5 04 1A  ................
04A0: 6A 05 01 A5 04 01 81 04  1B 03 01 10 0D 00 40 09  j.............@.
04B0: 80 0A 80 01 10 0C 00 43  00 43 01 03 0B 00 09 10  .......C.C......
04C0: 03 01 10 00 80 02 0B 00  02 80 80 D5 04 03 0C 00  ................
04D0: 02 80 01 69 05 02 0B 00  15 80 80 FB 04 0B 0A 00  ...i............
04E0: 02 0A 00 01 80 02 F5 04  05 09 00 48 24 80 23 1C  ...........H$.#.
04F0: 25 80 01 F8 04 1C 26 80  01 69 05 02 0B 00 0E 80  %.....&..i......
0500: 80 11 05 03 01 10 06 80  05 09 00 05 04 00 01 69  ...............i
0510: 05 02 0B 00 0B 80 80 27  05 03 01 10 06 80 05 09  .......'........
0520: 00 05 04 00 01 69 05 02  0B 00 01 80 80 3D 05 03  .....i.......=..
0530: 01 10 06 80 05 09 00 05  04 00 01 69 05 02 0B 00  ...........i....
0540: 16 80 80 53 05 03 01 10  06 80 05 09 00 05 04 00  ...S............
0550: 01 69 05 02 0B 00 23 80  80 69 05 03 01 10 06 80  .i....#..i......
0560: 05 09 00 05 04 00 01 69  05 1B 03 01 10 0D 00 40  .......i.......@
0570: 09 80 0A 80 01 10 0C 00  43 00 43 01 03 01 10 00  ........C.C.....
0580: 80 03 0B 00 09 10 02 0B  00 0E 80 80 99 05 03 01  ................
0590: 10 06 80 05 09 00 01 06  07 02 0B 00 0B 80 80 AF  ................
05A0: 05 03 01 10 06 80 05 09  00 05 04 00 01 06 07 02  ................
05B0: 0B 00 01 80 80 C5 05 03  01 10 06 80 05 09 00 05  ................
05C0: 04 00 01 06 07 02 0B 00  16 80 80 DB 05 03 01 10  ................
05D0: 06 80 05 09 00 05 04 00  01 06 07 02 0B 00 23 80  ..............#.
05E0: 80 F1 05 03 01 10 06 80  05 09 00 05 04 00 01 06  ................
05F0: 07 02 0B 00 1C 80 80 A5  06 02 0E 00 02 80 80 10  ................
0600: 06 1A F7 03 03 03 10 0E  00 48 27 80 23 01 27 06  .........H'.#.'.
0610: 02 0E 00 01 80 80 27 06  1A F7 03 03 03 10 0E 00  ......'.........
0620: 48 27 80 23 01 27 06 62  02 80 F0 FF FF 7F F0 FF  H'.#.'.b........
0630: FF 7F 6D 61 69 6E 00 80  1C 28 80 45 29 80 F0 FF  ..main...(.E)...
0640: FF 7F F0 FF FF 7F 77 68  6F 31 00 80 55 29 80 F0  ......who1..U)..
0650: FF FF 7F F0 FF FF 7F 77  68 6F 31 1C 2A 80 45 2B  .......who1.*.E+
0660: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 00 80 55  .........fdo1..U
0670: 2B 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 45 29  +.........fdo1E)
0680: 80 F0 FF FF 7F F0 FF FF  7F 77 68 69 31 00 80 1C  .........whi1...
0690: 0A 80 30 05 09 00 05 04  00 40 00 80 23 80 01 10  ..0......@..#...
06A0: 1C 80 01 06 07 02 0B 00  1E 80 80 B8 06 03 01 10  ................
06B0: 06 80 05 09 00 01 06 07  02 0B 00 2C 80 80 CE 06  ...........,....
06C0: 03 01 10 06 80 05 09 00  05 04 00 01 06 07 02 0B  ................
06D0: 00 0C 80 80 06 07 0B 0A  00 02 0A 00 0A 80 02 00  ................
06E0: 07 03 01 10 0D 00 40 09  80 0A 80 01 10 15 80 43  ......@........C
06F0: 00 43 01 05 09 00 48 24  80 23 1C 25 80 01 03 07  .C....H$.#.%....
0700: 1C 26 80 01 06 07 1B 03  13 00 2D 80 1B 03 06 00  .&........-.....
0710: 2E 80 1B 06 14 00 02 06  00 2F 80 80 26 07 03 14  ........./..&...
0720: 00 00 80 01 76 07 02 06  00 30 80 80 36 07 03 14  ....v....0..6...
0730: 00 00 80 01 76 07 02 06  00 31 80 80 46 07 03 14  ....v....1..F...
0740: 00 00 80 01 76 07 02 06  00 2E 80 80 56 07 03 14  ....v.......V...
0750: 00 02 80 01 76 07 02 06  00 32 80 80 66 07 03 14  ....v....2..f...
0760: 00 02 80 01 76 07 02 06  00 33 80 80 76 07 03 14  ....v....3..v...
0770: 00 02 80 01 76 07 1B                              ....v..         
```

#### Opcodes

```
  0: 0x022D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x022E [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
  2: 0x0233 [0x06] ExtData[1]->WorkLocal[0] = 0
  3: 0x0236 [0x06] ExtData[1]->WorkLocal[1] = 0
  4: 0x0239 [0x06] ExtData[1]->WorkLocal[2] = 0
  5: 0x023C [0x06] ExtData[1]->WorkLocal[3] = 0
  6: 0x023F [0x24] CREATE_DIALOG(message_id=7857*, default_option=0*, option_flags=0*)
    → "What's the visage's obtainment rate? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]"
  7: 0x0246 [0x25] WAIT_DIALOG_SELECT()
  8: 0x0247 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0259
  9: 0x024F [0x03] Work_Zone[1] = 1073741824*
 10: 0x0254 [0x21] END_EVENT
 11: 0x0255 [0x00] END_REQSTACK()

SUBROUTINE_0259:
 12: 0x0259 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[0]
 13: 0x025E [0x24] CREATE_DIALOG(message_id=7856*, default_option=0*, option_flags=0*)
    → "What's the torso's size? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]"
 14: 0x0265 [0x25] WAIT_DIALOG_SELECT()
 15: 0x0266 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0278
 16: 0x026E [0x03] Work_Zone[1] = 1073741824*
 17: 0x0273 [0x21] END_EVENT
 18: 0x0274 [0x00] END_REQSTACK()

SUBROUTINE_0278:
 19: 0x0278 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[0]
 20: 0x027D [0x06] Work_Zone[1] = 0
 21: 0x0280 [0x03] Work_Zone[3] = 2*
 22: 0x0285 [0x03] Work_Zone[4] = 3*
 23: 0x028A [0x03] Work_Zone[5] = 4*
 24: 0x028F [0x03] Work_Zone[6] = 5*
 25: 0x0294 [0x03] Work_Zone[7] = 6*
 26: 0x0299 [0x24] CREATE_DIALOG(message_id=7858*, default_option=0*, option_flags=0*)
    → "What rank are the legs' benefits? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]"
 27: 0x02A0 [0x25] WAIT_DIALOG_SELECT()
 28: 0x02A1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B3
 29: 0x02A9 [0x03] Work_Zone[1] = 1073741824*
 30: 0x02AE [0x21] END_EVENT
 31: 0x02AF [0x00] END_REQSTACK()

SUBROUTINE_02B3:
 32: 0x02B3 [0x06] Work_Zone[1] = 0
 33: 0x02B6 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[0]
 34: 0x02BB [0x24] CREATE_DIALOG(message_id=7859*, default_option=0*, option_flags=0*)
    → "Ready for an alluvion skirmish? [No./Alluvion A./Alluvion B./Alluvion C./Alluvion D./Alluvion E./Just a regular skirmish, please.]"
 35: 0x02C2 [0x25] WAIT_DIALOG_SELECT()
 36: 0x02C3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02D5
 37: 0x02CB [0x03] Work_Zone[1] = 1073741824*
 38: 0x02D0 [0x21] END_EVENT
 39: 0x02D1 [0x00] END_REQSTACK()

SUBROUTINE_02D5:
 40: 0x02D5 [0x06] Work_Zone[1] = 0
 41: 0x02D8 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 42: 0x02DD [0x02] IF !(ExtData[1]->WorkLocal[3] == 6*) GOTO 0x02EA
 43: 0x02E5 [0x03] ExtData[1]->WorkLocal[3] = 0*
 44: 0x02EA [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x02FA
 45: 0x02F2 [0x03] ExtData[1]->WorkLocal[14] = 5*
 46: 0x02F7 [0x01] GOTO 0x02FF
 47: 0x02FA [0x03] ExtData[1]->WorkLocal[14] = 1*

SUBROUTINE_02FF:
 48: 0x02FF [0x1A] CALL_SUBROUTINE(address=0x0372)
 49: 0x0302 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 50: 0x030B [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 51: 0x0314 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 52: 0x0319 [0x06] ExtData[1]->WorkLocal[4] = 0
 53: 0x031C [0x05] ExtData[1]->WorkLocal[8] = 1

SUBROUTINE_031F:
 54: 0x031F [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x0370
 55: 0x0327 [0x1A] CALL_SUBROUTINE(address=0x03F7)
 56: 0x032A [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
 57: 0x032F [0x48] [System] [7843*]:
    → "Only party members present with you in this area will be transported to [/this skirmish in ////this alluvion skirmish in /]$8."
 58: 0x0332 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0333 [0x24] CREATE_DIALOG(message_id=7844*, default_option=ExtData[1]->WorkLocal[8], option_flags=0*)
    → "Proceed? [Yes./No.]"
 60: 0x033A [0x25] WAIT_DIALOG_SELECT()
 61: 0x033B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x034F
 62: 0x0343 [0x06] ExtData[1]->WorkLocal[8] = 0
 63: 0x0346 [0x48] [System] [7851*]:
    → "Your request for entry is being considered..."
 64: 0x0349 [0x1A] CALL_SUBROUTINE(address=0x0478)
 65: 0x034C [0x01] GOTO 0x036D
 66: 0x034F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x036D
 67: 0x0357 [0x03] Work_Zone[1] = 1073741824*
 68: 0x035C [0x1A] CALL_SUBROUTINE(address=0x03F7)
 69: 0x035F [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
 70: 0x0364 [0x48] [System] [7846*]:
    → "You have chosen not to enter [/this skirmish in ////this alluvion skirmish in /]$8."
 71: 0x0367 [0x05] ExtData[1]->WorkLocal[4] = 1
 72: 0x036A [0x01] GOTO 0x036D

SUBROUTINE_036D:
 73: 0x036D [0x01] GOTO 0x031F
 74: 0x0370 [0x21] END_EVENT
 75: 0x0371 [0x00] END_REQSTACK()

SUBROUTINE_0372:
 76: 0x0372 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x03B8
 77: 0x037A [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x038A
 78: 0x0382 [0x03] ExtData[1]->WorkLocal[6] = 805*
 79: 0x0387 [0x01] GOTO 0x03B5
 80: 0x038A [0x02] IF !(ExtData[1]->WorkLocal[5] == 1*) GOTO 0x039A
 81: 0x0392 [0x03] ExtData[1]->WorkLocal[6] = 807*
 82: 0x0397 [0x01] GOTO 0x03B5
 83: 0x039A [0x02] IF !(ExtData[1]->WorkLocal[5] == 2*) GOTO 0x03AA
 84: 0x03A2 [0x03] ExtData[1]->WorkLocal[6] = 806*
 85: 0x03A7 [0x01] GOTO 0x03B5
 86: 0x03AA [0x02] IF !(ExtData[1]->WorkLocal[5] == 3*) GOTO 0x03B5
 87: 0x03B2 [0x01] GOTO 0x03B5

SUBROUTINE_03B5:
 88: 0x03B5 [0x01] GOTO 0x03CF
 89: 0x03B8 [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[5]
 90: 0x03BD [0x14] ExtData[1]->WorkLocal[6] *= 8*
 91: 0x03C2 [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[1]
 92: 0x03C7 [0x0C] ExtData[1]->WorkLocal[6]--
 93: 0x03CA [0x07] ExtData[1]->WorkLocal[6] += 800*

SUBROUTINE_03CF:
 94: 0x03CF [0x06] ExtData[1]->WorkLocal[7] = 0
 95: 0x03D2 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=2*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[0])
 96: 0x03DB [0x40] SET_BIT_WORK_RANGE(start_bit=3*, end_bit=5*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[1])
 97: 0x03E4 [0x40] SET_BIT_WORK_RANGE(start_bit=6*, end_bit=8*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[2])
 98: 0x03ED [0x40] SET_BIT_WORK_RANGE(start_bit=9*, end_bit=11*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[3])
 99: 0x03F6 [0x1B] RETURN

SUBROUTINE_03F7:
100: 0x03F7 [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x0407
101: 0x03FF [0x03] Work_Zone[2] = 259*
102: 0x0404 [0x01] GOTO 0x0477
103: 0x0407 [0x02] IF !(ExtData[1]->WorkLocal[5] == 1*) GOTO 0x0417
104: 0x040F [0x03] Work_Zone[2] = 264*
105: 0x0414 [0x01] GOTO 0x0477
106: 0x0417 [0x02] IF !(ExtData[1]->WorkLocal[5] == 2*) GOTO 0x0427
107: 0x041F [0x03] Work_Zone[2] = 271*
108: 0x0424 [0x01] GOTO 0x0477
109: 0x0427 [0x02] IF !(ExtData[1]->WorkLocal[5] == 3*) GOTO 0x0437
110: 0x042F [0x03] Work_Zone[2] = 275*
111: 0x0434 [0x01] GOTO 0x0477
112: 0x0437 [0x02] IF !(ExtData[1]->WorkLocal[5] == 4*) GOTO 0x0447
113: 0x043F [0x03] Work_Zone[2] = 4*
114: 0x0444 [0x01] GOTO 0x0477
115: 0x0447 [0x02] IF !(ExtData[1]->WorkLocal[5] == 5*) GOTO 0x0457
116: 0x044F [0x03] Work_Zone[2] = 2*
117: 0x0454 [0x01] GOTO 0x0477
118: 0x0457 [0x02] IF !(ExtData[1]->WorkLocal[5] == 6*) GOTO 0x0467
119: 0x045F [0x03] Work_Zone[2] = 2*
120: 0x0464 [0x01] GOTO 0x0477
121: 0x0467 [0x02] IF !(ExtData[1]->WorkLocal[5] == 7*) GOTO 0x0477
122: 0x046F [0x03] Work_Zone[2] = 2*
123: 0x0474 [0x01] GOTO 0x0477

SUBROUTINE_0477:
124: 0x0477 [0x1B] RETURN

SUBROUTINE_0478:
125: 0x0478 [0x06] ExtData[1]->WorkLocal[9] = 0
126: 0x047B [0x06] ExtData[1]->WorkLocal[12] = 0
127: 0x047E [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_0481:
128: 0x0481 [0x02] IF !(ExtData[1]->WorkLocal[9] == 0*) GOTO 0x04A8
129: 0x0489 [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x0497
130: 0x0491 [0x1A] CALL_SUBROUTINE(address=0x04A9)
131: 0x0494 [0x01] GOTO 0x04A5
132: 0x0497 [0x02] IF !(ExtData[1]->WorkLocal[12] == 1*) GOTO 0x04A5
133: 0x049F [0x1A] CALL_SUBROUTINE(address=0x056A)
134: 0x04A2 [0x01] GOTO 0x04A5

SUBROUTINE_04A5:
135: 0x04A5 [0x01] GOTO 0x0481
136: 0x04A8 [0x1B] RETURN

SUBROUTINE_04A9:
137: 0x04A9 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
138: 0x04AE [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[12])
139: 0x04B7 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
140: 0x04B9 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
141: 0x04BB [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[9]
142: 0x04C0 [0x03] Work_Zone[1] = 0*
143: 0x04C5 [0x02] IF !(ExtData[1]->WorkLocal[11] == 1*) GOTO 0x04D5
144: 0x04CD [0x03] ExtData[1]->WorkLocal[12] = 1*
145: 0x04D2 [0x01] GOTO 0x0569
146: 0x04D5 [0x02] IF !(ExtData[1]->WorkLocal[11] == 2*) GOTO 0x04FB
147: 0x04DD [0x0B] ExtData[1]->WorkLocal[10]++
148: 0x04E0 [0x02] IF !(ExtData[1]->WorkLocal[10] <= 5*) GOTO 0x04F5
149: 0x04E8 [0x05] ExtData[1]->WorkLocal[9] = 1
150: 0x04EB [0x48] [System] [7848*]:
    → "You cannot enter at this time. Please wait a moment and try again."
151: 0x04EE [0x23] WAIT_FOR_DIALOG_INTERACTION
152: 0x04EF [0x1C] WAIT(60* ticks)
153: 0x04F2 [0x01] GOTO 0x04F8
154: 0x04F5 [0x1C] WAIT(120* ticks)

SUBROUTINE_04F8:
155: 0x04F8 [0x01] GOTO 0x0569
156: 0x04FB [0x02] IF !(ExtData[1]->WorkLocal[11] == 3*) GOTO 0x0511
157: 0x0503 [0x03] Work_Zone[1] = 1073741824*
158: 0x0508 [0x05] ExtData[1]->WorkLocal[9] = 1
159: 0x050B [0x05] ExtData[1]->WorkLocal[4] = 1
160: 0x050E [0x01] GOTO 0x0569
161: 0x0511 [0x02] IF !(ExtData[1]->WorkLocal[11] == 4*) GOTO 0x0527
162: 0x0519 [0x03] Work_Zone[1] = 1073741824*
163: 0x051E [0x05] ExtData[1]->WorkLocal[9] = 1
164: 0x0521 [0x05] ExtData[1]->WorkLocal[4] = 1
165: 0x0524 [0x01] GOTO 0x0569
166: 0x0527 [0x02] IF !(ExtData[1]->WorkLocal[11] == 5*) GOTO 0x053D
167: 0x052F [0x03] Work_Zone[1] = 1073741824*
168: 0x0534 [0x05] ExtData[1]->WorkLocal[9] = 1
169: 0x0537 [0x05] ExtData[1]->WorkLocal[4] = 1
170: 0x053A [0x01] GOTO 0x0569
171: 0x053D [0x02] IF !(ExtData[1]->WorkLocal[11] == 6*) GOTO 0x0553
172: 0x0545 [0x03] Work_Zone[1] = 1073741824*
173: 0x054A [0x05] ExtData[1]->WorkLocal[9] = 1
174: 0x054D [0x05] ExtData[1]->WorkLocal[4] = 1
175: 0x0550 [0x01] GOTO 0x0569
176: 0x0553 [0x02] IF !(ExtData[1]->WorkLocal[11] == 7*) GOTO 0x0569
177: 0x055B [0x03] Work_Zone[1] = 1073741824*
178: 0x0560 [0x05] ExtData[1]->WorkLocal[9] = 1
179: 0x0563 [0x05] ExtData[1]->WorkLocal[4] = 1
180: 0x0566 [0x01] GOTO 0x0569

SUBROUTINE_0569:
181: 0x0569 [0x1B] RETURN

SUBROUTINE_056A:
182: 0x056A [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
183: 0x056F [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[12])
184: 0x0578 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
185: 0x057A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
186: 0x057C [0x03] Work_Zone[1] = 0*
187: 0x0581 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[9]
188: 0x0586 [0x02] IF !(ExtData[1]->WorkLocal[11] == 3*) GOTO 0x0599
189: 0x058E [0x03] Work_Zone[1] = 1073741824*
190: 0x0593 [0x05] ExtData[1]->WorkLocal[9] = 1
191: 0x0596 [0x01] GOTO 0x0706
192: 0x0599 [0x02] IF !(ExtData[1]->WorkLocal[11] == 4*) GOTO 0x05AF
193: 0x05A1 [0x03] Work_Zone[1] = 1073741824*
194: 0x05A6 [0x05] ExtData[1]->WorkLocal[9] = 1
195: 0x05A9 [0x05] ExtData[1]->WorkLocal[4] = 1
196: 0x05AC [0x01] GOTO 0x0706
197: 0x05AF [0x02] IF !(ExtData[1]->WorkLocal[11] == 5*) GOTO 0x05C5
198: 0x05B7 [0x03] Work_Zone[1] = 1073741824*
199: 0x05BC [0x05] ExtData[1]->WorkLocal[9] = 1
200: 0x05BF [0x05] ExtData[1]->WorkLocal[4] = 1
201: 0x05C2 [0x01] GOTO 0x0706
202: 0x05C5 [0x02] IF !(ExtData[1]->WorkLocal[11] == 6*) GOTO 0x05DB
203: 0x05CD [0x03] Work_Zone[1] = 1073741824*
204: 0x05D2 [0x05] ExtData[1]->WorkLocal[9] = 1
205: 0x05D5 [0x05] ExtData[1]->WorkLocal[4] = 1
206: 0x05D8 [0x01] GOTO 0x0706
207: 0x05DB [0x02] IF !(ExtData[1]->WorkLocal[11] == 7*) GOTO 0x05F1
208: 0x05E3 [0x03] Work_Zone[1] = 1073741824*
209: 0x05E8 [0x05] ExtData[1]->WorkLocal[9] = 1
210: 0x05EB [0x05] ExtData[1]->WorkLocal[4] = 1
211: 0x05EE [0x01] GOTO 0x0706
212: 0x05F1 [0x02] IF !(ExtData[1]->WorkLocal[11] == 8*) GOTO 0x06A5
213: 0x05F9 [0x02] IF !(ExtData[1]->WorkLocal[14] == 1*) GOTO 0x0610
214: 0x0601 [0x1A] CALL_SUBROUTINE(address=0x03F7)
215: 0x0604 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
216: 0x0609 [0x48] [System] [7845*]:
    → "Now entering [/a skirmish in ////an alluvion skirmish in /]$8."
217: 0x060C [0x23] WAIT_FOR_DIALOG_INTERACTION
218: 0x060D [0x01] GOTO 0x0627
219: 0x0610 [0x02] IF !(ExtData[1]->WorkLocal[14] == 5*) GOTO 0x0627
220: 0x0618 [0x1A] CALL_SUBROUTINE(address=0x03F7)
221: 0x061B [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
222: 0x0620 [0x48] [System] [7845*]:
    → "Now entering [/a skirmish in ////an alluvion skirmish in /]$8."
223: 0x0623 [0x23] WAIT_FOR_DIALOG_INTERACTION
224: 0x0624 [0x01] GOTO 0x0627

SUBROUTINE_0627:
225: 0x0627 [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
226: 0x0638 [0x1C] WAIT(90* ticks)
227: 0x063B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
228: 0x064C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
229: 0x065B [0x1C] WAIT(45* ticks)
230: 0x065E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
231: 0x066F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
232: 0x067E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
233: 0x068F [0x1C] WAIT(15* ticks)
234: 0x0692 [0x30] SET_UCOFF_CONTINUE_ZERO()
235: 0x0693 [0x05] ExtData[1]->WorkLocal[9] = 1
236: 0x0696 [0x05] ExtData[1]->WorkLocal[4] = 1
237: 0x0699 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=8*)
238: 0x06A2 [0x01] GOTO 0x0706
239: 0x06A5 [0x02] IF !(ExtData[1]->WorkLocal[11] == 9*) GOTO 0x06B8
240: 0x06AD [0x03] Work_Zone[1] = 1073741824*
241: 0x06B2 [0x05] ExtData[1]->WorkLocal[9] = 1
242: 0x06B5 [0x01] GOTO 0x0706
243: 0x06B8 [0x02] IF !(ExtData[1]->WorkLocal[11] == 10*) GOTO 0x06CE
244: 0x06C0 [0x03] Work_Zone[1] = 1073741824*
245: 0x06C5 [0x05] ExtData[1]->WorkLocal[9] = 1
246: 0x06C8 [0x05] ExtData[1]->WorkLocal[4] = 1
247: 0x06CB [0x01] GOTO 0x0706
248: 0x06CE [0x02] IF !(ExtData[1]->WorkLocal[11] == 11*) GOTO 0x0706
249: 0x06D6 [0x0B] ExtData[1]->WorkLocal[10]++
250: 0x06D9 [0x02] IF !(ExtData[1]->WorkLocal[10] <= 15*) GOTO 0x0700
251: 0x06E1 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
252: 0x06E6 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=2*)
253: 0x06EF [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
254: 0x06F1 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
255: 0x06F3 [0x05] ExtData[1]->WorkLocal[9] = 1
256: 0x06F6 [0x48] [System] [7848*]:
    → "You cannot enter at this time. Please wait a moment and try again."
257: 0x06F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
258: 0x06FA [0x1C] WAIT(60* ticks)
259: 0x06FD [0x01] GOTO 0x0703
260: 0x0700 [0x1C] WAIT(120* ticks)

SUBROUTINE_0703:
261: 0x0703 [0x01] GOTO 0x0706

SUBROUTINE_0706:
262: 0x0706 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0256 [0x01] GOTO 0x0259
# Dead code (unreachable instructions):
     0x0275 [0x01] GOTO 0x0278
# Dead code (unreachable instructions):
     0x02B0 [0x01] GOTO 0x02B3
# Dead code (unreachable instructions):
     0x02D2 [0x01] GOTO 0x02D5
# Dead code (unreachable instructions):
     0x0707 [0x03] ExtData[1]->WorkLocal[19] = 263*
     0x070C [0x1B] RETURN
     0x070D [0x03] ExtData[1]->WorkLocal[6] = 813*
     0x0712 [0x1B] RETURN
     0x0713 [0x06] ExtData[1]->WorkLocal[20] = 0
     0x0716 [0x02] IF !(ExtData[1]->WorkLocal[6] == 821*) GOTO 0x0726
     0x071E [0x03] ExtData[1]->WorkLocal[20] = 0*
     0x0723 [0x01] GOTO 0x0776
     0x0726 [0x02] IF !(ExtData[1]->WorkLocal[6] == 822*) GOTO 0x0736
     0x072E [0x03] ExtData[1]->WorkLocal[20] = 0*
     0x0733 [0x01] GOTO 0x0776
     0x0736 [0x02] IF !(ExtData[1]->WorkLocal[6] == 823*) GOTO 0x0746
     0x073E [0x03] ExtData[1]->WorkLocal[20] = 0*
     0x0743 [0x01] GOTO 0x0776
     0x0746 [0x02] IF !(ExtData[1]->WorkLocal[6] == 813*) GOTO 0x0756
     0x074E [0x03] ExtData[1]->WorkLocal[20] = 1*
     0x0753 [0x01] GOTO 0x0776
     0x0756 [0x02] IF !(ExtData[1]->WorkLocal[6] == 814*) GOTO 0x0766
     0x075E [0x03] ExtData[1]->WorkLocal[20] = 1*
     0x0763 [0x01] GOTO 0x0776
     0x0766 [0x02] IF !(ExtData[1]->WorkLocal[6] == 815*) GOTO 0x0776
     0x076E [0x03] ExtData[1]->WorkLocal[20] = 1*
     0x0773 [0x01] GOTO 0x0776
     0x0776 [0x1B] RETURN
```
