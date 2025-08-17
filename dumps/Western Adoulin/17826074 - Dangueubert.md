# 17826074 - Dangueubert

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Western Adoulin (ID: 256) |
| Block Size       | 456 bytes                 |
| Total Events     | 5                         |
| References Count | 25                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [546](#event-546)     | 0x0001       |    288 |             69 |
| [2558](#event-2558)   | 0x0121       |     26 |             14 |
| [5079](#event-5079)   | 0x013B       |      1 |              1 |
| [5146](#event-5146)   | 0x013C       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x269B      |        9883 |
|       1 | 0x269C      |        9884 |
|       2 | 0x0001      |           1 |
|       3 | 0x0000      |           0 |
|       4 | 0x269D      |        9885 |
|       5 | 0x40000000  |  1073741824 |
|       6 | 0x00C8      |         200 |
|       7 | 0x0002      |           2 |
|       8 | 0x26A7      |        9895 |
|       9 | 0xFFFFFFFF  |  4294967295 |
|      10 | 0x26A8      |        9896 |
|      11 | 0x26A9      |        9897 |
|      12 | 0x26AA      |        9898 |
|      13 | 0x0003      |           3 |
|      14 | 0x269E      |        9886 |
|      15 | 0x269F      |        9887 |
|      16 | 0x0004      |           4 |
|      17 | 0x26A2      |        9890 |
|      18 | 0x26A3      |        9891 |
|      19 | 0x26A4      |        9892 |
|      20 | 0x0005      |           5 |
|      21 | 0x1F2C      |        7980 |
|      22 | 0x1F2D      |        7981 |
|      23 | 0x1F2E      |        7982 |
|      24 | 0x1F2F      |        7983 |

## String References

- **7980**: The ferry that docks here transports pioneers to the chain of small islands that compose the Adoulinian residential area.
- **7981**: I doubt you intend to utilize it while you are on patrol, but feel free to follow your desires and board at any time.
- **7982**: As for possible problems, we are not experiencing any currently. Every vessel is on schedule and the seas are calm.
- **7983**: Oh, and should you ever wish to visit the residential area, simply pass through this arch and descend the steps to the dock. That is all, [sir/ma'am].
- **9883**: The watercraft that dock here transport pioneers and laymen alike to their private island plots replete with a cornucopia of facilities.
- **9884**: About what would you like to know? [Nothing./Send me to my Mog Garden!/Visiting others' Mog Gardens./Rent-a-Rooms./Mog Gardens./Expanding my Mog Garden.]
- **9885**: There shall be no stowing away while I'm on watch! Only registered pioneers are allowed aboard this vessel, you imposter!
- **9886**: If I were to describe what a Rent-a-Room means to pioneers in one word, it would be "convenience."
- **9887**: They are positioned upon deserted islands that came under Adoulin's jurisdiction once the alliance was formed and the old regime abandoned. As for amenities, the Rent-a-Rooms mirror those of similar facilities across Vana'diel.
- **9890**: Mog Gardens are special areas located on the islands dotting the Adoulin Archipelago which have a variety of facilities suited for all your gathering needs.
- **9891**: Absolutely no fee is required to take advantage of this service.
- **9892**: We hope that you utilize your Mog Garden to the fullest.
- **9895**: You may visit the Mog Gardens of the following party members. Is there anyone's in particular you would care to visit?
- **9896**: Visit whose Mog Garden? [No one's./%1's./%2's./%3's./%4's./%5's./%6's./%7's./%8's./%9's./%10's./%11's./%12's./%13's./%14's./%15's./%16's./%17's.]
- **9897**: Your wish is my command. This way, please.
- **9898**: I regret to inform you that none of your party members are currently allowing people to patron their Mog Gardens.

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

### Event 546

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 288 bytes |
| Instructions | 69        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 03 10 1E F0 FF FF 7F   ...............
0010: 6F 70 1D 00 80 23 24 01  80 02 80 00 00 25 02 00  op...#$......%..
0020: 10 03 80 00 29 00 01 1F  01 02 00 10 02 80 00 6D  ....)..........m
0030: 00 02 01 00 03 80 00 45  00 1D 04 80 23 03 01 10  .......E....#...
0040: 05 80 01 6A 00 45 06 80  F0 FF FF 7F F0 FF FF 7F  ...j.E..........
0050: 66 64 6F 30 03 80 55 06  80 F0 FF FF 7F F0 FF FF  fdo0..U.........
0060: 7F 66 64 6F 30 03 01 10  02 80 01 1F 01 02 00 10  .fdo0...........
0070: 07 80 00 DB 00 02 01 00  03 80 00 89 00 1D 04 80  ................
0080: 23 03 01 10 05 80 01 D8  00 C2 01 02 00 02 02 00  #...............
0090: 03 80 01 CF 00 1D 08 80  23 C2 01 02 00 0F 02 00  ........#.......
00A0: 09 80 3D 02 00 03 80 02  80 24 0A 80 03 80 02 00  ..=......$......
00B0: 25 02 00 10 03 80 00 C1  00 03 01 10 05 80 01 CC  %...............
00C0: 00 42 1D 0B 80 23 C2 02  00 10 01 10 01 D8 00 1D  .B...#..........
00D0: 0C 80 23 03 01 10 05 80  01 1F 01 02 00 10 0D 80  ..#.............
00E0: 00 F3 00 1D 0E 80 23 1D  0F 80 23 03 01 10 05 80  ......#...#.....
00F0: 01 1F 01 02 00 10 10 80  00 0F 01 1D 11 80 23 1D  ..............#.
0100: 12 80 23 1D 13 80 23 03  01 10 05 80 01 1F 01 02  ..#...#.........
0110: 00 10 14 80 00 1F 01 03  01 10 05 80 01 1F 01 21  ...............!
0120: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x000B [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=9883*)
    → "The watercraft that dock here transport pioneers and laymen alike to their private island plots replete with a cornucopia of facilities."
  6: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0016 [0x24] CREATE_DIALOG(message_id=9884*, default_option=1*, option_flags=ExtData[1]->WorkLocal[0])
    → "About what would you like to know? [Nothing./Send me to my Mog Garden!/Visiting others' Mog Gardens./Rent-a-Rooms./Mog Gardens./Expanding my Mog Garden.]"
  8: 0x001D [0x25] WAIT_DIALOG_SELECT()
  9: 0x001E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0029
 10: 0x0026 [0x01] GOTO 0x011F
 11: 0x0029 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x006D
 12: 0x0031 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0045
 13: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=9885*)
    → "There shall be no stowing away while I'm on watch! Only registered pioneers are allowed aboard this vessel, you imposter!"
 14: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003D [0x03] Work_Zone[1] = 1073741824*
 16: 0x0042 [0x01] GOTO 0x006A
 17: 0x0045 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x0056 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
 19: 0x0065 [0x03] Work_Zone[1] = 1*

SUBROUTINE_006A:
 20: 0x006A [0x01] GOTO 0x011F
 21: 0x006D [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00DB
 22: 0x0075 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0089
 23: 0x007D [0x1D] PRINT_EVENT_MESSAGE(message_id=9885*)
    → "There shall be no stowing away while I'm on watch! Only registered pioneers are allowed aboard this vessel, you imposter!"
 24: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0081 [0x03] Work_Zone[1] = 1073741824*
 26: 0x0086 [0x01] GOTO 0x00D8
 27: 0x0089 [0xC2] PARTY_STATE_CHECK: ExtData[1]->WorkLocal[2] = mask of visitable party members
 28: 0x008D [0x02] IF !(ExtData[1]->WorkLocal[2] == 0*) GOTO 0x00CF
 29: 0x0095 [0x1D] PRINT_EVENT_MESSAGE(message_id=9895*)
    → "You may visit the Mog Gardens of the following party members. Is there anyone's in particular you would care to visit?"
 30: 0x0098 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0099 [0xC2] PARTY_STATE_CHECK: ExtData[1]->WorkLocal[2] = mask of visitable party members
 32: 0x009D [0x0F] ExtData[1]->WorkLocal[2] ^= 4294967295*
 33: 0x00A2 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[2], bit_index_work_offset=0*, condition_work_offset=1*)
 34: 0x00A9 [0x24] CREATE_DIALOG(message_id=9896*, default_option=0*, option_flags=ExtData[1]->WorkLocal[2])
    → "Visit whose Mog Garden? [No one's./%1's./%2's./%3's./%4's./%5's./%6's./%7's./%8's./%9's./%10's./%11's./%12's./%13's./%14's./%15's./%16's./%17's.]"
 35: 0x00B0 [0x25] WAIT_DIALOG_SELECT()
 36: 0x00B1 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C1
 37: 0x00B9 [0x03] Work_Zone[1] = 1073741824*
 38: 0x00BE [0x01] GOTO 0x00CC
 39: 0x00C1 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 40: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=9897*)
    → "Your wish is my command. This way, please."
 41: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00C6 [0xC2] PARTY_STATE_CHECK: Work_Zone[1] = check if party member (from Work_Zone[0]) house is open

SUBROUTINE_00CC:
 43: 0x00CC [0x01] GOTO 0x00D8
 44: 0x00CF [0x1D] PRINT_EVENT_MESSAGE(message_id=9898*)
    → "I regret to inform you that none of your party members are currently allowing people to patron their Mog Gardens."
 45: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00D3 [0x03] Work_Zone[1] = 1073741824*

SUBROUTINE_00D8:
 47: 0x00D8 [0x01] GOTO 0x011F
 48: 0x00DB [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x00F3
 49: 0x00E3 [0x1D] PRINT_EVENT_MESSAGE(message_id=9886*)
    → "If I were to describe what a Rent-a-Room means to pioneers in one word, it would be "convenience.""
 50: 0x00E6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=9887*)
    → "They are positioned upon deserted islands that came under Adoulin's jurisdiction once the alliance was formed and the old regime abandoned. As for amenities, the Rent-a-Rooms mirror those of similar facilities across Vana'diel."
 52: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x00EB [0x03] Work_Zone[1] = 1073741824*
 54: 0x00F0 [0x01] GOTO 0x011F
 55: 0x00F3 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x010F
 56: 0x00FB [0x1D] PRINT_EVENT_MESSAGE(message_id=9890*)
    → "Mog Gardens are special areas located on the islands dotting the Adoulin Archipelago which have a variety of facilities suited for all your gathering needs."
 57: 0x00FE [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=9891*)
    → "Absolutely no fee is required to take advantage of this service."
 59: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=9892*)
    → "We hope that you utilize your Mog Garden to the fullest."
 61: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x0107 [0x03] Work_Zone[1] = 1073741824*
 63: 0x010C [0x01] GOTO 0x011F
 64: 0x010F [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x011F
 65: 0x0117 [0x03] Work_Zone[1] = 1073741824*
 66: 0x011C [0x01] GOTO 0x011F

SUBROUTINE_011F:
 67: 0x011F [0x21] END_EVENT
 68: 0x0120 [0x00] END_REQSTACK()
```

### Event 2558

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0121   |
| Data Size    | 26 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:    1E F0 FF FF 7F 42 6F  70 1D 15 80 23 1D 16 80   .....Bop...#...
0130: 23 1D 17 80 23 1D 18 80  23 21 00                 #...#...#!.     
```

#### Opcodes

```
  0: 0x0121 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0126 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x0127 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0128 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0129 [0x1D] PRINT_EVENT_MESSAGE(message_id=7980*)
    → "The ferry that docks here transports pioneers to the chain of small islands that compose the Adoulinian residential area."
  5: 0x012C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x012D [0x1D] PRINT_EVENT_MESSAGE(message_id=7981*)
    → "I doubt you intend to utilize it while you are on patrol, but feel free to follow your desires and board at any time."
  7: 0x0130 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0131 [0x1D] PRINT_EVENT_MESSAGE(message_id=7982*)
    → "As for possible problems, we are not experiencing any currently. Every vessel is on schedule and the seas are calm."
  9: 0x0134 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0135 [0x1D] PRINT_EVENT_MESSAGE(message_id=7983*)
    → "Oh, and should you ever wish to visit the residential area, simply pass through this arch and descend the steps to the dock. That is all, [sir/ma'am]."
 11: 0x0138 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0139 [0x21] END_EVENT
 13: 0x013A [0x00] END_REQSTACK()
```

### Event 5079

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   00                         .    
```

#### Opcodes

```
  0: 0x013B [0x00] END_REQSTACK()
```

### Event 5146

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                      00                       .   
```

#### Opcodes

```
  0: 0x013C [0x00] END_REQSTACK()
```
