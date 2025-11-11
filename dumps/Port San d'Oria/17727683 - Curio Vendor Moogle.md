# 17727683 - Curio Vendor Moogle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 1064 bytes                |
| Total Events     | 3                         |
| References Count | 36                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [9600](#event-9600)   | 0x0001       |      5 |              3 |
| [9601](#event-9601)   | 0x0006       |    884 |            162 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2EEE      |       12014 |
|       1 | 0x40000000  |  1073741824 |
|       2 | 0x0000      |           0 |
|       3 | 0x2EEF      |       12015 |
|       4 | 0x2EF0      |       12016 |
|       5 | 0x2EF1      |       12017 |
|       6 | 0x2EF3      |       12019 |
|       7 | 0x2EF2      |       12018 |
|       8 | 0x2EF4      |       12020 |
|       9 | 0x0008      |           8 |
|      10 | 0x000F      |          15 |
|      11 | 0x0010      |          16 |
|      12 | 0x001F      |          31 |
|      13 | 0x2EF5      |       12021 |
|      14 | 0x0011      |          17 |
|      15 | 0x0012      |          18 |
|      16 | 0x000A      |          10 |
|      17 | 0x2EF6      |       12022 |
|      18 | 0x2EF7      |       12023 |
|      19 | 0x0001      |           1 |
|      20 | 0x1928      |        6440 |
|      21 | 0x2EF8      |       12024 |
|      22 | 0xFFFFFFFF  |  4294967295 |
|      23 | 0x0020      |          32 |
|      24 | 0x030F      |         783 |
|      25 | 0x0310      |         784 |
|      26 | 0x031A      |         794 |
|      27 | 0x031B      |         795 |
|      28 | 0x0339      |         825 |
|      29 | 0x033A      |         826 |
|      30 | 0x033B      |         827 |
|      31 | 0x037E      |         894 |
|      32 | 0x0384      |         900 |
|      33 | 0x0B6E      |        2926 |
|      34 | 0x03E8      |        1000 |
|      35 | 0x0002      |           2 |

## String References

- **6440**: You do not have enough gil.
- **12014**: I've set up shop at this site in search of souls to sell sundries to, kupo! Come back later for some glorious goodies!
- **12015**: Come hither, able adventurer! From precipitously perilous peaks to completely creepy caves, I've gathered glorious goodies to sell to one such as yourself!
- **12016**: Y-you don't seriously suspect I stole this sumptuous stash through some surreptitious scheme!? I assure you I acquired them on the up-and-up!
- **12017**: You won't find frivolous frauds here, only absolutely authentic articles, kupo!
- **12018**: Back to buy, kupo?
- **12019**: Tremendous timing! I've imported an incredible inventory of immaculate items!
- **12020**: What would you like? [Nothing for now./Medicine./Ammunition./Ninjutsu tools./Foodstuffs./Scrolls/materials./Keys./Equipment./Various key items.]
- **12021**: Get your hands on what? [None of these./$3: $17 gil./$3: $18 gil./$3: $19 gil./$3: $20 gil./$3: $21 gil./$3: $22 gil./$3: $23 gil./$3: $24 gil./$3: $25 gil./$3: $26 gil./$3: $27 gil./$3: $28 gil./$3: $29 gil./$3: $30 gil./$3: $31 gil./$3: $ gil./Previous page./Next page.]
- **12022**: $6 will run you $2 gil, kupo.
- **12023**: Purchase that item? ($0 gil) [Yes, please./No, thank you.]
- **12024**: Always a pleasure!

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

### Event 9600

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1A 0B 00 21 00                                  ...!.          
```

#### Opcodes

```
  0: 0x0001 [0x1A] CALL_SUBROUTINE(address=0x000B)
  1: 0x0004 [0x21] END_EVENT
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 9601

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0006    |
| Data Size    | 884 bytes |
| Instructions | 154       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   1A 1C  00 21 00 1E F0 FF FF 7F        ...!......
0010: 6F 70 1D 00 80 23 03 01  10 01 80 1B 03 00 00 03  op...#..........
0020: 10 03 01 00 04 10 03 03  00 05 10 03 02 00 06 10  ................
0030: 02 01 00 02 80 02 39 00  42 1E F0 FF FF 7F 6F 70  ......9.B.....op
0040: 02 01 00 02 80 02 66 00  02 00 00 02 80 00 5F 00  ......f......._.
0050: 1D 03 80 23 1D 04 80 23  1D 05 80 23 01 63 00 1D  ...#...#...#.c..
0060: 06 80 23 01 6A 00 1D 07  80 23 2E 06 05 00 06 04  ..#.j....#......
0070: 00 24 08 80 05 00 04 00  25 02 00 10 02 80 00 89  .$......%.......
0080: 00 03 01 10 01 80 01 89  00 03 05 00 00 10 02 05  ................
0090: 00 02 80 02 B6 00 02 05  00 09 80 00 A4 00 1A B7  ................
00A0: 00 01 B6 00 40 02 80 0A  80 01 10 05 00 40 0B 80  ....@........@..
00B0: 0C 80 01 10 02 80 1B 06  08 00 06 07 00 06 06 00  ................
00C0: 02 08 00 02 80 00 BC 01  1A BD 01 24 0D 80 07 00  ...........$....
00D0: 06 00 25 02 00 10 02 80  00 E6 00 05 08 00 03 01  ..%.............
00E0: 10 01 80 01 25 01 02 00  10 0E 80 00 FF 00 02 0A  ....%...........
00F0: 00 02 80 02 F9 00 0C 0A  00 06 07 00 01 25 01 02  .............%..
0100: 00 10 0F 80 00 25 01 03  0B 00 10 80 0C 0B 00 15  .....%..........
0110: 0B 00 0B 80 02 0A 00 0B  00 03 1F 01 0B 0A 00 06  ................
0120: 07 00 01 25 01 03 07 00  00 10 02 08 00 02 80 00  ...%............
0130: B9 01 03 10 00 0A 00 14  10 00 0B 80 07 10 00 07  ................
0140: 00 0C 10 00 9D 00 1A 03  03 10 10 00 9D 00 3A 03  ..............:.
0150: 04 10 10 00 03 02 10 03  00 1D 11 80 23 24 12 80  ............#$..
0160: 13 80 02 80 25 02 00 10  02 80 00 AE 01 02 03 00  ....%...........
0170: 04 10 03 7C 01 48 14 80  23 01 AB 01 40 02 80 0A  ...|.H..#...@...
0180: 80 01 10 05 00 40 0B 80  0C 80 01 10 10 00 43 00  .....@........C.
0190: 43 01 02 09 10 13 80 00  9D 01 01 A1 01 1D 15 80  C...............
01A0: 23 03 03 00 05 10 03 02  00 06 10 01 B9 01 02 00  #...............
01B0: 10 13 80 00 B9 01 01 B9  01 01 C0 00 1B 1A C0 02  ................
01C0: 03 09 00 0A 00 0B 09 00  14 09 00 0B 80 02 09 00  ................
01D0: 10 80 02 FB 01 03 09 00  10 80 3F 09 00 09 00 0B  ..........?.....
01E0: 80 03 0C 00 0A 00 14 0C  00 0B 80 03 0D 00 0C 00  ................
01F0: 07 0D 00 09 00 0C 0D 00  01 17 02 03 09 00 0B 80  ................
0200: 03 0C 00 0A 00 14 0C 00  0B 80 03 0D 00 0C 00 07  ................
0210: 0D 00 09 00 0C 0D 00 06  0F 00 02 0F 00 09 00 03  ................
0220: 61 02 03 0E 00 0A 00 14  0E 00 0B 80 07 0E 00 0F  a...............
0230: 00 03 10 00 0F 00 07 10  00 0B 80 9D 00 1A 03 0B  ................
0240: 00 0E 00 9D 05 DA 02 0B  00 0F 00 9D 00 3A 03 0B  .............:..
0250: 00 0E 00 9D 05 DA 02 0B  00 10 00 0B 0F 00 01 1A  ................
0260: 02 06 06 00 41 0C 00 0D  00 02 00 06 00 0F 06 00  ....A...........
0270: 16 80 40 09 00 0C 80 06  00 16 80 10 06 00 13 80  ..@.............
0280: 02 0A 00 02 80 02 92 02  3D 06 00 0E 80 13 80 01  ........=.......
0290: 99 02 3C 06 00 0E 80 13  80 03 0B 00 10 80 0C 0B  ..<.............
02A0: 00 15 0B 00 0B 80 02 0B  00 0A 00 02 B8 02 3D 06  ..............=.
02B0: 00 0F 80 13 80 01 BF 02  3C 06 00 0F 80 13 80 1B  ........<.......
02C0: 06 0F 00 02 0F 00 17 80  03 D9 02 9D 05 DA 02 02  ................
02D0: 80 0F 00 0B 0F 00 01 C3  02 1B 03 10 04 10 05 10  ................
02E0: 06 10 07 10 08 10 09 10  00 17 01 17 02 17 03 17  ................
02F0: 04 17 05 17 06 17 07 17  08 17 09 17 0A 17 0B 17  ................
0300: 0C 17 0D 17 0E 17 0F 17  10 17 11 17 12 17 13 17  ................
0310: 14 17 15 17 16 17 17 17  18 17 18 80 19 80 1A 80  ................
0320: 1B 80 1C 80 1D 80 1E 80  1F 80 20 80 21 80 02 80  .......... .!...
0330: 02 80 02 80 02 80 02 80  02 80 22 80 22 80 22 80  ..........".".".
0340: 22 80 22 80 22 80 22 80  22 80 22 80 22 80 02 80  "."."."."."."...
0350: 02 80 02 80 02 80 02 80  02 80 23 80 23 80 23 80  ..........#.#.#.
0360: 23 80 23 80 23 80 23 80  23 80 23 80 23 80 02 80  #.#.#.#.#.#.#...
0370: 02 80 02 80 02 80 02 80  02 80                    ..........      
```

#### Opcodes

```
  0: 0x0006 [0x1A] CALL_SUBROUTINE(address=0x001C)
  1: 0x0009 [0x21] END_EVENT
  2: 0x000A [0x00] END_REQSTACK()

SUBROUTINE_001C:
  3: 0x001C [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[3]
  4: 0x0021 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[4]
  5: 0x0026 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  6: 0x002B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[6]
  7: 0x0030 [0x02] IF !(ExtData[1]->WorkLocal[1] <= 0*) GOTO 0x0039
  8: 0x0038 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  9: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x0040 [0x02] IF !(ExtData[1]->WorkLocal[1] <= 0*) GOTO 0x0066
 13: 0x0048 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x005F
 14: 0x0050 [0x1D] PRINT_EVENT_MESSAGE(message_id=12015*)
    → "Come hither, able adventurer! From precipitously perilous peaks to completely creepy caves, I've gathered glorious goodies to sell to one such as yourself!"
 15: 0x0053 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=12016*)
    → "Y-you don't seriously suspect I stole this sumptuous stash through some surreptitious scheme!? I assure you I acquired them on the up-and-up!"
 17: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=12017*)
    → "You won't find frivolous frauds here, only absolutely authentic articles, kupo!"
 19: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x005C [0x01] GOTO 0x0063
 21: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=12019*)
    → "Tremendous timing! I've imported an incredible inventory of immaculate items!"
 22: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0063:
 23: 0x0063 [0x01] GOTO 0x006A
 24: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=12018*)
    → "Back to buy, kupo?"
 25: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_006A:
 26: 0x006A [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 27: 0x006B [0x06] ExtData[1]->WorkLocal[5] = 0
 28: 0x006E [0x06] ExtData[1]->WorkLocal[4] = 0
 29: 0x0071 [0x24] CREATE_DIALOG(message_id=12020*, default_option=ExtData[1]->WorkLocal[5], option_flags=ExtData[1]->WorkLocal[4])
    → "What would you like? [Nothing for now./Medicine./Ammunition./Ninjutsu tools./Foodstuffs./Scrolls/materials./Keys./Equipment./Various key items.]"
 30: 0x0078 [0x25] WAIT_DIALOG_SELECT()
 31: 0x0079 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0089
 32: 0x0081 [0x03] Work_Zone[1] = 1073741824*
 33: 0x0086 [0x01] GOTO 0x0089

SUBROUTINE_0089:
 34: 0x0089 [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[0]
 35: 0x008E [0x02] IF !(ExtData[1]->WorkLocal[5] <= 0*) GOTO 0x00B6
 36: 0x0096 [0x02] IF !(ExtData[1]->WorkLocal[5] == 8*) GOTO 0x00A4
 37: 0x009E [0x1A] CALL_SUBROUTINE(address=0x00B7)
 38: 0x00A1 [0x01] GOTO 0x00B6
 39: 0x00A4 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[5])
 40: 0x00AD [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=0*)

SUBROUTINE_00B6:
 41: 0x00B6 [0x1B] RETURN

SUBROUTINE_00B7:
 42: 0x00B7 [0x06] ExtData[1]->WorkLocal[8] = 0
 43: 0x00BA [0x06] ExtData[1]->WorkLocal[7] = 0
 44: 0x00BD [0x06] ExtData[1]->WorkLocal[6] = 0

SUBROUTINE_00C0:
 45: 0x00C0 [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x01BC
 46: 0x00C8 [0x1A] CALL_SUBROUTINE(address=0x01BD)
 47: 0x00CB [0x24] CREATE_DIALOG(message_id=12021*, default_option=ExtData[1]->WorkLocal[7], option_flags=ExtData[1]->WorkLocal[6])
    → "Get your hands on what? [None of these./$3: $17 gil./$3: $18 gil./$3: $19 gil./$3: $20 gil./$3: $21 gil./$3: $22 gil./$3: $23 gil./$3: $24 gil./$3: $25 gil./$3: $26 gil./$3: $27 gil./$3: $28 gil./$3: $29 gil./$3: $30 gil./$3: $31 gil./$3: $ gil./Previous page./Next page.]"
 48: 0x00D2 [0x25] WAIT_DIALOG_SELECT()
 49: 0x00D3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00E6
 50: 0x00DB [0x05] ExtData[1]->WorkLocal[8] = 1
 51: 0x00DE [0x03] Work_Zone[1] = 1073741824*
 52: 0x00E3 [0x01] GOTO 0x0125
 53: 0x00E6 [0x02] IF !(Work_Zone[0] == 17*) GOTO 0x00FF
 54: 0x00EE [0x02] IF !(ExtData[1]->WorkLocal[10] <= 0*) GOTO 0x00F9
 55: 0x00F6 [0x0C] ExtData[1]->WorkLocal[10]--
 56: 0x00F9 [0x06] ExtData[1]->WorkLocal[7] = 0
 57: 0x00FC [0x01] GOTO 0x0125
 58: 0x00FF [0x02] IF !(Work_Zone[0] == 18*) GOTO 0x0125
 59: 0x0107 [0x03] ExtData[1]->WorkLocal[11] = 10*
 60: 0x010C [0x0C] ExtData[1]->WorkLocal[11]--
 61: 0x010F [0x15] ExtData[1]->WorkLocal[11] /= 16*
 62: 0x0114 [0x02] IF !(ExtData[1]->WorkLocal[10] >= ExtData[1]->WorkLocal[11]) GOTO 0x011F
 63: 0x011C [0x0B] ExtData[1]->WorkLocal[10]++
 64: 0x011F [0x06] ExtData[1]->WorkLocal[7] = 0
 65: 0x0122 [0x01] GOTO 0x0125

SUBROUTINE_0125:
 66: 0x0125 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[0]
 67: 0x012A [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x01B9
 68: 0x0132 [0x03] ExtData[1]->WorkLocal[16] = ExtData[1]->WorkLocal[10]
 69: 0x0137 [0x14] ExtData[1]->WorkLocal[16] *= 16*
 70: 0x013C [0x07] ExtData[1]->WorkLocal[16] += ExtData[1]->WorkLocal[7]
 71: 0x0141 [0x0C] ExtData[1]->WorkLocal[16]--
 72: 0x0144 [0x9D] Work_Zone[3] = 0x031A[ExtData[1]->WorkLocal[16]] // Read WORD
 73: 0x014C [0x9D] Work_Zone[4] = 0x033A[ExtData[1]->WorkLocal[16]] // Read WORD
 74: 0x0154 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 75: 0x0159 [0x1D] PRINT_EVENT_MESSAGE(message_id=12022*)
    → "$6 will run you $2 gil, kupo."
 76: 0x015C [0x23] WAIT_FOR_DIALOG_INTERACTION
 77: 0x015D [0x24] CREATE_DIALOG(message_id=12023*, default_option=1*, option_flags=0*)
    → "Purchase that item? ($0 gil) [Yes, please./No, thank you.]"
 78: 0x0164 [0x25] WAIT_DIALOG_SELECT()
 79: 0x0165 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01AE
 80: 0x016D [0x02] IF !(ExtData[1]->WorkLocal[3] >= Work_Zone[4]) GOTO 0x017C
 81: 0x0175 [0x48] [System] [6440*]:
    → "You do not have enough gil."
 82: 0x0178 [0x23] WAIT_FOR_DIALOG_INTERACTION
 83: 0x0179 [0x01] GOTO 0x01AB
 84: 0x017C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=15*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[5])
 85: 0x0185 [0x40] SET_BIT_WORK_RANGE(start_bit=16*, end_bit=31*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[16])
 86: 0x018E [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 87: 0x0190 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 88: 0x0192 [0x02] IF !(Work_Zone[9] == 1*) GOTO 0x019D
 89: 0x019A [0x01] GOTO 0x01A1
 90: 0x019D [0x1D] PRINT_EVENT_MESSAGE(message_id=12024*)
    → "Always a pleasure!"
 91: 0x01A0 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_01A1:
 92: 0x01A1 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
 93: 0x01A6 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[6]

SUBROUTINE_01AB:
 94: 0x01AB [0x01] GOTO 0x01B9
 95: 0x01AE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01B9
 96: 0x01B6 [0x01] GOTO 0x01B9

SUBROUTINE_01B9:
 97: 0x01B9 [0x01] GOTO 0x00C0
 98: 0x01BC [0x1B] RETURN

SUBROUTINE_01BD:
 99: 0x01BD [0x1A] CALL_SUBROUTINE(address=0x02C0)
100: 0x01C0 [0x03] ExtData[1]->WorkLocal[9] = ExtData[1]->WorkLocal[10]
101: 0x01C5 [0x0B] ExtData[1]->WorkLocal[9]++
102: 0x01C8 [0x14] ExtData[1]->WorkLocal[9] *= 16*
103: 0x01CD [0x02] IF !(ExtData[1]->WorkLocal[9] <= 10*) GOTO 0x01FB
104: 0x01D5 [0x03] ExtData[1]->WorkLocal[9] = 10*
105: 0x01DA [0x3F] ExtData[1]->WorkLocal[9] = ExtData[1]->WorkLocal[9] % 16*
106: 0x01E1 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[10]
107: 0x01E6 [0x14] ExtData[1]->WorkLocal[12] *= 16*
108: 0x01EB [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[12]
109: 0x01F0 [0x07] ExtData[1]->WorkLocal[13] += ExtData[1]->WorkLocal[9]
110: 0x01F5 [0x0C] ExtData[1]->WorkLocal[13]--
111: 0x01F8 [0x01] GOTO 0x0217
112: 0x01FB [0x03] ExtData[1]->WorkLocal[9] = 16*
113: 0x0200 [0x03] ExtData[1]->WorkLocal[12] = ExtData[1]->WorkLocal[10]
114: 0x0205 [0x14] ExtData[1]->WorkLocal[12] *= 16*
115: 0x020A [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[12]
116: 0x020F [0x07] ExtData[1]->WorkLocal[13] += ExtData[1]->WorkLocal[9]
117: 0x0214 [0x0C] ExtData[1]->WorkLocal[13]--

SUBROUTINE_0217:
118: 0x0217 [0x06] ExtData[1]->WorkLocal[15] = 0

SUBROUTINE_021A:
119: 0x021A [0x02] IF !(ExtData[1]->WorkLocal[15] >= ExtData[1]->WorkLocal[9]) GOTO 0x0261
120: 0x0222 [0x03] ExtData[1]->WorkLocal[14] = ExtData[1]->WorkLocal[10]
121: 0x0227 [0x14] ExtData[1]->WorkLocal[14] *= 16*
122: 0x022C [0x07] ExtData[1]->WorkLocal[14] += ExtData[1]->WorkLocal[15]
123: 0x0231 [0x03] ExtData[1]->WorkLocal[16] = ExtData[1]->WorkLocal[15]
124: 0x0236 [0x07] ExtData[1]->WorkLocal[16] += 16*
125: 0x023B [0x9D] ExtData[1]->WorkLocal[11] = 0x031A[ExtData[1]->WorkLocal[14]] // Read WORD
126: 0x0243 [0x9D] 0x02DA[ExtData[1]->WorkLocal[15] * 2] = ExtData[1]->WorkLocal[11] // Write WORD
127: 0x024B [0x9D] ExtData[1]->WorkLocal[11] = 0x033A[ExtData[1]->WorkLocal[14]] // Read WORD
128: 0x0253 [0x9D] 0x02DA[ExtData[1]->WorkLocal[16] * 2] = ExtData[1]->WorkLocal[11] // Write WORD
129: 0x025B [0x0B] ExtData[1]->WorkLocal[15]++
130: 0x025E [0x01] GOTO 0x021A
131: 0x0261 [0x06] ExtData[1]->WorkLocal[6] = 0
132: 0x0264 [0x41] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[2] (bits ExtData[1]->WorkLocal[12]-ExtData[1]->WorkLocal[13])
133: 0x026D [0x0F] ExtData[1]->WorkLocal[6] ^= 4294967295*
134: 0x0272 [0x40] SET_BIT_WORK_RANGE(start_bit=ExtData[1]->WorkLocal[9], end_bit=31*, target=ExtData[1]->WorkLocal[6], source=4294967295*)
135: 0x027B [0x10] ExtData[1]->WorkLocal[6] <<= 1*
136: 0x0280 [0x02] IF !(ExtData[1]->WorkLocal[10] <= 0*) GOTO 0x0292
137: 0x0288 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[6], bit_index_work_offset=17*, condition_work_offset=1*)
138: 0x028F [0x01] GOTO 0x0299
139: 0x0292 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[6], bit_index_work_offset=17*, condition_work_offset=1*)

SUBROUTINE_0299:
140: 0x0299 [0x03] ExtData[1]->WorkLocal[11] = 10*
141: 0x029E [0x0C] ExtData[1]->WorkLocal[11]--
142: 0x02A1 [0x15] ExtData[1]->WorkLocal[11] /= 16*
143: 0x02A6 [0x02] IF !(ExtData[1]->WorkLocal[11] <= ExtData[1]->WorkLocal[10]) GOTO 0x02B8
144: 0x02AE [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[6], bit_index_work_offset=18*, condition_work_offset=1*)
145: 0x02B5 [0x01] GOTO 0x02BF
146: 0x02B8 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[6], bit_index_work_offset=18*, condition_work_offset=1*)

SUBROUTINE_02BF:
147: 0x02BF [0x1B] RETURN

SUBROUTINE_02C0:
148: 0x02C0 [0x06] ExtData[1]->WorkLocal[15] = 0

SUBROUTINE_02C3:
149: 0x02C3 [0x02] IF !(ExtData[1]->WorkLocal[15] >= 32*) GOTO 0x02D9
150: 0x02CB [0x9D] 0x02DA[ExtData[1]->WorkLocal[15] * 2] = 0* // Write WORD
151: 0x02D3 [0x0B] ExtData[1]->WorkLocal[15]++
152: 0x02D6 [0x01] GOTO 0x02C3
153: 0x02D9 [0x1B] RETURN
```

#### Data or dead code:

```
# Data Section: 0x02DA (160 bytes)
     0x02DA: 03 10 04 10 05 10 06 10 07 10 08 10 09 10 00 17
     0x02EA: 01 17 02 17 03 17 04 17 05 17 06 17 07 17 08 17
     0x02FA: 09 17 0A 17 0B 17 0C 17 0D 17 0E 17 0F 17 10 17
     0x030A: 11 17 12 17 13 17 14 17 15 17 16 17 17 17 18 17
     0x031A: 18 80 19 80 1A 80 1B 80 1C 80 1D 80 1E 80 1F 80
     0x032A: 20 80 21 80 02 80 02 80 02 80 02 80 02 80 02 80
     0x033A: 22 80 22 80 22 80 22 80 22 80 22 80 22 80 22 80
     0x034A: 22 80 22 80 02 80 02 80 02 80 02 80 02 80 02 80
     0x035A: 23 80 23 80 23 80 23 80 23 80 23 80 23 80 23 80
     0x036A: 23 80 23 80 02 80 02 80 02 80 02 80 02 80 02 80
# Dead code (unreachable instructions):
     0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
     0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
     0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
     0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=12014*)
    → "I've set up shop at this site in search of souls to sell sundries to, kupo! Come back later for some glorious goodies!"
     0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0016 [0x03] Work_Zone[1] = 1073741824*
     0x001B [0x1B] RETURN
```
