# 17830104 - Cunegonde

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 512 bytes                 |
| Total Events     | 3                         |
| References Count | 27                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [575](#event-575)     | 0x0001       |    318 |             71 |
| [2518](#event-2518)   | 0x013F       |     56 |             16 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x28F5      |       10485 |
|       2 | 0x28F6      |       10486 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0x28F4      |       10484 |
|       6 | 0x40000000  |  1073741824 |
|       7 | 0x00C8      |         200 |
|       8 | 0x0002      |           2 |
|       9 | 0x2900      |       10496 |
|      10 | 0xFFFFFFFF  |  4294967295 |
|      11 | 0x2901      |       10497 |
|      12 | 0x2902      |       10498 |
|      13 | 0x2903      |       10499 |
|      14 | 0x0003      |           3 |
|      15 | 0x28F7      |       10487 |
|      16 | 0x28F8      |       10488 |
|      17 | 0x0004      |           4 |
|      18 | 0x28FB      |       10491 |
|      19 | 0x28FC      |       10492 |
|      20 | 0x28FD      |       10493 |
|      21 | 0x0005      |           5 |
|      22 | 0x000A      |          10 |
|      23 | 0x1EE3      |        7907 |
|      24 | 0x1EE4      |        7908 |
|      25 | 0x1EE5      |        7909 |
|      26 | 0x1EE6      |        7910 |

## String References

- **7907**: Up ahead you can find the docks that lead pioneers like yourself to the residential areas on the outlying islands.
- **7908**: Oh, you are here on patrol? Thank you for checking in. I have nothing out of the ordinary to report.
- **7909**: Our vessels are running on time, and there have been no maritime accidents of late.
- **7910**: The boat leading to the residential area is just beyond this arch and down the stairs.
- **10484**: There shall be no stowing away while I'm on watch! Only registered pioneers are allowed aboard this vessel, you imposter!
- **10485**: The vessel that docks beyond here transports pioneers and laymen alike to their very own island plot containing various amenities.
- **10486**: What do you want to know about? [Nothing./Send me to my Mog Garden!/Visiting others' Mog Gardens./Rent-a-Rooms./Mog Gardens./Mog Garden expansion.]
- **10487**: I'm sure you can recall the Rent-a-Room you used back in the Middle Lands.
- **10488**: The ones here function in the exact same manner as the ones you've already grown to love as your homes-away-from-home.
- **10491**: Mog Gardens are special areas located on the islands dotting the Adoulin Archipelago which have a variety of facilities suited for all your gathering needs.
- **10492**: Absolutely no fee is required to take advantage of this service.
- **10493**: We hope that you utilize your Mog Garden to the fullest.
- **10496**: You can visit the Mog Gardens of the following party members. Is there anyone's in particular you want to visit?
- **10497**: Visit whose Mog Garden? [No one's./%1's./%2's./%3's./%4's./%5's./%6's./%7's./%8's./%9's./%10's./%11's./%12's./%13's./%14's./%15's./%16's./%17's.]
- **10498**: Okay, then. Right this way, please.
- **10499**: Sorry, but none of your party members have their Mog Gardens open to anyone at this time.

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

### Event 575

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 318 bytes |
| Instructions | 71        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 03 10 1E F0 FF FF 7F   ...............
0010: 6F 70 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 62  opf..........tlb
0020: 30 1D 01 80 23 24 02 80  03 80 00 00 25 02 00 10  0...#$......%...
0030: 04 80 00 38 00 01 2E 01  02 00 10 03 80 00 7C 00  ...8..........|.
0040: 02 01 00 04 80 00 54 00  1D 05 80 23 03 01 10 06  ......T....#....
0050: 80 01 79 00 45 07 80 F0  FF FF 7F F0 FF FF 7F 66  ..y.E..........f
0060: 64 6F 30 04 80 55 07 80  F0 FF FF 7F F0 FF FF 7F  do0..U..........
0070: 66 64 6F 30 03 01 10 03  80 01 2E 01 02 00 10 08  fdo0............
0080: 80 00 EA 00 02 01 00 04  80 00 98 00 1D 05 80 23  ...............#
0090: 03 01 10 06 80 01 E7 00  C2 01 02 00 02 02 00 04  ................
00A0: 80 01 DE 00 1D 09 80 23  C2 01 02 00 0F 02 00 0A  .......#........
00B0: 80 3D 02 00 04 80 03 80  24 0B 80 04 80 02 00 25  .=......$......%
00C0: 02 00 10 04 80 00 D0 00  03 01 10 06 80 01 DB 00  ................
00D0: 42 1D 0C 80 23 C2 02 00  10 01 10 01 E7 00 1D 0D  B...#...........
00E0: 80 23 03 01 10 06 80 01  2E 01 02 00 10 0E 80 00  .#..............
00F0: 02 01 1D 0F 80 23 1D 10  80 23 03 01 10 06 80 01  .....#...#......
0100: 2E 01 02 00 10 11 80 00  1E 01 1D 12 80 23 1D 13  .............#..
0110: 80 23 1D 14 80 23 03 01  10 06 80 01 2E 01 02 00  .#...#..........
0120: 10 15 80 00 2E 01 03 01  10 06 80 01 2E 01 66 00  ..............f.
0130: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 62 31 21 00     .........tlb1!. 
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0012 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb0" with entities [EventEntity, EventEntity], work=13*
  6: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=10485*)
    → "The vessel that docks beyond here transports pioneers and laymen alike to their very own island plot containing various amenities."
  7: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0025 [0x24] CREATE_DIALOG(message_id=10486*, default_option=1*, option_flags=ExtData[1]->WorkLocal[0])
    → "What do you want to know about? [Nothing./Send me to my Mog Garden!/Visiting others' Mog Gardens./Rent-a-Rooms./Mog Gardens./Mog Garden expansion.]"
  9: 0x002C [0x25] WAIT_DIALOG_SELECT()
 10: 0x002D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0038
 11: 0x0035 [0x01] GOTO 0x012E
 12: 0x0038 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007C
 13: 0x0040 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0054
 14: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=10484*)
    → "There shall be no stowing away while I'm on watch! Only registered pioneers are allowed aboard this vessel, you imposter!"
 15: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x004C [0x03] Work_Zone[1] = 1073741824*
 17: 0x0051 [0x01] GOTO 0x0079
 18: 0x0054 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 19: 0x0065 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
 20: 0x0074 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0079:
 21: 0x0079 [0x01] GOTO 0x012E
 22: 0x007C [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00EA
 23: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0098
 24: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=10484*)
    → "There shall be no stowing away while I'm on watch! Only registered pioneers are allowed aboard this vessel, you imposter!"
 25: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0090 [0x03] Work_Zone[1] = 1073741824*
 27: 0x0095 [0x01] GOTO 0x00E7
 28: 0x0098 [0xC2] PARTY_STATE_CHECK: ExtData[1]->WorkLocal[2] = mask of visitable party members
 29: 0x009C [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x00DE
 30: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=10496*)
    → "You can visit the Mog Gardens of the following party members. Is there anyone's in particular you want to visit?"
 31: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x00A8 [0xC2] PARTY_STATE_CHECK: ExtData[1]->WorkLocal[2] = mask of visitable party members
 33: 0x00AC [0x0F] ExtData[1]->WorkLocal[2] ^= 4294967295*
 34: 0x00B1 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=0*, condition_work_offset=1*)
 35: 0x00B8 [0x24] CREATE_DIALOG(message_id=10497*, default_option=0*, option_flags=ExtData[1]->WorkLocal[2])
    → "Visit whose Mog Garden? [No one's./%1's./%2's./%3's./%4's./%5's./%6's./%7's./%8's./%9's./%10's./%11's./%12's./%13's./%14's./%15's./%16's./%17's.]"
 36: 0x00BF [0x25] WAIT_DIALOG_SELECT()
 37: 0x00C0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00D0
 38: 0x00C8 [0x03] Work_Zone[1] = 1073741824*
 39: 0x00CD [0x01] GOTO 0x00DB
 40: 0x00D0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 41: 0x00D1 [0x1D] PRINT_EVENT_MESSAGE(message_id=10498*)
    → "Okay, then. Right this way, please."
 42: 0x00D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00D5 [0xC2] PARTY_STATE_CHECK: Work_Zone[1] = check if party member (from Work_Zone[0]) house is open

