# 17662775 - Event Master

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - Misareaux (ID: 216) |
| Block Size       | 1340 bytes                    |
| Total Events     | 2                             |
| References Count | 22                            |

## List of Events

| Event ID          | Entrypoint   |   Size |   Instructions |
|-------------------|--------------|--------|----------------|
| [301](#event-301) | 0x0000       |   1225 |            214 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2121      |        8481 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0x0032      |          50 |
|       4 | 0x0017      |          23 |
|       5 | 0x0018      |          24 |
|       6 | 0x001F      |          31 |
|       7 | 0x000D      |          13 |
|       8 | 0x00FF      |         255 |
|       9 | 0x0013      |          19 |
|      10 | 0x0002      |           2 |
|      11 | 0x2122      |        8482 |
|      12 | 0x0003      |           3 |
|      13 | 0x0004      |           4 |
|      14 | 0x0005      |           5 |
|      15 | 0x0006      |           6 |
|      16 | 0x0007      |           7 |
|      17 | 0x0008      |           8 |
|      18 | 0x0009      |           9 |
|      19 | 0x000A      |          10 |
|      20 | 0x000B      |          11 |
|      21 | 0x000C      |          12 |

## String References

- **8481**: What will you be doing? [Setting Fame./Contamination level./QS01: Missing in Action./QS02: I Dream of Flowers./QS03: Destiny Odyssey./QS04: Unidentified Research Object./QS05: Cookbook of Hope Bestowing./QS06: Smoke over the Coast./QS07: Soil and Green (Soil Quality)/QS07: Soil and Green (Fertilizer)/QS08: Dropping the Bomb./QS09: Wanted: Medical Supplies./Everything./Never mind.]
- **8482**: Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]

## Events

