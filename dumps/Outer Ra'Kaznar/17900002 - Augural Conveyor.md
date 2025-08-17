# 17900002 - Augural Conveyor

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Outer Ra'Kaznar (ID: 274) |
| Block Size       | 2148 bytes                |
| Total Events     | 5                         |
| References Count | 51                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [5500](#event-5500)   | 0x0001       |    556 |            120 |
| [5501](#event-5501)   | 0x022D       |      2 |              2 |
| [5503](#event-5503)   | 0x022F       |      3 |              3 |
| [5502](#event-5502)   | 0x0232       |   1344 |            289 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0005      |           5 |
|       2 | 0x0001      |           1 |
|       3 | 0x001F      |          31 |
|       4 | 0xFFFFFFFF  |  4294967295 |
|       5 | 0x1E5F      |        7775 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x0010      |          16 |
|       8 | 0x0012      |          18 |
|       9 | 0x000C      |          12 |
|      10 | 0x000F      |          15 |
|      11 | 0x0004      |           4 |
|      12 | 0x000B      |          11 |
|      13 | 0x001D      |          29 |
|      14 | 0x0003      |           3 |
|      15 | 0x1E4B      |        7755 |
|      16 | 0x1E4C      |        7756 |
|      17 | 0x1E53      |        7763 |
|      18 | 0x1E4E      |        7758 |
|      19 | 0x1E59      |        7769 |
|      20 | 0x1E58      |        7768 |
|      21 | 0x0002      |           2 |
|      22 | 0x0006      |           6 |
|      23 | 0x1E5A      |        7770 |
|      24 | 0x1E5B      |        7771 |
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
|      36 | 0x1E50      |        7760 |
|      37 | 0x003C      |          60 |
|      38 | 0x0078      |         120 |
|      39 | 0x1E4D      |        7757 |
|      40 | 0x005A      |          90 |
|      41 | 0x00C9      |         201 |
|      42 | 0x002D      |          45 |
|      43 | 0x00C8      |         200 |
|      44 | 0x000A      |          10 |
|      45 | 0x0335      |         821 |
|      46 | 0x0336      |         822 |
|      47 | 0x0337      |         823 |
|      48 | 0x032D      |         813 |
|      49 | 0x032E      |         814 |
|      50 | 0x032F      |         815 |

## String References

- **7755**: Only party members present with you in this area will be transported to [/this skirmish in ////this alluvion skirmish in /]$8.
- **7756**: Proceed? [Yes./No.]
- **7757**: Now entering [/a skirmish in ////an alluvion skirmish in /]$8.
- **7758**: You have chosen not to enter [/this skirmish in ////this alluvion skirmish in /]$8.
- **7760**: You cannot enter at this time. Please wait a moment and try again.
- **7763**: Your request for entry is being considered...
- **7768**: What's the torso's size? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]
- **7769**: What's the visage's obtainment rate? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]
- **7770**: What rank are the legs' benefits? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]
- **7771**: Ready for an alluvion skirmish? [No./Alluvion A./Alluvion B./Alluvion C./Alluvion D./Alluvion E./Just a regular skirmish, please.]
- **7775**: Enter which battlefield? [None./Endeavoring to Awaken./Endeavoring to Awaken./ /Behind the Sluices./Stonewalled./The Gates./Saved by the Bell./Quiescence./The Charlatan./Yggdrasil Beckons./Yggdrasil Beckons./Watery Grave./Mistress of Ceremonies./A Barrel of Laughs./Sinister Reign./The Ygnas Directive 6./Skirmishes./[Fractures/Obscured Domains]./Alluvion skirmishes./The Silent Forest./Wind of Eternity./Phantasmic Heroes.]

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
00F0: 77 03 40 00 80 0C 80 01  10 06 00 40 07 80 0D 80  w.@........@....
0100: 01 10 07 00 03 0D 00 01  10 01 33 01 1A 77 03 40  ..........3..w.@
0110: 00 80 0C 80 01 10 06 00  40 07 80 0D 80 01 10 07  ........@.......
0120: 00 03 0D 00 01 10 40 09  80 0A 80 01 10 0E 80 43  ......@........C
0130: 00 43 01 01 B7 01 02 0E  00 01 80 80 B7 01 3E 11  .C............>.
0140: 00 07 80 8D 01 03 01 10  00 80 40 09 80 0A 80 01  ..........@.....
0150: 10 01 80 43 00 43 01 03  05 00 02 10 03 00 00 03  ...C.C..........
0160: 10 03 01 00 04 10 03 02  00 05 10 03 03 00 06 10  ................
0170: 1A 77 03 40 00 80 0C 80  01 10 06 00 40 07 80 0D  .w.@........@...
0180: 80 01 10 07 00 03 0D 00  01 10 01 B4 01 1A 77 03  ..............w.
0190: 40 00 80 0C 80 01 10 06  00 40 07 80 0D 80 01 10  @........@......
01A0: 07 00 03 0D 00 01 10 40  09 80 0A 80 01 10 0E 80  .......@........
01B0: 43 00 43 01 01 B7 01 06  04 00 05 08 00 02 04 00  C.C.............
01C0: 00 80 00 0E 02 1A 10 02  03 03 10 0E 00 48 0F 80  .............H..
01D0: 23 24 10 80 08 00 00 80  25 02 00 10 00 80 00 ED  #$......%.......
01E0: 01 06 08 00 48 11 80 1A  7D 04 01 0B 02 02 00 10  ....H...}.......
01F0: 02 80 00 0B 02 03 01 10  06 80 1A 10 02 03 03 10  ................
0200: 0E 00 48 12 80 05 04 00  01 0B 02 01 BD 01 21 00  ..H...........!.
0210: 02 0E 00 02 80 80 1E 02  1A FC 03 01 2C 02 02 0E  ............,...
0220: 00 01 80 80 2C 02 1A FC  03 01 2C 02 1B           ....,.....,..   
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
 26: 0x0073 [0x24] CREATE_DIALOG(message_id=7775*, default_option=0*, option_flags=ExtData[1]->WorkLocal[15])
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
 51: 0x00EF [0x1A] CALL_SUBROUTINE(address=0x0377)
 52: 0x00F2 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 53: 0x00FB [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 54: 0x0104 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 55: 0x0109 [0x01] GOTO 0x0133
 56: 0x010C [0x1A] CALL_SUBROUTINE(address=0x0377)
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
 75: 0x0170 [0x1A] CALL_SUBROUTINE(address=0x0377)
 76: 0x0173 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 77: 0x017C [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 78: 0x0185 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 79: 0x018A [0x01] GOTO 0x01B4
 80: 0x018D [0x1A] CALL_SUBROUTINE(address=0x0377)
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
 93: 0x01CD [0x48] [System] [7755*]:
    → "Only party members present with you in this area will be transported to [/this skirmish in ////this alluvion skirmish in /]$8."
 94: 0x01D0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 95: 0x01D1 [0x24] CREATE_DIALOG(message_id=7756*, default_option=ExtData[1]->WorkLocal[8], option_flags=0*)
    → "Proceed? [Yes./No.]"
 96: 0x01D8 [0x25] WAIT_DIALOG_SELECT()
 97: 0x01D9 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01ED
 98: 0x01E1 [0x06] ExtData[1]->WorkLocal[8] = 0
 99: 0x01E4 [0x48] [System] [7763*]:
    → "Your request for entry is being considered..."
100: 0x01E7 [0x1A] CALL_SUBROUTINE(address=0x047D)
101: 0x01EA [0x01] GOTO 0x020B
102: 0x01ED [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x020B
103: 0x01F5 [0x03] Work_Zone[1] = 1073741824*
104: 0x01FA [0x1A] CALL_SUBROUTINE(address=0x0210)
105: 0x01FD [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
106: 0x0202 [0x48] [System] [7758*]:
    → "You have chosen not to enter [/this skirmish in ////this alluvion skirmish in /]$8."
107: 0x0205 [0x05] ExtData[1]->WorkLocal[4] = 1
108: 0x0208 [0x01] GOTO 0x020B

SUBROUTINE_020B:
109: 0x020B [0x01] GOTO 0x01BD
110: 0x020E [0x21] END_EVENT
111: 0x020F [0x00] END_REQSTACK()

SUBROUTINE_0210:
112: 0x0210 [0x02] IF !(ExtData[1]->WorkLocal[14] == 1*) GOTO 0x021E
113: 0x0218 [0x1A] CALL_SUBROUTINE(address=0x03FC)
114: 0x021B [0x01] GOTO 0x022C
115: 0x021E [0x02] IF !(ExtData[1]->WorkLocal[14] == 5*) GOTO 0x022C
116: 0x0226 [0x1A] CALL_SUBROUTINE(address=0x03FC)
117: 0x0229 [0x01] GOTO 0x022C

SUBROUTINE_022C:
118: 0x022C [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x008A [0x01] GOTO 0x008D
```

### Event 5501

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x022D  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                         21 00                  !. 
```

#### Opcodes

```
  0: 0x022D [0x21] END_EVENT
  1: 0x022E [0x00] END_REQSTACK()
```

### Event 5503

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x022F  |
| Data Size    | 3 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0220:                                               42                 B
0230: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x022F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0230 [0x21] END_EVENT
  2: 0x0231 [0x00] END_REQSTACK()
```

### Event 5502

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0232     |
| Data Size    | 1344 bytes |
| Instructions | 263        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0230:       42 03 05 00 02 10  06 00 00 06 01 00 06 02    B.............
0240: 00 06 03 00 24 13 80 00  80 00 80 25 02 00 10 00  ....$......%....
0250: 80 00 5E 02 03 01 10 06  80 21 00 01 5E 02 03 00  ..^......!..^...
0260: 00 00 10 24 14 80 00 80  00 80 25 02 00 10 00 80  ...$......%.....
0270: 00 7D 02 03 01 10 06 80  21 00 01 7D 02 03 01 00  .}......!..}....
0280: 00 10 06 01 10 03 03 10  15 80 03 04 10 0E 80 03  ................
0290: 05 10 0B 80 03 06 10 01  80 03 07 10 16 80 24 17  ..............$.
02A0: 80 00 80 00 80 25 02 00  10 00 80 00 B8 02 03 01  .....%..........
02B0: 10 06 80 21 00 01 B8 02  06 01 10 03 02 00 00 10  ...!............
02C0: 24 18 80 00 80 00 80 25  02 00 10 00 80 00 DA 02  $......%........
02D0: 03 01 10 06 80 21 00 01  DA 02 06 01 10 03 03 00  .....!..........
02E0: 00 10 02 03 00 16 80 00  EF 02 03 03 00 00 80 02  ................
02F0: 03 00 00 80 02 FF 02 03  0E 00 01 80 01 04 03 03  ................
0300: 0E 00 02 80 1A 77 03 40  00 80 0C 80 01 10 06 00  .....w.@........
0310: 40 07 80 0D 80 01 10 07  00 03 0D 00 01 10 06 04  @...............
0320: 00 05 08 00 02 04 00 00  80 00 75 03 1A FC 03 03  ..........u.....
0330: 03 10 0E 00 48 0F 80 23  24 10 80 08 00 00 80 25  ....H..#$......%
0340: 02 00 10 00 80 00 54 03  06 08 00 48 11 80 1A 7D  ......T....H...}
0350: 04 01 72 03 02 00 10 02  80 00 72 03 03 01 10 06  ..r.......r.....
0360: 80 1A FC 03 03 03 10 0E  00 48 12 80 05 04 00 01  .........H......
0370: 72 03 01 24 03 21 00 02  03 00 00 80 02 BD 03 02  r..$.!..........
0380: 05 00 00 80 80 8F 03 03  06 00 19 80 01 BA 03 02  ................
0390: 05 00 02 80 80 9F 03 03  06 00 1A 80 01 BA 03 02  ................
03A0: 05 00 15 80 80 AF 03 03  06 00 1B 80 01 BA 03 02  ................
03B0: 05 00 0E 80 80 BA 03 01  BA 03 01 D4 03 03 06 00  ................
03C0: 05 00 14 06 00 1C 80 07  06 00 01 00 0C 06 00 07  ................
03D0: 06 00 1D 80 06 07 00 40  00 80 15 80 07 00 00 00  .......@........
03E0: 40 0E 80 01 80 07 00 01  00 40 16 80 1C 80 07 00  @........@......
03F0: 02 00 40 1E 80 0C 80 07  00 03 00 1B 02 05 00 00  ..@.............
0400: 80 80 0C 04 03 02 10 1F  80 01 7C 04 02 05 00 02  ..........|.....
0410: 80 80 1C 04 03 02 10 20  80 01 7C 04 02 05 00 15  ....... ..|.....
0420: 80 80 2C 04 03 02 10 21  80 01 7C 04 02 05 00 0E  ..,....!..|.....
0430: 80 80 3C 04 03 02 10 22  80 01 7C 04 02 05 00 0B  ..<...."..|.....
0440: 80 80 4C 04 03 02 10 0B  80 01 7C 04 02 05 00 01  ..L.......|.....
0450: 80 80 5C 04 03 02 10 15  80 01 7C 04 02 05 00 16  ..\.......|.....
0460: 80 80 6C 04 03 02 10 15  80 01 7C 04 02 05 00 23  ..l.......|....#
0470: 80 80 7C 04 03 02 10 15  80 01 7C 04 1B 06 09 00  ..|.......|.....
0480: 06 0C 00 06 0A 00 02 09  00 00 80 00 AD 04 02 0C  ................
0490: 00 00 80 80 9C 04 1A AE  04 01 AA 04 02 0C 00 02  ................
04A0: 80 80 AA 04 1A 6F 05 01  AA 04 01 86 04 1B 03 01  .....o..........
04B0: 10 0D 00 40 09 80 0A 80  01 10 0C 00 43 00 43 01  ...@........C.C.
04C0: 03 0B 00 09 10 03 01 10  00 80 02 0B 00 02 80 80  ................
04D0: DA 04 03 0C 00 02 80 01  6E 05 02 0B 00 15 80 80  ........n.......
04E0: 00 05 0B 0A 00 02 0A 00  01 80 02 FA 04 05 09 00  ................
04F0: 48 24 80 23 1C 25 80 01  FD 04 1C 26 80 01 6E 05  H$.#.%.....&..n.
0500: 02 0B 00 0E 80 80 16 05  03 01 10 06 80 05 09 00  ................
0510: 05 04 00 01 6E 05 02 0B  00 0B 80 80 2C 05 03 01  ....n.......,...
0520: 10 06 80 05 09 00 05 04  00 01 6E 05 02 0B 00 01  ..........n.....
0530: 80 80 42 05 03 01 10 06  80 05 09 00 05 04 00 01  ..B.............
0540: 6E 05 02 0B 00 16 80 80  58 05 03 01 10 06 80 05  n.......X.......
0550: 09 00 05 04 00 01 6E 05  02 0B 00 23 80 80 6E 05  ......n....#..n.
0560: 03 01 10 06 80 05 09 00  05 04 00 01 6E 05 1B 03  ............n...
0570: 01 10 0D 00 40 09 80 0A  80 01 10 0C 00 43 00 43  ....@........C.C
0580: 01 03 01 10 00 80 03 0B  00 09 10 02 0B 00 0E 80  ................
0590: 80 9E 05 03 01 10 06 80  05 09 00 01 0B 07 02 0B  ................
05A0: 00 0B 80 80 B4 05 03 01  10 06 80 05 09 00 05 04  ................
05B0: 00 01 0B 07 02 0B 00 01  80 80 CA 05 03 01 10 06  ................
05C0: 80 05 09 00 05 04 00 01  0B 07 02 0B 00 16 80 80  ................
05D0: E0 05 03 01 10 06 80 05  09 00 05 04 00 01 0B 07  ................
05E0: 02 0B 00 23 80 80 F6 05  03 01 10 06 80 05 09 00  ...#............
05F0: 05 04 00 01 0B 07 02 0B  00 1C 80 80 AA 06 02 0E  ................
0600: 00 02 80 80 15 06 1A FC  03 03 03 10 0E 00 48 27  ..............H'
0610: 80 23 01 2C 06 02 0E 00  01 80 80 2C 06 1A FC 03  .#.,.......,....
0620: 03 03 10 0E 00 48 27 80  23 01 2C 06 62 02 80 F0  .....H'.#.,.b...
0630: FF FF 7F F0 FF FF 7F 6D  61 69 6E 00 80 1C 28 80  .......main...(.
0640: 45 29 80 F0 FF FF 7F F0  FF FF 7F 77 68 6F 31 00  E).........who1.
0650: 80 55 29 80 F0 FF FF 7F  F0 FF FF 7F 77 68 6F 31  .U).........who1
0660: 1C 2A 80 45 2B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  .*.E+.........fd
0670: 6F 31 00 80 55 2B 80 F0  FF FF 7F F0 FF FF 7F 66  o1..U+.........f
0680: 64 6F 31 45 29 80 F0 FF  FF 7F F0 FF FF 7F 77 68  do1E).........wh
0690: 69 31 00 80 1C 0A 80 30  05 09 00 05 04 00 40 00  i1.....0......@.
06A0: 80 23 80 01 10 1C 80 01  0B 07 02 0B 00 1E 80 80  .#..............
06B0: BD 06 03 01 10 06 80 05  09 00 01 0B 07 02 0B 00  ................
06C0: 2C 80 80 D3 06 03 01 10  06 80 05 09 00 05 04 00  ,...............
06D0: 01 0B 07 02 0B 00 0C 80  80 0B 07 0B 0A 00 02 0A  ................
06E0: 00 0A 80 02 05 07 03 01  10 0D 00 40 09 80 0A 80  ...........@....
06F0: 01 10 15 80 43 00 43 01  05 09 00 48 24 80 23 1C  ....C.C....H$.#.
0700: 25 80 01 08 07 1C 26 80  01 0B 07 1B 1B 1B 06 13  %.....&.........
0710: 00 02 06 00 2D 80 80 21  07 03 13 00 00 80 01 71  ....-..!.......q
0720: 07 02 06 00 2E 80 80 31  07 03 13 00 00 80 01 71  .......1.......q
0730: 07 02 06 00 2F 80 80 41  07 03 13 00 00 80 01 71  ..../..A.......q
0740: 07 02 06 00 30 80 80 51  07 03 13 00 02 80 01 71  ....0..Q.......q
0750: 07 02 06 00 31 80 80 61  07 03 13 00 02 80 01 71  ....1..a.......q
0760: 07 02 06 00 32 80 80 71  07 03 13 00 02 80 01 71  ....2..q.......q
0770: 07 1B                                             ..              
```

#### Opcodes

```
  0: 0x0232 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0233 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[2]
  2: 0x0238 [0x06] ExtData[1]->WorkLocal[0] = 0
  3: 0x023B [0x06] ExtData[1]->WorkLocal[1] = 0
  4: 0x023E [0x06] ExtData[1]->WorkLocal[2] = 0
  5: 0x0241 [0x06] ExtData[1]->WorkLocal[3] = 0
  6: 0x0244 [0x24] CREATE_DIALOG(message_id=7769*, default_option=0*, option_flags=0*)
    → "What's the visage's obtainment rate? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]"
  7: 0x024B [0x25] WAIT_DIALOG_SELECT()
  8: 0x024C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x025E
  9: 0x0254 [0x03] Work_Zone[1] = 1073741824*
 10: 0x0259 [0x21] END_EVENT
 11: 0x025A [0x00] END_REQSTACK()

SUBROUTINE_025E:
 12: 0x025E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[0]
 13: 0x0263 [0x24] CREATE_DIALOG(message_id=7768*, default_option=0*, option_flags=0*)
    → "What's the torso's size? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]"
 14: 0x026A [0x25] WAIT_DIALOG_SELECT()
 15: 0x026B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x027D
 16: 0x0273 [0x03] Work_Zone[1] = 1073741824*
 17: 0x0278 [0x21] END_EVENT
 18: 0x0279 [0x00] END_REQSTACK()

SUBROUTINE_027D:
 19: 0x027D [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[0]
 20: 0x0282 [0x06] Work_Zone[1] = 0
 21: 0x0285 [0x03] Work_Zone[3] = 2*
 22: 0x028A [0x03] Work_Zone[4] = 3*
 23: 0x028F [0x03] Work_Zone[5] = 4*
 24: 0x0294 [0x03] Work_Zone[6] = 5*
 25: 0x0299 [0x03] Work_Zone[7] = 6*
 26: 0x029E [0x24] CREATE_DIALOG(message_id=7770*, default_option=0*, option_flags=0*)
    → "What rank are the legs' benefits? [Never mind./Rank I./Rank II./Rank III./Rank IV./Rank V.]"
 27: 0x02A5 [0x25] WAIT_DIALOG_SELECT()
 28: 0x02A6 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02B8
 29: 0x02AE [0x03] Work_Zone[1] = 1073741824*
 30: 0x02B3 [0x21] END_EVENT
 31: 0x02B4 [0x00] END_REQSTACK()

SUBROUTINE_02B8:
 32: 0x02B8 [0x06] Work_Zone[1] = 0
 33: 0x02BB [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[0]
 34: 0x02C0 [0x24] CREATE_DIALOG(message_id=7771*, default_option=0*, option_flags=0*)
    → "Ready for an alluvion skirmish? [No./Alluvion A./Alluvion B./Alluvion C./Alluvion D./Alluvion E./Just a regular skirmish, please.]"
 35: 0x02C7 [0x25] WAIT_DIALOG_SELECT()
 36: 0x02C8 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02DA
 37: 0x02D0 [0x03] Work_Zone[1] = 1073741824*
 38: 0x02D5 [0x21] END_EVENT
 39: 0x02D6 [0x00] END_REQSTACK()

SUBROUTINE_02DA:
 40: 0x02DA [0x06] Work_Zone[1] = 0
 41: 0x02DD [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[0]
 42: 0x02E2 [0x02] IF !(ExtData[1]->WorkLocal[3] == 6*) GOTO 0x02EF
 43: 0x02EA [0x03] ExtData[1]->WorkLocal[3] = 0*
 44: 0x02EF [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x02FF
 45: 0x02F7 [0x03] ExtData[1]->WorkLocal[14] = 5*
 46: 0x02FC [0x01] GOTO 0x0304
 47: 0x02FF [0x03] ExtData[1]->WorkLocal[14] = 1*

SUBROUTINE_0304:
 48: 0x0304 [0x1A] CALL_SUBROUTINE(address=0x0377)
 49: 0x0307 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=11*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[6])
 50: 0x0310 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=29*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[7])
 51: 0x0319 [0x03] ExtData[1]->WorkLocal[13] = Work_Zone[1]
 52: 0x031E [0x06] ExtData[1]->WorkLocal[4] = 0
 53: 0x0321 [0x05] ExtData[1]->WorkLocal[8] = 1

SUBROUTINE_0324:
 54: 0x0324 [0x02] IF !(ExtData[1]->WorkLocal[4] == 0*) GOTO 0x0375
 55: 0x032C [0x1A] CALL_SUBROUTINE(address=0x03FC)
 56: 0x032F [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
 57: 0x0334 [0x48] [System] [7755*]:
    → "Only party members present with you in this area will be transported to [/this skirmish in ////this alluvion skirmish in /]$8."
 58: 0x0337 [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x0338 [0x24] CREATE_DIALOG(message_id=7756*, default_option=ExtData[1]->WorkLocal[8], option_flags=0*)
    → "Proceed? [Yes./No.]"
 60: 0x033F [0x25] WAIT_DIALOG_SELECT()
 61: 0x0340 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0354
 62: 0x0348 [0x06] ExtData[1]->WorkLocal[8] = 0
 63: 0x034B [0x48] [System] [7763*]:
    → "Your request for entry is being considered..."
 64: 0x034E [0x1A] CALL_SUBROUTINE(address=0x047D)
 65: 0x0351 [0x01] GOTO 0x0372
 66: 0x0354 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0372
 67: 0x035C [0x03] Work_Zone[1] = 1073741824*
 68: 0x0361 [0x1A] CALL_SUBROUTINE(address=0x03FC)
 69: 0x0364 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
 70: 0x0369 [0x48] [System] [7758*]:
    → "You have chosen not to enter [/this skirmish in ////this alluvion skirmish in /]$8."
 71: 0x036C [0x05] ExtData[1]->WorkLocal[4] = 1
 72: 0x036F [0x01] GOTO 0x0372

SUBROUTINE_0372:
 73: 0x0372 [0x01] GOTO 0x0324
 74: 0x0375 [0x21] END_EVENT
 75: 0x0376 [0x00] END_REQSTACK()

SUBROUTINE_0377:
 76: 0x0377 [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x03BD
 77: 0x037F [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x038F
 78: 0x0387 [0x03] ExtData[1]->WorkLocal[6] = 805*
 79: 0x038C [0x01] GOTO 0x03BA
 80: 0x038F [0x02] IF !(ExtData[1]->WorkLocal[5] == 1*) GOTO 0x039F
 81: 0x0397 [0x03] ExtData[1]->WorkLocal[6] = 807*
 82: 0x039C [0x01] GOTO 0x03BA
 83: 0x039F [0x02] IF !(ExtData[1]->WorkLocal[5] == 2*) GOTO 0x03AF
 84: 0x03A7 [0x03] ExtData[1]->WorkLocal[6] = 806*
 85: 0x03AC [0x01] GOTO 0x03BA
 86: 0x03AF [0x02] IF !(ExtData[1]->WorkLocal[5] == 3*) GOTO 0x03BA
 87: 0x03B7 [0x01] GOTO 0x03BA

SUBROUTINE_03BA:
 88: 0x03BA [0x01] GOTO 0x03D4
 89: 0x03BD [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[5]
 90: 0x03C2 [0x14] ExtData[1]->WorkLocal[6] *= 8*
 91: 0x03C7 [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[1]
 92: 0x03CC [0x0C] ExtData[1]->WorkLocal[6]--
 93: 0x03CF [0x07] ExtData[1]->WorkLocal[6] += 800*

SUBROUTINE_03D4:
 94: 0x03D4 [0x06] ExtData[1]->WorkLocal[7] = 0
 95: 0x03D7 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=2*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[0])
 96: 0x03E0 [0x40] SET_BIT_WORK_RANGE(start_bit=3*, end_bit=5*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[1])
 97: 0x03E9 [0x40] SET_BIT_WORK_RANGE(start_bit=6*, end_bit=8*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[2])
 98: 0x03F2 [0x40] SET_BIT_WORK_RANGE(start_bit=9*, end_bit=11*, target=ExtData[1]->WorkLocal[7], source=ExtData[1]->WorkLocal[3])
 99: 0x03FB [0x1B] RETURN

SUBROUTINE_03FC:
100: 0x03FC [0x02] IF !(ExtData[1]->WorkLocal[5] == 0*) GOTO 0x040C
101: 0x0404 [0x03] Work_Zone[2] = 259*
102: 0x0409 [0x01] GOTO 0x047C
103: 0x040C [0x02] IF !(ExtData[1]->WorkLocal[5] == 1*) GOTO 0x041C
104: 0x0414 [0x03] Work_Zone[2] = 264*
105: 0x0419 [0x01] GOTO 0x047C
106: 0x041C [0x02] IF !(ExtData[1]->WorkLocal[5] == 2*) GOTO 0x042C
107: 0x0424 [0x03] Work_Zone[2] = 271*
108: 0x0429 [0x01] GOTO 0x047C
109: 0x042C [0x02] IF !(ExtData[1]->WorkLocal[5] == 3*) GOTO 0x043C
110: 0x0434 [0x03] Work_Zone[2] = 275*
111: 0x0439 [0x01] GOTO 0x047C
112: 0x043C [0x02] IF !(ExtData[1]->WorkLocal[5] == 4*) GOTO 0x044C
113: 0x0444 [0x03] Work_Zone[2] = 4*
114: 0x0449 [0x01] GOTO 0x047C
115: 0x044C [0x02] IF !(ExtData[1]->WorkLocal[5] == 5*) GOTO 0x045C
116: 0x0454 [0x03] Work_Zone[2] = 2*
117: 0x0459 [0x01] GOTO 0x047C
118: 0x045C [0x02] IF !(ExtData[1]->WorkLocal[5] == 6*) GOTO 0x046C
119: 0x0464 [0x03] Work_Zone[2] = 2*
120: 0x0469 [0x01] GOTO 0x047C
121: 0x046C [0x02] IF !(ExtData[1]->WorkLocal[5] == 7*) GOTO 0x047C
122: 0x0474 [0x03] Work_Zone[2] = 2*
123: 0x0479 [0x01] GOTO 0x047C

SUBROUTINE_047C:
124: 0x047C [0x1B] RETURN

SUBROUTINE_047D:
125: 0x047D [0x06] ExtData[1]->WorkLocal[9] = 0
126: 0x0480 [0x06] ExtData[1]->WorkLocal[12] = 0
127: 0x0483 [0x06] ExtData[1]->WorkLocal[10] = 0

SUBROUTINE_0486:
128: 0x0486 [0x02] IF !(ExtData[1]->WorkLocal[9] == 0*) GOTO 0x04AD
129: 0x048E [0x02] IF !(ExtData[1]->WorkLocal[12] == 0*) GOTO 0x049C
130: 0x0496 [0x1A] CALL_SUBROUTINE(address=0x04AE)
131: 0x0499 [0x01] GOTO 0x04AA
132: 0x049C [0x02] IF !(ExtData[1]->WorkLocal[12] == 1*) GOTO 0x04AA
133: 0x04A4 [0x1A] CALL_SUBROUTINE(address=0x056F)
134: 0x04A7 [0x01] GOTO 0x04AA

SUBROUTINE_04AA:
135: 0x04AA [0x01] GOTO 0x0486
136: 0x04AD [0x1B] RETURN

SUBROUTINE_04AE:
137: 0x04AE [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
138: 0x04B3 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[12])
139: 0x04BC [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
140: 0x04BE [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
141: 0x04C0 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[9]
142: 0x04C5 [0x03] Work_Zone[1] = 0*
143: 0x04CA [0x02] IF !(ExtData[1]->WorkLocal[11] == 1*) GOTO 0x04DA
144: 0x04D2 [0x03] ExtData[1]->WorkLocal[12] = 1*
145: 0x04D7 [0x01] GOTO 0x056E
146: 0x04DA [0x02] IF !(ExtData[1]->WorkLocal[11] == 2*) GOTO 0x0500
147: 0x04E2 [0x0B] ExtData[1]->WorkLocal[10]++
148: 0x04E5 [0x02] IF !(ExtData[1]->WorkLocal[10] <= 5*) GOTO 0x04FA
149: 0x04ED [0x05] ExtData[1]->WorkLocal[9] = 1
150: 0x04F0 [0x48] [System] [7760*]:
    → "You cannot enter at this time. Please wait a moment and try again."
151: 0x04F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
152: 0x04F4 [0x1C] WAIT(60* ticks)
153: 0x04F7 [0x01] GOTO 0x04FD
154: 0x04FA [0x1C] WAIT(120* ticks)

SUBROUTINE_04FD:
155: 0x04FD [0x01] GOTO 0x056E
156: 0x0500 [0x02] IF !(ExtData[1]->WorkLocal[11] == 3*) GOTO 0x0516
157: 0x0508 [0x03] Work_Zone[1] = 1073741824*
158: 0x050D [0x05] ExtData[1]->WorkLocal[9] = 1
159: 0x0510 [0x05] ExtData[1]->WorkLocal[4] = 1
160: 0x0513 [0x01] GOTO 0x056E
161: 0x0516 [0x02] IF !(ExtData[1]->WorkLocal[11] == 4*) GOTO 0x052C
162: 0x051E [0x03] Work_Zone[1] = 1073741824*
163: 0x0523 [0x05] ExtData[1]->WorkLocal[9] = 1
164: 0x0526 [0x05] ExtData[1]->WorkLocal[4] = 1
165: 0x0529 [0x01] GOTO 0x056E
166: 0x052C [0x02] IF !(ExtData[1]->WorkLocal[11] == 5*) GOTO 0x0542
167: 0x0534 [0x03] Work_Zone[1] = 1073741824*
168: 0x0539 [0x05] ExtData[1]->WorkLocal[9] = 1
169: 0x053C [0x05] ExtData[1]->WorkLocal[4] = 1
170: 0x053F [0x01] GOTO 0x056E
171: 0x0542 [0x02] IF !(ExtData[1]->WorkLocal[11] == 6*) GOTO 0x0558
172: 0x054A [0x03] Work_Zone[1] = 1073741824*
173: 0x054F [0x05] ExtData[1]->WorkLocal[9] = 1
174: 0x0552 [0x05] ExtData[1]->WorkLocal[4] = 1
175: 0x0555 [0x01] GOTO 0x056E
176: 0x0558 [0x02] IF !(ExtData[1]->WorkLocal[11] == 7*) GOTO 0x056E
177: 0x0560 [0x03] Work_Zone[1] = 1073741824*
178: 0x0565 [0x05] ExtData[1]->WorkLocal[9] = 1
179: 0x0568 [0x05] ExtData[1]->WorkLocal[4] = 1
180: 0x056B [0x01] GOTO 0x056E

SUBROUTINE_056E:
181: 0x056E [0x1B] RETURN

SUBROUTINE_056F:
182: 0x056F [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
183: 0x0574 [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[12])
184: 0x057D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
185: 0x057F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
186: 0x0581 [0x03] Work_Zone[1] = 0*
187: 0x0586 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[9]
188: 0x058B [0x02] IF !(ExtData[1]->WorkLocal[11] == 3*) GOTO 0x059E
189: 0x0593 [0x03] Work_Zone[1] = 1073741824*
190: 0x0598 [0x05] ExtData[1]->WorkLocal[9] = 1
191: 0x059B [0x01] GOTO 0x070B
192: 0x059E [0x02] IF !(ExtData[1]->WorkLocal[11] == 4*) GOTO 0x05B4
193: 0x05A6 [0x03] Work_Zone[1] = 1073741824*
194: 0x05AB [0x05] ExtData[1]->WorkLocal[9] = 1
195: 0x05AE [0x05] ExtData[1]->WorkLocal[4] = 1
196: 0x05B1 [0x01] GOTO 0x070B
197: 0x05B4 [0x02] IF !(ExtData[1]->WorkLocal[11] == 5*) GOTO 0x05CA
198: 0x05BC [0x03] Work_Zone[1] = 1073741824*
199: 0x05C1 [0x05] ExtData[1]->WorkLocal[9] = 1
200: 0x05C4 [0x05] ExtData[1]->WorkLocal[4] = 1
201: 0x05C7 [0x01] GOTO 0x070B
202: 0x05CA [0x02] IF !(ExtData[1]->WorkLocal[11] == 6*) GOTO 0x05E0
203: 0x05D2 [0x03] Work_Zone[1] = 1073741824*
204: 0x05D7 [0x05] ExtData[1]->WorkLocal[9] = 1
205: 0x05DA [0x05] ExtData[1]->WorkLocal[4] = 1
206: 0x05DD [0x01] GOTO 0x070B
207: 0x05E0 [0x02] IF !(ExtData[1]->WorkLocal[11] == 7*) GOTO 0x05F6
208: 0x05E8 [0x03] Work_Zone[1] = 1073741824*
209: 0x05ED [0x05] ExtData[1]->WorkLocal[9] = 1
210: 0x05F0 [0x05] ExtData[1]->WorkLocal[4] = 1
211: 0x05F3 [0x01] GOTO 0x070B
212: 0x05F6 [0x02] IF !(ExtData[1]->WorkLocal[11] == 8*) GOTO 0x06AA
213: 0x05FE [0x02] IF !(ExtData[1]->WorkLocal[14] == 1*) GOTO 0x0615
214: 0x0606 [0x1A] CALL_SUBROUTINE(address=0x03FC)
215: 0x0609 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
216: 0x060E [0x48] [System] [7757*]:
    → "Now entering [/a skirmish in ////an alluvion skirmish in /]$8."
217: 0x0611 [0x23] WAIT_FOR_DIALOG_INTERACTION
218: 0x0612 [0x01] GOTO 0x062C
219: 0x0615 [0x02] IF !(ExtData[1]->WorkLocal[14] == 5*) GOTO 0x062C
220: 0x061D [0x1A] CALL_SUBROUTINE(address=0x03FC)
221: 0x0620 [0x03] Work_Zone[3] = ExtData[1]->WorkLocal[14]
222: 0x0625 [0x48] [System] [7757*]:
    → "Now entering [/a skirmish in ////an alluvion skirmish in /]$8."
223: 0x0628 [0x23] WAIT_FOR_DIALOG_INTERACTION
224: 0x0629 [0x01] GOTO 0x062C

SUBROUTINE_062C:
225: 0x062C [0x62] LOAD_EVENT_SCHEDULER: Load scheduler "main" with entities [LocalPlayer, LocalPlayer], work=[1*, 0*]
226: 0x063D [0x1C] WAIT(90* ticks)
227: 0x0640 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
228: 0x0651 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "who1" with entities [LocalPlayer, LocalPlayer], work=201*
229: 0x0660 [0x1C] WAIT(45* ticks)
230: 0x0663 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
231: 0x0674 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
232: 0x0683 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "whi1" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
233: 0x0694 [0x1C] WAIT(15* ticks)
234: 0x0697 [0x30] SET_UCOFF_CONTINUE_ZERO()
235: 0x0698 [0x05] ExtData[1]->WorkLocal[9] = 1
236: 0x069B [0x05] ExtData[1]->WorkLocal[4] = 1
237: 0x069E [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=7*, target=Work_Zone[1], source=8*)
238: 0x06A7 [0x01] GOTO 0x070B
239: 0x06AA [0x02] IF !(ExtData[1]->WorkLocal[11] == 9*) GOTO 0x06BD
240: 0x06B2 [0x03] Work_Zone[1] = 1073741824*
241: 0x06B7 [0x05] ExtData[1]->WorkLocal[9] = 1
242: 0x06BA [0x01] GOTO 0x070B
243: 0x06BD [0x02] IF !(ExtData[1]->WorkLocal[11] == 10*) GOTO 0x06D3
244: 0x06C5 [0x03] Work_Zone[1] = 1073741824*
245: 0x06CA [0x05] ExtData[1]->WorkLocal[9] = 1
246: 0x06CD [0x05] ExtData[1]->WorkLocal[4] = 1
247: 0x06D0 [0x01] GOTO 0x070B
248: 0x06D3 [0x02] IF !(ExtData[1]->WorkLocal[11] == 11*) GOTO 0x070B
249: 0x06DB [0x0B] ExtData[1]->WorkLocal[10]++
250: 0x06DE [0x02] IF !(ExtData[1]->WorkLocal[10] <= 15*) GOTO 0x0705
251: 0x06E6 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[13]
252: 0x06EB [0x40] SET_BIT_WORK_RANGE(start_bit=12*, end_bit=15*, target=Work_Zone[1], source=2*)
253: 0x06F4 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
254: 0x06F6 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
255: 0x06F8 [0x05] ExtData[1]->WorkLocal[9] = 1
256: 0x06FB [0x48] [System] [7760*]:
    → "You cannot enter at this time. Please wait a moment and try again."
257: 0x06FE [0x23] WAIT_FOR_DIALOG_INTERACTION
258: 0x06FF [0x1C] WAIT(60* ticks)
259: 0x0702 [0x01] GOTO 0x0708
260: 0x0705 [0x1C] WAIT(120* ticks)

SUBROUTINE_0708:
261: 0x0708 [0x01] GOTO 0x070B

SUBROUTINE_070B:
262: 0x070B [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x025B [0x01] GOTO 0x025E
# Dead code (unreachable instructions):
     0x027A [0x01] GOTO 0x027D
# Dead code (unreachable instructions):
     0x02B5 [0x01] GOTO 0x02B8
# Dead code (unreachable instructions):
     0x02D7 [0x01] GOTO 0x02DA
# Dead code (unreachable instructions):
     0x070C [0x1B] RETURN
     0x070D [0x1B] RETURN
     0x070E [0x06] ExtData[1]->WorkLocal[19] = 0
     0x0711 [0x02] IF !(ExtData[1]->WorkLocal[6] == 821*) GOTO 0x0721
     0x0719 [0x03] ExtData[1]->WorkLocal[19] = 0*
     0x071E [0x01] GOTO 0x0771
     0x0721 [0x02] IF !(ExtData[1]->WorkLocal[6] == 822*) GOTO 0x0731
     0x0729 [0x03] ExtData[1]->WorkLocal[19] = 0*
     0x072E [0x01] GOTO 0x0771
     0x0731 [0x02] IF !(ExtData[1]->WorkLocal[6] == 823*) GOTO 0x0741
     0x0739 [0x03] ExtData[1]->WorkLocal[19] = 0*
     0x073E [0x01] GOTO 0x0771
     0x0741 [0x02] IF !(ExtData[1]->WorkLocal[6] == 813*) GOTO 0x0751
     0x0749 [0x03] ExtData[1]->WorkLocal[19] = 1*
     0x074E [0x01] GOTO 0x0771
     0x0751 [0x02] IF !(ExtData[1]->WorkLocal[6] == 814*) GOTO 0x0761
     0x0759 [0x03] ExtData[1]->WorkLocal[19] = 1*
     0x075E [0x01] GOTO 0x0771
     0x0761 [0x02] IF !(ExtData[1]->WorkLocal[6] == 815*) GOTO 0x0771
     0x0769 [0x03] ExtData[1]->WorkLocal[19] = 1*
     0x076E [0x01] GOTO 0x0771
     0x0771 [0x1B] RETURN
```
