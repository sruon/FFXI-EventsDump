# 16794029 - Tswe Panipahr

## Common Data

| Field            | Value              |
|------------------|--------------------|
| Zone             | Bibiki Bay (ID: 4) |
| Block Size       | 540 bytes          |
| Total Events     | 2                  |
| References Count | 32                 |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [35](#event-35)       | 0x0001       |    386 |            118 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D34      |        7476 |
|       1 | 0x1D35      |        7477 |
|       2 | 0x1D36      |        7478 |
|       3 | 0x1D37      |        7479 |
|       4 | 0x0000      |           0 |
|       5 | 0x0001      |           1 |
|       6 | 0x1D4F      |        7503 |
|       7 | 0x1D50      |        7504 |
|       8 | 0x0002      |           2 |
|       9 | 0x1D51      |        7505 |
|      10 | 0x0050      |          80 |
|      11 | 0x1D3B      |        7483 |
|      12 | 0x1D3A      |        7482 |
|      13 | 0x028D      |         653 |
|      14 | 0x01F4      |         500 |
|      15 | 0x1D52      |        7506 |
|      16 | 0x000A      |          10 |
|      17 | 0x1D54      |        7508 |
|      18 | 0x1D55      |        7509 |
|      19 | 0x1D53      |        7507 |
|      20 | 0x1D3D      |        7485 |
|      21 | 0x1D3E      |        7486 |
|      22 | 0x1D3F      |        7487 |
|      23 | 0x1D40      |        7488 |
|      24 | 0x1D41      |        7489 |
|      25 | 0x1D48      |        7496 |
|      26 | 0x1D42      |        7490 |
|      27 | 0x1D43      |        7491 |
|      28 | 0x1D44      |        7492 |
|      29 | 0x1D45      |        7493 |
|      30 | 0x1D46      |        7494 |
|      31 | 0x1D47      |        7495 |

## String References

- **7476**: Welcome to Sunset Docks!
- **7477**: Enjoy a sightseeing tour of Bibiki Bay, an initiative of the Fishermen's Guild!
- **7478**: How may I help you?
- **7479**: What do you want to do? [Nothing in particular./Buy a ticket./Ask about the tours.]
- **7482**: Thank you, [sir/ma'am]! Have a wonderrrful trip!
- **7483**: I'm sorry, [sir/ma'am]. You don't have enough gil to purrrchase a ticket.
- **7485**: Which tour do you wish to have explained?
- **7486**: Choose a tour: [Dhalmel Rock tour./Maliyakaleya Reef tour./Purgonorgo Isle tour.]
- **7487**: The Dhalmel Rrrock tour takes a gentle, southerly course along the western coastline.
- **7488**: You can see the majestic pillars of rrrock towering above the surf, and watch the waves crrrash against Washboard Wake while enjoying the refrrreshing sea breeze.
- **7489**: The manaclipper turns to pass through the legs of Dhalmel Rrrock before making its way back to Sunset Docks. This is the most rrrelaxing of the tours.
- **7490**: This tour takes you on an easterly course past the menacing Seawolf Swirrrl as it rounds the cape of Mhaura.
- **7491**: The stunning Maliyakaleya Reef is the highlight of the trip, home to a menagerrrie of colorful sea life to tempt your fishing line.
- **7492**: After passing through the rrreef, the manaclipper makes its way back to Sunset Docks to complete this brrreathtakingly beautiful tour.
- **7493**: The manaclipper leaves here from Sunset Docks on a southeasterly course.
- **7494**: This tour provides a safe and pleasant rrride to the tropical paradise of Purgonorgo Isle.
- **7495**: Manaclippers arrive rrregularly to ferry passengers back to Sunset Docks, so there's no need to worry about time. Sit back, rrrelax, and enjoy a long, lazy stay on this beautiful island.
- **7496**: Is there anything else I can help you with?
- **7503**: Tickets for the manaclipper are $2 gil. Multi-tickets, which allow you to rrride ten times, can be purrrchased for a mere $5 gil.
- **7504**: Which would you like? [6 ($2 gil)./$6 ($5 gil)./Nothing today.]
- **7505**: You cannot buy morrre than one $3. Use the one you have now to ride the next ship.
- **7506**: Your $3 is valid for $4 more [trip/trips].
- **7507**: You do not need to purrrchase a new ticket at this time.
- **7508**: If you want, you can purrrchase a new one for $5 gil.
- **7509**: Purrrchase a new multi-ticket? [Yes ($5 gil)./No.]

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

### Event 35

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 386 bytes |
| Instructions | 95        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 1D 02   ........#...#..
0010: 80 23 24 03 80 04 80 04  80 25 02 00 10 05 80 00  .#$......%......
0020: 10 01 1D 06 80 23 24 07  80 08 80 04 80 25 02 00  .....#$......%..
0030: 10 04 80 00 6A 00 42 43  00 43 01 3E 04 10 04 80  ....j.BC.C.>....
0040: 4C 00 1D 09 80 23 06 01  10 01 67 00 02 05 10 0A  L....#....g.....
0050: 80 03 5E 00 1D 0B 80 23  06 01 10 01 67 00 1D 0C  ..^....#....g...
0060: 80 23 03 01 10 05 80 01  0D 01 02 00 10 05 80 00  .#..............
0070: FF 00 42 43 00 43 01 03  03 10 0D 80 03 07 10 0E  ..BC.C..........
0080: 80 3E 04 10 05 80 E1 00  1D 0F 80 23 02 06 10 10  .>.........#....
0090: 80 03 D7 00 1D 11 80 23  24 12 80 05 80 04 80 25  .......#$......%
00A0: 02 00 10 04 80 00 C6 00  02 05 10 0E 80 03 BA 00  ................
00B0: 1D 0B 80 23 06 01 10 01  C3 00 1D 0C 80 23 03 01  ...#.........#..
00C0: 10 08 80 01 D4 00 02 00  10 05 80 00 D4 00 06 01  ................
00D0: 10 01 D4 00 01 DE 00 1D  13 80 23 06 01 10 01 FC  ..........#.....
00E0: 00 02 05 10 0E 80 03 F3  00 1D 0B 80 23 06 01 10  ............#...
00F0: 01 FC 00 1D 0C 80 23 03  01 10 08 80 01 0D 01 02  ......#.........
0100: 00 10 08 80 00 0D 01 06  01 10 01 0D 01 01 81 01  ................
0110: 02 00 10 08 80 00 81 01  1D 14 80 23 24 15 80 04  ...........#$...
0120: 80 04 80 25 02 00 10 04  80 00 42 01 1D 16 80 23  ...%......B....#
0130: 1D 17 80 23 1D 18 80 23  1D 19 80 23 01 12 00 01  ...#...#...#....
0140: 7E 01 02 00 10 05 80 00  60 01 1D 1A 80 23 1D 1B  ~.......`....#..
0150: 80 23 1D 1C 80 23 1D 19  80 23 01 12 00 01 7E 01  .#...#...#....~.
0160: 02 00 10 08 80 00 7E 01  1D 1D 80 23 1D 1E 80 23  ......~....#...#
0170: 1D 1F 80 23 1D 19 80 23  01 12 00 01 7E 01 01 81  ...#...#....~...
0180: 01 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7476*)
    → "Welcome to Sunset Docks!"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7477*)
    → "Enjoy a sightseeing tour of Bibiki Bay, an initiative of the Fishermen's Guild!"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x1D] PRINT_EVENT_MESSAGE(message_id=7478*)
    → "How may I help you?"
  6: 0x0011 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0012 [0x24] CREATE_DIALOG(message_id=7479*, default_option=0*, option_flags=0*)
    → "What do you want to do? [Nothing in particular./Buy a ticket./Ask about the tours.]"
  8: 0x0019 [0x25] WAIT_DIALOG_SELECT()
  9: 0x001A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0110
 10: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7503*)
    → "Tickets for the manaclipper are $2 gil. Multi-tickets, which allow you to rrride ten times, can be purrrchased for a mere $5 gil."
 11: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0026 [0x24] CREATE_DIALOG(message_id=7504*, default_option=2*, option_flags=0*)
    → "Which would you like? [6 ($2 gil)./$6 ($5 gil)./Nothing today.]"
 13: 0x002D [0x25] WAIT_DIALOG_SELECT()
 14: 0x002E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006A
 15: 0x0036 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 16: 0x0037 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 17: 0x0039 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 18: 0x003B [0x3E] IF !(Work_Zone[4] bit 0*) GOTO 0x004C
 19: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=7505*)
    → "You cannot buy morrre than one $3. Use the one you have now to ride the next ship."
 20: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0046 [0x06] Work_Zone[1] = 0
 22: 0x0049 [0x01] GOTO 0x0067
 23: 0x004C [0x02] IF !(Work_Zone[5] >= 80*) GOTO 0x005E
 24: 0x0054 [0x1D] PRINT_EVENT_MESSAGE(message_id=7483*)
    → "I'm sorry, [sir/ma'am]. You don't have enough gil to purrrchase a ticket."
 25: 0x0057 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0058 [0x06] Work_Zone[1] = 0
 27: 0x005B [0x01] GOTO 0x0067
 28: 0x005E [0x1D] PRINT_EVENT_MESSAGE(message_id=7482*)
    → "Thank you, [sir/ma'am]! Have a wonderrrful trip!"
 29: 0x0061 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0062 [0x03] Work_Zone[1] = 1*

SUBROUTINE_0067:
 31: 0x0067 [0x01] GOTO 0x010D
 32: 0x006A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00FF
 33: 0x0072 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 34: 0x0073 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 35: 0x0075 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 36: 0x0077 [0x03] Work_Zone[3] = 653*
 37: 0x007C [0x03] Work_Zone[7] = 500*
 38: 0x0081 [0x3E] IF !(Work_Zone[4] bit 1*) GOTO 0x00E1
 39: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7506*)
    → "Your $3 is valid for $4 more [trip/trips]."
 40: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x008C [0x02] IF !(Work_Zone[6] >= 10*) GOTO 0x00D7
 42: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=7508*)
    → "If you want, you can purrrchase a new one for $5 gil."
 43: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x0098 [0x24] CREATE_DIALOG(message_id=7509*, default_option=1*, option_flags=0*)
    → "Purrrchase a new multi-ticket? [Yes ($5 gil)./No.]"
 45: 0x009F [0x25] WAIT_DIALOG_SELECT()
 46: 0x00A0 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00C6
 47: 0x00A8 [0x02] IF !(Work_Zone[5] >= 500*) GOTO 0x00BA
 48: 0x00B0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7483*)
    → "I'm sorry, [sir/ma'am]. You don't have enough gil to purrrchase a ticket."
 49: 0x00B3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x00B4 [0x06] Work_Zone[1] = 0
 51: 0x00B7 [0x01] GOTO 0x00C3
 52: 0x00BA [0x1D] PRINT_EVENT_MESSAGE(message_id=7482*)
    → "Thank you, [sir/ma'am]! Have a wonderrrful trip!"
 53: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x00BE [0x03] Work_Zone[1] = 2*

SUBROUTINE_00C3:
 55: 0x00C3 [0x01] GOTO 0x00D4
 56: 0x00C6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00D4
 57: 0x00CE [0x06] Work_Zone[1] = 0
 58: 0x00D1 [0x01] GOTO 0x00D4

SUBROUTINE_00D4:
 59: 0x00D4 [0x01] GOTO 0x00DE
 60: 0x00D7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7507*)
    → "You do not need to purrrchase a new ticket at this time."
 61: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x00DB [0x06] Work_Zone[1] = 0

SUBROUTINE_00DE:
 63: 0x00DE [0x01] GOTO 0x00FC
 64: 0x00E1 [0x02] IF !(Work_Zone[5] >= 500*) GOTO 0x00F3
 65: 0x00E9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7483*)
    → "I'm sorry, [sir/ma'am]. You don't have enough gil to purrrchase a ticket."
 66: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x00ED [0x06] Work_Zone[1] = 0
 68: 0x00F0 [0x01] GOTO 0x00FC
 69: 0x00F3 [0x1D] PRINT_EVENT_MESSAGE(message_id=7482*)
    → "Thank you, [sir/ma'am]! Have a wonderrrful trip!"
 70: 0x00F6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 71: 0x00F7 [0x03] Work_Zone[1] = 2*

SUBROUTINE_00FC:
 72: 0x00FC [0x01] GOTO 0x010D
 73: 0x00FF [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x010D
 74: 0x0107 [0x06] Work_Zone[1] = 0
 75: 0x010A [0x01] GOTO 0x010D

SUBROUTINE_010D:
 76: 0x010D [0x01] GOTO 0x0181
 77: 0x0110 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x0181
 78: 0x0118 [0x1D] PRINT_EVENT_MESSAGE(message_id=7485*)
    → "Which tour do you wish to have explained?"
 79: 0x011B [0x23] WAIT_FOR_DIALOG_INTERACTION
 80: 0x011C [0x24] CREATE_DIALOG(message_id=7486*, default_option=0*, option_flags=0*)
    → "Choose a tour: [Dhalmel Rock tour./Maliyakaleya Reef tour./Purgonorgo Isle tour.]"
 81: 0x0123 [0x25] WAIT_DIALOG_SELECT()
 82: 0x0124 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0142
 83: 0x012C [0x1D] PRINT_EVENT_MESSAGE(message_id=7487*)
    → "The Dhalmel Rrrock tour takes a gentle, southerly course along the western coastline."
 84: 0x012F [0x23] WAIT_FOR_DIALOG_INTERACTION
 85: 0x0130 [0x1D] PRINT_EVENT_MESSAGE(message_id=7488*)
    → "You can see the majestic pillars of rrrock towering above the surf, and watch the waves crrrash against Washboard Wake while enjoying the refrrreshing sea breeze."
 86: 0x0133 [0x23] WAIT_FOR_DIALOG_INTERACTION
 87: 0x0134 [0x1D] PRINT_EVENT_MESSAGE(message_id=7489*)
    → "The manaclipper turns to pass through the legs of Dhalmel Rrrock before making its way back to Sunset Docks. This is the most rrrelaxing of the tours."
 88: 0x0137 [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x0138 [0x1D] PRINT_EVENT_MESSAGE(message_id=7496*)
    → "Is there anything else I can help you with?"
 90: 0x013B [0x23] WAIT_FOR_DIALOG_INTERACTION
 91: 0x013C [0x01] GOTO 0x0012

SUBROUTINE_017E:
 92: 0x017E [0x01] GOTO 0x0181

SUBROUTINE_0181:
 93: 0x0181 [0x21] END_EVENT
 94: 0x0182 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x013F [0x01] GOTO 0x017E
     0x015D [0x01] GOTO 0x017E
     0x017B [0x01] GOTO 0x017E
```
