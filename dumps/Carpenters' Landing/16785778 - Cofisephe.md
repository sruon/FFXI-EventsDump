# 16785778 - Cofisephe

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Carpenters' Landing (ID: 2) |
| Block Size       | 304 bytes                   |
| Total Events     | 2                           |
| References Count | 16                          |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [31](#event-31)       | 0x0001       |    214 |             64 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D19      |        7449 |
|       1 | 0x1D1A      |        7450 |
|       2 | 0x1D1B      |        7451 |
|       3 | 0x0002      |           2 |
|       4 | 0x0000      |           0 |
|       5 | 0x1D1D      |        7453 |
|       6 | 0x0032      |          50 |
|       7 | 0x1D14      |        7444 |
|       8 | 0x1D1C      |        7452 |
|       9 | 0x0001      |           1 |
|      10 | 0x000A      |          10 |
|      11 | 0x1D1E      |        7454 |
|      12 | 0x1D1F      |        7455 |
|      13 | 0x1D20      |        7456 |
|      14 | 0x012C      |         300 |
|      15 | 0x1D12      |        7442 |

## String References

- **7442**: Thank you, [sir/madame]. Enjoy your trip.
- **7444**: I'm sorry, [sir/madame]. You don't have enough gil to purchase a ticket.
- **7449**: Welcome to Carpenters' Landing.
- **7450**: Barge tickets can be purchased for $2 gil. Multi-tickets, which allow you to ride ten times, are available for a discounted price of $3 gil. Will you be sailing with us today?
- **7451**: Purchase... [6 ($2 gil)./$6 ($3 gil)./Nothing today.]
- **7452**: Thank you, [sir/madam]. I hope you enjoy sailing with us.
- **7453**: You cannot buy more than one $3. Use the one you currently have to ride the next ship.
- **7454**: Your $3 is valid for $4 more [trip/trips]. You do not need to purchase a new ticket at this time.
- **7455**: Your $3 is valid for $4 more [trip/trips]. If you wish, you can purchase a new one for $3 gil.
- **7456**: Purchase a new multi-ticket? [Yes ($3 gil)./No.]

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

### Event 31

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 214 bytes |
| Instructions | 64        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 24 02   ........#...#$.
0010: 80 03 80 04 80 25 02 00  10 04 80 00 4F 00 3E 07  .....%......O.>.
0020: 10 04 80 2F 00 1D 05 80  23 06 01 10 01 4C 00 42  .../....#....L.B
0030: 43 00 43 01 02 03 10 06  80 03 43 00 1D 07 80 23  C.C.......C....#
0040: 01 4C 00 1D 08 80 23 03  01 10 09 80 01 D5 00 02  .L....#.........
0050: 00 10 09 80 00 C7 00 3E  07 10 09 80 A7 00 02 06  .......>........
0060: 10 0A 80 04 70 00 1D 0B  80 23 06 01 10 01 A4 00  ....p....#......
0070: 1D 0C 80 23 24 0D 80 09  80 04 80 25 02 00 10 04  ...#$......%....
0080: 80 00 A4 00 42 43 00 43  01 02 03 10 0E 80 03 98  ....BC.C........
0090: 00 1D 07 80 23 01 A1 00  1D 0F 80 23 03 01 10 03  ....#......#....
00A0: 80 01 A4 00 01 C4 00 42  43 00 43 01 02 03 10 0E  .......BC.C.....
00B0: 80 03 BB 00 1D 07 80 23  01 C4 00 1D 08 80 23 03  .......#......#.
00C0: 01 10 03 80 01 D5 00 02  00 10 03 80 00 D5 00 06  ................
00D0: 01 10 01 D5 00 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7449*)
    → "Welcome to Carpenters' Landing."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7450*)
    → "Barge tickets can be purchased for $2 gil. Multi-tickets, which allow you to ride ten times, are available for a discounted price of $3 gil. Will you be sailing with us today?"
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x24] CREATE_DIALOG(message_id=7451*, default_option=2*, option_flags=0*)
    → "Purchase... [6 ($2 gil)./$6 ($3 gil)./Nothing today.]"
  6: 0x0015 [0x25] WAIT_DIALOG_SELECT()
  7: 0x0016 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x004F
  8: 0x001E [0x3E] IF !(Work_Zone[7] bit 0*) GOTO 0x002F
  9: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7453*)
    → "You cannot buy more than one $3. Use the one you currently have to ride the next ship."
 10: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0029 [0x06] Work_Zone[1] = 0
 12: 0x002C [0x01] GOTO 0x004C
 13: 0x002F [0x42] SET_CLI_EVENT_CANCEL_DATA()
 14: 0x0030 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 15: 0x0032 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 16: 0x0034 [0x02] IF !(Work_Zone[3] >= 50*) GOTO 0x0043
 17: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7444*)
    → "I'm sorry, [sir/madame]. You don't have enough gil to purchase a ticket."
 18: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0040 [0x01] GOTO 0x004C
 20: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=7452*)
    → "Thank you, [sir/madam]. I hope you enjoy sailing with us."
 21: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0047 [0x03] Work_Zone[1] = 1*