### Event 301

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x0000     |
| Data Size    | 1225 bytes |
| Instructions | 20         |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 24 00 80 01 80 01 80 25  02 00 10 01 80 00 50 00  $......%......P.
0010: 71 10 02 80 71 11 02 10  02 02 10 01 80 03 28 00  q...q.........(.
0020: 03 02 10 01 80 01 35 00  02 02 10 03 80 02 35 00  ......5.......5.
0030: 03 02 10 03 80 40 01 80  04 80 01 10 02 10 40 05  .....@........@.
0040: 80 06 80 01 10 02 80 43  00 43 01 21 00 01 60 00  .......C.C.!..`.
0050: 02 00 10 07 80 00 60 00  06 01 10 21 00 01 60 00  ......`....!..`.
0060: 03 02 10 00 10 9D 07 6D  00 02 10 21 00 8D 00 8E  .......m...!....
0070: 00 CA 00 27 01 84 01 E1  01 3E 02 9B 02 F8 02 55  ...'.....>.....U
0080: 03 B2 03 0F 04 6C 04 8D  00 8D 00 8D 00 1B 71 10  .....l........q.
0090: 02 80 71 11 02 10 02 02  10 01 80 03 A6 00 03 02  ..q.............
00A0: 10 01 80 01 B3 00 02 02  10 08 80 02 B3 00 03 02  ................
00B0: 10 08 80 40 01 80 04 80  01 10 02 10 40 05 80 06  ...@........@...
00C0: 80 01 10 09 80 43 00 43  01 1B 06 01 10 40 05 80  .....C.C.....@..
00D0: 06 80 01 10 0A 80 43 00  43 01 02 02 80 02 80 00  ......C.C.......
00E0: 26 01 06 01 10 40 05 80  06 80 01 10 0A 80 24 0B  &....@........$.
00F0: 80 01 80 01 80 25 02 00  10 01 80 00 0A 01 40 01  .....%........@.
0100: 80 04 80 01 10 02 80 01  1F 01 02 00 10 02 80 00  ................
0110: 1E 01 40 01 80 04 80 01  10 0A 80 01 1F 01 1B 43  ..@............C
0120: 00 43 01 01 DA 00 1B 06  01 10 40 05 80 06 80 01  .C........@.....
0130: 10 0C 80 43 00 43 01 02  02 80 02 80 00 83 01 06  ...C.C..........
0140: 01 10 40 05 80 06 80 01  10 0C 80 24 0B 80 01 80  ..@........$....
0150: 01 80 25 02 00 10 01 80  00 67 01 40 01 80 04 80  ..%......g.@....
0160: 01 10 02 80 01 7C 01 02  00 10 02 80 00 7B 01 40  .....|.......{.@
0170: 01 80 04 80 01 10 0A 80  01 7C 01 1B 43 00 43 01  .........|..C.C.
0180: 01 37 01 1B 06 01 10 40  05 80 06 80 01 10 0D 80  .7.....@........
0190: 43 00 43 01 02 02 80 02  80 00 E0 01 06 01 10 40  C.C............@
01A0: 05 80 06 80 01 10 0D 80  24 0B 80 01 80 01 80 25  ........$......%
01B0: 02 00 10 01 80 00 C4 01  40 01 80 04 80 01 10 02  ........@.......
01C0: 80 01 D9 01 02 00 10 02  80 00 D8 01 40 01 80 04  ............@...
01D0: 80 01 10 0A 80 01 D9 01  1B 43 00 43 01 01 94 01  .........C.C....
01E0: 1B 06 01 10 40 05 80 06  80 01 10 0E 80 43 00 43  ....@........C.C
01F0: 01 02 02 80 02 80 00 3D  02 06 01 10 40 05 80 06  .......=....@...
0200: 80 01 10 0E 80 24 0B 80  01 80 01 80 25 02 00 10  .....$......%...
0210: 01 80 00 21 02 40 01 80  04 80 01 10 02 80 01 36  ...!.@.........6
0220: 02 02 00 10 02 80 00 35  02 40 01 80 04 80 01 10  .......5.@......
0230: 0A 80 01 36 02 1B 43 00  43 01 01 F1 01 1B 06 01  ...6..C.C.......
0240: 10 40 05 80 06 80 01 10  0F 80 43 00 43 01 02 02  .@........C.C...
0250: 80 02 80 00 9A 02 06 01  10 40 05 80 06 80 01 10  .........@......
0260: 0F 80 24 0B 80 01 80 01  80 25 02 00 10 01 80 00  ..$......%......
0270: 7E 02 40 01 80 04 80 01  10 02 80 01 93 02 02 00  ~.@.............
0280: 10 02 80 00 92 02 40 01  80 04 80 01 10 0A 80 01  ......@.........
0290: 93 02 1B 43 00 43 01 01  4E 02 1B 06 01 10 40 05  ...C.C..N.....@.
02A0: 80 06 80 01 10 10 80 43  00 43 01 02 02 80 02 80  .......C.C......
02B0: 00 F7 02 06 01 10 40 05  80 06 80 01 10 10 80 24  ......@........$
02C0: 0B 80 01 80 01 80 25 02  00 10 01 80 00 DB 02 40  ......%........@
02D0: 01 80 04 80 01 10 02 80  01 F0 02 02 00 10 02 80  ................
02E0: 00 EF 02 40 01 80 04 80  01 10 0A 80 01 F0 02 1B  ...@............
02F0: 43 00 43 01 01 AB 02 1B  06 01 10 40 05 80 06 80  C.C........@....
0300: 01 10 11 80 43 00 43 01  02 02 80 02 80 00 54 03  ....C.C.......T.
0310: 06 01 10 40 05 80 06 80  01 10 11 80 24 0B 80 01  ...@........$...
0320: 80 01 80 25 02 00 10 01  80 00 38 03 40 01 80 04  ...%......8.@...
0330: 80 01 10 02 80 01 4D 03  02 00 10 02 80 00 4C 03  ......M.......L.
0340: 40 01 80 04 80 01 10 0A  80 01 4D 03 1B 43 00 43  @.........M..C.C
0350: 01 01 08 03 1B 06 01 10  40 05 80 06 80 01 10 12  ........@.......
0360: 80 43 00 43 01 02 02 80  02 80 00 B1 03 06 01 10  .C.C............
0370: 40 05 80 06 80 01 10 12  80 24 0B 80 01 80 01 80  @........$......
0380: 25 02 00 10 01 80 00 95  03 40 01 80 04 80 01 10  %........@......
0390: 02 80 01 AA 03 02 00 10  02 80 00 A9 03 40 01 80  .............@..
03A0: 04 80 01 10 0A 80 01 AA  03 1B 43 00 43 01 01 65  ..........C.C..e
03B0: 03 1B 06 01 10 40 05 80  06 80 01 10 13 80 43 00  .....@........C.
03C0: 43 01 02 02 80 02 80 00  0E 04 06 01 10 40 05 80  C............@..
03D0: 06 80 01 10 13 80 24 0B  80 01 80 01 80 25 02 00  ......$......%..
03E0: 10 01 80 00 F2 03 40 01  80 04 80 01 10 02 80 01  ......@.........
03F0: 07 04 02 00 10 02 80 00  06 04 40 01 80 04 80 01  ..........@.....
0400: 10 0A 80 01 07 04 1B 43  00 43 01 01 C2 03 1B 06  .......C.C......
0410: 01 10 40 05 80 06 80 01  10 14 80 43 00 43 01 02  ..@........C.C..
0420: 02 80 02 80 00 6B 04 06  01 10 40 05 80 06 80 01  .....k....@.....
0430: 10 14 80 24 0B 80 01 80  01 80 25 02 00 10 01 80  ...$......%.....
0440: 00 4F 04 40 01 80 04 80  01 10 02 80 01 64 04 02  .O.@.........d..
0450: 00 10 02 80 00 63 04 40  01 80 04 80 01 10 0A 80  .....c.@........
0460: 01 64 04 1B 43 00 43 01  01 1F 04 1B 06 01 10 40  .d..C.C........@
0470: 05 80 06 80 01 10 15 80  43 00 43 01 02 02 80 02  ........C.C.....
0480: 80 00 C8 04 06 01 10 40  05 80 06 80 01 10 15 80  .......@........
0490: 24 0B 80 01 80 01 80 25  02 00 10 01 80 00 AC 04  $......%........
04A0: 40 01 80 04 80 01 10 02  80 01 C1 04 02 00 10 02  @...............
04B0: 80 00 C0 04 40 01 80 04  80 01 10 0A 80 01 C1 04  ....@...........
04C0: 1B 43 00 43 01 01 7C 04  1B                       .C.C..|..       
```

#### Opcodes

```
  0: 0x0000 [0x24] CREATE_DIALOG(message_id=8481*, default_option=0*, option_flags=0*)
    → "What will you be doing? [Setting Fame./Contamination level./QS01: Missing in Action./QS02: I Dream of Flowers./QS03: Destiny Odyssey./QS04: Unidentified Research Object./QS05: Cookbook of Hope Bestowing./QS06: Smoke over the Coast./QS07: Soil and Green (Soil Quality)/QS07: Soil and Green (Fertilizer)/QS08: Dropping the Bomb./QS09: Wanted: Medical Supplies./Everything./Never mind.]"
  1: 0x0007 [0x25] WAIT_DIALOG_SELECT()
  2: 0x0008 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0050
  3: 0x0010 [0x71] USER_INPUT_HANDLER: Open numerical input dialog (work=1*)
  4: 0x0014 [0x71] USER_INPUT_HANDLER: Process numerical input A (work=Work_Zone[2])
  5: 0x0018 [0x02] IF !(Work_Zone[2] >= 0*) GOTO 0x0028
  6: 0x0020 [0x03] Work_Zone[2] = 0*
  7: 0x0025 [0x01] GOTO 0x0035
  8: 0x0028 [0x02] IF !(Work_Zone[2] <= 50*) GOTO 0x0035
  9: 0x0030 [0x03] Work_Zone[2] = 50*

SUBROUTINE_0035:
 10: 0x0035 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=Work_Zone[2])
 11: 0x003E [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=1*)
 12: 0x0047 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 13: 0x0049 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 14: 0x004B [0x21] END_EVENT
 15: 0x004C [0x00] END_REQSTACK()

SUBROUTINE_0060:
 16: 0x0060 [0x03] Work_Zone[2] = Work_Zone[0]
 17: 0x0065 [0x9D] CALL 0x006D[Work_Zone[2]] // Jump table
 18: 0x006B [0x21] END_EVENT
 19: 0x006C [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Data Section: 0x006D (258 bytes)
     0x006D: 8D 00 8E 00 CA 00 27 01 84 01 E1 01 3E 02 9B 02
     0x007D: F8 02 55 03 B2 03 0F 04 6C 04 8D 00 8D 00 8D 00
     0x008D: 1B 71 10 02 80 71 11 02 10 02 02 10 01 80 03 A6
     0x009D: 00 03 02 10 01 80 01 B3 00 02 02 10 08 80 02 B3
     0x00AD: 00 03 02 10 08 80 40 01 80 04 80 01 10 02 10 40
     0x00BD: 05 80 06 80 01 10 09 80 43 00 43 01 1B 06 01 10
     0x00CD: 40 05 80 06 80 01 10 0A 80 43 00 43 01 02 02 80
     0x00DD: 02 80 00 26 01 06 01 10 40 05 80 06 80 01 10 0A
     0x00ED: 80 24 0B 80 01 80 01 80 25 02 00 10 01 80 00 0A
     0x00FD: 01 40 01 80 04 80 01 10 02 80 01 1F 01 02 00 10
     0x010D: 02 80 00 1E 01 40 01 80 04 80 01 10 0A 80 01 1F
     0x011D: 01 1B 43 00 43 01 01 DA 00 1B 06 01 10 40 05 80
     0x012D: 06 80 01 10 0C 80 43 00 43 01 02 02 80 02 80 00
     0x013D: 83 01 06 01 10 40 05 80 06 80 01 10 0C 80 24 0B
     0x014D: 80 01 80 01 80 25 02 00 10 01 80 00 67 01 40 01
     0x015D: 80 04 80 01 10 02 80 01 7C 01 02 00 10 02 80 00
     0x016D: 7B 01
# Dead code (unreachable instructions):
     0x004D [0x01] GOTO 0x0060
     0x005D [0x01] GOTO 0x0060
# Dead code (unreachable instructions):
     0x016F [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x0178 [0x01] GOTO 0x017C
     0x017B [0x1B] RETURN
     0x017C [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x017E [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0180 [0x01] GOTO 0x0137
     0x0183 [0x1B] RETURN
     0x0184 [0x06] Work_Zone[1] = 0
     0x0187 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=4*)
     0x0190 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0192 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0194 [0x02] IF !(1* == 1*) GOTO 0x01E0
     0x019C [0x06] Work_Zone[1] = 0
     0x019F [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=4*)
     0x01A8 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x01AF [0x25] WAIT_DIALOG_SELECT()
     0x01B0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01C4
     0x01B8 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x01C1 [0x01] GOTO 0x01D9
     0x01C4 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01D8
     0x01CC [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x01D5 [0x01] GOTO 0x01D9
     0x01D8 [0x1B] RETURN
     0x01D9 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x01DB [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x01DD [0x01] GOTO 0x0194
     0x01E0 [0x1B] RETURN
     0x01E1 [0x06] Work_Zone[1] = 0
     0x01E4 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=5*)
     0x01ED [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x01EF [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x01F1 [0x02] IF !(1* == 1*) GOTO 0x023D
     0x01F9 [0x06] Work_Zone[1] = 0
     0x01FC [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=5*)
     0x0205 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x020C [0x25] WAIT_DIALOG_SELECT()
     0x020D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0221
     0x0215 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x021E [0x01] GOTO 0x0236
     0x0221 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0235
     0x0229 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x0232 [0x01] GOTO 0x0236
     0x0235 [0x1B] RETURN
     0x0236 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0238 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x023A [0x01] GOTO 0x01F1
     0x023D [0x1B] RETURN
     0x023E [0x06] Work_Zone[1] = 0
     0x0241 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=6*)
     0x024A [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x024C [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x024E [0x02] IF !(1* == 1*) GOTO 0x029A
     0x0256 [0x06] Work_Zone[1] = 0
     0x0259 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=6*)
     0x0262 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x0269 [0x25] WAIT_DIALOG_SELECT()
     0x026A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x027E
     0x0272 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x027B [0x01] GOTO 0x0293
     0x027E [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0292
     0x0286 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x028F [0x01] GOTO 0x0293
     0x0292 [0x1B] RETURN
     0x0293 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0295 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0297 [0x01] GOTO 0x024E
     0x029A [0x1B] RETURN
     0x029B [0x06] Work_Zone[1] = 0
     0x029E [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=7*)
     0x02A7 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x02A9 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x02AB [0x02] IF !(1* == 1*) GOTO 0x02F7
     0x02B3 [0x06] Work_Zone[1] = 0
     0x02B6 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=7*)
     0x02BF [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x02C6 [0x25] WAIT_DIALOG_SELECT()
     0x02C7 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x02DB
     0x02CF [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x02D8 [0x01] GOTO 0x02F0
     0x02DB [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x02EF
     0x02E3 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x02EC [0x01] GOTO 0x02F0
     0x02EF [0x1B] RETURN
     0x02F0 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x02F2 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x02F4 [0x01] GOTO 0x02AB
     0x02F7 [0x1B] RETURN
     0x02F8 [0x06] Work_Zone[1] = 0
     0x02FB [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=8*)
     0x0304 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0306 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0308 [0x02] IF !(1* == 1*) GOTO 0x0354
     0x0310 [0x06] Work_Zone[1] = 0
     0x0313 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=8*)
     0x031C [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x0323 [0x25] WAIT_DIALOG_SELECT()
     0x0324 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0338
     0x032C [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x0335 [0x01] GOTO 0x034D
     0x0338 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x034C
     0x0340 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x0349 [0x01] GOTO 0x034D
     0x034C [0x1B] RETURN
     0x034D [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x034F [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0351 [0x01] GOTO 0x0308
     0x0354 [0x1B] RETURN
     0x0355 [0x06] Work_Zone[1] = 0
     0x0358 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=9*)
     0x0361 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0363 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0365 [0x02] IF !(1* == 1*) GOTO 0x03B1
     0x036D [0x06] Work_Zone[1] = 0
     0x0370 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=9*)
     0x0379 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x0380 [0x25] WAIT_DIALOG_SELECT()
     0x0381 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0395
     0x0389 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x0392 [0x01] GOTO 0x03AA
     0x0395 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x03A9
     0x039D [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x03A6 [0x01] GOTO 0x03AA
     0x03A9 [0x1B] RETURN
     0x03AA [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x03AC [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x03AE [0x01] GOTO 0x0365
     0x03B1 [0x1B] RETURN
     0x03B2 [0x06] Work_Zone[1] = 0
     0x03B5 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=10*)
     0x03BE [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x03C0 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x03C2 [0x02] IF !(1* == 1*) GOTO 0x040E
     0x03CA [0x06] Work_Zone[1] = 0
     0x03CD [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=10*)
     0x03D6 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x03DD [0x25] WAIT_DIALOG_SELECT()
     0x03DE [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x03F2
     0x03E6 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x03EF [0x01] GOTO 0x0407
     0x03F2 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0406
     0x03FA [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x0403 [0x01] GOTO 0x0407
     0x0406 [0x1B] RETURN
     0x0407 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0409 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x040B [0x01] GOTO 0x03C2
     0x040E [0x1B] RETURN
     0x040F [0x06] Work_Zone[1] = 0
     0x0412 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=11*)
     0x041B [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x041D [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x041F [0x02] IF !(1* == 1*) GOTO 0x046B
     0x0427 [0x06] Work_Zone[1] = 0
     0x042A [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=11*)
     0x0433 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x043A [0x25] WAIT_DIALOG_SELECT()
     0x043B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x044F
     0x0443 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x044C [0x01] GOTO 0x0464
     0x044F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0463
     0x0457 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x0460 [0x01] GOTO 0x0464
     0x0463 [0x1B] RETURN
     0x0464 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x0466 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x0468 [0x01] GOTO 0x041F
     0x046B [0x1B] RETURN
     0x046C [0x06] Work_Zone[1] = 0
     0x046F [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=12*)
     0x0478 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x047A [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x047C [0x02] IF !(1* == 1*) GOTO 0x04C8
     0x0484 [0x06] Work_Zone[1] = 0
     0x0487 [0x40] SET_BIT_WORK_RANGE(start_bit=24*, end_bit=31*, target=Work_Zone[1], source=12*)
     0x0490 [0x24] CREATE_DIALOG(message_id=8482*, default_option=0*, option_flags=0*)
    → "Please be making a choice. [Starting: [off/on]/Ending: [off/on]/Quitting.]"
     0x0497 [0x25] WAIT_DIALOG_SELECT()
     0x0498 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04AC
     0x04A0 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=1*)
     0x04A9 [0x01] GOTO 0x04C1
     0x04AC [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x04C0
     0x04B4 [0x40] SET_BIT_WORK_RANGE(start_bit=0*, end_bit=23*, target=Work_Zone[1], source=2*)
     0x04BD [0x01] GOTO 0x04C1
     0x04C0 [0x1B] RETURN
     0x04C1 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
     0x04C3 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
     0x04C5 [0x01] GOTO 0x047C
     0x04C8 [0x1B] RETURN
```
