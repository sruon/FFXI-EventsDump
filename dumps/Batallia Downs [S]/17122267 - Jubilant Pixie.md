# 17122267 - Jubilant Pixie

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 880 bytes                   |
| Total Events     | 3                           |
| References Count | 57                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [4003](#event-4003)   | 0x0001       |    590 |            124 |
| [4004](#event-4004)   | 0x024F       |     33 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0003      |           3 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0006      |           6 |
|       4 | 0x0007      |           7 |
|       5 | 0x0009      |           9 |
|       6 | 0x0005      |           5 |
|       7 | 0x000A      |          10 |
|       8 | 0x2062      |        8290 |
|       9 | 0x4849      |       18505 |
|      10 | 0x0002      |           2 |
|      11 | 0x494C      |       18764 |
|      12 | 0x49B6      |       18870 |
|      13 | 0x0004      |           4 |
|      14 | 0x4A0A      |       18954 |
|      15 | 0x4561      |       17761 |
|      16 | 0x4AAB      |       19115 |
|      17 | 0x4562      |       17762 |
|      18 | 0x0008      |           8 |
|      19 | 0x4A0B      |       18955 |
|      20 | 0x462E      |       17966 |
|      21 | 0x4AAC      |       19116 |
|      22 | 0x000B      |          11 |
|      23 | 0x4930      |       18736 |
|      24 | 0x000C      |          12 |
|      25 | 0x4814      |       18452 |
|      26 | 0x000D      |          13 |
|      27 | 0x4B4B      |       19275 |
|      28 | 0x000E      |          14 |
|      29 | 0x4B67      |       19303 |
|      30 | 0x000F      |          15 |
|      31 | 0x48A9      |       18601 |
|      32 | 0x0010      |          16 |
|      33 | 0x4563      |       17763 |
|      34 | 0x0011      |          17 |
|      35 | 0x4931      |       18737 |
|      36 | 0x0012      |          18 |
|      37 | 0x494D      |       18765 |
|      38 | 0x0013      |          19 |
|      39 | 0x4AAD      |       19117 |
|      40 | 0x0014      |          20 |
|      41 | 0x48AA      |       18602 |
|      42 | 0x2063      |        8291 |
|      43 | 0x2064      |        8292 |
|      44 | 0x00C9      |         201 |
|      45 | 0x2065      |        8293 |
|      46 | 0x0065      |         101 |
|      47 | 0x03E7      |         999 |
|      48 | 0x00CA      |         202 |
|      49 | 0x2067      |        8295 |
|      50 | 0x2068      |        8296 |
|      51 | 0x0066      |         102 |
|      52 | 0x2069      |        8297 |
|      53 | 0x206A      |        8298 |
|      54 | 0x206B      |        8299 |
|      55 | 0x206C      |        8300 |
|      56 | 0x206D      |        8301 |

## String References

- **8290**: By my troth, what a thrilling battle! When thou landed the felling blow, a shiver ran down my wings! As promised, here is thy reward.
- **8291**: Dost thou find this enchantment to thy liking?
- **8292**: Accept the item? [Accept./Refuse. ($0 times remaining)]
- **8293**: Splendid! May it serve thee well.
- **8295**: Ah, 'tis unfortunate. Sadly, my folk are not well-versed in the penchants of adventurers these days...
- **8296**: In that event, we shall prepare thy weapon to be enchanted anew. May thou be once more triumphant in battle anon!
- **8297**: What's this? 'Twould appear that thy weapon can endure no further enchantments.
- **8298**: Though it may fall short of thy expectations, pray accept it.
- **8299**: Otherwise, we shall have no choice but to dispose of it.
- **8300**: Many thanks for thine assistance!
- **8301**: Pray accept this $0 as but a humble token of our gratitude.

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

### Event 4003

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 590 bytes |
| Instructions | 124       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 00 80 41 01  80 01 80 02 10 01 00 41   .....A........A
0010: 02 80 03 80 02 10 02 00  41 04 80 05 80 02 10 09  ........A.......
0020: 00 03 03 00 06 80 08 03  00 09 00 03 05 00 03 10  ................
0030: 03 06 00 04 10 03 07 00  05 10 41 01 80 01 80 06  ..........A.....
0040: 10 08 00 20 01 1C 07 80  1E F0 FF FF 7F 6F 70 1D  ... .........op.
0050: 08 80 23 02 02 00 02 80  80 63 00 03 04 00 09 80  ..#......c......
0060: 01 93 01 02 02 00 0A 80  80 73 00 03 04 00 0B 80  .........s......
0070: 01 93 01 02 02 00 00 80  80 83 00 03 04 00 0C 80  ................
0080: 01 93 01 02 02 00 0D 80  80 93 00 03 04 00 0E 80  ................
0090: 01 93 01 02 02 00 06 80  80 A3 00 03 04 00 0F 80  ................
00A0: 01 93 01 02 02 00 03 80  80 B3 00 03 04 00 10 80  ................
00B0: 01 93 01 02 02 00 04 80  80 C3 00 03 04 00 11 80  ................
00C0: 01 93 01 02 02 00 12 80  80 D3 00 03 04 00 13 80  ................
00D0: 01 93 01 02 02 00 05 80  80 E3 00 03 04 00 14 80  ................
00E0: 01 93 01 02 02 00 07 80  80 F3 00 03 04 00 15 80  ................
00F0: 01 93 01 02 02 00 16 80  80 03 01 03 04 00 17 80  ................
0100: 01 93 01 02 02 00 18 80  80 13 01 03 04 00 19 80  ................
0110: 01 93 01 02 02 00 1A 80  80 23 01 03 04 00 1B 80  .........#......
0120: 01 93 01 02 02 00 1C 80  80 33 01 03 04 00 1D 80  .........3......
0130: 01 93 01 02 02 00 1E 80  80 43 01 03 04 00 1F 80  .........C......
0140: 01 93 01 02 02 00 20 80  80 53 01 03 04 00 21 80  ...... ..S....!.
0150: 01 93 01 02 02 00 22 80  80 63 01 03 04 00 23 80  ......"..c....#.
0160: 01 93 01 02 02 00 24 80  80 73 01 03 04 00 25 80  ......$..s....%.
0170: 01 93 01 02 02 00 26 80  80 83 01 03 04 00 27 80  ......&.......'.
0180: 01 93 01 02 02 00 28 80  80 93 01 03 04 00 29 80  ......(.......).
0190: 01 93 01 CC 01 04 00 05  00 06 00 07 00 1D 2A 80  ..............*.
01A0: 23 93 01 80 03 02 10 03  00 24 2B 80 01 80 01 80  #........$+.....
01B0: 25 02 00 10 01 80 00 FC  01 03 01 10 2C 80 43 00  %...........,.C.
01C0: 43 01 03 0A 00 02 10 02  0A 00 00 80 00 F4 01 1D  C...............
01D0: 2D 80 23 03 01 10 2E 80  02 08 00 01 80 00 F1 01  -.#.............
01E0: 45 2C 80 F8 FF FF 7F F8  FF FF 7F 71 73 74 63 01  E,.........qstc.
01F0: 80 01 F9 01 03 01 10 2F  80 01 4C 02 02 00 10 02  ......./..L.....
0200: 80 00 4C 02 03 01 10 30  80 43 00 43 01 03 0A 00  ..L....0.C.C....
0210: 02 10 02 0A 00 00 80 00  44 02 02 03 00 01 80 02  ........D.......
0220: 32 02 1D 31 80 23 1D 32  80 23 03 01 10 33 80 01  2..1.#.2.#...3..
0230: 41 02 1D 34 80 23 1D 35  80 23 1D 36 80 23 01 A4  A..4.#.5.#.6.#..
0240: 01 01 49 02 03 01 10 2F  80 01 4C 02 42 21 00     ..I..../..L.B!. 
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = 3*
  1: 0x0006 [0x41] ExtData[1]->WorkLocal[1] = Work_Zone[2] (bits 0*-0*)
  2: 0x000F [0x41] ExtData[1]->WorkLocal[2] = Work_Zone[2] (bits 1*-6*)
  3: 0x0018 [0x41] ExtData[1]->WorkLocal[9] = Work_Zone[2] (bits 7*-9*)
  4: 0x0021 [0x03] ExtData[1]->WorkLocal[3] = 5*
  5: 0x0026 [0x08] ExtData[1]->WorkLocal[3] -= ExtData[1]->WorkLocal[9]
  6: 0x002B [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[3]
  7: 0x0030 [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[4]
  8: 0x0035 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[5]
  9: 0x003A [0x41] ExtData[1]->WorkLocal[8] = Work_Zone[6] (bits 0*-0*)
 10: 0x0043 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
 11: 0x0045 [0x1C] WAIT(10* ticks)
 12: 0x0048 [0x1E] EventEntity looks at LocalPlayer and starts talking
 13: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x004E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 15: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=8290*)
    → "By my troth, what a thrilling battle! When thou landed the felling blow, a shiver ran down my wings! As promised, here is thy reward."
 16: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0053 [0x02] IF !(ExtData[1]->WorkLocal[2] == 1*) GOTO 0x0063
 18: 0x005B [0x03] ExtData[1]->WorkLocal[4] = 18505*
 19: 0x0060 [0x01] GOTO 0x0193
 20: 0x0063 [0x02] IF !(ExtData[1]->WorkLocal[2] == 2*) GOTO 0x0073
 21: 0x006B [0x03] ExtData[1]->WorkLocal[4] = 18764*
 22: 0x0070 [0x01] GOTO 0x0193
 23: 0x0073 [0x02] IF !(ExtData[1]->WorkLocal[2] == 3*) GOTO 0x0083
 24: 0x007B [0x03] ExtData[1]->WorkLocal[4] = 18870*
 25: 0x0080 [0x01] GOTO 0x0193
 26: 0x0083 [0x02] IF !(ExtData[1]->WorkLocal[2] == 4*) GOTO 0x0093
 27: 0x008B [0x03] ExtData[1]->WorkLocal[4] = 18954*
 28: 0x0090 [0x01] GOTO 0x0193
 29: 0x0093 [0x02] IF !(ExtData[1]->WorkLocal[2] == 5*) GOTO 0x00A3
 30: 0x009B [0x03] ExtData[1]->WorkLocal[4] = 17761*
 31: 0x00A0 [0x01] GOTO 0x0193
 32: 0x00A3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 6*) GOTO 0x00B3
 33: 0x00AB [0x03] ExtData[1]->WorkLocal[4] = 19115*
 34: 0x00B0 [0x01] GOTO 0x0193
 35: 0x00B3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 7*) GOTO 0x00C3
 36: 0x00BB [0x03] ExtData[1]->WorkLocal[4] = 17762*
 37: 0x00C0 [0x01] GOTO 0x0193
 38: 0x00C3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 8*) GOTO 0x00D3
 39: 0x00CB [0x03] ExtData[1]->WorkLocal[4] = 18955*
 40: 0x00D0 [0x01] GOTO 0x0193
 41: 0x00D3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 9*) GOTO 0x00E3
 42: 0x00DB [0x03] ExtData[1]->WorkLocal[4] = 17966*
 43: 0x00E0 [0x01] GOTO 0x0193
 44: 0x00E3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 10*) GOTO 0x00F3
 45: 0x00EB [0x03] ExtData[1]->WorkLocal[4] = 19116*
 46: 0x00F0 [0x01] GOTO 0x0193
 47: 0x00F3 [0x02] IF !(ExtData[1]->WorkLocal[2] == 11*) GOTO 0x0103
 48: 0x00FB [0x03] ExtData[1]->WorkLocal[4] = 18736*
 49: 0x0100 [0x01] GOTO 0x0193
 50: 0x0103 [0x02] IF !(ExtData[1]->WorkLocal[2] == 12*) GOTO 0x0113
 51: 0x010B [0x03] ExtData[1]->WorkLocal[4] = 18452*
 52: 0x0110 [0x01] GOTO 0x0193
 53: 0x0113 [0x02] IF !(ExtData[1]->WorkLocal[2] == 13*) GOTO 0x0123
 54: 0x011B [0x03] ExtData[1]->WorkLocal[4] = 19275*
 55: 0x0120 [0x01] GOTO 0x0193
 56: 0x0123 [0x02] IF !(ExtData[1]->WorkLocal[2] == 14*) GOTO 0x0133
 57: 0x012B [0x03] ExtData[1]->WorkLocal[4] = 19303*
 58: 0x0130 [0x01] GOTO 0x0193
 59: 0x0133 [0x02] IF !(ExtData[1]->WorkLocal[2] == 15*) GOTO 0x0143
 60: 0x013B [0x03] ExtData[1]->WorkLocal[4] = 18601*
 61: 0x0140 [0x01] GOTO 0x0193
 62: 0x0143 [0x02] IF !(ExtData[1]->WorkLocal[2] == 16*) GOTO 0x0153
 63: 0x014B [0x03] ExtData[1]->WorkLocal[4] = 17763*
 64: 0x0150 [0x01] GOTO 0x0193
 65: 0x0153 [0x02] IF !(ExtData[1]->WorkLocal[2] == 17*) GOTO 0x0163
 66: 0x015B [0x03] ExtData[1]->WorkLocal[4] = 18737*
 67: 0x0160 [0x01] GOTO 0x0193
 68: 0x0163 [0x02] IF !(ExtData[1]->WorkLocal[2] == 18*) GOTO 0x0173
 69: 0x016B [0x03] ExtData[1]->WorkLocal[4] = 18765*
 70: 0x0170 [0x01] GOTO 0x0193
 71: 0x0173 [0x02] IF !(ExtData[1]->WorkLocal[2] == 19*) GOTO 0x0183
 72: 0x017B [0x03] ExtData[1]->WorkLocal[4] = 19117*
 73: 0x0180 [0x01] GOTO 0x0193
 74: 0x0183 [0x02] IF !(ExtData[1]->WorkLocal[2] == 20*) GOTO 0x0193
 75: 0x018B [0x03] ExtData[1]->WorkLocal[4] = 18602*
 76: 0x0190 [0x01] GOTO 0x0193