SUBROUTINE_00DB:
 44: 0x00DB [0x01] GOTO 0x00E7
 45: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=10499*)
    → "Sorry, but none of your party members have their Mog Gardens open to anyone at this time."
 46: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x00E2 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_00E7:
 48: 0x00E7 [0x01] GOTO 0x012E
 49: 0x00EA [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0102
 50: 0x00F2 [0x1D] PRINT_EVENT_MESSAGE(message_id=10487*)
    → "I'm sure you can recall the Rent-a-Room you used back in the Middle Lands."
 51: 0x00F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x00F6 [0x1D] PRINT_EVENT_MESSAGE(message_id=10488*)
    → "The ones here function in the exact same manner as the ones you've already grown to love as your homes-away-from-home."
 53: 0x00F9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x00FA [0x03] Work_Zone[1] = 1073741824*
 55: 0x00FF [0x01] GOTO 0x012E
 56: 0x0102 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x011E
 57: 0x010A [0x1D] PRINT_EVENT_MESSAGE(message_id=10491*)
    → "Mog Gardens are special areas located on the islands dotting the Adoulin Archipelago which have a variety of facilities suited for all your gathering needs."
 58: 0x010D [0x23] WAIT_FOR_DIALOG_INTERACTION
 59: 0x010E [0x1D] PRINT_EVENT_MESSAGE(message_id=10492*)
    → "Absolutely no fee is required to take advantage of this service."
 60: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x0112 [0x1D] PRINT_EVENT_MESSAGE(message_id=10493*)
    → "We hope that you utilize your Mog Garden to the fullest."
 62: 0x0115 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x0116 [0x03] Work_Zone[1] = 1073741824*
 64: 0x011B [0x01] GOTO 0x012E
 65: 0x011E [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x012E
 66: 0x0126 [0x03] Work_Zone[1] = 1073741824*
 67: 0x012B [0x01] GOTO 0x012E

SUBROUTINE_012E:
 68: 0x012E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlb1" with entities [EventEntity, EventEntity], work=13*
 69: 0x013D [0x21] END_EVENT
 70: 0x013E [0x00] END_REQSTACK()
```

### Event 2518

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013F   |
| Data Size    | 56 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                               1E                 .
0140: F0 FF FF 7F 42 6F 70 66  16 80 F8 FF FF 7F F8 FF  ....Bopf........
0150: FF 7F 74 6C 6B 30 1D 17  80 23 1D 18 80 23 1D 19  ..tlk0...#...#..
0160: 80 23 1D 1A 80 23 66 16  80 F8 FF FF 7F F8 FF FF  .#...#f.........
0170: 7F 74 6C 6B 31 21 00                              .tlk1!.         
```

#### Opcodes

```
  0: 0x013F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0144 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0145 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0146 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0147 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=10*
  5: 0x0156 [0x1D] PRINT_EVENT_MESSAGE(message_id=7907*)
    → "Up ahead you can find the docks that lead pioneers like yourself to the residential areas on the outlying islands."
  6: 0x0159 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x015A [0x1D] PRINT_EVENT_MESSAGE(message_id=7908*)
    → "Oh, you are here on patrol? Thank you for checking in. I have nothing out of the ordinary to report."
  8: 0x015D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x015E [0x1D] PRINT_EVENT_MESSAGE(message_id=7909*)
    → "Our vessels are running on time, and there have been no maritime accidents of late."
 10: 0x0161 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0162 [0x1D] PRINT_EVENT_MESSAGE(message_id=7910*)
    → "The boat leading to the residential area is just beyond this arch and down the stairs."
 12: 0x0165 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0166 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=10*
 14: 0x0175 [0x21] END_EVENT
 15: 0x0176 [0x00] END_REQSTACK()
```
