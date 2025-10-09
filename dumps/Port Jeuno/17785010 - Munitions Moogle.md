# 17785010 - Munitions Moogle

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 1152 bytes           |
| Total Events     | 4                    |
| References Count | 54                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [445](#event-445)     | 0x0001       |    700 |            184 |
| [446](#event-446)     | 0x02BD       |    101 |             29 |
| [447](#event-447)     | 0x0322       |    101 |             30 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x250E      |        9486 |
|       1 | 0x0001      |           1 |
|       2 | 0x0000      |           0 |
|       3 | 0x2513      |        9491 |
|       4 | 0x250F      |        9487 |
|       5 | 0x2510      |        9488 |
|       6 | 0x2511      |        9489 |
|       7 | 0x2512      |        9490 |
|       8 | 0x2514      |        9492 |
|       9 | 0x2515      |        9493 |
|      10 | 0x2516      |        9494 |
|      11 | 0x2517      |        9495 |
|      12 | 0x0002      |           2 |
|      13 | 0x0003      |           3 |
|      14 | 0x0004      |           4 |
|      15 | 0x0005      |           5 |
|      16 | 0x0006      |           6 |
|      17 | 0x0007      |           7 |
|      18 | 0x2518      |        9496 |
|      19 | 0x2519      |        9497 |
|      20 | 0x251A      |        9498 |
|      21 | 0x251B      |        9499 |
|      22 | 0x251C      |        9500 |
|      23 | 0x251D      |        9501 |
|      24 | 0x251E      |        9502 |
|      25 | 0x251F      |        9503 |
|      26 | 0x2520      |        9504 |
|      27 | 0x2521      |        9505 |
|      28 | 0x0008      |           8 |
|      29 | 0x66E7      |       26343 |
|      30 | 0x66E8      |       26344 |
|      31 | 0x66E9      |       26345 |
|      32 | 0x66EA      |       26346 |
|      33 | 0x66EB      |       26347 |
|      34 | 0x66EC      |       26348 |
|      35 | 0x66ED      |       26349 |
|      36 | 0x66EE      |       26350 |
|      37 | 0x5671      |       22129 |
|      38 | 0x5672      |       22130 |
|      39 | 0x5673      |       22131 |
|      40 | 0x567B      |       22139 |
|      41 | 0x567C      |       22140 |
|      42 | 0x567D      |       22141 |
|      43 | 0x567E      |       22142 |
|      44 | 0x567F      |       22143 |
|      45 | 0x2522      |        9506 |
|      46 | 0x2523      |        9507 |
|      47 | 0x2527      |        9511 |
|      48 | 0x2528      |        9512 |
|      49 | 0x2529      |        9513 |
|      50 | 0x252A      |        9514 |
|      51 | 0x2526      |        9510 |
|      52 | 0x2524      |        9508 |
|      53 | 0x2525      |        9509 |

## String References

- **9486**: Welcome to the ammunition retrieval service.
- **9487**: I'm pleased to announce that we've come up with a way for you to retrieve specific ammunition storage items that you may have previously lost--but one time only!
- **9488**: If you want to retrieve one of said items, all you need to do is trade me the corresponding weapon.
- **9489**: Please keep in mind that this is a one-time-only service per weapon. There will be no second retrieval process available.
- **9490**: Please note that this system is specific to the ammunition storage items, and you will not be able to retrieve a discarded weapon itself.
- **9491**: Any questions? [Tell me about the service./What weapons are applicable?/What do I do if I've lost it?/Back.]
- **9492**: I have compiled all applicable weapons into one list. If it's not on the list, I cannot help you.
- **9494**: The $8 is related to the $9.
- **9495**: If you wish to retrieve your $8, trade me your $9.
- **9496**: Before I forget, I would like to remind you that you have the Recycle Bin feature.
- **9497**: Do you know this feature? [The one in the Items menu?/The one on my desktop?/No clue.]
- **9498**: That's right. Make sure to check there if you accidentally discard something you didn't mean to.
- **9499**: I suppose an explanation is in order.
- **9500**: If you accidentally discard something you didn't mean to, stay calm and open up the Items submenu from the main menu.
- **9501**: At the top right is an entry for the Recycle Bin. You can retrieve your accidentally discarded item from there.
- **9502**: Up to ten items you have discarded while in your current area are stored in the bin.
- **9503**: If you throw away 11 or more items, the oldest ones are deleted first. The bin is also emptied when you log out or change areas.
- **9504**: If you make a mistake, don't panic. Check the bin first!
- **9505**: Hopefully this will help you avoid any accidents in the future!
- **9506**: You want to retrieve the item associated with this weapon? Let me take a look.
- **9507**: Hmm. The item associated with this weapon is the $0.
- **9508**: But you've already retrieved the item once before, so I cannot help you again.
- **9509**: Hang on...I think you've got that item located in a storage system somewhere. Take a good look.
- **9510**: I'm sorry. My services don't apply to that item.
- **9511**: This will be your one and only retrieval of your $0. Are you sure?
- **9512**: Retrieve your $0? [Yes./No.]
- **9513**: Here you are. Make sure not to lose it again!
- **9514**: Understood. Let me know if you change your mind.

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

### Event 445

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 700 bytes |
| Instructions | 167       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 03 10 03 02 00 04 10   ...............
0010: 03 03 00 05 10 03 04 00  06 10 03 05 00 07 10 03  ................
0020: 06 00 08 10 03 07 00 09  10 06 09 00 06 0B 00 06  ................
0030: 0C 00 1E F0 FF FF 7F 1D  00 80 23 03 08 00 01 80  ..........#.....
0040: 02 08 00 02 80 02 1C 02  24 03 80 0B 00 02 80 25  ........$......%
0050: 02 00 10 02 80 00 70 00  03 0B 00 00 10 1D 04 80  ......p.........
0060: 23 1D 05 80 23 1D 06 80  23 1D 07 80 23 01 19 02  #...#...#...#...
0070: 02 00 10 01 80 00 D1 01  03 0B 00 00 10 1D 08 80  ................
0080: 23 0B 08 00 02 08 00 01  80 02 CE 01 1A 22 02 D4  #............"..
0090: 02 09 80 0C 00 02 80 25  02 00 10 02 80 00 BE 00  .......%........
00A0: 03 09 00 00 10 03 0C 00  00 10 1A 4E 02 1D 0A 80  ...........N....
00B0: 23 93 01 17 1D 0B 80 23  93 02 80 01 CB 01 02 00  #......#........
00C0: 10 01 80 00 E4 00 03 09  00 00 10 03 0C 00 00 10  ................
00D0: 1A 4E 02 1D 0A 80 23 93  01 17 1D 0B 80 23 93 02  .N....#......#..
00E0: 80 01 CB 01 02 00 10 0C  80 00 0A 01 03 09 00 00  ................
00F0: 10 03 0C 00 00 10 1A 4E  02 1D 0A 80 23 93 01 17  .......N....#...
0100: 1D 0B 80 23 93 02 80 01  CB 01 02 00 10 0D 80 00  ...#............
0110: 30 01 03 09 00 00 10 03  0C 00 00 10 1A 4E 02 1D  0............N..
0120: 0A 80 23 93 01 17 1D 0B  80 23 93 02 80 01 CB 01  ..#......#......
0130: 02 00 10 0E 80 00 56 01  03 09 00 00 10 03 0C 00  ......V.........
0140: 00 10 1A 4E 02 1D 0A 80  23 93 01 17 1D 0B 80 23  ...N....#......#
0150: 93 02 80 01 CB 01 02 00  10 0F 80 00 7C 01 03 09  ............|...
0160: 00 00 10 03 0C 00 00 10  1A 4E 02 1D 0A 80 23 93  .........N....#.
0170: 01 17 1D 0B 80 23 93 02  80 01 CB 01 02 00 10 10  .....#..........
0180: 80 00 A2 01 03 09 00 00  10 03 0C 00 00 10 1A 4E  ...............N
0190: 02 1D 0A 80 23 93 01 17  1D 0B 80 23 93 02 80 01  ....#......#....
01A0: CB 01 02 00 10 11 80 00  C8 01 03 09 00 00 10 03  ................
01B0: 0C 00 00 10 1A 4E 02 1D  0A 80 23 93 01 17 1D 0B  .....N....#.....
01C0: 80 23 93 02 80 01 CB 01  0C 08 00 01 84 00 01 19  .#..............
01D0: 02 02 00 10 0C 80 00 14  02 03 0B 00 00 10 1D 12  ................
01E0: 80 23 24 13 80 02 80 02  80 25 02 00 10 02 80 00  .#$......%......
01F0: F9 01 1D 14 80 23 01 11  02 1D 15 80 23 1D 16 80  .....#......#...
0200: 23 1D 17 80 23 1D 18 80  23 1D 19 80 23 1D 1A 80  #...#...#...#...
0210: 23 01 19 02 03 08 00 02  80 01 40 00 1D 1B 80 23  #.........@....#
0220: 21 00 06 09 00 02 09 00  1C 80 03 4D 02 9D 0A 8D  !..........M....
0230: 02 0A 00 09 00 1C 80 9D  0F AD 02 0A 00 09 00 1C  ................
0240: 80 D4 03 09 00 0A 00 0B  09 00 01 25 02 1B 03 00  ...........%....
0250: 17 02 80 03 01 17 02 80  02 09 00 02 80 04 8C 02  ................
0260: 02 09 00 1C 80 03 89 02  9D 0A 8D 02 0A 00 09 00  ................
0270: 1C 80 03 00 17 0A 00 9D  0A 9D 02 0A 00 09 00 1C  ................
0280: 80 03 01 17 0A 00 01 89  02 01 8C 02 1B 1D 80 1E  ................
0290: 80 1F 80 20 80 21 80 22  80 23 80 24 80 25 80 26  ... .!.".#.$.%.&
02A0: 80 27 80 28 80 29 80 2A  80 2B 80 2C 80 02 10 03  .'.(.).*.+.,....
02B0: 10 04 10 05 10 06 10 07  10 08 10 09 10           .............   
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x000B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x0010 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x0015 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[6]
  5: 0x001A [0x03] ExtData[1]->WorkLocal[5] = Work_Zone[7]
  6: 0x001F [0x03] ExtData[1]->WorkLocal[6] = Work_Zone[8]
  7: 0x0024 [0x03] ExtData[1]->WorkLocal[7] = Work_Zone[9]
  8: 0x0029 [0x06] ExtData[1]->WorkLocal[9] = 0
  9: 0x002C [0x06] ExtData[1]->WorkLocal[11] = 0
 10: 0x002F [0x06] ExtData[1]->WorkLocal[12] = 0
 11: 0x0032 [0x1E] EventEntity looks at LocalPlayer and starts talking
 12: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=9486*)
    → "Welcome to the ammunition retrieval service."
 13: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x003B [0x03] ExtData[1]->WorkLocal[8] = 1*
 15: 0x0040 [0x02] IF !(ExtData[1]->WorkLocal[8] <= 0*) GOTO 0x021C
 16: 0x0048 [0x24] CREATE_DIALOG(message_id=9491*, default_option=ExtData[1]->WorkLocal[11], option_flags=0*)
    → "Any questions? [Tell me about the service./What weapons are applicable?/What do I do if I've lost it?/Back.]"
 17: 0x004F [0x25] WAIT_DIALOG_SELECT()
 18: 0x0050 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0070
 19: 0x0058 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[0]
 20: 0x005D [0x1D] PRINT_EVENT_MESSAGE(message_id=9487*)
    → "I'm pleased to announce that we've come up with a way for you to retrieve specific ammunition storage items that you may have previously lost--but one time only!"
 21: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0061 [0x1D] PRINT_EVENT_MESSAGE(message_id=9488*)
    → "If you want to retrieve one of said items, all you need to do is trade me the corresponding weapon."
 23: 0x0064 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0065 [0x1D] PRINT_EVENT_MESSAGE(message_id=9489*)
    → "Please keep in mind that this is a one-time-only service per weapon. There will be no second retrieval process available."
 25: 0x0068 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0069 [0x1D] PRINT_EVENT_MESSAGE(message_id=9490*)
    → "Please note that this system is specific to the ammunition storage items, and you will not be able to retrieve a discarded weapon itself."
 27: 0x006C [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x006D [0x01] GOTO 0x0219
 29: 0x0070 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x01D1
 30: 0x0078 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[0]
 31: 0x007D [0x1D] PRINT_EVENT_MESSAGE(message_id=9492*)
    → "I have compiled all applicable weapons into one list. If it's not on the list, I cannot help you."
 32: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0081 [0x0B] ExtData[1]->WorkLocal[8]++

SUBROUTINE_0084:
 34: 0x0084 [0x02] IF !(ExtData[1]->WorkLocal[8] <= 1*) GOTO 0x01CE
 35: 0x008C [0x1A] CALL_SUBROUTINE(address=0x0222)
 36: 0x008F [0xD4] MAP_QUERY_WINDOW: Test and open query window (flag=0x09, work=[0x0C80, 0x0200, 0x2580])
 37: 0x0098 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00BE
 38: 0x00A0 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
 39: 0x00A5 [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
 40: 0x00AA [0x1A] CALL_SUBROUTINE(address=0x024E)
 41: 0x00AD [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
 42: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x00B1 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
 44: 0x00B4 [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
 45: 0x00B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00B8 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 47: 0x00BB [0x01] GOTO 0x01CB
 48: 0x00BE [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00E4
 49: 0x00C6 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
 50: 0x00CB [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
 51: 0x00D0 [0x1A] CALL_SUBROUTINE(address=0x024E)
 52: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
 53: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x00D7 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
 55: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
 56: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00DE [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 58: 0x00E1 [0x01] GOTO 0x01CB
 59: 0x00E4 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x010A
 60: 0x00EC [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
 61: 0x00F1 [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
 62: 0x00F6 [0x1A] CALL_SUBROUTINE(address=0x024E)
 63: 0x00F9 [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
 64: 0x00FC [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x00FD [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
 66: 0x0100 [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
 67: 0x0103 [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x0104 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 69: 0x0107 [0x01] GOTO 0x01CB
 70: 0x010A [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x0130
 71: 0x0112 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
 72: 0x0117 [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
 73: 0x011C [0x1A] CALL_SUBROUTINE(address=0x024E)
 74: 0x011F [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
 75: 0x0122 [0x23] WAIT_FOR_DIALOG_INTERACTION
 76: 0x0123 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
 77: 0x0126 [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
 78: 0x0129 [0x23] WAIT_FOR_DIALOG_INTERACTION
 79: 0x012A [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 80: 0x012D [0x01] GOTO 0x01CB
 81: 0x0130 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x0156
 82: 0x0138 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
 83: 0x013D [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
 84: 0x0142 [0x1A] CALL_SUBROUTINE(address=0x024E)
 85: 0x0145 [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
 86: 0x0148 [0x23] WAIT_FOR_DIALOG_INTERACTION
 87: 0x0149 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
 88: 0x014C [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
 89: 0x014F [0x23] WAIT_FOR_DIALOG_INTERACTION
 90: 0x0150 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
 91: 0x0153 [0x01] GOTO 0x01CB
 92: 0x0156 [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x017C
 93: 0x015E [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
 94: 0x0163 [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
 95: 0x0168 [0x1A] CALL_SUBROUTINE(address=0x024E)
 96: 0x016B [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
 97: 0x016E [0x23] WAIT_FOR_DIALOG_INTERACTION
 98: 0x016F [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
 99: 0x0172 [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
100: 0x0175 [0x23] WAIT_FOR_DIALOG_INTERACTION
101: 0x0176 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
102: 0x0179 [0x01] GOTO 0x01CB
103: 0x017C [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x01A2
104: 0x0184 [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
105: 0x0189 [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
106: 0x018E [0x1A] CALL_SUBROUTINE(address=0x024E)
107: 0x0191 [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
108: 0x0194 [0x23] WAIT_FOR_DIALOG_INTERACTION
109: 0x0195 [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
110: 0x0198 [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
111: 0x019B [0x23] WAIT_FOR_DIALOG_INTERACTION
112: 0x019C [0x93] DISPLAY_ITEM_INFO(item_id=0*)
113: 0x019F [0x01] GOTO 0x01CB
114: 0x01A2 [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x01C8
115: 0x01AA [0x03] ExtData[1]->WorkLocal[9] = Work_Zone[0]
116: 0x01AF [0x03] ExtData[1]->WorkLocal[12] = Work_Zone[0]
117: 0x01B4 [0x1A] CALL_SUBROUTINE(address=0x024E)
118: 0x01B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=9494*)
    → "The $8 is related to the $9."
119: 0x01BA [0x23] WAIT_FOR_DIALOG_INTERACTION
120: 0x01BB [0x93] DISPLAY_ITEM_INFO(item_id=Work_Zone_1700[1])
121: 0x01BE [0x1D] PRINT_EVENT_MESSAGE(message_id=9495*)
    → "If you wish to retrieve your $8, trade me your $9."
122: 0x01C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
123: 0x01C2 [0x93] DISPLAY_ITEM_INFO(item_id=0*)
124: 0x01C5 [0x01] GOTO 0x01CB
125: 0x01C8 [0x0C] ExtData[1]->WorkLocal[8]--

SUBROUTINE_01CB:
126: 0x01CB [0x01] GOTO 0x0084
127: 0x01CE [0x01] GOTO 0x0219
128: 0x01D1 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0214
129: 0x01D9 [0x03] ExtData[1]->WorkLocal[11] = Work_Zone[0]
130: 0x01DE [0x1D] PRINT_EVENT_MESSAGE(message_id=9496*)
    → "Before I forget, I would like to remind you that you have the Recycle Bin feature."
131: 0x01E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
132: 0x01E2 [0x24] CREATE_DIALOG(message_id=9497*, default_option=0*, option_flags=0*)
    → "Do you know this feature? [The one in the Items menu?/The one on my desktop?/No clue.]"
133: 0x01E9 [0x25] WAIT_DIALOG_SELECT()
134: 0x01EA [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x01F9
135: 0x01F2 [0x1D] PRINT_EVENT_MESSAGE(message_id=9498*)
    → "That's right. Make sure to check there if you accidentally discard something you didn't mean to."
136: 0x01F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
137: 0x01F6 [0x01] GOTO 0x0211
138: 0x01F9 [0x1D] PRINT_EVENT_MESSAGE(message_id=9499*)
    → "I suppose an explanation is in order."
139: 0x01FC [0x23] WAIT_FOR_DIALOG_INTERACTION
140: 0x01FD [0x1D] PRINT_EVENT_MESSAGE(message_id=9500*)
    → "If you accidentally discard something you didn't mean to, stay calm and open up the Items submenu from the main menu."
141: 0x0200 [0x23] WAIT_FOR_DIALOG_INTERACTION
142: 0x0201 [0x1D] PRINT_EVENT_MESSAGE(message_id=9501*)
    → "At the top right is an entry for the Recycle Bin. You can retrieve your accidentally discarded item from there."
143: 0x0204 [0x23] WAIT_FOR_DIALOG_INTERACTION
144: 0x0205 [0x1D] PRINT_EVENT_MESSAGE(message_id=9502*)
    → "Up to ten items you have discarded while in your current area are stored in the bin."
145: 0x0208 [0x23] WAIT_FOR_DIALOG_INTERACTION
146: 0x0209 [0x1D] PRINT_EVENT_MESSAGE(message_id=9503*)
    → "If you throw away 11 or more items, the oldest ones are deleted first. The bin is also emptied when you log out or change areas."
147: 0x020C [0x23] WAIT_FOR_DIALOG_INTERACTION
148: 0x020D [0x1D] PRINT_EVENT_MESSAGE(message_id=9504*)
    → "If you make a mistake, don't panic. Check the bin first!"
149: 0x0210 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0211:
150: 0x0211 [0x01] GOTO 0x0219
151: 0x0214 [0x03] ExtData[1]->WorkLocal[8] = 0*

SUBROUTINE_0219:
152: 0x0219 [0x01] GOTO 0x0040
153: 0x021C [0x1D] PRINT_EVENT_MESSAGE(message_id=9505*)
    → "Hopefully this will help you avoid any accidents in the future!"
154: 0x021F [0x23] WAIT_FOR_DIALOG_INTERACTION
155: 0x0220 [0x21] END_EVENT
156: 0x0221 [0x00] END_REQSTACK()

SUBROUTINE_0222:
157: 0x0222 [0x06] ExtData[1]->WorkLocal[9] = 0
158: 0x0225 [0x02] IF !(ExtData[1]->WorkLocal[9] >= 8*) GOTO 0x024D
159: 0x022D [0x9D] IF (0x028D) ExtData[1]->WorkLocal[9] = ExtData[1]->WorkLocal[10] // extra=0x801C
160: 0x0237 [0x9D] Table[0x02AD] = ExtData[1]->WorkLocal[10] // p3=ExtData[1]->WorkLocal[9], p4=0x801C
161: 0x0241 [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[09 00 0A 00 0B 09 00 01...])
162: 0x025F [0x02] IF !(0x0902 == 0x1C00) GOTO 0x8903
163: 0x0267 [0x02] IF !(0x0A9D ^ 0x028D) GOTO 0x0900
164: 0x026F [0x00] END_REQSTACK()
165: 0x0270 [0x1C] WAIT(0x0380 ticks)
166: 0x0273 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0274 [0x17] ExtData[1]->WorkLocal[10] = cos(0x0A9D) * 0x029D
     0x027B [0x0A] 0x0900 &= ~(1 << 0x1C00)
     0x0280 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 169279747/0x0A170103))
     0x0285 [0x00] END_REQSTACK()
     0x0286 [0x01] GOTO 0x0289
     0x0289 [0x01] GOTO 0x028C
     0x028C [0x1B] RETURN
     0x028D [0x1D] PRINT_EVENT_MESSAGE(message_id=0x1E80)
     0x0290 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149613599/0x8020801F))
     0x0295 [0x21] END_EVENT
     0x0296 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149810210/0x80238022))
     0x029B [0x24] CREATE_DIALOG(message_id=0x2580, default_option=0x2680, option_flags=0x2780)
     0x02A2 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2150203432/0x80298028))
     0x02A7 [0x2A] GET_REQ_LEVEL(level=128, entity_id=Unknown NPC (ID: 2150400043/0x802C802B))
     0x02AD [0x02] IF !(0x0310 == 0x0410) GOTO 0x1005
     0x02B5 [0x06] 0x0710 = 0
     0x02B8 [0x10] Work_Zone[8] <<= Work_Zone[9]
```

### Event 446

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02BD    |
| Data Size    | 101 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02B0:                                         03 00 00               ...
02C0: 02 10 03 01 00 03 10 03  02 00 04 10 03 03 00 05  ................
02D0: 10 06 09 00 1E F0 FF FF  7F 03 02 10 02 00 1D 2D  ...............-
02E0: 80 23 1D 2E 80 23 42 1D  2F 80 23 24 30 80 01 80  .#...#B./.#$0...
02F0: 02 80 25 02 00 10 02 80  00 07 03 1D 31 80 23 03  ..%.........1.#.
0300: 01 10 01 80 01 20 03 02  00 10 01 80 00 1B 03 1D  ..... ..........
0310: 32 80 23 03 01 10 0C 80  01 20 03 03 01 10 02 80  2.#...... ......
0320: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x02BD [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x02C2 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x02C7 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x02CC [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x02D1 [0x06] ExtData[1]->WorkLocal[9] = 0
  5: 0x02D4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x02D9 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
  7: 0x02DE [0x1D] PRINT_EVENT_MESSAGE(message_id=9506*)
    → "You want to retrieve the item associated with this weapon? Let me take a look."
  8: 0x02E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x02E2 [0x1D] PRINT_EVENT_MESSAGE(message_id=9507*)
    → "Hmm. The item associated with this weapon is the $0."
 10: 0x02E5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x02E6 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 12: 0x02E7 [0x1D] PRINT_EVENT_MESSAGE(message_id=9511*)
    → "This will be your one and only retrieval of your $0. Are you sure?"
 13: 0x02EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x02EB [0x24] CREATE_DIALOG(message_id=9512*, default_option=1*, option_flags=0*)
    → "Retrieve your $0? [Yes./No.]"
 15: 0x02F2 [0x25] WAIT_DIALOG_SELECT()
 16: 0x02F3 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0307
 17: 0x02FB [0x1D] PRINT_EVENT_MESSAGE(message_id=9513*)
    → "Here you are. Make sure not to lose it again!"
 18: 0x02FE [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x02FF [0x03] Work_Zone[1] = 1*
 20: 0x0304 [0x01] GOTO 0x0320
 21: 0x0307 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x031B
 22: 0x030F [0x1D] PRINT_EVENT_MESSAGE(message_id=9514*)
    → "Understood. Let me know if you change your mind."
 23: 0x0312 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x0313 [0x03] Work_Zone[1] = 2*
 25: 0x0318 [0x01] GOTO 0x0320
 26: 0x031B [0x03] Work_Zone[1] = 0*

SUBROUTINE_0320:
 27: 0x0320 [0x21] END_EVENT
 28: 0x0321 [0x00] END_REQSTACK()
```

### Event 447

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0322    |
| Data Size    | 101 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0320:       03 00 00 02 10 03  01 00 03 10 03 02 00 04    ..............
0330: 10 03 03 00 05 10 06 09  00 1E F0 FF FF 7F 02 03  ................
0340: 00 02 80 80 4D 03 1D 33  80 23 01 85 03 02 03 00  ....M..3.#......
0350: 01 80 80 69 03 03 02 10  02 00 1D 2D 80 23 1D 2E  ...i.......-.#..
0360: 80 23 1D 34 80 23 01 85  03 02 03 00 0C 80 80 85  .#.4.#..........
0370: 03 03 02 10 02 00 1D 2D  80 23 1D 2E 80 23 1D 35  .......-.#...#.5
0380: 80 23 01 85 03 21 00                              .#...!.         
```

#### Opcodes

```
  0: 0x0322 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0327 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[3]
  2: 0x032C [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[4]
  3: 0x0331 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[5]
  4: 0x0336 [0x06] ExtData[1]->WorkLocal[9] = 0
  5: 0x0339 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x033E [0x02] IF !(ExtData[1]->WorkLocal[3] == 0*) GOTO 0x034D
  7: 0x0346 [0x1D] PRINT_EVENT_MESSAGE(message_id=9510*)
    → "I'm sorry. My services don't apply to that item."
  8: 0x0349 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x034A [0x01] GOTO 0x0385
 10: 0x034D [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x0369
 11: 0x0355 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 12: 0x035A [0x1D] PRINT_EVENT_MESSAGE(message_id=9506*)
    → "You want to retrieve the item associated with this weapon? Let me take a look."
 13: 0x035D [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x035E [0x1D] PRINT_EVENT_MESSAGE(message_id=9507*)
    → "Hmm. The item associated with this weapon is the $0."
 15: 0x0361 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0362 [0x1D] PRINT_EVENT_MESSAGE(message_id=9508*)
    → "But you've already retrieved the item once before, so I cannot help you again."
 17: 0x0365 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0366 [0x01] GOTO 0x0385
 19: 0x0369 [0x02] IF !(ExtData[1]->WorkLocal[3] == 2*) GOTO 0x0385
 20: 0x0371 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 21: 0x0376 [0x1D] PRINT_EVENT_MESSAGE(message_id=9506*)
    → "You want to retrieve the item associated with this weapon? Let me take a look."
 22: 0x0379 [0x23] WAIT_FOR_DIALOG_INTERACTION
 23: 0x037A [0x1D] PRINT_EVENT_MESSAGE(message_id=9507*)
    → "Hmm. The item associated with this weapon is the $0."
 24: 0x037D [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x037E [0x1D] PRINT_EVENT_MESSAGE(message_id=9509*)
    → "Hang on...I think you've got that item located in a storage system somewhere. Take a good look."
 26: 0x0381 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0382 [0x01] GOTO 0x0385

SUBROUTINE_0385:
 28: 0x0385 [0x21] END_EVENT
 29: 0x0386 [0x00] END_REQSTACK()
```