SUBROUTINE_0193:
 77: 0x0193 [0xCC] ITEM_INFO_WINDOW_HANDLER(case=0x01 - Open item info window (with chase), check_value=ExtData[1]->WorkLocal[4], buffer1=ExtData[1]->WorkLocal[5], buffer2=ExtData[1]->WorkLocal[6], buffer3=ExtData[1]->WorkLocal[7])
 78: 0x019D [0x1D] PRINT_EVENT_MESSAGE(message_id=8291*)
    → "Dost thou find this enchantment to thy liking?"
 79: 0x01A0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x01A1 [0x93] DISPLAY_ITEM_INFO(item_id=0*)

SUBROUTINE_01A4:
 81: 0x01A4 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[3]
 82: 0x01A9 [0x24] CREATE_DIALOG(message_id=8292*, default_option=0*, option_flags=0*)
    → "Accept the item? [Accept./Refuse. ($0 times remaining)]"
 83: 0x01B0 [0x25] WAIT_DIALOG_SELECT()
 84: 0x01B1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01FC
 85: 0x01B9 [0x03] Work_Zone[1] = 201*
 86: 0x01BE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 87: 0x01C0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 88: 0x01C2 [0x03] ExtData[1]->WorkLocal[10] = Work_Zone[2]
 89: 0x01C7 [0x02] IF !(ExtData[1]->WorkLocal[10] == 3*) GOTO 0x01F4
 90: 0x01CF [0x1D] PRINT_EVENT_MESSAGE(message_id=8293*)
    → "Splendid! May it serve thee well."
 91: 0x01D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 92: 0x01D3 [0x03] Work_Zone[1] = 101*
 93: 0x01D8 [0x02] IF !(ExtData[1]->WorkLocal[8] == 0*) GOTO 0x01F1
 94: 0x01E0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 95: 0x01F1 [0x01] GOTO 0x01F9
 96: 0x01F4 [0x03] Work_Zone[1] = 999*