SUBROUTINE_004C:
 23: 0x004C [0x01] GOTO 0x00D5
 24: 0x004F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00C7
 25: 0x0057 [0x3E] IF !(Work_Zone[7] bit 1*) GOTO 0x00A7
 26: 0x005E [0x02] IF !(Work_Zone[6] < 10*) GOTO 0x0070
 27: 0x0066 [0x1D] PRINT_EVENT_MESSAGE(message_id=7454*)
    → "Your $3 is valid for $4 more [trip/trips]. You do not need to purchase a new ticket at this time."
 28: 0x0069 [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x006A [0x06] Work_Zone[1] = 0
 30: 0x006D [0x01] GOTO 0x00A4
 31: 0x0070 [0x1D] PRINT_EVENT_MESSAGE(message_id=7455*)
    → "Your $3 is valid for $4 more [trip/trips]. If you wish, you can purchase a new one for $3 gil."
 32: 0x0073 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0074 [0x24] CREATE_DIALOG(message_id=7456*, default_option=1*, option_flags=0*)
    → "Purchase a new multi-ticket? [Yes ($3 gil)./No.]"
 34: 0x007B [0x25] WAIT_DIALOG_SELECT()
 35: 0x007C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x00A4
 36: 0x0084 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 37: 0x0085 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 38: 0x0087 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 39: 0x0089 [0x02] IF !(Work_Zone[3] >= 300*) GOTO 0x0098
 40: 0x0091 [0x1D] PRINT_EVENT_MESSAGE(message_id=7444*)
    → "I'm sorry, [sir/madame]. You don't have enough gil to purchase a ticket."
 41: 0x0094 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x0095 [0x01] GOTO 0x00A1
 43: 0x0098 [0x1D] PRINT_EVENT_MESSAGE(message_id=7442*)
    → "Thank you, [sir/madame]. Enjoy your trip."
 44: 0x009B [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x009C [0x03] Work_Zone[1] = 2*

SUBROUTINE_00A1:
 46: 0x00A1 [0x01] GOTO 0x00A4

SUBROUTINE_00A4:
 47: 0x00A4 [0x01] GOTO 0x00C4
 48: 0x00A7 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 49: 0x00A8 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 50: 0x00AA [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 51: 0x00AC [0x02] IF !(Work_Zone[3] >= 300*) GOTO 0x00BB
 52: 0x00B4 [0x1D] PRINT_EVENT_MESSAGE(message_id=7444*)
    → "I'm sorry, [sir/madame]. You don't have enough gil to purchase a ticket."
 53: 0x00B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x00B8 [0x01] GOTO 0x00C4
 55: 0x00BB [0x1D] PRINT_EVENT_MESSAGE(message_id=7452*)
    → "Thank you, [sir/madam]. I hope you enjoy sailing with us."
 56: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x00BF [0x03] Work_Zone[1] = 2*

SUBROUTINE_00C4:
 58: 0x00C4 [0x01] GOTO 0x00D5
 59: 0x00C7 [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00D5
 60: 0x00CF [0x06] Work_Zone[1] = 0
 61: 0x00D2 [0x01] GOTO 0x00D5

SUBROUTINE_00D5:
 62: 0x00D5 [0x21] END_EVENT
 63: 0x00D6 [0x00] END_REQSTACK()
```
