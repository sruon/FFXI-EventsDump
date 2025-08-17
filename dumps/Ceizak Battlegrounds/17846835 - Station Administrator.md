# 17846835 - Station Administrator

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 380 bytes                      |
| Total Events     | 2                              |
| References Count | 18                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [3001](#event-3001)   | 0x0001       |    283 |             69 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x1D85      |        7557 |
|       3 | 0x40000000  |  1073741824 |
|       4 | 0x1D86      |        7558 |
|       5 | 0x0007      |           7 |
|       6 | 0x0002      |           2 |
|       7 | 0x1D87      |        7559 |
|       8 | 0x0006      |           6 |
|       9 | 0x0003      |           3 |
|      10 | 0x1D88      |        7560 |
|      11 | 0x1D89      |        7561 |
|      12 | 0x0004      |           4 |
|      13 | 0x1D8B      |        7563 |
|      14 | 0x0005      |           5 |
|      15 | 0x1D8D      |        7565 |
|      16 | 0x1D8A      |        7562 |
|      17 | 0x1D8C      |        7564 |

## String References

- **7557**: Thanks for coming all this way. I'd love to offer you some hospitality, but we'd need to get this frontier station completed first! Could you lend us a hand by signing up for a coalition assignment?
- **7558**: Thanks so much for delivering this $3! I can't wait to see how this station looks once it's built. If you want, you can go pick up your reward from the manager who gave you this assignment.
- **7559**: We're glad you tried your best, but destroyed $5 are useless to us. Sorry, but can you pick up another one from the manager in charge?
- **7560**: Welcome to the frontier! This station has already been built, but you can always help construct some bivouacs or keep them supplied.
- **7561**: Frontier stations are self-sufficient, but the bivouacs are sadly not. We'd be extremely appreciative if you could undertake some assignments to make sure they stay in operation.
- **7562**: Hello, there! We have some materials we'd like delivered to town, but we have to go through the right channels. Would you mind undertaking a coalition assignment to transport them back?
- **7563**: Thank you for helping us out. Here's the $3. All we ask is that you take it to the manager in charge of this assignment.
- **7564**: Thank you for helping us out. All we ask is that you deliver your cargo safely to the manager in charge of this assignment.
- **7565**: Well, here's another $3, but please be careful not to break this one.

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

### Event 3001

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 283 bytes |
| Instructions | 69        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 03 01  00 00 80 03 02 00 00 80   ...............
0010: 1E F0 FF FF 7F 6F 70 02  00 00 00 80 80 37 00 6E  .....op......7.n
0020: F8 FF FF 7F 01 80 99 F8  FF FF 7F 1D 02 80 23 03  ..............#.
0030: 01 10 03 80 01 1A 01 02  00 00 01 80 80 5D 00 42  .............].B
0040: 03 02 10 01 00 1D 04 80  23 6E F8 FF FF 7F 05 80  ........#n......
0050: 99 F8 FF FF 7F 03 01 10  01 80 01 1A 01 02 00 00  ................
0060: 06 80 80 82 00 03 02 10  01 00 1D 07 80 23 6E F8  .............#n.
0070: FF FF 7F 08 80 99 F8 FF  FF 7F 03 01 10 03 80 01  ................
0080: 1A 01 02 00 00 09 80 80  9A 00 1D 0A 80 23 1D 0B  .............#..
0090: 80 23 03 01 10 03 80 01  1A 01 02 00 00 0C 80 80  .#..............
00A0: C0 00 42 03 02 10 02 00  1D 0D 80 23 6E F8 FF FF  ..B........#n...
00B0: 7F 05 80 99 F8 FF FF 7F  03 01 10 06 80 01 1A 01  ................
00C0: 02 00 00 0E 80 80 E6 00  42 03 02 10 02 00 1D 0F  ........B.......
00D0: 80 23 6E F8 FF FF 7F 08  80 99 F8 FF FF 7F 03 01  .#n.............
00E0: 10 09 80 01 1A 01 02 00  00 08 80 80 06 01 6E F8  ..............n.
00F0: FF FF 7F 01 80 99 F8 FF  FF 7F 1D 10 80 23 03 01  .............#..
0100: 10 03 80 01 1A 01 02 00  00 05 80 80 1A 01 1D 11  ................
0110: 80 23 03 01 10 03 80 01  1A 01 21 00              .#........!.    
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x03] ExtData[1]->WorkLocal[1] = 0*
  2: 0x000B [0x03] ExtData[1]->WorkLocal[2] = 0*
  3: 0x0010 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0015 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0016 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0037
  7: 0x001F [0x6E] EventEntity uses emote 1*
  8: 0x0026 [0x99] Wait for EventEntity animation to complete
  9: 0x002B [0x1D] PRINT_EVENT_MESSAGE(message_id=7557*)
    → "Thanks for coming all this way. I'd love to offer you some hospitality, but we'd need to get this frontier station completed first! Could you lend us a hand by signing up for a coalition assignment?"
 10: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x002F [0x03] Work_Zone[1] = 1073741824*
 12: 0x0034 [0x01] GOTO 0x011A
 13: 0x0037 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x005D
 14: 0x003F [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0040 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 16: 0x0045 [0x1D] PRINT_EVENT_MESSAGE(message_id=7558*)
    → "Thanks so much for delivering this $3! I can't wait to see how this station looks once it's built. If you want, you can go pick up your reward from the manager who gave you this assignment."
 17: 0x0048 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0049 [0x6E] EventEntity uses emote 7*
 19: 0x0050 [0x99] Wait for EventEntity animation to complete
 20: 0x0055 [0x03] Work_Zone[1] = 1*
 21: 0x005A [0x01] GOTO 0x011A
 22: 0x005D [0x02] IF !(ExtData[1]->WorkLocal[0] == 2*) GOTO 0x0082
 23: 0x0065 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[1]
 24: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=7559*)
    → "We're glad you tried your best, but destroyed $5 are useless to us. Sorry, but can you pick up another one from the manager in charge?"
 25: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x006E [0x6E] EventEntity uses emote 6*
 27: 0x0075 [0x99] Wait for EventEntity animation to complete
 28: 0x007A [0x03] Work_Zone[1] = 1073741824*
 29: 0x007F [0x01] GOTO 0x011A
 30: 0x0082 [0x02] IF !(ExtData[1]->WorkLocal[0] == 3*) GOTO 0x009A
 31: 0x008A [0x1D] PRINT_EVENT_MESSAGE(message_id=7560*)
    → "Welcome to the frontier! This station has already been built, but you can always help construct some bivouacs or keep them supplied."
 32: 0x008D [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x008E [0x1D] PRINT_EVENT_MESSAGE(message_id=7561*)
    → "Frontier stations are self-sufficient, but the bivouacs are sadly not. We'd be extremely appreciative if you could undertake some assignments to make sure they stay in operation."
 34: 0x0091 [0x23] WAIT_FOR_DIALOG_INTERACTION
 35: 0x0092 [0x03] Work_Zone[1] = 1073741824*
 36: 0x0097 [0x01] GOTO 0x011A
 37: 0x009A [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x00C0
 38: 0x00A2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 39: 0x00A3 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 40: 0x00A8 [0x1D] PRINT_EVENT_MESSAGE(message_id=7563*)
    → "Thank you for helping us out. Here's the $3. All we ask is that you take it to the manager in charge of this assignment."
 41: 0x00AB [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00AC [0x6E] EventEntity uses emote 7*
 43: 0x00B3 [0x99] Wait for EventEntity animation to complete
 44: 0x00B8 [0x03] Work_Zone[1] = 2*
 45: 0x00BD [0x01] GOTO 0x011A
 46: 0x00C0 [0x02] IF !(ExtData[1]->WorkLocal[0] == 5*) GOTO 0x00E6
 47: 0x00C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 48: 0x00C9 [0x03] Work_Zone[2] = ExtData[1]->WorkLocal[2]
 49: 0x00CE [0x1D] PRINT_EVENT_MESSAGE(message_id=7565*)
    → "Well, here's another $3, but please be careful not to break this one."
 50: 0x00D1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x00D2 [0x6E] EventEntity uses emote 6*
 52: 0x00D9 [0x99] Wait for EventEntity animation to complete
 53: 0x00DE [0x03] Work_Zone[1] = 3*
 54: 0x00E3 [0x01] GOTO 0x011A
 55: 0x00E6 [0x02] IF !(ExtData[1]->WorkLocal[0] == 6*) GOTO 0x0106
 56: 0x00EE [0x6E] EventEntity uses emote 1*
 57: 0x00F5 [0x99] Wait for EventEntity animation to complete
 58: 0x00FA [0x1D] PRINT_EVENT_MESSAGE(message_id=7562*)
    → "Hello, there! We have some materials we'd like delivered to town, but we have to go through the right channels. Would you mind undertaking a coalition assignment to transport them back?"
 59: 0x00FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x00FE [0x03] Work_Zone[1] = 1073741824*
 61: 0x0103 [0x01] GOTO 0x011A
 62: 0x0106 [0x02] IF !(ExtData[1]->WorkLocal[0] == 7*) GOTO 0x011A
 63: 0x010E [0x1D] PRINT_EVENT_MESSAGE(message_id=7564*)
    → "Thank you for helping us out. All we ask is that you deliver your cargo safely to the manager in charge of this assignment."
 64: 0x0111 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0112 [0x03] Work_Zone[1] = 1073741824*
 66: 0x0117 [0x01] GOTO 0x011A

SUBROUTINE_011A:
 67: 0x011A [0x21] END_EVENT
 68: 0x011B [0x00] END_REQSTACK()
```