SUBROUTINE_01F9:
 97: 0x01F9 [0x01] GOTO 0x024C
 98: 0x01FC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x024C
 99: 0x0204 [0x03] Work_Zone[1] = 202*
100: 0x0209 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
101: 0x020B [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
102: 0x020D [0x03] ExtData[1]->WorkLocal[10] = Work_Zone[2]
103: 0x0212 [0x02] IF !(ExtData[1]->WorkLocal[10] == 3*) GOTO 0x0244
104: 0x021A [0x02] IF !(ExtData[1]->WorkLocal[3] <= 0*) GOTO 0x0232
105: 0x0222 [0x1D] PRINT_EVENT_MESSAGE(message_id=8295*)
    → "Ah, 'tis unfortunate. Sadly, my folk are not well-versed in the penchants of adventurers these days..."
106: 0x0225 [0x23] WAIT_FOR_DIALOG_INTERACTION
107: 0x0226 [0x1D] PRINT_EVENT_MESSAGE(message_id=8296*)
    → "In that event, we shall prepare thy weapon to be enchanted anew. May thou be once more triumphant in battle anon!"
108: 0x0229 [0x23] WAIT_FOR_DIALOG_INTERACTION
109: 0x022A [0x03] Work_Zone[1] = 102*
110: 0x022F [0x01] GOTO 0x0241
111: 0x0232 [0x1D] PRINT_EVENT_MESSAGE(message_id=8297*)
    → "What's this? 'Twould appear that thy weapon can endure no further enchantments."
112: 0x0235 [0x23] WAIT_FOR_DIALOG_INTERACTION
113: 0x0236 [0x1D] PRINT_EVENT_MESSAGE(message_id=8298*)
    → "Though it may fall short of thy expectations, pray accept it."
114: 0x0239 [0x23] WAIT_FOR_DIALOG_INTERACTION
115: 0x023A [0x1D] PRINT_EVENT_MESSAGE(message_id=8299*)
    → "Otherwise, we shall have no choice but to dispose of it."
116: 0x023D [0x23] WAIT_FOR_DIALOG_INTERACTION
117: 0x023E [0x01] GOTO 0x01A4

SUBROUTINE_0241:
118: 0x0241 [0x01] GOTO 0x0249
119: 0x0244 [0x03] Work_Zone[1] = 999*

SUBROUTINE_0249:
120: 0x0249 [0x01] GOTO 0x024C

SUBROUTINE_024C:
121: 0x024C [0x42] SET_CLI_EVENT_CANCEL_DATA()
122: 0x024D [0x21] END_EVENT
123: 0x024E [0x00] END_REQSTACK()
```

### Event 4004

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x024F   |
| Data Size    | 33 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0240:                                               03                 .
0250: 0B 00 02 10 20 01 1C 07  80 1E F0 FF FF 7F 6F 70  .... .........op
0260: 1D 37 80 23 03 02 10 0B  00 1D 38 80 23 42 21 00  .7.#......8.#B!.
```

#### Opcodes

```
  0: 0x024F [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[2]
  1: 0x0254 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x0256 [0x1C] WAIT(10* ticks)
  3: 0x0259 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x025E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x025F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0260 [0x1D] PRINT_EVENT_MESSAGE(message_id=8300*)
    → "Many thanks for thine assistance!"
  7: 0x0263 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0264 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[11]
  9: 0x0269 [0x1D] PRINT_EVENT_MESSAGE(message_id=8301*)
    → "Pray accept this $0 as but a humble token of our gratitude."
 10: 0x026C [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x026D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x026E [0x21] END_EVENT
 13: 0x026F [0x00] END_REQSTACK()
```
