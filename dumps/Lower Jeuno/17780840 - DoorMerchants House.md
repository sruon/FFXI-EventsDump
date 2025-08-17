# 17780840 - DoorMerchants House

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 3192 bytes            |
| Total Events     | 20                    |
| References Count | 61                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [64](#event-64)          | 0x0001       |    216 |             29 |
| [63](#event-63)          | 0x00D9       |    531 |             78 |
| [25](#event-25)          | 0x02EC       |    216 |             29 |
| [164](#event-164)        | 0x03C4       |    428 |             75 |
| [229](#event-229)        | 0x0570       |    216 |             29 |
| [163](#event-163)        | 0x0648       |    387 |             52 |
| [132](#event-132)        | 0x07CB       |    305 |             45 |
| [1](#event-1)            | 0x08FC       |     23 |              7 |
| [5](#event-5)            | 0x0913       |     52 |             14 |
| [4](#event-4)            | 0x0947       |    108 |             26 |
| [2](#event-2)            | 0x09B3       |     21 |              7 |
| [3](#event-3)            | 0x09C8       |     21 |              7 |
| [0](#event-0)            | 0x09DD       |     53 |             13 |
| [60](#event-60)          | 0x0A12       |    267 |             42 |
| [10040](#event-10040)    | 0x0B1D       |      1 |              1 |
| [10042](#event-10042)    | 0x0B1E       |      1 |              1 |
| [20089](#event-20089)    | 0x0B1F       |      1 |              1 |
| [65535.1](#event-655351) | 0x0B20       |      2 |              2 |
| [65535.2](#event-655352) | 0x0B22       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x01D2      |         466 |
|       3 | 0x0003      |           3 |
|       4 | 0x0091      |         145 |
|       5 | 0x1CDE      |        7390 |
|       6 | 0x003C      |          60 |
|       7 | 0x00A0      |         160 |
|       8 | 0x1CDF      |        7391 |
|       9 | 0x1CE0      |        7392 |
|      10 | 0x0078      |         120 |
|      11 | 0x1CE1      |        7393 |
|      12 | 0x1CE2      |        7394 |
|      13 | 0x001E      |          30 |
|      14 | 0x1CE3      |        7395 |
|      15 | 0x1CE4      |        7396 |
|      16 | 0x000F      |          15 |
|      17 | 0x1CE5      |        7397 |
|      18 | 0x006E      |         110 |
|      19 | 0x005A      |          90 |
|      20 | 0x1CE6      |        7398 |
|      21 | 0x1CE7      |        7399 |
|      22 | 0x1CE8      |        7400 |
|      23 | 0x1CE9      |        7401 |
|      24 | 0x1CEA      |        7402 |
|      25 | 0x1CEB      |        7403 |
|      26 | 0x0001      |           1 |
|      27 | 0x1CEC      |        7404 |
|      28 | 0x1CED      |        7405 |
|      29 | 0x00C0      |         192 |
|      30 | 0x1CEE      |        7406 |
|      31 | 0x1CEF      |        7407 |
|      32 | 0x1CF0      |        7408 |
|      33 | 0x1CF1      |        7409 |
|      34 | 0x007A      |         122 |
|      35 | 0x1CF2      |        7410 |
|      36 | 0x1CF3      |        7411 |
|      37 | 0x1CF4      |        7412 |
|      38 | 0x1CF5      |        7413 |
|      39 | 0x00C9      |         201 |
|      40 | 0x1CF7      |        7415 |
|      41 | 0x1CF8      |        7416 |
|      42 | 0x1CF9      |        7417 |
|      43 | 0x1CFA      |        7418 |
|      44 | 0x1F52      |        8018 |
|      45 | 0x1F53      |        8019 |
|      46 | 0x1F54      |        8020 |
|      47 | 0x1F55      |        8021 |
|      48 | 0x1F56      |        8022 |
|      49 | 0x1F57      |        8023 |
|      50 | 0x00D9      |         217 |
|      51 | 0x1F58      |        8024 |
|      52 | 0x1F59      |        8025 |
|      53 | 0x1F5A      |        8026 |
|      54 | 0x1F5B      |        8027 |
|      55 | 0x1F5C      |        8028 |
|      56 | 0x1F5D      |        8029 |
|      57 | 0x1F5E      |        8030 |
|      58 | 0x1F5F      |        8031 |
|      59 | 0x1F60      |        8032 |
|      60 | 0x1F61      |        8033 |

## String References

- **7403**: Will you bring me the herb? [Yes, I'll go./No way.]
- **8023**: Will you help us? [Of course I will./Not right now.]

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

### Event 64

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 216 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 46 01 42 45 00  80 F0 FF FF 7F F0 FF FF    .F.BE.........
0010: 7F 66 64 6F 31 01 80 55  00 80 F0 FF FF 7F F0 FF  .fdo1..U........
0020: FF 7F 66 64 6F 31 75 00  02 80 75 01 38 03 80 45  ..fdo1u...u.8..E
0030: 04 80 F8 FF FF 7F F8 FF  FF 7F 63 6D 36 30 01 80  ..........cm60..
0040: 55 04 80 F8 FF FF 7F F8  FF FF 7F 63 6D 36 30 29  U..........cm60)
0050: 03 F0 FF FF 7F 1C 29 03  0F 50 0F 01 0E 4E 00 0F  ......)..P...N..
0060: 50 0F 01 4C 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  P..LE..........f
0070: 64 69 31 01 80 55 00 80  F0 FF FF 7F F0 FF FF 7F  di1..U..........
0080: 66 64 69 31 29 03 0F 50  0F 01 0F 2B 0F 50 0F 01  fdi1)..P...+.P..
0090: 05 80 23 27 04 0F 50 0F  01 10 1C 06 80 4D 45 00  ..#'..P......ME.
00A0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 55  .........fdo1..U
00B0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 4E 01  ..........fdo1N.
00C0: 0F 50 0F 01 46 00 45 00  80 F0 FF FF 7F F0 FF FF  .P..F.E.........
00D0: 7F 66 64 69 31 01 80 21  00                       .fdi1..!.       
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0005 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0006 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0017 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0026 [0x75] LOAD_ROOM(Load indoor room, room=466*)
  6: 0x002A [0x75] LOAD_ROOM(No action)
  7: 0x002C [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  8: 0x002F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm60" with entities [EventEntity, EventEntity], work=[145*, 0*]
  9: 0x0040 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm60" with entities [EventEntity, EventEntity], work=145*
 10: 0x004F [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1C)
 11: 0x0056 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0E)
 12: 0x005D [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 13: 0x0063 [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x0064 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0075 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 16: 0x0084 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0F)
 17: 0x008B [0x2B] Dietmund (ID: 17780751/0x010F500F) [7390*]:
    → "Who the hell are you? Get outta here!"
 18: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0093 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x10)
 20: 0x009A [0x1C] WAIT(60* ticks)
 21: 0x009D [0x4D] EventEntity->StatusEvent = 9 // Close door
 22: 0x009E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x00AF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 24: 0x00BE [0x4E] SET_ENTITY_HIDE_FLAG: Hide Dietmund (ID: 17780751/0x010F500F)
 25: 0x00C4 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x00C6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x00D7 [0x21] END_EVENT
 28: 0x00D8 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00D9    |
| Data Size    | 531 bytes |
| Instructions | 78        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                             20 01 46 01 42 4C 45            .F.BLE
00E0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 01 80  ..........fdo1..
00F0: 55 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 75  U..........fdo1u
0100: 00 02 80 75 01 5C 00 07  80 5C 01 07 80 38 03 80  ...u.\...\...8..
0110: 45 04 80 F8 FF FF 7F F8  FF FF 7F 63 6D 36 31 01  E..........cm61.
0120: 80 55 04 80 F8 FF FF 7F  F8 FF FF 7F 63 6D 36 31  .U..........cm61
0130: 29 03 F0 FF FF 7F 1D 29  03 0F 50 0F 01 11 4E 00  )......)..P...N.
0140: 0F 50 0F 01 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  .P..E..........f
0150: 64 69 31 01 80 55 00 80  F0 FF FF 7F F0 FF FF 7F  di1..U..........
0160: 66 64 69 31 2B 0F 50 0F  01 08 80 23 4A 0F 50 0F  fdi1+.P....#J.P.
0170: 01 F0 FF FF 7F 6F 76 0F  50 0F 01 2B 0F 50 0F 01  .....ov.P..+.P..
0180: 09 80 23 27 03 0F 50 0F  01 13 1C 0A 80 45 04 80  ..#'..P......E..
0190: F8 FF FF 7F F8 FF FF 7F  63 6D 36 32 01 80 55 04  ........cm62..U.
01A0: 80 F8 FF FF 7F F8 FF FF  7F 63 6D 36 32 29 04 0F  .........cm62)..
01B0: 50 0F 01 1F 27 03 0F 50  0F 01 14 2B 0F 50 0F 01  P...'..P...+.P..
01C0: 0B 80 23 29 04 0F 50 0F  01 15 1C 06 80 4E 00 10  ..#)..P......N..
01D0: 50 0F 01 2B 10 50 0F 01  0C 80 23 4A 0F 50 0F 01  P..+.P....#J.P..
01E0: 10 50 0F 01 27 03 10 50  0F 01 09 27 04 10 50 0F  .P..'..P...'..P.
01F0: 01 07 1C 0D 80 45 04 80  F8 FF FF 7F F8 FF FF 7F  .....E..........
0200: 63 6D 36 33 01 80 55 04  80 F8 FF FF 7F F8 FF FF  cm63..U.........
0210: 7F 63 6D 36 33 29 05 10  50 0F 01 0F 4A 0F 50 0F  .cm63)..P...J.P.
0220: 01 10 50 0F 01 6F 76 0F  50 0F 01 27 03 0F 50 0F  ..P..ov.P..'..P.
0230: 01 16 2B 0F 50 0F 01 0E  80 23 2B 10 50 0F 01 0F  ..+.P....#+.P...
0240: 80 23 27 04 0F 50 0F 01  17 27 04 10 50 0F 01 08  .#'..P...'..P...
0250: 1C 10 80 29 05 0F 50 0F  01 1F 4A 0F 50 0F 01 F0  ...)..P...J.P...
0260: FF FF 7F 6F 76 0F 50 0F  01 45 04 80 F8 FF FF 7F  ...ov.P..E......
0270: F8 FF FF 7F 63 6D 36 34  01 80 55 04 80 F8 FF FF  ....cm64..U.....
0280: 7F F8 FF FF 7F 63 6D 36  34 27 03 0F 50 0F 01 14  .....cm64'..P...
0290: 2B 0F 50 0F 01 11 80 23  29 04 0F 50 0F 01 15 45  +.P....#)..P...E
02A0: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 32 01 80  ..........fdo2..
02B0: 55 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 32 5C  U..........fdo2\
02C0: 00 12 80 5C 01 12 80 4E  01 0F 50 0F 01 4E 01 10  ...\...N..P..N..
02D0: 50 0F 01 4D 1C 13 80 46  00 45 00 80 F0 FF FF 7F  P..M...F.E......
02E0: F0 FF FF 7F 66 64 69 32  01 80 21 00              ....fdi2..!.    
```

#### Opcodes

```
  0: 0x00D9 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00DB [0x46] CAMERA_CONTROL: Disable user control
  2: 0x00DD [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x00DE [0x4C] EventEntity->StatusEvent = 8 // Open door
  4: 0x00DF [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x00F0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  6: 0x00FF [0x75] LOAD_ROOM(Load indoor room, room=466*)
  7: 0x0103 [0x75] LOAD_ROOM(No action)
  8: 0x0105 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 160*
  9: 0x0109 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 160*
 10: 0x010D [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 11: 0x0110 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm61" with entities [EventEntity, EventEntity], work=[145*, 0*]
 12: 0x0121 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm61" with entities [EventEntity, EventEntity], work=145*
 13: 0x0130 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1D)
 14: 0x0137 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x11)
 15: 0x013E [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 16: 0x0144 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0155 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x0164 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7391*]:
    → "Who the hell are you?"
 19: 0x016B [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x016C [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at LocalPlayer
 21: 0x0175 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 22: 0x0176 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dietmund (ID: 17780751/0x010F500F) Render.Flags0 and Render.Flags3 conditions are met
 23: 0x017B [0x2B] Dietmund (ID: 17780751/0x010F500F) [7392*]:
    → "Oh, you were there with those chocobos in Upper Jeuno, weren't ya?"
 24: 0x0182 [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x0183 [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x13)
 26: 0x018A [0x1C] WAIT(120* ticks)
 27: 0x018D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm62" with entities [EventEntity, EventEntity], work=[145*, 0*]
 28: 0x019E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm62" with entities [EventEntity, EventEntity], work=145*
 29: 0x01AD [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x1F)
 30: 0x01B4 [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
 31: 0x01BB [0x2B] Dietmund (ID: 17780751/0x010F500F) [7393*]:
    → "Well, give that thief a message for me. That bird's mine, and I'm gonna get it back...one way or another!"
 32: 0x01C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x01C3 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
 34: 0x01CA [0x1C] WAIT(60* ticks)
 35: 0x01CD [0x4E] SET_ENTITY_HIDE_FLAG: Show Domingart (ID: 17780752/0x010F5010)
 36: 0x01D3 [0x2B] Domingart (ID: 17780752/0x010F5010) [7394*]:
    → "Did you find him, Dad?"
 37: 0x01DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x01DB [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at Domingart (ID: 17780752/0x010F5010)
 39: 0x01E4 [0x27] REQ_SET(priority=0x03, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x09)
 40: 0x01EB [0x27] REQ_SET(priority=0x04, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x07)
 41: 0x01F2 [0x1C] WAIT(30* ticks)
 42: 0x01F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm63" with entities [EventEntity, EventEntity], work=[145*, 0*]
 43: 0x0206 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm63" with entities [EventEntity, EventEntity], work=145*
 44: 0x0215 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0F)
 45: 0x021C [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at Domingart (ID: 17780752/0x010F5010)
 46: 0x0225 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 47: 0x0226 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dietmund (ID: 17780751/0x010F500F) Render.Flags0 and Render.Flags3 conditions are met
 48: 0x022B [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x16)
 49: 0x0232 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7395*]:
    → "None of your business. Now go get ready for school."
 50: 0x0239 [0x23] WAIT_FOR_DIALOG_INTERACTION
 51: 0x023A [0x2B] Domingart (ID: 17780752/0x010F5010) [7396*]:
    → "Okay."
 52: 0x0241 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x0242 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x17)
 54: 0x0249 [0x27] REQ_SET(priority=0x04, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x08)
 55: 0x0250 [0x1C] WAIT(15* ticks)
 56: 0x0253 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x1F)
 57: 0x025A [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at LocalPlayer
 58: 0x0263 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 59: 0x0264 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dietmund (ID: 17780751/0x010F500F) Render.Flags0 and Render.Flags3 conditions are met
 60: 0x0269 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm64" with entities [EventEntity, EventEntity], work=[145*, 0*]
 61: 0x027A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm64" with entities [EventEntity, EventEntity], work=145*
 62: 0x0289 [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
 63: 0x0290 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7397*]:
    → "Just tell that scumbag to give back what's mine."
 64: 0x0297 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0298 [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
 66: 0x029F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 67: 0x02B0 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 68: 0x02BF [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 110*
 69: 0x02C3 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 110*
 70: 0x02C7 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Dietmund (ID: 17780751/0x010F500F)
 71: 0x02CD [0x4E] SET_ENTITY_HIDE_FLAG: Hide Domingart (ID: 17780752/0x010F5010)
 72: 0x02D3 [0x4D] EventEntity->StatusEvent = 9 // Close door
 73: 0x02D4 [0x1C] WAIT(90* ticks)
 74: 0x02D7 [0x46] CAMERA_CONTROL: Restore default settings
 75: 0x02D9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 76: 0x02EA [0x21] END_EVENT
 77: 0x02EB [0x00] END_REQSTACK()
```

### Event 25

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x02EC    |
| Data Size    | 216 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02E0:                                      20 01 46 01               .F.
02F0: 42 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  BE..........fdo1
0300: 01 80 55 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..U..........fdo
0310: 31 75 00 02 80 75 01 38  03 80 45 04 80 F8 FF FF  1u...u.8..E.....
0320: 7F F8 FF FF 7F 63 6D 36  30 01 80 55 04 80 F8 FF  .....cm60..U....
0330: FF 7F F8 FF FF 7F 63 6D  36 30 29 03 F0 FF FF 7F  ......cm60).....
0340: 1C 29 03 0F 50 0F 01 0E  4E 00 0F 50 0F 01 4C 45  .)..P...N..P..LE
0350: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 01 80  ..........fdi1..
0360: 55 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 29  U..........fdi1)
0370: 03 0F 50 0F 01 0F 2B 0F  50 0F 01 14 80 23 27 04  ..P...+.P....#'.
0380: 0F 50 0F 01 10 1C 06 80  4D 45 00 80 F0 FF FF 7F  .P......ME......
0390: F0 FF FF 7F 66 64 6F 31  01 80 55 00 80 F0 FF FF  ....fdo1..U.....
03A0: 7F F0 FF FF 7F 66 64 6F  31 4E 01 0F 50 0F 01 46  .....fdo1N..P..F
03B0: 00 45 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
03C0: 01 80 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x02EC [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x02EE [0x46] CAMERA_CONTROL: Disable user control
  2: 0x02F0 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x02F1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0302 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0311 [0x75] LOAD_ROOM(Load indoor room, room=466*)
  6: 0x0315 [0x75] LOAD_ROOM(No action)
  7: 0x0317 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  8: 0x031A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm60" with entities [EventEntity, EventEntity], work=[145*, 0*]
  9: 0x032B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm60" with entities [EventEntity, EventEntity], work=145*
 10: 0x033A [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1C)
 11: 0x0341 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0E)
 12: 0x0348 [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 13: 0x034E [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x034F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x0360 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 16: 0x036F [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0F)
 17: 0x0376 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7398*]:
    → "You again? How many times do I gotta tell ya? That chocobo's mine. Go tell him I want it back, or else."
 18: 0x037D [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x037E [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x10)
 20: 0x0385 [0x1C] WAIT(60* ticks)
 21: 0x0388 [0x4D] EventEntity->StatusEvent = 9 // Close door
 22: 0x0389 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x039A [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 24: 0x03A9 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Dietmund (ID: 17780751/0x010F500F)
 25: 0x03AF [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x03B1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x03C2 [0x21] END_EVENT
 28: 0x03C3 [0x00] END_REQSTACK()
```

### Event 164

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x03C4    |
| Data Size    | 428 bytes |
| Instructions | 75        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03C0:             20 01 46 01  42 45 00 80 F0 FF FF 7F       .F.BE......
03D0: F0 FF FF 7F 66 64 6F 31  01 80 55 00 80 F0 FF FF  ....fdo1..U.....
03E0: 7F F0 FF FF 7F 66 64 6F  31 75 00 02 80 75 01 5C  .....fdo1u...u.\
03F0: 00 07 80 5C 01 07 80 38  03 80 45 04 80 F8 FF FF  ...\...8..E.....
0400: 7F F8 FF FF 7F 63 6D 36  35 01 80 55 04 80 F8 FF  .....cm65..U....
0410: FF 7F F8 FF FF 7F 63 6D  36 35 29 03 F0 FF FF 7F  ......cm65).....
0420: 1C 29 03 0F 50 0F 01 0E  4E 00 0F 50 0F 01 4C 45  .)..P...N..P..LE
0430: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 69 31 01 80  ..........fdi1..
0440: 55 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 69 31 29  U..........fdi1)
0450: 03 0F 50 0F 01 0F 27 04  0F 50 0F 01 16 2B 0F 50  ..P...'..P...+.P
0460: 0F 01 15 80 23 2B 0F 50  0F 01 16 80 23 29 05 0F  ....#+.P....#)..
0470: 50 0F 01 17 27 03 0F 50  0F 01 14 2B 0F 50 0F 01  P...'..P...+.P..
0480: 17 80 23 2B 0F 50 0F 01  18 80 23 29 04 0F 50 0F  ..#+.P....#)..P.
0490: 01 15 24 19 80 1A 80 01  80 25 02 00 10 01 80 00  ..$......%......
04A0: E6 04 2B 0F 50 0F 01 1B  80 23 2B 10 50 0F 01 1C  ..+.P....#+.P...
04B0: 80 23 4B 0F 50 0F 01 1D  80 6F 76 0F 50 0F 01 2B  .#K.P....ov.P..+
04C0: 0F 50 0F 01 1E 80 23 4A  0F 50 0F 01 F0 FF FF 7F  .P....#J.P......
04D0: 6F 76 0F 50 0F 01 2B 0F  50 0F 01 1F 80 23 03 01  ov.P..+.P....#..
04E0: 10 01 80 01 1B 05 02 00  10 1A 80 00 1B 05 2B 0F  ..............+.
04F0: 50 0F 01 20 80 23 2B 10  50 0F 01 1C 80 23 4B 0F  P.. .#+.P....#K.
0500: 50 0F 01 1D 80 6F 76 0F  50 0F 01 2B 0F 50 0F 01  P....ov.P..+.P..
0510: 1E 80 23 03 01 10 1A 80  01 1B 05 27 03 0F 50 0F  ..#........'..P.
0520: 01 12 27 04 0F 50 0F 01  10 1C 06 80 4D 45 00 80  ..'..P......ME..
0530: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 55 00  ........fdo1..U.
0540: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 5C 00 12  .........fdo1\..
0550: 80 5C 01 12 80 4E 01 0F  50 0F 01 46 00 45 00 80  .\...N..P..F.E..
0560: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 01 80 21 00  ........fdi1..!.
```

#### Opcodes

```
  0: 0x03C4 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x03C6 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x03C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x03C9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x03DA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x03E9 [0x75] LOAD_ROOM(Load indoor room, room=466*)
  6: 0x03ED [0x75] LOAD_ROOM(No action)
  7: 0x03EF [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 160*
  8: 0x03F3 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 160*
  9: 0x03F7 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 10: 0x03FA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm65" with entities [EventEntity, EventEntity], work=[145*, 0*]
 11: 0x040B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm65" with entities [EventEntity, EventEntity], work=145*
 12: 0x041A [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1C)
 13: 0x0421 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0E)
 14: 0x0428 [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 15: 0x042E [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x042F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0440 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x044F [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0F)
 19: 0x0456 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x16)
 20: 0x045D [0x2B] Dietmund (ID: 17780751/0x010F500F) [7399*]:
    → "Who the... Oh, it's you. My kid's down with an awful fever."
 21: 0x0464 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0465 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7400*]:
    → "The doc said an herb from Qufim should bring the fever down, but I have to stay here and watch over him."
 23: 0x046C [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x046D [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x17)
 25: 0x0474 [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
 26: 0x047B [0x2B] Dietmund (ID: 17780751/0x010F500F) [7401*]:
    → "I feel bad sayin' this, but could you go find some for me?"
 27: 0x0482 [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x0483 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7402*]:
    → "I was gonna head out once he started feeling better, but I don't have much time! Please!"
 29: 0x048A [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x048B [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
 31: 0x0492 [0x24] CREATE_DIALOG(message_id=7403*, default_option=1*, option_flags=0*)
    → "Will you bring me the herb? [Yes, I'll go./No way.]"
 32: 0x0499 [0x25] WAIT_DIALOG_SELECT()
 33: 0x049A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x04E6
 34: 0x04A2 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7404*]:
    → "Thanks. I won't forget it!"
 35: 0x04A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x04AA [0x2B] Domingart (ID: 17780752/0x010F5010) [7405*]:
    → "Aauhh... Daddy..."
 37: 0x04B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x04B2 [0x4B] UPDATE_ENTITY_YAW(entity=Dietmund (ID: 17780751/0x010F500F), yaw=1.1°*)
 39: 0x04B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 40: 0x04BA [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dietmund (ID: 17780751/0x010F500F) Render.Flags0 and Render.Flags3 conditions are met
 41: 0x04BF [0x2B] Dietmund (ID: 17780751/0x010F500F) [7406*]:
    → "It's okay... Hang in there!"
 42: 0x04C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x04C7 [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at LocalPlayer
 44: 0x04D0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 45: 0x04D1 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dietmund (ID: 17780751/0x010F500F) Render.Flags0 and Render.Flags3 conditions are met
 46: 0x04D6 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7407*]:
    → "There's a special flower on Qufim that only blooms at night. The doc said its roots should bring down his fever. Please, hurry!"
 47: 0x04DD [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x04DE [0x03] Work_Zone[1] = 0*
 49: 0x04E3 [0x01] GOTO 0x051B
 50: 0x04E6 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x051B
 51: 0x04EE [0x2B] Dietmund (ID: 17780751/0x010F500F) [7408*]:
    → "Heh, typical... But come back if you ever change your mind. I don't care who helps me now."
 52: 0x04F5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x04F6 [0x2B] Domingart (ID: 17780752/0x010F5010) [7405*]:
    → "Aauhh... Daddy..."
 54: 0x04FD [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x04FE [0x4B] UPDATE_ENTITY_YAW(entity=Dietmund (ID: 17780751/0x010F500F), yaw=1.1°*)
 56: 0x0505 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 57: 0x0506 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dietmund (ID: 17780751/0x010F500F) Render.Flags0 and Render.Flags3 conditions are met
 58: 0x050B [0x2B] Dietmund (ID: 17780751/0x010F500F) [7406*]:
    → "It's okay... Hang in there!"
 59: 0x0512 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x0513 [0x03] Work_Zone[1] = 1*
 61: 0x0518 [0x01] GOTO 0x051B

SUBROUTINE_051B:
 62: 0x051B [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x12)
 63: 0x0522 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x10)
 64: 0x0529 [0x1C] WAIT(60* ticks)
 65: 0x052C [0x4D] EventEntity->StatusEvent = 9 // Close door
 66: 0x052D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 67: 0x053E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 68: 0x054D [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 110*
 69: 0x0551 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 110*
 70: 0x0555 [0x4E] SET_ENTITY_HIDE_FLAG: Hide Dietmund (ID: 17780751/0x010F500F)
 71: 0x055B [0x46] CAMERA_CONTROL: Restore default settings
 72: 0x055D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 73: 0x056E [0x21] END_EVENT
 74: 0x056F [0x00] END_REQSTACK()
```

### Event 229

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0570    |
| Data Size    | 216 bytes |
| Instructions | 29        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0570: 20 01 46 01 42 45 00 80  F0 FF FF 7F F0 FF FF 7F   .F.BE..........
0580: 66 64 6F 31 01 80 55 00  80 F0 FF FF 7F F0 FF FF  fdo1..U.........
0590: 7F 66 64 6F 31 75 00 02  80 75 01 38 03 80 45 04  .fdo1u...u.8..E.
05A0: 80 F8 FF FF 7F F8 FF FF  7F 63 6D 36 30 01 80 55  .........cm60..U
05B0: 04 80 F8 FF FF 7F F8 FF  FF 7F 63 6D 36 30 29 03  ..........cm60).
05C0: F0 FF FF 7F 1C 29 03 0F  50 0F 01 0E 4E 00 0F 50  .....)..P...N..P
05D0: 0F 01 4C 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ..LE..........fd
05E0: 69 31 01 80 55 00 80 F0  FF FF 7F F0 FF FF 7F 66  i1..U..........f
05F0: 64 69 31 29 03 0F 50 0F  01 0F 2B 0F 50 0F 01 21  di1)..P...+.P..!
0600: 80 23 27 04 0F 50 0F 01  10 1C 06 80 4D 45 00 80  .#'..P......ME..
0610: F0 FF FF 7F F0 FF FF 7F  66 64 6F 31 01 80 55 00  ........fdo1..U.
0620: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 4E 01 0F  .........fdo1N..
0630: 50 0F 01 46 00 45 00 80  F0 FF FF 7F F0 FF FF 7F  P..F.E..........
0640: 66 64 69 31 01 80 21 00                           fdi1..!.        
```

#### Opcodes

```
  0: 0x0570 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0572 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0574 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x0575 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x0586 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x0595 [0x75] LOAD_ROOM(Load indoor room, room=466*)
  6: 0x0599 [0x75] LOAD_ROOM(No action)
  7: 0x059B [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  8: 0x059E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm60" with entities [EventEntity, EventEntity], work=[145*, 0*]
  9: 0x05AF [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm60" with entities [EventEntity, EventEntity], work=145*
 10: 0x05BE [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1C)
 11: 0x05C5 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0E)
 12: 0x05CC [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 13: 0x05D2 [0x4C] EventEntity->StatusEvent = 8 // Open door
 14: 0x05D3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 15: 0x05E4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 16: 0x05F3 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0F)
 17: 0x05FA [0x2B] Dietmund (ID: 17780751/0x010F500F) [7409*]:
    → "There's a special flower on Qufim that only blooms at night. The doc said its roots should bring down his fever. Please, hurry!"
 18: 0x0601 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0602 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x10)
 20: 0x0609 [0x1C] WAIT(60* ticks)
 21: 0x060C [0x4D] EventEntity->StatusEvent = 9 // Close door
 22: 0x060D [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 23: 0x061E [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 24: 0x062D [0x4E] SET_ENTITY_HIDE_FLAG: Hide Dietmund (ID: 17780751/0x010F500F)
 25: 0x0633 [0x46] CAMERA_CONTROL: Restore default settings
 26: 0x0635 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0646 [0x21] END_EVENT
 28: 0x0647 [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0648    |
| Data Size    | 387 bytes |
| Instructions | 52        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0640:                          20 01 46 01 42 4C 45 00           .F.BLE.
0650: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 01 80 55  .........fdo1..U
0660: 00 80 F0 FF FF 7F F0 FF  FF 7F 66 64 6F 31 75 00  ..........fdo1u.
0670: 02 80 75 01 5C 00 22 80  5C 01 22 80 45 04 80 F8  ..u.\.".\.".E...
0680: FF FF 7F F8 FF FF 7F 63  6D 36 61 01 80 55 04 80  .......cm6a..U..
0690: F8 FF FF 7F F8 FF FF 7F  63 6D 36 61 38 03 80 29  ........cm6a8..)
06A0: 03 F0 FF FF 7F 1E 4E 00  10 50 0F 01 45 00 80 F0  ......N..P..E...
06B0: FF FF 7F F0 FF FF 7F 66  64 69 31 01 80 55 00 80  .......fdi1..U..
06C0: F0 FF FF 7F F0 FF FF 7F  66 64 69 31 29 03 10 50  ........fdi1)..P
06D0: 0F 01 07 4A F0 FF FF 7F  10 50 0F 01 2B 10 50 0F  ...J.....P..+.P.
06E0: 01 23 80 23 45 04 80 F8  FF FF 7F F8 FF FF 7F 63  .#.#E..........c
06F0: 6D 36 62 01 80 29 03 10  50 0F 01 0A 1C 06 80 27  m6b..)..P......'
0700: 03 10 50 0F 01 0C 55 04  80 F8 FF FF 7F F8 FF FF  ..P...U.........
0710: 7F 63 6D 36 62 2B 10 50  0F 01 24 80 23 29 04 10  .cm6b+.P..$.#)..
0720: 50 0F 01 0D 2B 10 50 0F  01 25 80 23 29 04 10 50  P...+.P..%.#)..P
0730: 0F 01 0E 2B 10 50 0F 01  26 80 23 27 03 F0 FF FF  ...+.P..&.#'....
0740: 7F 1F 27 05 10 50 0F 01  0B 1C 0D 80 45 04 80 F8  ..'..P......E...
0750: FF FF 7F F8 FF FF 7F 63  6D 36 63 01 80 55 04 80  .......cm6c..U..
0760: F8 FF FF 7F F8 FF FF 7F  63 6D 36 63 29 06 10 50  ........cm6c)..P
0770: 0F 01 0F 45 27 80 F0 FF  FF 7F F0 FF FF 7F 71 73  ...E'.........qs
0780: 74 63 01 80 45 00 80 F0  FF FF 7F F0 FF FF 7F 66  tc..E..........f
0790: 64 6F 32 01 80 55 00 80  F0 FF FF 7F F0 FF FF 7F  do2..U..........
07A0: 66 64 6F 32 5C 00 12 80  5C 01 12 80 4E 01 10 50  fdo2\...\...N..P
07B0: 0F 01 4D 1C 13 80 46 00  45 00 80 F0 FF FF 7F F0  ..M...F.E.......
07C0: FF FF 7F 66 64 69 32 01  80 21 00                 ...fdi2..!.     
```

#### Opcodes

```
  0: 0x0648 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x064A [0x46] CAMERA_CONTROL: Disable user control
  2: 0x064C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x064D [0x4C] EventEntity->StatusEvent = 8 // Open door
  4: 0x064E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  5: 0x065F [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  6: 0x066E [0x75] LOAD_ROOM(Load indoor room, room=466*)
  7: 0x0672 [0x75] LOAD_ROOM(No action)
  8: 0x0674 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 122*
  9: 0x0678 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 122*
 10: 0x067C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm6a" with entities [EventEntity, EventEntity], work=[145*, 0*]
 11: 0x068D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm6a" with entities [EventEntity, EventEntity], work=145*
 12: 0x069C [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 13: 0x069F [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1E)
 14: 0x06A6 [0x4E] SET_ENTITY_HIDE_FLAG: Show Domingart (ID: 17780752/0x010F5010)
 15: 0x06AC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 16: 0x06BD [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 17: 0x06CC [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x07)
 18: 0x06D3 [0x4A] LocalPlayer looks at Domingart (ID: 17780752/0x010F5010)
 19: 0x06DC [0x2B] Domingart (ID: 17780752/0x010F5010) [7410*]:
    → "Hello. Are you here for my dad?"
 20: 0x06E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x06E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm6b" with entities [EventEntity, EventEntity], work=[145*, 0*]
 22: 0x06F5 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0A)
 23: 0x06FC [0x1C] WAIT(60* ticks)
 24: 0x06FF [0x27] REQ_SET(priority=0x03, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0C)
 25: 0x0706 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm6b" with entities [EventEntity, EventEntity], work=145*
 26: 0x0715 [0x2B] Domingart (ID: 17780752/0x010F5010) [7411*]:
    → "He went out to run an errand, but he said he'd be right back."
 27: 0x071C [0x23] WAIT_FOR_DIALOG_INTERACTION
 28: 0x071D [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0D)
 29: 0x0724 [0x2B] Domingart (ID: 17780752/0x010F5010) [7412*]:
    → "Oh, yeah. He asked me to give this to you."
 30: 0x072B [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x072C [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0E)
 32: 0x0733 [0x2B] Domingart (ID: 17780752/0x010F5010) [7413*]:
    → "Well, I've got places to go to. See you later!"
 33: 0x073A [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x073B [0x27] REQ_SET(priority=0x03, entity_id=LocalPlayer, tag_num=0x1F)
 35: 0x0742 [0x27] REQ_SET(priority=0x05, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0B)
 36: 0x0749 [0x1C] WAIT(30* ticks)
 37: 0x074C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm6c" with entities [EventEntity, EventEntity], work=[145*, 0*]
 38: 0x075D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm6c" with entities [EventEntity, EventEntity], work=145*
 39: 0x076C [0x29] REQ_SET_WAIT(priority=0x06, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x0F)
 40: 0x0773 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 41: 0x0784 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 42: 0x0795 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 43: 0x07A4 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 110*
 44: 0x07A8 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 110*
 45: 0x07AC [0x4E] SET_ENTITY_HIDE_FLAG: Hide Domingart (ID: 17780752/0x010F5010)
 46: 0x07B2 [0x4D] EventEntity->StatusEvent = 9 // Close door
 47: 0x07B3 [0x1C] WAIT(90* ticks)
 48: 0x07B6 [0x46] CAMERA_CONTROL: Restore default settings
 49: 0x07B8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 50: 0x07C9 [0x21] END_EVENT
 51: 0x07CA [0x00] END_REQSTACK()
```

### Event 132

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x07CB    |
| Data Size    | 305 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
07C0:                                   20 01 46 01 42              .F.B
07D0: 45 00 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 01  E..........fdo1.
07E0: 80 55 00 80 F0 FF FF 7F  F0 FF FF 7F 66 64 6F 31  .U..........fdo1
07F0: 75 00 02 80 75 01 45 04  80 F8 FF FF 7F F8 FF FF  u...u.E.........
0800: 7F 63 6D 36 30 01 80 55  04 80 F8 FF FF 7F F8 FF  .cm60..U........
0810: FF 7F 63 6D 36 30 38 03  80 29 03 F0 FF FF 7F 1C  ..cm608..)......
0820: 29 03 0F 50 0F 01 0E 29  03 10 50 0F 01 05 4E 00  )..P...)..P...N.
0830: 0F 50 0F 01 4E 00 10 50  0F 01 4C 45 00 80 F0 FF  .P..N..P..LE....
0840: FF 7F F0 FF FF 7F 66 64  69 31 01 80 55 00 80 F0  ......fdi1..U...
0850: FF FF 7F F0 FF FF 7F 66  64 69 31 29 03 0F 50 0F  .......fdi1)..P.
0860: 01 0F 27 04 0F 50 0F 01  14 2B 0F 50 0F 01 28 80  ..'..P...+.P..(.
0870: 23 29 05 0F 50 0F 01 15  4A 0F 50 0F 01 10 50 0F  #)..P...J.P...P.
0880: 01 2B 0F 50 0F 01 29 80  23 4A 0F 50 0F 01 F0 FF  .+.P..).#J.P....
0890: FF 7F 27 03 10 50 0F 01  06 2A 03 10 50 0F 01 4A  ..'..P...*..P..J
08A0: 0F 50 0F 01 10 50 0F 01  2B 10 50 0F 01 2A 80 23  .P...P..+.P..*.#
08B0: 4A 0F 50 0F 01 F0 FF FF  7F 6F 70 2B 0F 50 0F 01  J.P......op+.P..
08C0: 2B 80 23 45 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  +.#E..........fd
08D0: 6F 32 01 80 55 00 80 F0  FF FF 7F F0 FF FF 7F 66  o2..U..........f
08E0: 64 6F 32 4D 1C 13 80 46  00 45 00 80 F0 FF FF 7F  do2M...F.E......
08F0: F0 FF FF 7F 66 64 69 32  01 80 21 00              ....fdi2..!.    
```

#### Opcodes

```
  0: 0x07CB [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x07CD [0x46] CAMERA_CONTROL: Disable user control
  2: 0x07CF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  3: 0x07D0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  4: 0x07E1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  5: 0x07F0 [0x75] LOAD_ROOM(Load indoor room, room=466*)
  6: 0x07F4 [0x75] LOAD_ROOM(No action)
  7: 0x07F6 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm60" with entities [EventEntity, EventEntity], work=[145*, 0*]
  8: 0x0807 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm60" with entities [EventEntity, EventEntity], work=145*
  9: 0x0816 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 10: 0x0819 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1C)
 11: 0x0820 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0E)
 12: 0x0827 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x05)
 13: 0x082E [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 14: 0x0834 [0x4E] SET_ENTITY_HIDE_FLAG: Show Domingart (ID: 17780752/0x010F5010)
 15: 0x083A [0x4C] EventEntity->StatusEvent = 8 // Open door
 16: 0x083B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x084C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x085B [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0F)
 19: 0x0862 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
 20: 0x0869 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7415*]:
    → "Oh, it's you. Thanks to you, I remembered what it is that keeps me going. For that, you have my sincerest thanks."
 21: 0x0870 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x0871 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
 23: 0x0878 [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at Domingart (ID: 17780752/0x010F5010)
 24: 0x0881 [0x2B] Dietmund (ID: 17780751/0x010F500F) [7416*]:
    → "Hey, say thank you for the medicine, okay?"
 25: 0x0888 [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x0889 [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at LocalPlayer
 27: 0x0892 [0x27] REQ_SET(priority=0x03, entity_id=Domingart (ID: 17780752/0x010F5010), tag_num=0x06)
 28: 0x0899 [0x2A] GET_REQ_LEVEL(level=3, entity_id=Domingart (ID: 17780752/0x010F5010))
 29: 0x089F [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at Domingart (ID: 17780752/0x010F5010)
 30: 0x08A8 [0x2B] Domingart (ID: 17780752/0x010F5010) [7417*]:
    → "Thank you very much!"
 31: 0x08AF [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x08B0 [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at LocalPlayer
 33: 0x08B9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 34: 0x08BA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 35: 0x08BB [0x2B] Dietmund (ID: 17780751/0x010F500F) [7418*]:
    → "You'd make a great beastmaster. I'll do my best to return to the basics, like you."
 36: 0x08C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x08C3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 38: 0x08D4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 39: 0x08E3 [0x4D] EventEntity->StatusEvent = 9 // Close door
 40: 0x08E4 [0x1C] WAIT(90* ticks)
 41: 0x08E7 [0x46] CAMERA_CONTROL: Restore default settings
 42: 0x08E9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 43: 0x08FA [0x21] END_EVENT
 44: 0x08FB [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x08FC   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
08F0:                                      1A 46 0A 27              .F.'
0900: 04 0F 50 0F 01 16 2B 0F  50 0F 01 2C 80 23 1A DA  ..P...+.P..,.#..
0910: 0A 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x08FC [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x08FF [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x16)
  2: 0x0906 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8018*]:
    → "Sorry, I'm busy. Something awful has happened, and it'll take one helluva beastmaster to sort it out."
  3: 0x090D [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x090E [0x1A] CALL_SUBROUTINE(address=0x0ADA)
  5: 0x0911 [0x21] END_EVENT
  6: 0x0912 [0x00] END_REQSTACK()
```

### Event 5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0913   |
| Data Size    | 52 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0910:          1A 46 0A 27 04  0F 50 0F 01 14 2B 0F 50     .F.'..P...+.P
0920: 0F 01 2D 80 23 27 05 0F  50 0F 01 15 2B 0F 50 0F  ..-.#'..P...+.P.
0930: 01 2E 80 23 06 01 10 2B  0F 50 0F 01 2F 80 23 1A  ...#...+.P../.#.
0940: 61 09 1A DA 0A 21 00                              a....!.         
```

#### Opcodes

```
  0: 0x0913 [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x0916 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
  2: 0x091D [0x2B] Dietmund (ID: 17780751/0x010F500F) [8019*]:
    → "Perfect timing! We were hoping to find a renowned beastmaster like you to take care of a little problem."
  3: 0x0924 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0925 [0x27] REQ_SET(priority=0x05, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
  5: 0x092C [0x2B] Dietmund (ID: 17780751/0x010F500F) [8020*]:
    → "You see, the beasts who inhabit Eldieme are acting strange lately. It's like they're under someone's control. They've attacked adventurers, and recently killed one!"
  6: 0x0933 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0934 [0x06] Work_Zone[1] = 0
  8: 0x0937 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8021*]:
    → "People suspect we beastmasters have something to do with it. You should know we'd never do anything like that. Won't you look into this for us?"
  9: 0x093E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x093F [0x1A] CALL_SUBROUTINE(address=0x0961)
 11: 0x0942 [0x1A] CALL_SUBROUTINE(address=0x0ADA)
 12: 0x0945 [0x21] END_EVENT
 13: 0x0946 [0x00] END_REQSTACK()
```

### Event 4

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0947    |
| Data Size    | 108 bytes |
| Instructions | 26        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0940:                      1A  46 0A 27 04 0F 50 0F 01         .F.'..P..
0950: 16 2B 0F 50 0F 01 30 80  23 1A 61 09 1A DA 0A 21  .+.P..0.#.a....!
0960: 00 06 01 10 24 31 80 1A  80 01 80 25 02 00 10 01  ....$1.....%....
0970: 80 00 9F 09 03 02 10 32  80 27 04 0F 50 0F 01 14  .......2.'..P...
0980: 2B 0F 50 0F 01 33 80 23  2B 0F 50 0F 01 34 80 23  +.P..3.#+.P..4.#
0990: 29 05 0F 50 0F 01 15 03  01 10 1A 80 01 B2 09 02  )..P............
09A0: 00 10 1A 80 00 B2 09 2B  0F 50 0F 01 35 80 23 01  .......+.P..5.#.
09B0: B2 09 1B                                          ...             
```

#### Opcodes

```
  0: 0x0947 [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x094A [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x16)
  2: 0x0951 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8022*]:
    → "You see, the beasts that inhabit Eldieme are acting strange lately. It's like someone or something is controlling them. Could you look into it for us?"
  3: 0x0958 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0959 [0x1A] CALL_SUBROUTINE(address=0x0961)
  5: 0x095C [0x1A] CALL_SUBROUTINE(address=0x0ADA)
  6: 0x095F [0x21] END_EVENT
  7: 0x0960 [0x00] END_REQSTACK()

SUBROUTINE_0961:
  8: 0x0961 [0x06] Work_Zone[1] = 0
  9: 0x0964 [0x24] CREATE_DIALOG(message_id=8023*, default_option=1*, option_flags=0*)
    → "Will you help us? [Of course I will./Not right now.]"
 10: 0x096B [0x25] WAIT_DIALOG_SELECT()
 11: 0x096C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x099F
 12: 0x0974 [0x03] Work_Zone[2] = 217*
 13: 0x0979 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
 14: 0x0980 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8024*]:
    → "I knew you would! Many skilled beastmasters have gone, but none have returned. Maybe they've fallen to whatever is controlling the beasts!"
 15: 0x0987 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0988 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8025*]:
    → "Take $6 to protect yourself. Ask Osker in the stables in Upper Jeuno to help you."
 17: 0x098F [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0990 [0x29] REQ_SET_WAIT(priority=0x05, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
 19: 0x0997 [0x03] Work_Zone[1] = 1*
 20: 0x099C [0x01] GOTO 0x09B2
 21: 0x099F [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x09B2
 22: 0x09A7 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8026*]:
    → "You're the only one we can turn to! Please come back as soon as you can."
 23: 0x09AE [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x09AF [0x01] GOTO 0x09B2

SUBROUTINE_09B2:
 25: 0x09B2 [0x1B] RETURN
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x09B3   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
09B0:          1A 46 0A 03 02  10 32 80 2B 0F 50 0F 01     .F....2.+.P..
09C0: 34 80 23 1A DA 0A 21 00                           4.#...!.        
```

#### Opcodes

```
  0: 0x09B3 [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x09B6 [0x03] Work_Zone[2] = 217*
  2: 0x09BB [0x2B] Dietmund (ID: 17780751/0x010F500F) [8025*]:
    → "Take $6 to protect yourself. Ask Osker in the stables in Upper Jeuno to help you."
  3: 0x09C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x09C3 [0x1A] CALL_SUBROUTINE(address=0x0ADA)
  5: 0x09C6 [0x21] END_EVENT
  6: 0x09C7 [0x00] END_REQSTACK()
```

### Event 3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x09C8   |
| Data Size    | 21 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
09C0:                          1A 46 0A 03 02 10 32 80          .F....2.
09D0: 2B 0F 50 0F 01 36 80 23  1A DA 0A 21 00           +.P..6.#...!.   
```

#### Opcodes

```
  0: 0x09C8 [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x09CB [0x03] Work_Zone[2] = 217*
  2: 0x09D0 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8027*]:
    → "So you've got $6. Good work! You will know when to use it. Now, to the Eldieme Necropolis!"
  3: 0x09D7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x09D8 [0x1A] CALL_SUBROUTINE(address=0x0ADA)
  5: 0x09DB [0x21] END_EVENT
  6: 0x09DC [0x00] END_REQSTACK()
```

### Event 0

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x09DD   |
| Data Size    | 53 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
09D0:                                         1A 46 0A               .F.
09E0: 27 03 0F 50 0F 01 14 2B  0F 50 0F 01 37 80 23 29  '..P...+.P..7.#)
09F0: 04 0F 50 0F 01 15 27 04  0F 50 0F 01 16 2B 0F 50  ..P...'..P...+.P
0A00: 0F 01 38 80 23 2B 0F 50  0F 01 39 80 23 1A DA 0A  ..8.#+.P..9.#...
0A10: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x09DD [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x09E0 [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x14)
  2: 0x09E7 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8028*]:
    → "So that was what was happening. I'm happy that the honor of beastmasters has been cleared. On behalf of everyone here, I thank you."
  3: 0x09EE [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x09EF [0x29] REQ_SET_WAIT(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x15)
  5: 0x09F6 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x16)
  6: 0x09FD [0x2B] Dietmund (ID: 17780751/0x010F500F) [8029*]:
    → "Pets are precious to beastmasters. I almost lost one, so I know how it feels."
  7: 0x0A04 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0A05 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8030*]:
    → "The other night I dreamed I was riding my old chocobo across the plains. Brutus told me he'd let me see it again, and I can't wait!"
  9: 0x0A0C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0A0D [0x1A] CALL_SUBROUTINE(address=0x0ADA)
 11: 0x0A10 [0x21] END_EVENT
 12: 0x0A11 [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0A12    |
| Data Size    | 267 bytes |
| Instructions | 42        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0A10:       1A 46 0A 27 03 0F  50 0F 01 1C 2B 0F 50 0F    .F.'..P...+.P.
0A20: 01 3A 80 23 27 04 0F 50  0F 01 1D 2B 0F 50 0F 01  .:.#'..P...+.P..
0A30: 3B 80 23 2B 0F 50 0F 01  3C 80 23 2A 04 0F 50 0F  ;.#+.P..<.#*..P.
0A40: 01 1A DA 0A 21 00 20 01  46 01 42 45 00 80 F0 FF  ....!. .F.BE....
0A50: FF 7F F0 FF FF 7F 66 64  6F 31 01 80 55 00 80 F0  ......fdo1..U...
0A60: FF FF 7F F0 FF FF 7F 66  64 6F 31 75 00 02 80 75  .......fdo1u...u
0A70: 01 45 04 80 F8 FF FF 7F  F8 FF FF 7F 63 6D 36 30  .E..........cm60
0A80: 01 80 55 04 80 F8 FF FF  7F F8 FF FF 7F 63 6D 36  ..U..........cm6
0A90: 30 38 03 80 29 03 F0 FF  FF 7F 1C 29 03 0F 50 0F  08..)......)..P.
0AA0: 01 0E 4E 00 0F 50 0F 01  4C 4A 0F 50 0F 01 F0 FF  ..N..P..LJ.P....
0AB0: FF 7F 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..E..........fdi
0AC0: 31 01 80 55 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
0AD0: 69 31 29 03 0F 50 0F 01  0F 1B 27 04 0F 50 0F 01  i1)..P....'..P..
0AE0: 10 1C 06 80 4D 45 00 80  F0 FF FF 7F F0 FF FF 7F  ....ME..........
0AF0: 66 64 6F 32 01 80 55 00  80 F0 FF FF 7F F0 FF FF  fdo2..U.........
0B00: 7F 66 64 6F 32 4D 1C 13  80 46 00 45 00 80 F0 FF  .fdo2M...F.E....
0B10: FF 7F F0 FF FF 7F 66 64  69 32 01 80 1B           ......fdi2...   
```

#### Opcodes

```
  0: 0x0A12 [0x1A] CALL_SUBROUTINE(address=0x0A46)
  1: 0x0A15 [0x27] REQ_SET(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x1C)
  2: 0x0A1C [0x2B] Dietmund (ID: 17780751/0x010F500F) [8031*]:
    → "The other day I was finally able to ride my old chocobo... It was like, well, a dream come true. I never remembered riding to be so exciting."
  3: 0x0A23 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0A24 [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x1D)
  5: 0x0A2B [0x2B] Dietmund (ID: 17780751/0x010F500F) [8032*]:
    → "Ahhhhhh-choo! Excuse me. I think I caught myself a cold riding that old girl all night. My son's been taking care of me since morning."
  6: 0x0A32 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0A33 [0x2B] Dietmund (ID: 17780751/0x010F500F) [8033*]:
    → "I don't know how to thank you for all you've done for me. I think I'll take me some of that great medicine you got for my son and get back into bed. Be seeing you! <Cough-cough!>"
  8: 0x0A3A [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0A3B [0x2A] GET_REQ_LEVEL(level=4, entity_id=Dietmund (ID: 17780751/0x010F500F))
 10: 0x0A41 [0x1A] CALL_SUBROUTINE(address=0x0ADA)
 11: 0x0A44 [0x21] END_EVENT
 12: 0x0A45 [0x00] END_REQSTACK()

SUBROUTINE_0A46:
 13: 0x0A46 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
 14: 0x0A48 [0x46] CAMERA_CONTROL: Disable user control
 15: 0x0A4A [0x42] SET_CLI_EVENT_CANCEL_DATA()
 16: 0x0A4B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 17: 0x0A5C [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 18: 0x0A6B [0x75] LOAD_ROOM(Load indoor room, room=466*)
 19: 0x0A6F [0x75] LOAD_ROOM(No action)
 20: 0x0A71 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "cm60" with entities [EventEntity, EventEntity], work=[145*, 0*]
 21: 0x0A82 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "cm60" with entities [EventEntity, EventEntity], work=145*
 22: 0x0A91 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 23: 0x0A94 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=LocalPlayer, tag_num=0x1C)
 24: 0x0A9B [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0E)
 25: 0x0AA2 [0x4E] SET_ENTITY_HIDE_FLAG: Show Dietmund (ID: 17780751/0x010F500F)
 26: 0x0AA8 [0x4C] EventEntity->StatusEvent = 8 // Open door
 27: 0x0AA9 [0x4A] Dietmund (ID: 17780751/0x010F500F) looks at LocalPlayer
 28: 0x0AB2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 29: 0x0AC3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 30: 0x0AD2 [0x29] REQ_SET_WAIT(priority=0x03, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x0F)
 31: 0x0AD9 [0x1B] RETURN

SUBROUTINE_0ADA:
 32: 0x0ADA [0x27] REQ_SET(priority=0x04, entity_id=Dietmund (ID: 17780751/0x010F500F), tag_num=0x10)
 33: 0x0AE1 [0x1C] WAIT(60* ticks)
 34: 0x0AE4 [0x4D] EventEntity->StatusEvent = 9 // Close door
 35: 0x0AE5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 36: 0x0AF6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=200*
 37: 0x0B05 [0x4D] EventEntity->StatusEvent = 9 // Close door
 38: 0x0B06 [0x1C] WAIT(90* ticks)
 39: 0x0B09 [0x46] CAMERA_CONTROL: Restore default settings
 40: 0x0B0B [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 41: 0x0B1C [0x1B] RETURN
```

### Event 10040

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0B1D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B10:                                         00                     .  
```

#### Opcodes

```
  0: 0x0B1D [0x00] END_REQSTACK()
```

### Event 10042

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0B1E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B10:                                            00                   . 
```

#### Opcodes

```
  0: 0x0B1E [0x00] END_REQSTACK()
```

### Event 20089

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0B1F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B10:                                               00                 .
```

#### Opcodes

```
  0: 0x0B1F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0B20  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B20: 4C 00                                             L.              
```

#### Opcodes

```
  0: 0x0B20 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0B21 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0B22  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0B20:       4D 00                                         M.            
```

#### Opcodes

```
  0: 0x0B22 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0B23 [0x00] END_REQSTACK()
```
